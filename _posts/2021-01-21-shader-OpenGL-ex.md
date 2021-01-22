---
layout: post
title: "特效编程笔记 -- OpenGL 的 Windows 组件 和 扩展"
author:
location: "珠海"
categories: ["特效"]
tags: ["特效", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

<https://riptutorial.com/zh-CN/opengl>
OpenGL 是由一些充满智慧的人设计的，他们拥有丰富的图形程序设计 API 设计经验。


## WGL

WGL（可以发音为 wiggle）代表“Windows-GL”，如“Windows 和 OpenGL 之间的接口” - 来自 Windows API 的一组函数，用于与 OpenGL 通信。WGL 函数具有 wgl 前缀，其标记具有 WGL_ 前缀。

Microsoft 系统支持的默认 OpenGL 版本为 1.1。这是一个非常旧的版本（最近的版本是 4.5）。获取最新版本的方法是更新图形驱动程序，但您的图形卡必须支持这些新版本。

可以在此处找到 WGL 功能的完整列表。
[from](https://docs.microsoft.com/zh-cn/windows/win32/opengl/wgl-functions)

```
wglCopyContext
wglCreateContext
wglCreateLayerContext
wglDeleteContext
wglDescribeLayerPlane
wglGetCurrentContext
wglGetCurrentDC
wglGetLayerPaletteEntries
wglGetProcAddress
wglMakeCurrent
wglRealizeLayerPalette
wglSetLayerPaletteEntries
wglShareLists
wglSwapLayerBuffers
wglUseFontBitmaps
wglUseFontOutlines
```


## 图形设备接口（GDI）

GDI（今天更新为 GDI+）是一个 2D 绘图界面，允许您在 Windows 中绘制窗口。
您需要 GDI 来初始化 OpenGL 并允许它与它交互（但实际上不会使用 GDI 本身）。

在 GDI 中，每个窗口都有一个设备上下文（DC），用于在调用函数时标识绘图目标（将其作为参数传递）。
但是，OpenGL 使用自己的渲染上下文（RC）。因此，DC 将用于创建 RC。


## 渲染上下文

我们可以简单地创建渲染上下文：

```cpp
/* RENDERING CONTEXT */
HGLRC rc = wglCreateContext(dc);
wglMakeCurrent(dc, rc);
/* ***************** */
```

请注意，一次只能有一个线程使用 RC。如果你希望稍后从另一个线程使用它，你必须 wglMakeCurrent 那里调用 wglMakeCurrent 来再次激活它（这将在它当前处于活动状态的线程上停用它，依此类推）。


## OpenGL 扩展

对 OpenGL 的原始功能的任何添加都称为扩展。通常，它们可以使某些事情变得合法，扩展参数值范围，扩展 GLSL，甚至添加全新的功能。

有三个主要的扩展组：供应商，EXT 和 ARB。供应商扩展来自特定供应商，它们具有供应商特定标记，如 AMD 或 NV。
EXT 扩展由多个供应商共同完成。一段时间后，它们可能会成为 ARB 扩展，这些都是官方支持的 ARB 和 ARB 批准的扩展。

要获取所有扩展的函数指针类型和函数原型， 并且如前所述，来自 OpenGL 1.2 和更高版本的所有函数指针类型，必须从 OpenGL 注册表下载头文件。
如上所述，对于新应用程序，最好使用核心配置文件，因此最好包括 GL/glcorearb.h 而不是 GL/gl.h 和 GL/glext.h（如果您使用的是 GL/glcorearb.h 那么请不包括 GL/gl.h）。

在 GL/wglext.h 中还有 WGL 的扩展。例如，获取所有支持的扩展列表的函数实际上是一个扩展本身，即 wglGetExtensionsStringARB（它返回一个大字符串，其中包含所有支持的扩展的空格分隔列表）。

获取扩展也是通过 wglGetProcAddress 处理的，所以我们可以像以前一样使用我们的包装器。


## Windows wglGetProcAddress

<https://www.khronos.org/opengl/wiki/Load_OpenGL_Functions>

So in order to get the address of any GL function one can try with wglGetProcAddress and if it fails, try again with the Win32's GetProcAddress:

```cpp
void *GetAnyGLFuncAddress(const char *name)
{
    void *p = (void *)wglGetProcAddress(name);
    if(p == 0 ||
        (p == (void*)0x1) || (p == (void*)0x2) || (p == (void*)0x3) ||
        (p == (void*)-1) )
    {
        HMODULE module = LoadLibraryA("opengl32.dll");
        p = (void *)GetProcAddress(module, name);
    }

    return p;
}
```


## OpenGL ARB

[from {% include relref_csdn.html %}](https://blog.csdn.net/qq_31243065/article/details/105466436)
这样 OpenGL 体系结构审核委员会 (ARB, OpenGL Architecture Reiview Board) 就诞生了。

```cpp
GLint nNum;
glGetIntegerv(GL_NUM_EXTENSIONS, &nNum); // 跟上一个示例一样，获取扩展支持数量

// 遍历所有扩展
for (GLint i = 0; i < nNum; ++i) {
    // 判断是否支持扩展名为: WGL_EXT_swap_control 的扩展
    if (strcmp("WGL_EXT_swap_control", (const char *)glGetStringi(GL_EXTENSIONS, i)) == 0)
    {
        // 支持则获取这个扩展函数的函数指针
        wglSwapIntervalExt = (PFNWGLSWAPINTERVALEXTPROC)wglGetProcAddress("wglSwapIntervalExt");
        if (wglSwapIntervalExt != NULL) {
            // 调用设置这个扩展
            wglSwapIntervalExt(1);
        }
     }
}
```


## OpenGL 扩展识别示例

前缀 | 提 供 商
---- | ----
SGI_ | Silicon Graphics
ATI_ | ATI Tenchnologies
AMD_ | Advanced Micro Devices
NV_ | NVIDIA
IBM_ | IBM
WGL_ | Microsoft
EXT_ | Cross-Vendor
ARB_ | ARB Approved

[第十二课：OpenGL 扩展 {% include relref_csdn.html %}](https://blog.csdn.net/qq_22822335/article/details/50682294)

ARB vs EXT vs …
扩展的名字暗示了它的适用范围：

* GL_: 所有平台；
* GLX_: 只有 Linux 和 Mac 下可使用（X11）；
* WGL_: 只有 Windows 下可使用。
* EXT: 通用的扩展。
* ARB: 已经被 OpenGL 架构评审委员会的所有成员接受（EXT 扩展没多久后就经常被提升为 ARB）的扩展。
* NV/AMD/INTEL: 顾名思义。

-----
<p class='reviewtip'>2021-01-21: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://riptutorial.com/zh-CN/opengl]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/riptutorial.com/d14cbeb5.html" %})
- [https://docs.microsoft.com/zh-cn/windows/win32/opengl/wgl-functions]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/docs.microsoft.com/2204bf30.html" %})
- [https://www.khronos.org/opengl/wiki/Load_OpenGL_Functions]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/www.khronos.org/108527e1.html" %})
- [https://blog.csdn.net/qq_31243065/article/details/105466436]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/blog.csdn.net/213dac02.html" %})
- [https://blog.csdn.net/qq_22822335/article/details/50682294]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/blog.csdn.net/ea7981bb.html" %})
