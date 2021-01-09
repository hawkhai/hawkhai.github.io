---
layout: post
title: "特效编程笔记 -- ARM MALI OpenGL ES Emulator for Windows"
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


## Windows OpenGL ES Sample

搞了一天，终于转起来了。Windows 上用 ARM MALI OpenGL ES Emulator 模拟一个 OpenGL ES 环境。

{% include image.html url="/assets/images/201204-shader-windows-opengles~87/win-opengles-sample.webp" %}


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

{% include image.html url="/assets/images/201204-shader-windows-opengles~87/1909670-c54245befab0e77c.webp" %}

{% include image.html url="/assets/images/201204-shader-windows-opengles~87/1909670-1190f4934b884c90.webp"
caption="图形处理的一般流程" %}

{% include image.html url="/assets/images/201204-shader-windows-opengles~87/1909670-20d2b8256bdd054e.webp"
caption="OpenGL ES 2.0 的可编程管线" %}

{% include image.html url="/assets/images/201204-shader-windows-opengles~87/1909670-16aeb651d6c99957.webp"
caption="坐标系统" %}


## OpenGL ES Emulator 横向比较

PowerVR、Adreno、Mali 三大主流移动 GPU。[from](https://www.expreview.com/44528-all.html)

厂商 | 名称
---- | ----
AMD | ~~OpenGL ES 2.0 Emulator~~ 2008 年卖给了高通（Qualcomm）
ARM | OpenGL ES 2.0 Emulator v1.2 [ARM Mali Emulator](https://developer.arm.com/tools-and-software/graphics-and-gaming/opengl-es-emulator/downloads)
Qualcomm | Adreno SDK 2.2 [Adreno GPU SDK](https://developer.qualcomm.com/software/adreno-gpu-sdk/tools)
NVIDIA | ~~x86 Windows OpenGL ES 2.0 Emulator~~ Tegra 没有找到地方下载
PowerVR | PowerVR SDK [PowerVR SDK](https://community.imgtec.com/developers/powervr/installers/)

费不尽力的老力，都下载下来，整理好了：<https://gitee.com/hawkhai/opengl-3rd.git>

维基百科给出的列表，也不知道真的假的。[link {% include relref_wiki.html %}](https://zh.wikipedia.org/wiki/Adreno)

* PowerVR – Imagination Technologies 研发的移动 GPU，用于第三方授权。
* Mali – ARM Norway 研发的移动 GPU，用于第三方授权。
* Vivante – 图芯技术 研发的移动 GPU，用于第三方授权。
* Tegra – NVIDIA 研发的移动 SoC，不向第三方授权。
* VideoCore – Broadcom 研发的移动 GPU，允许第三方授权。
* Intel Atom – Intel 计算机处理器产品，不向第三方授权。
* AMD APU – AMD 计算机处理器产品，不向第三方授权。
* Adreno – Qualcomm 研发的移动 GPU，用于第三方授权。


### ARM Mali

eglChooseConfig 的第二个参数里必须包含 EGL_OPENGL_ES2_BIT 才能建立 ES 2.0 的 context。


### gpu profiling tools

There are three major mobile GPU vendors nowadays and they provide decent graphics profiling tools:

* For ARM Mali GPU: https://malideveloper.arm.com/resources/tools/mali-graphics-debugger/
* For Imagination PowerVR GPU: https://community.imgtec.com/developers/powervr/tools/pvrtune/
* For Qualcomm Adreno GPU: https://developer.qualcomm.com/software/adreno-gpu-profiler


## References

- [1] [Using OpenGL ES on windows desktops via EGL](https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/)
- [2] [Android OpenGL 开发 -- EGL 的使用 {% include relref_cnblogs.html %}](https://www.cnblogs.com/wellcherish/p/12727906.html)
- [3] [OpenGL ES Emulator 横向比较 {% include relref_cnblogs.html %}](https://www.cnblogs.com/gongminmin/archive/2011/04/25/2027684.html)
- [4] [OpenGL ES Emulator 再次横向比较](http://www.klayge.org/2012/01/28/opengl-es-emulator%e5%86%8d%e6%ac%a1%e6%a8%aa%e5%90%91%e6%af%94%e8%be%83/)
- [5] [OpenGL ES Emulator 横向比较](http://www.klayge.org/2011/04/20/opengl-es-emulator%E6%A8%AA%E5%90%91%E6%AF%94%E8%BE%83/)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [https://www.khronos.org/registry/OpenGL/index_es.php]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.khronos.org/bb75bed1.php" %})
- [https://developer.arm.com/tools-and-software/graphics-and-gaming/opengl-es-emulator/downloads]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/developer.arm.com/37ace0b1.html" %})
- [https://www.expreview.com/44528-all.html]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.expreview.com/a785c1d4.html" %})
- [https://developer.qualcomm.com/software/adreno-gpu-sdk/tools]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/developer.qualcomm.com/df53d96a.html" %})
- [https://community.imgtec.com/developers/powervr/installers/]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/community.imgtec.com/1b0beb50.html" %})
- [https://gitee.com/hawkhai/opengl-3rd.git]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/gitee.com/3cdcc6e8.git" %})
- [https://zh.wikipedia.org/wiki/Adreno]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/zh.wikipedia.org/1c77f069.html" %})
- [https://malideveloper.arm.com/resources/tools/mali-graphics-debugger/]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/malideveloper.arm.com/d774b230.html" %})
- [https://community.imgtec.com/developers/powervr/tools/pvrtune/]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/community.imgtec.com/2fe6cf9a.html" %})
- [https://developer.qualcomm.com/software/adreno-gpu-profiler]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/developer.qualcomm.com/a5a0a370.html" %})
- [https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.saschawillems.de/5efcfffd.html" %})
- [https://www.cnblogs.com/wellcherish/p/12727906.html]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.cnblogs.com/37af50ce.html" %})
- [https://www.cnblogs.com/gongminmin/archive/2011/04/25/2027684.html]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.cnblogs.com/04b6eb64.html" %})
- [http://www.klayge.org/2012/01/28/opengl-es-emulator%e5%86%8d%e6%ac%a1%e6%a8%aa%e5%90%91%e6%af%94%e8%be%83/]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.klayge.org/08cb85c8.html" %})
- [http://www.klayge.org/2011/04/20/opengl-es-emulator%E6%A8%AA%E5%90%91%E6%AF%94%E8%BE%83/]({% include relref.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.klayge.org/2e190eaf.html" %})
