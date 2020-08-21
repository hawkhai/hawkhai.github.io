---
layout: post
title: "Using SSH tunnelling to access home router"
location: "Japan"
tags: [ssh, tunnel, home, router]
---

For personal reference:

**My current setup:**

* Router has a static IP provided by my ISP
* Router web server is accessible from 192.168.1.1 (home network)
* SSH server box in my home network with a static IP of 192.168.1.130 (home network)
* Router port forwarding is setup to forward router SSH port to my SSH server box (192.168.1.130:22)
* SSH server box is configured to only accept public/private key authentication; password disabled

**Reason for access:**

I want to be able to access my router web server from outside to configure some settings on the fly, like VPN settings, etc.

**How:**

* Run the following command:

{% highlight shell %}
# -L form: -L local-port:target:target-port
# 'user' = SSH username
$ ssh -i /path/to/ssh/key -L 8080:192.168.1.1:80 user@router-static-ip
{% endhighlight %}

* Open localhost:8080 to access the router web server.
* That's it!
