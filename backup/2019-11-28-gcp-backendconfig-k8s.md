---
layout: post
title: "Extending the timeout of a Kubernetes service in GCP"
location: "Japan"
tags: [k8s, timeout, gcp, ingress]
---

This is related to a [previous post](https://blog.hawkhai.com/blog/2018/03/31/access-pods-k8s) about Kubernetes services. This time, it's about extending the timeout of an Ingress. We had a situation where we had to download a huge file from one of our exposed services. The download takes about two minutes to complete. This didn't really worked out since by default, GCP load balancers that are associated with k8s Ingresses have a timeout value of 30s. For a time, we just did manual updates by going to the GCP k8s Services and Ingress console, opening the backend service under the Ingress, and editing the Timeout section to the desired seconds. But since we do have a cluster blue/green deployment, we had to do this every time we recreate our clusters.

Enter [BackendConfig](https://cloud.google.com/kubernetes-engine/docs/concepts/backendconfig) custom resource. With this, we can associate a BackendConfig resource to the service in question using GCP-specific annotations. Reusing the reverse proxy YAML from [this post](https://blog.hawkhai.com/blog/2018/03/31/access-pods-k8s), we add a BackendConfig resource.



{% highlight ruby %}
apiVersion: cloud.google.com/v1beta1
kind: BackendConfig
metadata:
  name: serviceproxy-backendconfig
spec:
  timeoutSec: 7200
  connectionDraining:
    drainingTimeoutSec: 60

---

apiVersion: v1
kind: Service
metadata:
  name: serviceproxy
  annotations:
    beta.cloud.google.com/backend-config: '{"ports": {"80":"serviceproxy-backendconfig"}}'
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

Deploying this will set the timeout of the service to two hours.
