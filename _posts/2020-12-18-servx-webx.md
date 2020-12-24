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


## 找代码的几个地方

* <https://sourceforge.net/>
* <http://www.codeproject.com>
* <http://search.csdn.net/>


## 用 FileZilla 搭建 FTP 服务器及相关问题

<https://segmentfault.com/a/1190000009033181>


## NetBeans 忽略配置

NetBeans 源码忽略报错后，配置存在：`C:\Users\86138\AppData\Roaming\NetBeans\11.0\var\attributes.xml`。


## HTML5 视频播放

[HTML5 视频直播（二）](https://imququ.com/post/html5-live-player-2.html)

想在博客里面支持视频。`Emscripten` 动图 gif 方案的问题就是 gif 图片太大，想搞一个 mp4，结果排版和手机上，存在问题，还不如 gif。所以这个方案没用。
用 `gifsicle -O3 animation.gif -o animation-optimized.gif --colors 256` 压缩一下，效果还勉强能接受。

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://sourceforge.net/]({% include relref.html url="/backup/2020-12-18-servx-webx.md/sourceforge.net/f577c4c2.html" %})
- [2] [http://www.codeproject.com]({% include relref.html url="/backup/2020-12-18-servx-webx.md/www.codeproject.com/05a0c83e.html" %})
- [3] [http://search.csdn.net/]({% include relref.html url="/backup/2020-12-18-servx-webx.md/search.csdn.net/37e536ff.html" %})
- [4] [https://segmentfault.com/a/1190000009033181]({% include relref.html url="/backup/2020-12-18-servx-webx.md/segmentfault.com/a7e55d6e.html" %})
- [5] [https://imququ.com/post/html5-live-player-2.html]({% include relref.html url="/backup/2020-12-18-servx-webx.md/imququ.com/df29ec8c.html" %})
