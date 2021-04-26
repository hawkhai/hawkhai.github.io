---
layout: post
title: "图形学笔记 -- GPU OpenGL ES 应用性能优化"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

GLSL optimizer based on Mesa's GLSL compiler. Used in Unity for mobile shader optimization.
[glsl-optimizer {% include relref_github.html %}](https://github.com/aras-p/glsl-optimizer)

能在 CPU 完成的，尽量不要在 GPU 里面完成，比如投影矩阵。[from {% include relref_zhihu.html %}](https://www.zhihu.com/question/367207731)
传入 vertex shader 后，每个流水单元会计算投影矩阵，导致大量重复的计算（有多少个顶点就有多少次重复的计算）。
Vertex Shader 里面的代码，每个顶点都要执行一次。
Pixel Shader 里面的代码，每个像素都要执行一次。[Compute Shader 简介](http://frankorz.com/2021/04/17/compute-shader/)

{% include image.html url="/assets/images/210127-shader-opengl-es-optimize/cpu-gpu-compare.png" %}
{% include image.html url="/assets/images/210127-shader-opengl-es-optimize/cpu-gpu-speed.png" caption="示意图<br/>CPU 与 GPU 之间的数据传输速度为整个系统的瓶颈" %}


## 删除调试信息

* 尽量不要调用 `glGetError()`，如果需要，每帧不要超过一次，因为它需要占用较多的时间。


## 避免调用阻塞图形管道的函数

* `glReadPixels()`
* `glCopyTexImage()`
* `glTexSubImage()`


## Refs

- [1] [Mali GPU OpenGL ES 应用性能优化 -- 基本概念 {% include relref_csdn.html %}](https://blog.csdn.net/MyArrow/article/details/17675711)
- [2] [shader 性能优化总结 {% include relref_csdn.html %}](https://blog.csdn.net/qq_35312463/article/details/108438410)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-27-shader-OpenGL-ES-Optimize.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/aras-p/glsl-optimizer]({% include relrefx.html url="/backup/2021-01-27-shader-OpenGL-ES-Optimize.md/github.com/229ba20b.html" %})
- [https://www.zhihu.com/question/367207731]({% include relrefx.html url="/backup/2021-01-27-shader-OpenGL-ES-Optimize.md/www.zhihu.com/6d809638.html" %})
- [http://frankorz.com/2021/04/17/compute-shader/]({% include relrefx.html url="/backup/2021-01-27-shader-OpenGL-ES-Optimize.md/frankorz.com/d7006ee5.html" %})
- [https://blog.csdn.net/MyArrow/article/details/17675711]({% include relrefx.html url="/backup/2021-01-27-shader-OpenGL-ES-Optimize.md/blog.csdn.net/1961eac9.html" %})
- [https://blog.csdn.net/qq_35312463/article/details/108438410]({% include relrefx.html url="/backup/2021-01-27-shader-OpenGL-ES-Optimize.md/blog.csdn.net/eabf4220.html" %})
