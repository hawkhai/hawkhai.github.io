---
layout: post
title: "“特效编程”笔记 -- 可编程渲染管线 OpenGL/GLSL 基础"
location: "珠海"
categories: ["特效"]
tags: [特效, OpenGL]
mathjax: true
toc: true
---

用 vscode+glsl canvas 插件可以作为一个 shader 开发环境。最终选择了：glsl。

* [OpenGL 学习 -- 开发环境](https://www.cnblogs.com/gispathfinder/p/6985769.html)
* [3D games on the Web GLSL 着色器](https://developer.mozilla.org/zh-CN/docs/Games/Techniques/3D_on_the_web/GLSL_Shaders)
* [如何搭建 OpenGL ES 或者 GLSL 的开发环境](https://bbs.csdn.net/topics/380180878)
* [win7, 64bit 下的 OpenGL 着色语言（glsl）开发环境配置（原）](https://www.cnblogs.com/yanhuiw/p/3281028.html)
* [GLSL 环境搭建](https://blog.csdn.net/u010724874/article/details/48543593)

{% include image.html url="/images/OpenGL-GLSL/982bc51480a085f6878fe5e4656de446_720w.png" %}


## 什么是 Shader Language

三大 Shader 编程语言（CG / HLSL / GLSL）。Shader Language 目前主要有 3 种语言：

1. 基于 OpenGL 的 OpenGL Shading Language，简称 GLSL；
2. 基于 DirectX 的 High Level Shading Language，简称 HLSL；
3. 还有 NVIDIA 公司的 C for Graphic，简称 Cg 语言。


### Cg

GLSL 与 HLSL 分别基于 OpenGL 和 Direct3D 的接口，两者不能混用。

Cg 是一个可以被 OpenGL 和 Direct3D 广泛支持的图形处理器编程语言。
Cg 语言和 OpenGL、Direct3D 并不是同一层次的语言，而是 OpenGL 和 DirectX 的上层，
即 Cg 程序是运行在 OpenGL 和 DirectX 标准顶点和像素着色的基础上的。
Cg 由 NVIDIA 公司和微软公司相互协作在标准硬件光照语言的语法和语义上达成了一致开发。
所以，HLSL 和 Cg 其实是同一种语言。


## OpenGL / GLSL 渲染环境搭建

显卡驱动支持 OpenGL 3.2 及以上版本。
freeglut 库或者 glut 库。
glew 库。
集成开发环境（Visual Studio 2013）


## OpenGL / GLSL

{% include image.html url="/images/OpenGL-GLSL/pipeline.png" %}

图 2.6 GPU 的渲染流水线实现。颜色表示了不同阶段的可配置性或可编程性：
绿色表示该流水线阶段是完全可编程控制的，
黄色表示该流水线阶段可以配置但不是可编程的，
蓝色表示该流水线阶段是由 GPU 固定实现的，开发者没有任何控制权。
实线表示该 shader 必须由开发者编程实现，虚线表示该 Shader 是可选的。

{% include image.html url="/images/OpenGL-GLSL/gpu_pipeline.png" %}

图 2.11 OpenGL 和 DirectX 的屏幕坐标系差异。对于一张 512\*512 大小的图像，在 OpenGL 中其（0, 0）点在左下角，而在 DirectX 中其（0, 0）点在左上角。

{% include image.html url="/images/OpenGL-GLSL/ScreenMapping_OpenGL_DirectX.png" %}


## 参考

* [Unity Manual Compute shaders](https://docs.unity3d.com/Manual/class-ComputeShader.html)
* [三大 Shader 编程语言（CG / HLSL / GLSL）](https://zhuanlan.zhihu.com/p/47433678)
* [《Unity Shader 入门精要》随书彩色插图](http://candycat1992.github.io/unity_shaders_book/unity_shaders_book_images.html)
* [可编程渲染管线比固定管线的优势在哪？有什么应用？](https://www.zhihu.com/question/28024422/answer/39097192)
