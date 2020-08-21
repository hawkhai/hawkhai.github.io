---
layout: post
title: "Updates to Camera Class Filter Driver for Windows"
location: "Japan"
tags: [wdm, filter-driver, camera, driver, windows]
---

Updated 2019/03/13:

A pretty good writeup that explains the internals of writing a camera filter driver in Windows can be found [here](https://virusbulletin.com/virusbulletin/2018/09/through-looking-glass-webcam-interception-and-protection-kernel-mode/). I'm putting this information out as this repo is one of the references used in the writeup.

Original post:

This post is a bit of a departure from my usual golang/cloud-related ramblings. I posted an open-source [camera class filter driver](https://github.com/hawkhai/windows-camera-class-filter-driver) for Windows ages ago hoping that it would help someone working on a similar project. If you are familiar with this type of driver, you probably know that it's not that straightforward to write mainly due to it being generally undocumented. A lot of reverse engineering has been done to write this driver. Anyway, recently, someone pointed out to me that it's been discussed in [this forum post](https://www.osronline.com/showthread.cfm?link=288736). So if you're working on a similar project, give it a whirl, and if you find some issues, I would appreciate it if you could submit a PR for fixes. Thanks.
