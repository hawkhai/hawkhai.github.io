---
layout: post
title: "Ubuntu 16.04 LTS to Ubuntu 18.04 LTS"
location: "Japan"
tags: [ubuntu, upgrade, xenial, bionic]
---

I just upgraded my home server from Ubuntu 16.04 LTS to 18.04 LTS without any problems so far. For context, this server runs a Samba file server using ZFS. Although after update, I had to run the following command to my pool:

{% highlight shell %}
# pool name is 'm0'
$ sudo zpool upgrade m0
{% endhighlight %}

By the way, at the time of this writing, Ubuntu Server update is not yet available (I think you have to wait for 18.04.1). I used the following command to update mine:

{% highlight shell %}
$ do-release-upgrade -m server -d
{% endhighlight %}
