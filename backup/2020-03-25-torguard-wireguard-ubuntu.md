---
layout: post
title: "Connecting to Torguard VPN using Wireguard from Ubuntu"
location: "Japan"
tags: [torguard, wireguard, ubuntu, linux]
---

As of this writing, Torguard's desktop app still doesn't support Wireguard out of the box. I'm using Ubuntu 19.10 for testing.

If you haven't installed Wireguard yet, you can refer to the installation instructions [here](https://www.wireguard.com/install/). In my case, it was:

{% highlight shell %}
$ sudo apt install wireguard
{% endhighlight %}

Next, you need to login to your Torguard client area, go to Tools --> Enable Wireguard Access. Select a location (in my case, I chose Asia-Singapore2) then click 'Enable Wireguard'. You will be presented with an option to download the generated config file (in my case Asia-Singapore2.conf). Download it and save it to /etc/wireguard/.

To enable the VPN connection, run:

{% highlight shell %}
# The last bit should correspond to the filename of your config file without the '.conf',
# in my case 'Asia-Singapore2'
$ sudo wg-quick up Asia-Singapore2

# Confirm with:
$ sudo wg

# If no issues, you can check your public IP with:
$ curl ipecho.net/plain; echo 
{% endhighlight %}

Finally, to disconnect, run:

{% highlight shell %}
$ sudo wg-quick down Asia-Singapore2
{% endhighlight %}

That's it.
