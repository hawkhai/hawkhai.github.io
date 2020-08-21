---
layout: post
title: "Using glog together with cobra in golang"
location: "Japan"
tags: [golang, glog, cobra]
comments: true
---

If you have been programming with golang, you've probably heard of [cobra](https://github.com/spf13/cobra). I use it extensively at work and also in my personal projects.

Recently though, I've been using [glog](https://github.com/golang/glog) more and more. And I quite like it. The thing is, it has a couple of flag definitions in its `init()` function using golang's builtin `flag` library. And I wanted to include those flags into cobra's flag definitions. This is how I did it.

{% gist 221e26cea495e5adc3ae6a323b4fbdba %}

Generated help information will now look something like this.

{% highlight shell %}
# run the help command
$ ./cobraglog -h
Use glog with cobra.

Usage:
   [flags]

Flags:
      --alsologtostderr                  log to standard error as well as files
      --echo string                      echo string (default "hello")
      --log_backtrace_at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log_dir string                   If non-empty, write log files in this directory
      --logtostderr                      log to standard error instead of files
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          log level for V logs
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging
  -h, --help                             help for this command
{% endhighlight %}

Note that our cobra-defined flag `--echo` is also there. The rest are defined by glog internally. Finally, run the application.

{% highlight shell %}
# run the binary, providing the logtostderr flag defined by glog
$ ./cobraglog --logtostderr
I1129 13:49:34.166660    2138 main.go:28] echo (info): hello
W1129 13:49:34.166718    2138 main.go:29] echo (warn): hello
E1129 13:49:34.166722    2138 main.go:30] echo (error): hello
{% endhighlight %}

Here's another example using subcommands.

{% gist 447f983882720d817f3b92088f98aaa3 %}
