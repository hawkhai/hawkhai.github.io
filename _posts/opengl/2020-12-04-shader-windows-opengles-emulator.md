---
layout: post
title: "图形学笔记 -- ARM MALI OpenGL ES Emulator for Windows"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
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

<table class="tablestyle" ntablew="2:8"></table>

厂商 | 名称
---- | ----
AMD | ~~OpenGL ES 2.0 Emulator~~ 2008 年卖给了高通（Qualcomm）
ARM | OpenGL ES 2.0 Emulator v1.2 [ARM Mali Emulator](https://developer.arm.com/tools-and-software/graphics-and-gaming/opengl-es-emulator/downloads)
Qualcomm | Adreno SDK 2.2 [Adreno GPU SDK](https://developer.qualcomm.com/software/adreno-gpu-sdk/tools)
NVIDIA | ~~Windows OpenGL ES 2.0 Emulator~~ Tegra 没有找到地方下载
PowerVR | PowerVR SDK [PowerVR Graphics SDK {% include relref_github.html %}](https://powervr-graphics.github.io/)
**Google** | [ANGLE - Almost Native Graphics Layer Engine](http://angleproject.org/) Chrome、Qt & Webgl 也是基于它实现的！**QT GLES & Android emulator** **自己编译 Angle 有点费力，在最新版本的 cocos2dx 拷贝出来不能用，最后发现：从最新版本的 QT 包里面把 EGL & GLESv2.dll 拷贝出来，跑的非常完美。**

[ANGLE {% include relref_github.html %}](https://github.com/google/angle)
A conformant OpenGL ES implementation for Windows, Mac, Linux, iOS and Android.

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

[How to optimize the graphics performance of your Cocos2d-x games](https://docs.cocos2d-x.org/cocos2d-x/v3/en/advanced_topics/optimizing.html)
There are three major mobile GPU vendors nowadays and they provide decent graphics profiling tools:

* For ARM Mali GPU: <https://malideveloper.arm.com/resources/tools/mali-graphics-debugger/>
* For Imagination PowerVR GPU: <https://community.imgtec.com/developers/powervr/tools/pvrtune/>
* For Qualcomm Adreno GPU: <https://developer.qualcomm.com/software/adreno-gpu-profiler>


### Android 模拟器

```
D/libEGL: loaded /vendor/lib/egl/libEGL_emulation.so
D/libEGL: loaded /vendor/lib/egl/libGLESv1_CM_emulation.so
D/libEGL: loaded /vendor/lib/egl/libGLESv2_emulation.so
D/EGL_emulation: eglCreateContext: 0xf279fb20: maj 3 min 0 rcv 3
D/EGL_emulation: eglMakeCurrent: 0xf279fb20: ver 3 0 (tinfo 0xf2af3030) (first time)
D/HostConnection: HostComposition ext ANDROID_EMU_CHECKSUM_HELPER_v1
                                      ANDROID_EMU_native_sync_v2
                                      ANDROID_EMU_native_sync_v3
                                      ANDROID_EMU_native_sync_v4
                                      ANDROID_EMU_dma_v1
                                      ANDROID_EMU_direct_mem
                                      ANDROID_EMU_host_composition_v1
                                      ANDROID_EMU_host_composition_v2
                                      ANDROID_EMU_YUV_Cache
                                      ANDROID_EMU_async_unmap_buffer
                                      GL_OES_EGL_image_external_essl3
                                      GL_OES_vertex_array_object
                                      GL_KHR_texture_compression_astc_ldr
                                      ANDROID_EMU_host_side_tracing
                                      ANDROID_EMU_async_frame_commands
                                      ANDROID_EMU_gles_max_version_3_0
```


## References

- [1] [Using OpenGL ES on windows desktops via EGL](https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/)
- [2] [Android OpenGL 开发 -- EGL 的使用 {% include relref_cnblogs.html %}](https://www.cnblogs.com/wellcherish/p/12727906.html)
- [3] [OpenGL ES Emulator 横向比较 {% include relref_cnblogs.html %}](https://www.cnblogs.com/gongminmin/archive/2011/04/25/2027684.html)
- [4] [OpenGL ES Emulator 再次横向比较](http://www.klayge.org/2012/01/28/opengl-es-emulator%e5%86%8d%e6%ac%a1%e6%a8%aa%e5%90%91%e6%af%94%e8%be%83/)
- [5] [OpenGL ES Emulator 横向比较](http://www.klayge.org/2011/04/20/opengl-es-emulator%E6%A8%AA%E5%90%91%E6%AF%94%E8%BE%83/)
- [6] [全球知名 GPU 厂家（附其深度报告） {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/uANsBYLG4l2v-dUx6FIpcw)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-12-04-shader-windows-opengles-emulator.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.khronos.org/registry/OpenGL/index_es.php]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.khronos.org/bb75bed1.php" %})
- [https://developer.arm.com/tools-and-software/graphics-and-gaming/opengl-es-emulator/downloads]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/developer.arm.com/37ace0b1.html" %})
- [https://www.expreview.com/44528-all.html]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.expreview.com/a785c1d4.html" %})
- [https://developer.qualcomm.com/software/adreno-gpu-sdk/tools]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/developer.qualcomm.com/df53d96a.html" %})
- [https://powervr-graphics.github.io/]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/powervr-graphics.github.io/ad82179d.html" %})
- [http://angleproject.org/]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/angleproject.org/9fa646c0.html" %})
- [https://github.com/google/angle]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/github.com/bb7c3f0b.html" %})
- [https://zh.wikipedia.org/wiki/Adreno]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/zh.wikipedia.org/1c77f069.html" %})
- [https://docs.cocos2d-x.org/cocos2d-x/v3/en/advanced_topics/optimizing.html]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/docs.cocos2d-x.org/a4ba856f.html" %})
- [https://malideveloper.arm.com/resources/tools/mali-graphics-debugger/]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/malideveloper.arm.com/d774b230.html" %})
- [https://community.imgtec.com/developers/powervr/tools/pvrtune/]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/community.imgtec.com/2fe6cf9a.html" %})
- [https://developer.qualcomm.com/software/adreno-gpu-profiler]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/developer.qualcomm.com/a5a0a370.html" %})
- [https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.saschawillems.de/5efcfffd.html" %})
- [https://www.cnblogs.com/wellcherish/p/12727906.html]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.cnblogs.com/37af50ce.html" %})
- [https://www.cnblogs.com/gongminmin/archive/2011/04/25/2027684.html]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.cnblogs.com/04b6eb64.html" %})
- [http://www.klayge.org/2012/01/28/opengl-es-emulator%e5%86%8d%e6%ac%a1%e6%a8%aa%e5%90%91%e6%af%94%e8%be%83/]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.klayge.org/08cb85c8.html" %})
- [http://www.klayge.org/2011/04/20/opengl-es-emulator%E6%A8%AA%E5%90%91%E6%AF%94%E8%BE%83/]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/www.klayge.org/2e190eaf.html" %})
- [https://mp.weixin.qq.com/s/uANsBYLG4l2v-dUx6FIpcw]({% include relrefx.html url="/backup/2020-12-04-shader-windows-opengles-emulator.md/mp.weixin.qq.com/7f95cacc.html" %})
