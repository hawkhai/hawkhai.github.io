---
layout: post
title: "特效编程笔记 -- OpenGL ES Emulator for Windows / PowerVR Adreno Mali"
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

OpenGL ES is an embedded version of OpenGL mostly used on mobile devices that offer only limited GPU capabilities compared to modern desktop GPUS.

{% include image.html url="/assets/images/210116-shader-windows-opengles~28/20210117002134.png" %}

EGL is a native platform interface that connects the windowing systems to one of Khronos’ APIs, e.g. OpenGL ES.

相关下载：<https://www.khronos.org/registry/OpenGL/index_es.php>


## OpenGL ES Emulator 横向比较

PowerVR、Adreno、Mali 三大主流移动 GPU。[from](https://www.expreview.com/44528-all.html)

厂商 | 名称
---- | ----
AMD | ~~OpenGL ES 2.0 Emulator~~ 2008 年卖给了高通（Qualcomm）
ARM | OpenGL ES 2.0 Emulator v1.2 [ARM Mali Emulator](https://developer.arm.com/tools-and-software/graphics-and-gaming/opengl-es-emulator/downloads)
Qualcomm | Adreno SDK 2.2 [Adreno GPU SDK](https://developer.qualcomm.com/software/adreno-gpu-sdk/tools)
NVIDIA | ~~Windows OpenGL ES 2.0 Emulator~~ Tegra 没有找到地方下载
PowerVR | PowerVR SDK [PowerVR Graphics SDK {% include relref_github.html %}](https://powervr-graphics.github.io/)

费不尽力的老力，都下载下来，整理好了：<https://gitee.com/hawkhai/opengl-3rd.git>


## ARM Mali


## Qualcomm Adreno

Welcome to QUALCOMM's Adreno™ Software Development Kit (SDK). This is version 3.0.0 of the SDK that includes support for OpenGL ES 2.0 and 3.0 through PC emulation under Windows XP. The SDK is provided as a development environment for QUALCOMM's Adreno™ graphics processors, and is intended to help ease the learning curve of said technology.


### OpenGL ES Unified Emulators

QUALCOMM's OpenGL ES 2.0 / 3.0 Emulator is designed to emulate functionality exposed by QUALCOMM's Adreno™ GPUs. The purpose of this emulator is to aid developers in their design of OpenGL ES games and applications. The emulator allows developers to get a head start designing their graphics code before hardware supporting OpenGL ES is available, and even after this hardware becomes available developing on a PC is often advantageous due to superior developer and debugging tools.

The emulator has five major features:

* Support of core OpenGL ES 2.0 / 3.0 functionality
* Support for many important OpenGL ES 2.0 extensions
* Support of core OpenGL ES 1.x functionality
* Support for many OpenGL ES 1.x extensions
* Support for EGL 1.3


### About Demos

Samples are to tutorials, what demos are to samples. While samples showcase complex effects that may make use of multiple tutorial concepts, demos make use of a combination of sample effects to show off the capabilities of QUALCOMM mobile graphics hardware.


### About Tutorials

Tutorials are example programs that demonstrate a specific 2D or 3D capability of our hardware. These programs are simpler to understand than sample applications, and are the recommended starting point for anyone new to OpenGL ES. Additionally, tutorials do not rely upon a framework, and do not require user input.


### About Samples

**Samples are a little bit more complex than tutorials.** They show how to achieve interesting effects using our hardware sometimes through the use of a combination of multiple tutorial techniques. Samples make use of a common code base called the "Sample Framework" that provides a platform agnostic development environment.

进阶路线：$$Tutorials \leadsto Samples \leadsto Demos$$。
If you are new to OpenGL ES 2.0, then we suggest that you go through the tutorials first, and then move on to sample programs. Currently there are no tutorials for OpenSL ES.


### opengl adreno 仿真报错

**Could not Load from Adreno device driver: eglGetError**
[answer](https://stackoverflow.com/questions/22971187/how-to-fix-could-not-load-from-adreno-device-drivereglgeterror)

* 将 adreno 中的 `AdrenoSDK\Bin_d\driver` 文件夹拷贝执行文件夹位置。
* After a long struggle and some answers from [qualcomm developer site](https://developer.qualcomm.com/forum/qdn-forums/maximize-hardware/mobile-gaming-graphics-adreno/27651) got the solution.
Install the x86 version of this redist. <http://www.microsoft.com/en-us/download/details.aspx?id=30679>

这个加载逻辑有点怪。如果都搞好了，win32 的加载顺序包含：

{% include image.html url="/assets/images/210116-shader-windows-opengles~28/20210116132811.png" %}


## Imagination PowerVR

PVRVFrame is provided for platforms without native support for OpenGL ES but where OpenGL is supported.

PVRVFrame is included as part of the PowerVR SDK and provides a set of desktop emulation libraries for OpenGL ES wrapping desktop OpenGL allowing deployment of OpenGL ES applications on desktop Windows, macOS, and Linux which can help to speed up development times and improve productivity.

The PVRVFrame library filenames are:

* libEGL.dll (EGL)
* libGLES_CM.dll (OpenGL ES 1.x)
* libGLESv2.dll (OpenGL ES 2.0 and 3.x)

The PowerVR SDK has a number of third-party dependencies, each of which may have their own license:

* [glm {% include relref_github.html %}](https://github.com/g-truc/glm): OpenGL Mathematics
* [pugixml {% include relref_github.html %}](https://github.com/zeux/pugixml): Light-weight, simple and fast XML parser for C++ with XPath support
* **[concurrentqueue {% include relref_github.html %}](https://github.com/cameron314/concurrentqueue)**: A fast multi-producer, multi-consumer lock-free concurrent queue for C++11
* [glslang {% include relref_github.html %}](https://github.com/KhronosGroup/glslang): Shader front end and validator
* [tinygltf {% include relref_github.html %}](https://github.com/syoyo/tinygltf): Header only C++11 tiny glTF 2.0 library
* [vma {% include relref_github.html %}](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator): Vulkan Memory Allocator
* [vulkan {% include relref_github.html %}](https://github.com/KhronosGroup/Vulkan-Docs): Sources for the formal documentation of the Vulkan API


## References

- [1] [Using OpenGL ES on windows desktops via EGL](https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/)
- [2] [Android OpenGL 开发 -- EGL 的使用 {% include relref_cnblogs.html %}](https://www.cnblogs.com/wellcherish/p/12727906.html)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [https://www.khronos.org/registry/OpenGL/index_es.php]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/www.khronos.org/bb75bed1.php" %})
- [https://www.expreview.com/44528-all.html]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/www.expreview.com/a785c1d4.html" %})
- [https://developer.arm.com/tools-and-software/graphics-and-gaming/opengl-es-emulator/downloads]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/developer.arm.com/37ace0b1.html" %})
- [https://developer.qualcomm.com/software/adreno-gpu-sdk/tools]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/developer.qualcomm.com/df53d96a.html" %})
- [https://powervr-graphics.github.io/]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/powervr-graphics.github.io/ad82179d.html" %})
- [https://gitee.com/hawkhai/opengl-3rd.git]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/gitee.com/3cdcc6e8.git" %})
- [https://stackoverflow.com/questions/22971187/how-to-fix-could-not-load-from-adreno-device-drivereglgeterror]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/stackoverflow.com/e2968e58.html" %})
- [https://developer.qualcomm.com/forum/qdn-forums/maximize-hardware/mobile-gaming-graphics-adreno/27651]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/developer.qualcomm.com/94e2f3fd.html" %})
- [http://www.microsoft.com/en-us/download/details.aspx?id=30679]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/www.microsoft.com/1e45c851.aspx" %})
- [https://github.com/g-truc/glm]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/277752ea.html" %})
- [https://github.com/zeux/pugixml]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/9f7a73a3.html" %})
- [https://github.com/cameron314/concurrentqueue]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/dcb43f62.html" %})
- [https://github.com/KhronosGroup/glslang]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/da49f811.html" %})
- [https://github.com/syoyo/tinygltf]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/98011aa3.html" %})
- [https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/b9ef732d.html" %})
- [https://github.com/KhronosGroup/Vulkan-Docs]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/ccfbd39a.html" %})
- [https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/www.saschawillems.de/5efcfffd.html" %})
- [https://www.cnblogs.com/wellcherish/p/12727906.html]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/www.cnblogs.com/37af50ce.html" %})
