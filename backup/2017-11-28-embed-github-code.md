---
layout: post
title: "Embed code from GitHub to GitHub Pages blog like Gist"
location: "Japan"
tags: [gist-it, github-pages, jekyll]
comments: true
---

I've found this [nifty little tool](https://gist-it.appspot.com/) that can embed codes directly from your GitHub repositories without using Gist. It's very easy to use. For example, if you want to embed, say, [this whole file](https://github.com/hawkhai/rusttrace/blob/master/src/main.rs), you only need to add this snippet somewhere in your post.md file.

{% highlight html %}
<script charset="UTF-8" src="https://gist-it.appspot.com/github.com/hawkhai/rusttrace/blob/master/src/main.rs?footer=minimal"></script>
{% endhighlight %}

The `?footer=minimal` part is optional. It will look something like this:

<script charset="UTF-8" src="https://gist-it.appspot.com/github.com/hawkhai/rusttrace/blob/master/src/main.rs?footer=minimal"></script>

It can also embed just a section of code based on line numbers. For example, to embed line 234 to line 257 of [this file](https://github.com/hawkhai/rmq/blob/master/rabbitmq.go), this snippet will do.

{% highlight html %}
<script charset="UTF-8" src="https://gist-it.appspot.com/github.com/hawkhai/rmq/blob/master/rabbitmq.go?slice=233:257&footer=minimal"></script>
{% endhighlight %}

It will look something like this:

<script charset="UTF-8" src="https://gist-it.appspot.com/github.com/hawkhai/rmq/blob/master/rabbitmq.go?slice=233:257&footer=minimal"></script>

Just note that the `slice=` parameter is zero-based and GitHub's line numbering starts at 1.

Finally, if you have an HTTPS blog, make sure to use `https://gist-it.appspot.com/...`, not `http://gist-it.appspot.com/...`.
