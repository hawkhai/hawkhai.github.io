---
layout: post
title: "“特效编程”笔记 -- ARM MALI OpenGL ES Emulator for Windows"
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
---


## Windows OpenGL ES Sample

搞了一天，终于转起来了。Windows 上用 ARM MALI OpenGL ES Emulator 模拟一个 OpenGL ES 环境。

{% include image.html url="/images/OpenGL-GLSL/win-opengles-sample.gif" %}


## Introduction

Android 是 OpengGL ES，Windows 上用 ARM MALI OpenGL ES Emulator 模拟一个 OpenGL ES 环境。

OpenGL ES is an embedded version of OpenGL mostly used on mobile devices that offer only limited GPU capabilities compared to modern desktop GPUS.

EGL is a native platform interface that connects the windowing systems to one of Khronos’ APIs, e.g. OpenGL ES.

相关下载：<https://www.khronos.org/registry/OpenGL/index_es.php>

**ARM MALI OpenGL ES Emulator for Windows**
OpenGL ES Emulator: 3.0.2 February 23, 2017
<https://developer.arm.com/tools-and-software/graphics-and-gaming/opengl-es-emulator/downloads>


## EGL 是什么

EGL 实际上是 OpenGL 和设备（又或者叫操作系统）间的中间件，因为 OpenGL 是标准的，但设备是千奇百怪的，要对接就需要一个中间件做协调。也就是说一个设备要支持 OpenGL，那么它需要开发一套相对应的 EGL 来对接。EGL 主要负责初始化 OpenGL 的运行环境和设备间的交互，简单的说就是 OpenGL 负责绘图 EGL 负责和设备交互。

Khronos 是 OpenGL，OpenGL ES，OpenVG 和 EGL 等规范的定义者。

{% include image.html url="/images/OpenGL-GLSL/1909670-c54245befab0e77c.webp" %}

{% include image.html url="/images/OpenGL-GLSL/1909670-1190f4934b884c90.webp"
caption=" 图形处理的一般流程 " %}

{% include image.html url="/images/OpenGL-GLSL/1909670-20d2b8256bdd054e.webp"
caption=" OpenGL ES 2.0 的可编程管线 " %}

{% include image.html url="/images/OpenGL-GLSL/1909670-16aeb651d6c99957.webp"
caption=" 坐标系统 " %}


## OpenGL ES Emulator 横向比较

厂商 | 名称
---- | ----
AMD | OpenGL ES 2.0 Emulator
ARM | OpenGL ES 2.0 Emulator v1.2 [ARM Mali Emulator](https://developer.arm.com/tools-and-software/graphics-and-gaming/opengl-es-emulator/downloads)
Qualcomm | Adreno SDK 2.2 [Adreno GPU SDK](https://developer.qualcomm.com/software/adreno-gpu-sdk/tools)
NVIDIA | x86 Windows OpenGL ES 2.0 Emulator
PowerVR | PowerVR SDK [PowerVR SDK](https://community.imgtec.com/developers/powervr/installers/)


## References

- [1] [Using OpenGL ES on windows desktops via EGL](https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/)
- [2] [Android OpenGL 开发 -- EGL 的使用](https://www.cnblogs.com/wellcherish/p/12727906.html)
- [3] [OpenGL ES Emulator 横向比较](https://www.cnblogs.com/gongminmin/archive/2011/04/25/2027684.html)
- [4] [OpenGL ES Emulator 再次横向比较](http://www.klayge.org/2012/01/28/opengl-es-emulator%e5%86%8d%e6%ac%a1%e6%a8%aa%e5%90%91%e6%af%94%e8%be%83/)

-----

<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>

- [1] [https://developer.arm.com/tools-and-software/graphics-and-gaming/opengl-es-emulator/downloads]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/developer.arm.com/37ace0b1421c804520f135a65bd01689.html" %})
- [2] [https://developer.qualcomm.com/software/adreno-gpu-sdk/tools]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/developer.qualcomm.com/df53d96aa1f521b644847378f20266c0.html" %})
- [3] [https://community.imgtec.com/developers/powervr/installers/]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/community.imgtec.com/1b0beb50133ff59365c00e54c2b53ca1.html" %})
- [4] [https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.saschawillems.de/5efcfffd3d6f715447fe138eb7046661.html" %})
- [5] [https://www.cnblogs.com/wellcherish/p/12727906.html]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.cnblogs.com/37af50ce6d7e06011c904dcf8456cfdb.html" %})
- [6] [https://www.cnblogs.com/gongminmin/archive/2011/04/25/2027684.html]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.cnblogs.com/04b6eb64f673ee1d4a5ceecfbd73f72a.html" %})
- [7] [http://www.klayge.org/2012/01/28/opengl-es-emulator%e5%86%8d%e6%ac%a1%e6%a8%aa%e5%90%91%e6%af%94%e8%be%83/]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.klayge.org/08cb85c8d0ec6d64248df47c220e9bcc.html" %})
