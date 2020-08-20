---
layout: post
title: "Using nginx basic authentication in Kubernetes"
location: "Japan"
tags: [nginx, Kubernetes, basic-auth]
---

This post is somewhat related to a [previous post](https://blog.hawkhai.com/blog/2018/03/31/access-pods-k8s) about accessing k8s services using nginx reverse proxy. Let's try to add a simple basic authentication to these services at the proxy level. Now, this may come in handy in non-production environments but at the very least, make sure that you are doing this over HTTPS as basic authentication credentials are not encrypted.

We will be using the `htpasswd` tool to generate our passwords. In Ubuntu, you can install this using the following command:

{% highlight shell %}
$ sudo apt-get install apache2-utils
{% endhighlight %}

Let's generate our password file:

{% highlight shell %}
$ htpasswd -c passfile user1
New password:
Re-type new password:
Adding password for user user1
$ cat passfile
user1:$apr1$c/7lb2VS$SQ9pPJ8XfNpPH.jmnHRsE0
{% endhighlight %}

Let's add a config map to our previous YAML file and enable basic authentication to `svc1` only:

{% highlight ruby %}
apiVersion: v1
kind: ConfigMap
metadata:
  name: basicauth
  data:
    htpasswd: |
      # generate: $ htpasswd -c {file} username (then input password)
      user1:$apr1$c/7lb2VS$SQ9pPJ8XfNpPH.jmnHRsE0

---

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
        auth_basic "mobingi";
        auth_basic_user_file /etc/serviceproxy/htpasswd;
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
        - name: htpasswd
          mountPath: /etc/serviceproxy/
      volumes:
      - name: config-volume
        configMap:
          name: serviceproxy-conf
          items:
          - key: serviceproxy.conf
            path: serviceproxy.conf
      - name: htpasswd
        configMap:
          name: basicauth
          items:
          - key: htpasswd
            path: htpasswd

---

apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: serviceproxy-hpa
  ...
{% endhighlight %}

You should now be able to access `svc1` using your username:password.

{% highlight shell %}
$ curl -u user1:password https://development.mobingi.com/svc1/some-endpoint
{% endhighlight %}

That's it!
