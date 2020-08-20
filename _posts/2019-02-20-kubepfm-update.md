---
layout: post
title: "Update to kubepfm, a kubectl port-forward wrapper for multiple pods"
location: "Japan"
tags: [kubepfm, kubectl, k8s, kubernetes, port-forward]
---

Updated 2019/02/20:

- Support for namespaces [https://github.com/hawkhai/kubepfm/issues/1](https://github.com/hawkhai/kubepfm/issues/1)
- Improved handling of input patterns

Original post:

I recently uploaded a tool to GitHub that wraps `kubectl port-forward` command and supports port-forwarding to multiple pods. It's called [`kubepfm`](https://github.com/hawkhai/kubepfm). I use this tool heavily in my development work. You can check out the code [here](https://github.com/hawkhai/kubepfm). You might find this useful.
