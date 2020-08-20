---
layout: post
title: "A Windows service with an http endpoint for uploading a new version of itself"
location: "Japan"
categories: ["Code", "Go"]
comments: true
---

Recently, I've been working on a service that runs on a lot of VM's across different locations. If I have a new service build, updating all of the running instances quickly became a bit of a pain. I have to log in to every VM (in some cases through a VPN) and then do a manual upgrade. Now, there are probably tools that already exist for this type of use case but since I'm still learning Go at the moment, I thought this would be a good exercise.

Basically, this is a Windows service that has an http endpoint that accepts a file upload (in this case, a new version of itself). The service then saves this file, calls the `MoveFileEx` API with the `MOVEFILE_DELAY_UNTIL_REBOOT` flag, then reboots the system. I also added a simple client (still written in Go) that will upload the file.

With these tools, I can now update all the running service instances with a script.

Full source code [here](https://github.com/hawkhai/go-windows-delay-update-svc).
