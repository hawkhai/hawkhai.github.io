---
layout: post
title: "特效编程笔记 -- GPU OpenGL ES 应用性能优化"
author:
location: "珠海"
categories: ["特效"]
tags: ["特效", "OpenGL", "Irrlicht"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
---


## 删除调试信息

* 尽量不要调用 `glGetError()`，如果需要，每帧不要超过一次，因为它需要占用较多的时间。


## 避免调用阻塞图形管道的函数

* `glReadPixels()`
* `glCopyTexImage()`
* `glTexSubImage()`


# Refs

- [1] [Mali GPU OpenGL ES 应用性能优化 -- 基本概念 {% include relref_csdn.html %}](https://blog.csdn.net/MyArrow/article/details/17675711)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-27-shader-OpenGL-ES-Optimize.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/MyArrow/article/details/17675711]({% include relref.html url="/backup/2021-01-27-shader-OpenGL-ES-Optimize.md/blog.csdn.net/1961eac9.html" %})
