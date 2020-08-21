---
layout: post
title: "ATL service base code"
location: "Japan"
tags: [c++, windows, atl, service]
comments: true
---

Yet another service code for Windows. This time, it's an ATL service. ATL services are basically the same as [traditional Windows services](https://github.com/hawkhai/win32-base-service) but with some advantages.

* Can be started on-demand automatically by the first client call (via COM).
* Clients can call service functions with parameters and return values using COM. In traditional services, clients normally communicate using service control codes and you need some kind of IPC (named pipes, shared memory, etc.) for bi-directional data exchange.

A client console app is provided to demonstrate service function call with return value and service-to-client notification via IDispatch.

Check out the source code [here](https://github.com/hawkhai/base-atlcom-svc).
