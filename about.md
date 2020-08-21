---
layout: page
title: About
permalink: /about/
---

{% include image.html url="../images/photo.jpg" caption="" width="300px" max_width="300px" align="right" %}

Hi, my name is hawkhai and welcome to my blog.

## Work history

* Software Engineer
  * Android
  * Windows
  * iOS
  * Linux
* And many others (mostly C/C++)...

## Spoken languages
* English??

## Others

## Contact

<div>
{% if site.email_address %}
<a href="mailto: {{ site.email_address }}">
    <span class="fa-stack fa-lg">
        <i class="fa fa-circle fa-stack-2x"></i>
        <i class="fa fa-envelope fa-stack-1x fa-inverse"></i>
    </span>
</a>
{% endif %}

{% if site.twitter_username %}
<a href="https://twitter.com/{{ site.twitter_username }}">
    <span class="fa-stack fa-lg">
        <i class="fa fa-circle fa-stack-2x"></i>
        <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
    </span>
</a>
{% endif %}

{% if site.github_username %}
<a href="https://github.com/{{ site.github_username }}">
    <span class="fa-stack fa-lg">
        <i class="fa fa-circle fa-stack-2x"></i>
        <i class="fa fa-github fa-stack-1x fa-inverse"></i>
    </span>
</a>
{% endif %}
</div>

## PGP public key
{% highlight shell %}

{% endhighlight %}
