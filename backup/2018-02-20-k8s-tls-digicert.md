---
layout: post
title: "Creating a Kubernetes TLS secret using certificates from DigiCert"
location: "Japan"
tags: [DigiCert, Kubernetes, TLS]
---

It took me a while to make this work. I hope this will help someone out there who also is struggling with the same problem.

We use DigiCert as our SSL certificate provider. The package I received contained three files:

- a keyfile, filename.key
- a certificate file, filename.crt
- an intermediate certificate file, DigiCertCA.crt

I had to combine the two certificate files into a single file. I didn't really check the order but I appended the intermediate certificate to my certificate file. Something like this:

{% highlight shell %}
$ cp filename.crt tls.crt
$ cat DigiCertCA.crt >> tls.crt
$ cp filename.key tls.key
$ kubectl create secret tls mytls --key tls.key --cert tls.crt
{% endhighlight %}

I was able to successfully use the secret in a GCE Ingress:

{% highlight ruby %}
apiVersion: extensions/v1beta1
kind: Ingress
...
spec:
  tls:
  - secretName: mytls
  backend:
    serviceName: myservice
    servicePort: 80
...
{% endhighlight %}
