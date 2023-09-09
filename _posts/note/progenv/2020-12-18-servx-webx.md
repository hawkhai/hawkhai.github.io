---
layout: post
title: "开发环境 -- 服务端 & Web 前端 各种问题笔记"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "前端开发"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
archived: true
---


## 找代码的几个地方

* <https://sourceforge.net/>
* <https://www.codeproject.com/>
* <https://download.csdn.net/>
* <https://gitee.com/>
* <https://github.com/>


## SWIG

把 C/C++ 提供给高级语言调用。
SWIG is a software development tool that connects programs written in C and C++ with a variety of high-level programming languages.


## Emscripten

Branches for Emscripten, native (BridJ), and SWIG.
把 C/C++ 编译成 JS 代码。
Emscripten: An LLVM-to-Web Compiler


## Youtube 视频下载

<https://zh.savefrom.net/7/>
<https://ctb.doutui.net/youtube.php>


## 用 FileZilla 搭建 FTP 服务器及相关问题

<https://segmentfault.com/a/1190000009033181>


## NetBeans 忽略配置

NetBeans 源码忽略报错后，配置存在：`C:\Users\86138\AppData\Roaming\NetBeans\11.0\var\attributes.xml` 。


## HTML5 视频播放

[HTML5 视频直播（二）](https://imququ.com/post/html5-live-player-2.html)

想在博客里面支持视频。 `Emscripten` 动图 gif 方案的问题就是 gif 图片太大，想搞一个 mp4，结果排版和手机上，存在问题，还不如 gif。所以这个方案没用。
用 `gifsicle -O3 animation.gif -o animation-optimized.gif --colors 256` 压缩一下，效果还勉强能接受。

最终方案采用 webp，这个最牛逼，压缩率极高。gif2webp -- Tool for converting GIF images to WebP

* [Google 文档 gif2webp](https://developers.google.com/speed/webp/docs/gif2webp)
* [Google 下载 download](https://developers.google.com/speed/webp/download)
* [翻译文档 Google 转换 gif 为 webp 的工具 gif2webp {% include relref_jianshu.html %}](https://www.jianshu.com/p/be308b80f7aa)

```shell
gif2webp -q 75 -lossy -m 6 picture.gif -o picture.webp
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-12-18-servx-webx.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://sourceforge.net/]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/sourceforge.net/f577c4c2.html" %})
- [https://www.codeproject.com/]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/www.codeproject.com/acdb3b41.html" %})
- [https://download.csdn.net/]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/download.csdn.net/185f3ebc.html" %})
- [https://gitee.com/]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/gitee.com/14e83663.html" %})
- [https://github.com/]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/github.com/008ec445.html" %})
- [https://zh.savefrom.net/7/]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/zh.savefrom.net/3ae75bbb.html" %})
- [https://ctb.doutui.net/youtube.php]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/ctb.doutui.net/f1de05f9.php" %})
- [https://segmentfault.com/a/1190000009033181]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/segmentfault.com/a7e55d6e.html" %})
- [https://imququ.com/post/html5-live-player-2.html]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/imququ.com/df29ec8c.html" %})
- [https://developers.google.com/speed/webp/docs/gif2webp]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/developers.google.com/6b2fb33f.html" %})
- [https://developers.google.com/speed/webp/download]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/developers.google.com/a83dd668.html" %})
- [https://www.jianshu.com/p/be308b80f7aa]({% include relrefx.html url="/backup/2020-12-18-servx-webx.md/www.jianshu.com/4187b943.html" %})
