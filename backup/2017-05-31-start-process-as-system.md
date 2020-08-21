---
layout: post
title: "Start process as system using CreateProcessAsUser"
location: "Japan"
tags: [c++, windows, process]
comments: true
---

Note that this function assumes the caller to be running as SYSTEM as well (i.e. Windows service).

For self reference:

{% gist a5ab54fec75bbabf6dac33b917b44c9b %}
