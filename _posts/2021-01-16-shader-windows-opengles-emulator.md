---
layout: post
title: "特效编程笔记 -- OpenGL ES Emulator for Windows / PowerVR, Adreno, Mali"
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


## Imagination PowerVR

The PVRVFrame library filenames are:

* libEGL.dll (EGL)
* libGLES_CM.dll (OpenGL ES 1.x)
* libGLESv2.dll (OpenGL ES 2.0 and 3.x)

The PowerVR SDK has a number of third-party dependencies, each of which may have their own license:

* [glm {% include relref_github.html %}](https://github.com/g-truc/glm): OpenGL Mathematics
* [pugixml {% include relref_github.html %}](https://github.com/zeux/pugixml): Light-weight, simple and fast XML parser for C++ with XPath support
* [concurrentqueue {% include relref_github.html %}](https://github.com/cameron314/concurrentqueue): A fast multi-producer, multi-consumer lock-free concurrent queue for C++11
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
- [https://github.com/g-truc/glm]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/277752ea.html" %})
- [https://github.com/zeux/pugixml]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/9f7a73a3.html" %})
- [https://github.com/cameron314/concurrentqueue]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/dcb43f62.html" %})
- [https://github.com/KhronosGroup/glslang]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/da49f811.html" %})
- [https://github.com/syoyo/tinygltf]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/98011aa3.html" %})
- [https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/b9ef732d.html" %})
- [https://github.com/KhronosGroup/Vulkan-Docs]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/github.com/ccfbd39a.html" %})
- [https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/www.saschawillems.de/5efcfffd.html" %})
- [https://www.cnblogs.com/wellcherish/p/12727906.html]({% include relref.html url="/backup/2021-01-16-shader-windows-opengles-emulator.md/www.cnblogs.com/37af50ce.html" %})
