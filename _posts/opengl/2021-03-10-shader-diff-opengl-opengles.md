---
layout: post
title: "图形学笔记 -- OpenGL ES 与 OpenGL 的区别"
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

OpenGL_ES_2.x 为可编程渲染管线（Programmable）而设计。
2.x 并不向下兼容 1.x。

OpenGL ES 相对 OpenGL 删减了一切低效能的操作方式，有高性能的决不留低效能的，即只求效能不求兼容性。
比如：

1. 没有 double 型数据类型，但加入了高性能的定点小数数据类型；
2. 没有 glBegin/glEnd/glVertex，只能用 glDrawArrays/glDraw..。
3. 没有实时将非压缩图片数据转成压缩贴图的功能，程序必须直接提供压缩好的贴图。

[from](https://kheresy.wordpress.com/2010/04/09/opengl-es-2-0-%E7%B0%A1%E5%96%AE%E4%BB%8B%E7%B4%B9/)
[by](https://www.aies.cn/)
1. 在 OpenGL ES 2.0 裡也没有 OpenGL 的 matrix stack，程式开发者必须要自行计算投影矩阵以及各物件的 transform matrix，再传到 shader 裡做计算；虽然在 GPU 端的程式是有矩阵计算的功能，但是在 CPU 端就需要自己实作矩阵计算的基本演算法了。
2. 在 OpenGL ES 裡没有 glBegin() / glEnd() 这种 immediate mode 的函式，vertex 资料必须用 buffer object 或 vertex array 来处理。
3. 取消了 GL_QUADS / GL_POLYGONS 这两种 primitive 类型。
4. vertex 的所有资讯（包含本身的位置、颜色、normal 等等）都变成以抽象的 vertex attrib 来处理，需要自行定义并在 vertex shader 裡计算。
5. Lighting、material 也都是以抽象的形式，以 uniform 变数形式传进 shader 并自行计算。

OpenGLES 以及 shader 开发调试工具
1. shader 开发编辑器 kodelife，地址：https://hexler.net/products/kodelife
2. shader 调试工具 GAPID，google 开源的一个项目，地址：https://github.com/google/gapid
3. shader 调试工具 RenderDoc，地址：https://renderdoc.org/


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


## 其它注意事项

1. glDrawArrays 等函数中数据必须紧密排列，即间隔为 0
2. 各种数据的堆栈深度较低

OpenGL based Graphics : A state machine4
It's a state machine - Setup the stage, lighting, actors... Then draw it.
Sample OpenGL ES 2.0 program as following:


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

- [https://kheresy.wordpress.com/2010/04/09/opengl-es-2-0-%E7%B0%A1%E5%96%AE%E4%BB%8B%E7%B4%B9/]({% include relref.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/kheresy.wordpress.com/38817f5a.html" %})
- [https://www.aies.cn/]({% include relref.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/www.aies.cn/4c5019a6.html" %})
- [https://hexler.net/products/kodelife]({% include relref.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/hexler.net/b2c63114.html" %})
- [https://github.com/google/gapid]({% include relref.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/github.com/769c7e97.html" %})
- [https://renderdoc.org/]({% include relref.html url="/backup/2021-03-10-shader-diff-opengl-opengles.md/renderdoc.org/2eb66df8.html" %})
