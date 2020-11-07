---
title : Sitemap
---
var baseurl = "{{ site.baseurl }}";
var pagelist = [
{% for post in site.posts %}
"{{ post.url | replace:'index.html','' }}",{% endfor %}
{% for page in site.pages %}
"{{ page.url | replace:'index.html','' }}",{% endfor %}
];
