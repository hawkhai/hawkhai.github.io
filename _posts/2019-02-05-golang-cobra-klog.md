---
layout: post
title: "Using k8s.io/klog together with cobra in golang"
location: "Japan"
tags: [golang, klog, cobra]
comments: true
---

This post is somehow related to a [previous article](https://blog.hawkhai.com/blog/2017/12/01/golang-cobra-glog) about using [glog](https://github.com/golang/glog) together with [cobra](https://github.com/spf13/cobra). This time, we will be using [klog](https://github.com/kubernetes/klog) which is a Kubernetes fork of [glog](https://github.com/golang/glog).

{% gist c1d3267a6e5cc26b9025b4eed74ce00a %}

{% highlight shell %}
# run the -h command
$ ./cobraklog -h
Usage of ./cobraklog:
  -alsologtostderr
        log to standard error as well as files
  -log_backtrace_at value
        when logging hits line file:N, emit a stack trace
  -log_dir string
        If non-empty, write log files in this directory
  -log_file string
        If non-empty, use this log file
  -logtostderr
        log to standard error instead of files
  -skip_headers
        If true, avoid header prefixes in the log messages
  -stderrthreshold value
        logs at or above this threshold go to stderr (default 2)
  -v value
        log level for V logs
  -vmodule value
        comma-separated list of pattern=N settings for file-filtered logging
{% endhighlight %}

{% highlight shell %}
# run cobra's `help` command
$ ./cobraklog help
Use klog together with cobra.

Usage:
  cobraklog [command]

Available Commands:
  help        Help about any command
  run         run command

Flags:
      --alsologtostderr                  log to standard error as well as files
      --log_backtrace_at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log_dir string                   If non-empty, write log files in this directory
      --log_file string                  If non-empty, use this log file
      --logtostderr                      log to standard error instead of files
      --skip_headers                     If true, avoid header prefixes in the log messages
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          log level for V logs
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging
  -h, --help                             help for cobraklog

Use "cobraklog [command] --help" for more information about a command.
{% endhighlight %}

{% highlight shell %}
# run `help` on our subcommand `run`
$ ./cobraklog help run
Run command.

Usage:
  cobraklog run [flags]

Flags:
      --str string   string to print (default "hello world")
  -h, --help         help for run

Global Flags:
      --alsologtostderr                  log to standard error as well as files
      --log_backtrace_at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log_dir string                   If non-empty, write log files in this directory
      --log_file string                  If non-empty, use this log file
      --logtostderr                      log to standard error instead of files
      --skip_headers                     If true, avoid header prefixes in the log messages
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          log level for V logs
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging
{% endhighlight %}

{% highlight shell %}
# run the `run` subcommand
$ ./cobraklog run --logtostderr
I0205 16:37:39.110849   13672 main.go:41] echo=hello world

$ ./cobraklog run --logtostderr --str "hello alien world"
I0205 16:39:37.212187   13685 main.go:41] echo=hello alien world
{% endhighlight %}
