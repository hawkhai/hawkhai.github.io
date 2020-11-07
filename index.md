---
layout: page
title: Blog
author:
location:
categories:
tags:
toc:
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
permalink: /
---

<ul class="listing">
{% for post in site.posts %}
    {% capture y %}{{post.date | date:"%Y-%m"}}{% endcapture %}
    {% if year != y %}
        {% assign year = y %}
        <li class="listing-seperator">{{ y }}</li>
    {% endif %}

    {% if post.visibility != "hidden" %}
    <li class="listing-item">
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
        <a href="{{ post.url | prepend: site.baseurl }}" title="{{ post.title }}">{{ post.title }}</a>
    </li>
    {% endif %}
{% endfor %}
</ul>
