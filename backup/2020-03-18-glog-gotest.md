---
layout: post
title: "Output glog from go test"
location: "Japan"
tags: [golang, glog, test]
---

If you're using [glog](https://github.com/golang/glog) in your Go codes, you can output those when running `go test ...` by using the `--args` parameter:

{% highlight shell %}
$ go test -v ./... -count=1 -cover -race -mod=vendor --args --logtostderr --v=1
{% endhighlight %}
