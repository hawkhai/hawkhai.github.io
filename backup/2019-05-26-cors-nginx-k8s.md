---
layout: post
title: "Adding CORS support to nginx proxy in Kubernetes"
location: "Japan"
tags: [nginx, proxy, cors, Kubernetes]
---

At work, for a couple of months now, we've been using [Ambassador](https://www.getambassador.io/) as our main API gateway to our k8s services. We also have our own authorization service that uses Ambassador's [AuthService](https://www.getambassador.io/reference/services/auth-service) mechanism. Recently, we've had services that needed CORS support and although Ambassador has features that support the [enabling of CORS](https://www.getambassador.io/reference/cors), we had to update our authorization service to handle CORS-related requests. Instead of doing this, we tried adding the CORS support at the proxy level (nginx). I've wrote about this topic [here](https://blog.hawkhai.com/blog/2018/03/31/access-pods-k8s) and [here](https://blog.hawkhai.com/blog/2019/01/31/nginx-basicauth-k8s).

In the example below, the CORS support is added under the location `/svc2/`.

{% highlight ruby %}
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
        # Ref: https://enable-cors.org/server_nginx.html
        if ($request_method = 'OPTIONS') {
          add_header 'Access-Control-Allow-Origin' '*';
          add_header 'Access-Control-Allow-Methods' 'POST, OPTIONS';
          # Custom headers and headers various browsers *should* be OK with but aren't.
          add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization';
          # Tell client that this pre-flight info is valid for 20 days.
          add_header 'Access-Control-Max-Age' 1728000;
          add_header 'Content-Type' 'text/plain; charset=utf-8';
          add_header 'Content-Length' 0;
          return 204;
        }
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

    {..redacted..}
{% endhighlight %}

With that said, be aware of the [potential problems of using if in nginx](https://www.nginx.com/resources/wiki/start/topics/depth/ifisevil/).
