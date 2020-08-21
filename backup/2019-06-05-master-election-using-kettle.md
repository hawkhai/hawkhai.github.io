---
layout: post
title: "Using kettle library for master election using distributed locking"
location: "Japan"
tags: [redis, distributed-locking, master, worker]
---

I uploaded a simple library that abstracts the use of distributed locking to elect a master among group of workers at a specified time interval. It's called [`kettle`](https://github.com/hawkhai/kettle). You can find the source code [here](https://github.com/hawkhai/kettle).

We've been using this library mostly on these two recurring use case patterns:

* Consuming a [dynamodbstreams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) endpoint across multiple containers running in Kubernetes. In this case, the master tracks the dynamic addition/removal of shards of a specific endpoint and distributes those shards to the other worker containers.
* Distributing processing to multiple containers from a list of work items. In this case, we have a table of items where each item needs some processing applied to it. We scale out the number of containers to something directly proportional to the number of items on the list. Instead of all containers querying the same table simultaneously, the master will do the querying, publish each item to a pubsub topic, and workers will do the processing from the pubsub items.
