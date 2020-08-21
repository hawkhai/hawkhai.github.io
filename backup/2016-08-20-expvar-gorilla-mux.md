---
layout: post
title: "How to serve expvar when using gorilla/mux"
location: "Japan"
categories: ["Code", "golang"]
comments: true
---

For personal reference:

{% gist b6e639978dc2c21042ccea526700f214 %}

### Access root

{% highlight shell %}
http://localhost:8000
{% endhighlight %}


### Access expvar information

{% highlight shell %}
http://localhost:8000/debug/vars
{% endhighlight %}
