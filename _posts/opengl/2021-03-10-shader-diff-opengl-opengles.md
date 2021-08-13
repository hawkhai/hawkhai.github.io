---
layout: post
title: "图形学笔记 -- Shader：OpenGL ES 与 OpenGL 的区别"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---


## 工具

[^_^]: <https://chengkehan.github.io/Links.html>
几个有用的工具，用来抓取图形渲染帧，在分析其它项目以及排查渲染方面的 bug 时非常有用。
[渲染帧抓取工具 {% include relref_github.html %}](https://chengkehan.github.io/FrameCaptureTools.html)
OpenGLES 以及 shader 开发调试工具。
1. shader 开发编辑器 kodelife，地址：<https://hexler.net/products/kodelife>
2. shader 调试工具 GAPID，google 开源的一个项目，地址：<https://github.com/google/gapid>
3. shader 调试工具 RenderDoc，地址：<https://renderdoc.org/>
4. [Adreno GPU Profiler](https://developer.qualcomm.com/software/adreno-gpu-profiler)
5. [RenderDoc {% include relref_github.html %}](https://github.com/baldurk/renderdoc) is a stand-alone graphics debugging tool.
6. [Tegra Graphics Debugger](https://developer.nvidia.com/tegra-graphics-debugger)
7. [Intel® Graphics Performance Analyzers](https://software.intel.com/en-us/gpa)

* shader：RenderMonkey、FX Composer、OpenGL Shader Designer
* Tegra Debugger/SnapProfiler/Intel GPA
* Android：PerfHUD ES（Tegra）、Adreno Profiler（Adreno）、PVRTrace（PowerVR）、Mali Graphics Debugger（Mali）
* IOS：Xcode OpenGL ES Tools


## GLSL Versions vs GLSL ES Versions

[OpenGL / OpenGL ES Reference Compiler {% include relref_khronos.html %}](https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/)

```
OpenGL ES 2.0 (ESSL #version 100)
OpenGL ES 3.0 (ESSL #version 300 es)
OpenGL 2.0 (GLSL #version 110)
OpenGL 2.1 (GLSL #version 120)
OpenGL 3.0 (GLSL #version 130)
OpenGL 3.1 (GLSL #version 140)
OpenGL 3.2 (GLSL #version 150)
OpenGL 3.3 (GLSL #version 330)
```


### GLSL Versions

[from {% include relref_cnblogs.html %}](https://www.cnblogs.com/beeasy/p/6339313.html)
[from](http://www.c-jump.com/bcc/common/Talk3/OpenGL/Wk03_shader_intro/W03_0090_glsl_version_number.htm)
[from {% include relref_wiki.html %}](https://en.wikipedia.org/wiki/OpenGL_Shading_Language)
[GLSL Versions {% include relref_github.html %}](https://github.com/mattdesl/lwjgl-basics/wiki/GLSL-Versions)

GLSL 语法       | OpenGL 版本       | Date                  | Shader Preprocessor
----            | ----              | ----                  | ----
1.10.59         | 2.0               | 30 April 2004         | #version 110
**1.20**.8      | **2.1**           | 07 September 2006     | **#version 120**
1.30.10         | 3.0               | 22 November 2009      | #version 130
1.40.08         | 3.1               | 22 November 2009      | #version 140
1.50.11         | 3.2               | 04 December 2009      | #version 150
3.30.6          | 3.3               | 11 March 2010         | #version 330
4.00.9          | 4.0               | 24 July 2010          | #version 400


### GLSL ES Versions

OpenGL ES and WebGL use OpenGL ES Shading Language (abbreviated: GLSL ES or ESSL). (Android, iOS, WebGL)
OpenGL 2.0（#version 110）发布于 2004 年，OpenGL 2.1（#version 120）发布于 2006 年，OpenGL ES 2.0 发布于 2009 年。

GLSL ES<br/>语法 | OpenGL ES<br/>版本 | WebGL<br/>版本      | Based on GLSL<br/>语法 | Date             | Shader<br/>Preprocessor
----            | ----              | ----                  | ----                  | ----              | ----
1.00.17         | **2.0**           | 1.0                   | **1.20**              | 12 May 2009       | **#version 100**
3.00.6          | 3.0               | 2.0                   | 3.30                  | 29 January 2016   | #version 300 es


### Base OpenGL Versions for OpenGL ES

OpenGL ES 是从 OpenGL 裁剪定制而来的，去除了 glBegin/glEnd，四边形（GL_QUADS）、多边形（GL_POLYGONS）等复杂图元等许多非绝对必要的特性。

OpenGL ES Version | OpenGL Version
---- | ----
OpenGL ES 1.0 | OpenGL 1.3
OpenGL ES SC 1.0 | OpenGL 1.3
OpenGL ES 1.1 | OpenGL 1.5
**OpenGL ES 2.0** | **OpenGL 2.0**
OpenGL ES 3.0 | OpenGL 4.0+

Unity Macro | Target platform
---- | ----
SHADER_API_GLES | OpenGL ES 2.0
SHADER_API_GLES3 | OpenGL ES 3.0/3.1


## 历史

* 1992：OpenGL1.0~OpenGL 1.5 是经典的固定管线时代；
    * 顶点数组
    * 显示列表
    * 纹理对象
    * 帧缓冲区
    * 缓冲对象
* 2004：OpenGL 2.0~OpenGL2.1 是固定管线和可编程管线并存的时代；
    * 着色语言
    * 像素缓冲对象
* 2008：OpenGL 3.0~OpenGL4.x 开始是可编程管线崛起的时代
    * 划分出 core profile 和 compatibility profile
    * 帧缓冲区对象
    * 几何着色器
* 2010：4.0
    * Tessellation Shader

* 2003: OpenGLES 1.0 - OpenGL 1.1 固定管线
* 2007: OpenGLES 2.0 Programable Vertex and Fragment Shaders
* 2012: OpenGLES 3.0 Texture arrays, Multiple Render Targets
* 2014: OpenGLES 3.1 Compute Shaders
* 2015: OpenGLES 3.2 Tessellation and Geometry Shaders


## 正文

OpenGL_ES_2.x 为可编程渲染管线（Programmable）而设计。
2.x 并不向下兼容 1.x。[from {% include relref_csdn.html %}](https://blog.csdn.net/weiwangchao_/article/details/7831044)

* OpenGL_ES_1.x 为固定渲染管线（Fixed_Function）而设计。
* OpenGL_ES_2.x 为可编程渲染管线（Programmable）而设计。
    * 没有 double 型数据类型，但加入了高性能的定点小数数据类型；
    * 没有 glBegin/glEnd/glVertex，只能用 glDrawArrays/glDraw...；
    * 没有实时将非压缩图片数据转成压缩贴图的功能，程序必须直接提供压缩好的贴图。

[OpenGL ES 2.0 簡單介紹 from](https://kheresy.wordpress.com/2010/04/09/opengl-es-2-0-%E7%B0%A1%E5%96%AE%E4%BB%8B%E7%B4%B9/)
[在线繁体字转换器 by](https://www.aies.cn/)
1. 在 OpenGL ES 2.0 裡也没有 OpenGL 的 matrix stack，程式开发者必须要自行计算投影矩阵以及各物件的
    transform matrix，再传到 shader 裡做计算；虽然在 GPU 端的程式是有矩阵计算的功能，但是在 CPU 端就需要自己实作矩阵计算的基本演算法了。
2. 在 OpenGL ES 裡没有 glBegin() / glEnd() 这种 immediate mode 的函式，vertex 资料必须用 buffer object 或 vertex array 来处理。
3. 取消了 GL_QUADS / GL_POLYGONS 这两种 primitive 类型。
4. vertex 的所有资讯（包含本身的位置、颜色、normal 等等）都变成以抽象的 vertex attrib 来处理，需要自行定义并在 vertex shader 裡计算。
5. Lighting、material 也都是以抽象的形式，以 uniform 变数形式传进 shader 并自行计算。


## 数据类型

1. i GLint 整数型
2. f GLfixed 定点小数
3. x GLclampx 限定型定点小数

* attritude：一般用于各个顶点各不相同的量。如顶点颜色、坐标等。
* uniform：一般用于对于 3D 物体中所有顶点都相同的量。比如光源位置，统一变换矩阵等。
* varying：表示易变量，一般用于顶点着色器传递到片元着色器的量。
* const：常量。


## 删除的功能

1. glBegin/glEnd
2. glArrayElement
3. 显示列表
4. 求值器
5. 索引色模式
6. 自定义裁剪平面
7. glRect
8. 图像处理（这个一般显卡也没有，FireGL/Quadro 显卡有）
9. 反馈缓冲
10. 选择缓冲
11. 累积缓冲
12. 边界标志
13. glPolygonMode
14. GL_QUADS, GL_QUAD_STRIP, GL_POLYGON
15. glPushAttrib, glPopAttrib, glPushClientAttrib, glPopClientAttrib
16. TEXTURE_1D、TEXTURE_3D、TEXTURE_RECT、TEXTURE_CUBE_MAP
17. GL_COMBINE
18. 自动纹理坐标生成
19. 纹理边界
20. GL_CLAMP、GL_CLAMP_TO_BORDER
21. 消失纹理代表
22. 纹理 LOD 限定
23. 纹理偏好限定
24. 纹理自动压缩、解压缩
25. glDrawPixels, glPixelTransfer, glPixelZoom
26. glReadBuffer, glDrawBuffer, glCopyPixels


## Sample OpenGL ES 2.0

1. glDrawArrays 等函数中数据必须紧密排列，即间隔为 0。
2. 各种数据的堆栈深度较低。

OpenGL based Graphics : A state machine4
It's a state machine - Setup the stage, lighting, actors... Then draw it.


### Setup

```cpp
Handle = get_platform_specific_window_handle();
eglGetDisplay(handle);
eglInitialize();
eglBindAPI(EGL_OPENGL_ES_API);
eglChooseConfig();
eglCreateWindowSurface();
eglCreateContex();
eglMakeCurrent();
```


### Actors

```cpp
float afVertices [] = {...};
glEnableVertexAttribArray(0);
glVertexAttribPointer(VERTEX_ARRAY, GL_FLOAT, GL_FALSE, afVertices);
glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);
```


### Show

```cpp
eglSwapBuffers(eglDisplay, eglSurface);
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-10-shader-diff-opengl-opengles.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://chengkehan.github.io/Links.html]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/chengkehan.github.io/0d02c1f4.html" %})
- [https://chengkehan.github.io/FrameCaptureTools.html]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/chengkehan.github.io/8cad55e3.html" %})
- [https://hexler.net/products/kodelife]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/hexler.net/b2c63114.html" %})
- [https://github.com/google/gapid]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/github.com/769c7e97.html" %})
- [https://renderdoc.org/]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/renderdoc.org/2eb66df8.html" %})
- [https://developer.qualcomm.com/software/adreno-gpu-profiler]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/developer.qualcomm.com/a5a0a370.html" %})
- [https://github.com/baldurk/renderdoc]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/github.com/bb00e08f.html" %})
- [https://developer.nvidia.com/tegra-graphics-debugger]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/developer.nvidia.com/1e05e468.html" %})
- [https://software.intel.com/en-us/gpa]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/software.intel.com/5d46a23a.html" %})
- [https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/www.khronos.org/b532b03c.html" %})
- [https://www.cnblogs.com/beeasy/p/6339313.html]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/www.cnblogs.com/4e5820ec.html" %})
- [http://www.c-jump.com/bcc/common/Talk3/OpenGL/Wk03_shader_intro/W03_0090_glsl_version_number.htm]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/www.c-jump.com/6b7517e9.htm" %})
- [https://en.wikipedia.org/wiki/OpenGL_Shading_Language]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/en.wikipedia.org/f01b7d53.html" %})
- [https://github.com/mattdesl/lwjgl-basics/wiki/GLSL-Versions]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/github.com/83c1e163.html" %})
- [https://blog.csdn.net/weiwangchao_/article/details/7831044]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/blog.csdn.net/c61a6284.html" %})
- [https://kheresy.wordpress.com/2010/04/09/opengl-es-2-0-%E7%B0%A1%E5%96%AE%E4%BB%8B%E7%B4%B9/]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/kheresy.wordpress.com/38817f5a.html" %})
- [https://www.aies.cn/]({% include relrefx.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/www.aies.cn/4c5019a6.html" %})
