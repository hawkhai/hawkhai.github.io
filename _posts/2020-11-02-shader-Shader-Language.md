---
layout: post
title: "特效编程笔记 -- Shader Language 入门初探"
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

用 vscode+glsl canvas 插件可以作为一个 shader 开发环境。最终选择了：glsl。

* [OpenGL 学习 -- 开发环境 {% include relref_cnblogs.html %}](https://www.cnblogs.com/gispathfinder/p/6985769.html)
* [3D games on the Web GLSL 着色器](https://developer.mozilla.org/zh-CN/docs/Games/Techniques/3D_on_the_web/GLSL_Shaders)
* [如何搭建 OpenGL ES 或者 GLSL 的开发环境 {% include relref_csdn.html %}](https://bbs.csdn.net/topics/380180878)
* [win7, 64bit 下的 OpenGL 着色语言（glsl）开发环境配置（原） {% include relref_cnblogs.html %}](https://www.cnblogs.com/yanhuiw/p/3281028.html)
* [GLSL 环境搭建 {% include relref_csdn.html %}](https://blog.csdn.net/u010724874/article/details/48543593) / [The OpenGL® Programming Guide 9th Edition](http://opengl-redbook.com/)

{% include image.html url="/assets/images/201102-shader-shader-language/982bc51480a085f6878fe5e4656de446_720w.png" %}


## Shader Language？

三大 Shader 编程语言（CG / HLSL / GLSL）。Shader Language 目前主要有 3 种语言：

1. GLSL ( OpenGL ) 基于 OpenGL 的 OpenGL Shading Language，简称 GLSL；
2. HLSL ( DirectX ) 基于 DirectX 的 High Level Shading Language，简称 HLSL；
3. CG ( OpenGL & DirectX capable, made by NVIDIA ) 还有 NVIDIA 公司的 C for Graphic，简称 Cg 语言。


### Cg

GLSL 与 HLSL 分别基于 OpenGL 和 Direct3D 的接口，两者不能混用。

Cg 是一个可以被 OpenGL 和 Direct3D 广泛支持的图形处理器编程语言。
Cg 语言和 OpenGL、Direct3D 并不是同一层次的语言，而是 OpenGL 和 DirectX 的上层，
即 Cg 程序是运行在 OpenGL 和 DirectX 标准顶点和像素着色的基础上的。
Cg 由 NVIDIA 公司和微软公司相互协作在标准硬件光照语言的语法和语义上达成了一致开发。
所以，HLSL 和 Cg 其实是同一种语言。


## OpenGL / GLSL 渲染环境搭建

* 显卡驱动支持 OpenGL 3.2 及以上版本。
* freeglut 库或者 glut 库。
* glew 库。
* 集成开发环境（Visual Studio 2013）


## OpenGL / GLSL

{% include image.html url="/assets/images/201102-shader-shader-language/pipeline.png" %}

{% include image.html url="/assets/images/201102-shader-shader-language/gpu_pipeline.png" %}

图 2.6 GPU 的渲染流水线实现。颜色表示了不同阶段的可配置性或可编程性：
绿色表示该流水线阶段是完全可编程控制的，
黄色表示该流水线阶段可以配置但不是可编程的，
蓝色表示该流水线阶段是由 GPU 固定实现的，开发者没有任何控制权。
实线表示该 shader 必须由开发者编程实现，虚线表示该 Shader 是可选的。

{% include image.html url="/assets/images/201102-shader-shader-language/screenmapping_opengl_directx.png" %}

图 2.11 OpenGL 和 DirectX 的屏幕坐标系差异。对于一张 512\*512 大小的图像，在 OpenGL 中其（0, 0）点在左下角，而在 DirectX 中其（0, 0）点在左上角。


## EGL 介绍和使用

[EGL 介绍和使用 link {% include relref_csdn.html %}](https://blog.csdn.net/afei__/article/details/84867104)

EGL 是渲染 API（如 OpenGL ES）和原生窗口系统之间的接口。

通常来说，OpenGL 是一个操作 GPU 的 API，它通过驱动向 GPU 发送相关指令，控制图形渲染管线状态机的运行状态，但是当涉及到与本地窗口系统进行交互时，就需要这么一个中间层，且它最好是与平台无关的。

因此 EGL 被设计出来，作为 OpenGL 和原生窗口系统之间的桥梁。


## 一些牛逼

[士郎 Shader --- 实时水面模拟与渲染（一）](http://www.manew.com/thread-112638-1-1.html)


## 参考

- [1] [Unity Manual Compute shaders](https://docs.unity3d.com/Manual/class-ComputeShader.html)
- [2] [三大 Shader 编程语言（CG / HLSL / GLSL） {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/47433678)
- [3] [《Unity Shader 入门精要》随书彩色插图 {% include relref_github.html %}](http://candycat1992.github.io/unity_shaders_book/unity_shaders_book_images.html)
- [4] [可编程渲染管线比固定管线的优势在哪？有什么应用？ {% include relref_zhihu.html %}](https://www.zhihu.com/question/28024422/answer/39097192)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-11-02-shader-Shader-Language.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/gispathfinder/p/6985769.html]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/www.cnblogs.com/7f811159.html" %})
- [https://developer.mozilla.org/zh-CN/docs/Games/Techniques/3D_on_the_web/GLSL_Shaders]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/developer.mozilla.org/06f81e32.html" %})
- [https://bbs.csdn.net/topics/380180878]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/bbs.csdn.net/4fadc9bd.html" %})
- [https://www.cnblogs.com/yanhuiw/p/3281028.html]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/www.cnblogs.com/50e502ac.html" %})
- [https://blog.csdn.net/u010724874/article/details/48543593]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/blog.csdn.net/1d2af137.html" %})
- [http://opengl-redbook.com/]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/opengl-redbook.com/02741bc9.html" %})
- [https://blog.csdn.net/afei__/article/details/84867104]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/blog.csdn.net/c9956269.html" %})
- [http://www.manew.com/thread-112638-1-1.html]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/www.manew.com/cd5185d7.html" %})
- [https://docs.unity3d.com/Manual/class-ComputeShader.html]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/docs.unity3d.com/7518bb35.html" %})
- [https://zhuanlan.zhihu.com/p/47433678]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/zhuanlan.zhihu.com/92aa76cb.html" %})
- [http://candycat1992.github.io/unity_shaders_book/unity_shaders_book_images.html]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/candycat1992.github.io/6aae0a5d.html" %})
- [https://www.zhihu.com/question/28024422/answer/39097192]({% include relref.html url="/backup/2020-11-02-shader-Shader-Language.md/www.zhihu.com/e04b6106.html" %})
