---
layout: post
title: "开发环境 -- 服务端 & Web 前端 各种问题笔记"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "Web前端"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## HTML5 视频播放

[HTML5 视频直播（二）](https://imququ.com/post/html5-live-player-2.html)

想在博客里面支持视频。`Emscripten` 动图 gif 方案的问题就是 gif 图片太大，想搞一个 mp4，结果排版和手机上，存在问题，还不如 gif。所以这个方案没用。
用 `gifsicle -O3 animation.gif -o animation-optimized.gif --colors 256` 压缩一下，效果还勉强能接受。

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://imququ.com/post/html5-live-player-2.html]({% include relref.html url="/backup/2020-12-18-servx-webx.md/imququ.com/df29ec8c.html" %})
