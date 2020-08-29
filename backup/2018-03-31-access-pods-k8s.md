---
layout: post
title: "Accessing services in Kubernetes"
location: "Japan"
tags: [kubectl, Kubernetes, ingress, port-forward, nginx]
---

At [Mobingi](https://mobingi.com), when we are developing services that run on Kubernetes, we generally use [Minikube](https://github.com/kubernetes/minikube) or [Kubernetes in Docker for Mac](https://blog.docker.com/2018/01/docker-mac-kubernetes/). We also have a cluster that runs on [GKE](https://cloud.google.com/kubernetes-engine/) that we use for development. In this post, I will share how we access some of the services that are running on our development cluster.

## Using kubectl port-forward

Using [kubectl port-forward](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) is probably the cheapest and the most straightforward. For example, if I want to access a cluster service `svc1` through my localhost, I use `kubectl port-forward` like this:

{% highlight shell %}
$ kubectl get pod
NAME                            READY     STATUS    RESTARTS   AGE
svc1-66dd787767-d6b22           2/2       Running   0          7d
svc1-66dd787767-ks92f           2/2       Running   0          7d
svc2-578786c554-rlw2w           2/2       Running   0          7d

# This will connect to the first pod (we have two available):
$ kubectl port-forward `kubectl get pod --no-headers=true -o \
    custom-columns=:metadata.name | grep svc1 | head -n1` 8080:8080
Forwarding from 127.0.0.1:8080 -> 8080
{% endhighlight %}

The left `8080` is my local port, the right `8080` is the pod port where svc1 is running.

One thing to note with `kubectl port-forward` through is that it won't disconnect automatically even when the pod is restarted, say for example, due to an update from CI. I have to restart the command by doing a Ctrl+C and then rerun.

## Exposing the service using NodePort or LoadBalancer

This part is probably the easiest to setup. You can check the details from the Kubernetes [documentation](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services---service-types). But you have to be careful though, especially with load balancers. These are not cheap. We have gone with this route during our early Kubernetes days and we ended up with a lot of load balancers. This was when our clusters were still in AWS. In AWS, (I'm not sure if it is still the case now) when you specify `LoadBalancer` as service type, a classic load balancer will be provisioned for your service. That means one load balancer per exposed service!

When we moved to GKE, we started using [GLBC](https://github.com/kubernetes/ingress-gce) which uses an L7 load balancer via the Ingress API. This improved our costs a little bit since GLBC can support up to five backend services per load balancer using paths. The slight downside was that Ingress updates were a bit slow. It's not a big deal though since it's only in the development cluster and we use blue/green deployment in production. But still, some updates can take up to ten minutes.

## Using nginx as a reverse proxy to cluster services

In our quest to further minimize costs, we are currently using [nginx](https://www.nginx.com/) as our way of exposing services. We provisioned a single Ingress that points to an nginx service which serves as a reverse proxy to our cluster services. This was the cheapest for us as we only have one load balancer for all services. And updating the nginx reverse proxy service takes only a few seconds. So far, this worked for us with no significant problems for the past couple of months.

Here's an example of an nginx reverse proxy service:

{% highlight ruby %}
apiVersion: v1
kind: ConfigMap
metadata:
  name: serviceproxy-conf
data:
  serviceproxy.conf: |
    server {
        listen 80;
        server_name development.mobingi.com;
        resolver kube-dns.kube-system.svc.cluster.local valid=10s;

        location ~ ^/svc1/(.*)$ {
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $remote_addr;
            proxy_set_header Host $host;
            rewrite ^/svc1/(.*)$ /$1 break;
            proxy_pass "http://svc1.default.svc.cluster.local";
            proxy_http_version 1.1;
        }

        location ~ ^/svc2/(.*)$ {
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $remote_addr;
            proxy_set_header Host $host;
            rewrite ^/svc2/(.*)$ /$1 break;
            proxy_pass "http://svc2.default.svc.cluster.local";
            proxy_http_version 1.1;
        }

        # root health check requirement in GKE ingress
        location / {
            return 200 'healthy\n';
        }
    }

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: serviceproxy
spec:
  replicas: 1
  revisionHistoryLimit: 3
  selector:
    matchLabels:
      app: serviceproxy
  template:
    metadata:
      labels:
        app: serviceproxy
    spec:
      containers:
      - name: nginx
        image: nginx:1.13
        ports:
        - containerPort: 80
        volumeMounts:
        - name: config-volume
          mountPath: /etc/nginx/conf.d/
      volumes:
      - name: config-volume
        configMap:
          name: serviceproxy-conf
          items:
          - key: serviceproxy.conf
            path: serviceproxy.conf

---

apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: serviceproxy-hpa
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: serviceproxy
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 80

---

apiVersion: v1
kind: Service
metadata:
  name: serviceproxy
spec:
  type: NodePort
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
  selector:
    app: serviceproxy
{% endhighlight %}

In this example, all services, mainly `svc1` and `svc2`, are running in the `default` namespace. Save this as service.yaml and deploy:

{% highlight shell %}
$ kubectl create -f service.yaml
{% endhighlight %}

A sample Ingress controller for the reverse proxy service:

{% highlight ruby %}
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: serviceproxy-ingress
  annotations:
    kubernetes.io/ingress.class: "gce"
spec:
  tls:
  - secretName: mobingi-tls
  rules:
  - host: development.mobingi.com
    http:
      paths:
      - backend:
          serviceName: serviceproxy
          servicePort: 80
{% endhighlight %}

Save this as ingress.yaml and deploy:

{% highlight shell %}
$ kubectl create -f ingress.yaml
{% endhighlight %}

After everything is ready (Ingress provisioning takes some time), you should be able to access `svc1` through `https://development.mobingi.com/svc1/some-endpoint`, `svc2` through `https://development.mobingi.com/svc2/another-endpoint`, etc. Of course, you have to point your domain to your Ingress load balancer's IP address which you can see using the following command:

{% highlight shell %}
$ kubectl get ingress serviceproxy-ingress
NAME                   HOSTS                     ADDRESS          PORTS     AGE
serviceproxy-ingress   development.mobingi.com   1.2.3.4          80, 443   91d
{% endhighlight %}

If you're wondering how to setup the TLS portion, you can refer to my previous [post](https://blog.hawkhai.com/blog/2018/02/20/k8s-tls-digicert) about the very subject.
