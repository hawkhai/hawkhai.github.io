---
layout: post
title: "Using APC as FIFO queue in Windows"
location: "Japan"
tags: [c++, fifo, queue]
comments: true
---

In this way, we can implement a FIFO queue without using explicit locking/synchronization for enqueueing/dequeueing.

For self reference:

{% gist 48d81f079d64dabbad7fa80928159461 %}
