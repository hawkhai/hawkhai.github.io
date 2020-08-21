---
layout: post
title: "Output golang cmdline tools to stdout and file using tee"
location: "Japan"
tags: [golang, tee, stderr, stdout]
---

Some golang-based tools I've used (or even written) use the builtin `log` package that output logs to stderr by default. I also use [tee](https://en.wikipedia.org/wiki/Tee_(command)) for piping console outputs to file for later viewing. This is the command I generally use:

{% highlight shell %}
# Example tool:
$ sometool --flag1 --flag2 2>&1 | tee out.txt

# 2>&1 <-- redirect stderr to stdout
# tee <-- pipe the console output to out.txt while retaining the actual console logs during command execution
{% endhighlight %}
