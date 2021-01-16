---
layout: post
title: "特效编程笔记 -- PowerVR SDK OpenGLES Examples"
author:
location: "珠海"
categories: ["特效"]
tags: ["特效", "OpenGL"]
toc: true
toclistyle: none
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

最好的资料基本上是这些 GPU 厂商给的 demo，为了演示其芯片的能力，给的示例既全面又工整。

翻译完了。总体说来，目前 GPU 还停留在 PBR（基于物理的渲染）的时代，实时光线追踪 还处于萌芽状态。
也只有实现了 实时光线追踪，才可以达到分不清现实和游戏的程度。其计算量差不多是现有 GPU 一万倍。这也是在常规游戏中很难见到大规模透明反光物体的原因。


## HelloAPI

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/01_helloapi_helloapi.png" %}

绘制一个基本的三角形。


### API

* OpenGL ES 2.0+


## IntroducingPVRShell

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/02_introducingpvrshell_introducingpvrshell.png" %}

基本的 PVRShell 使用。


### API

* OpenGL ES 2.0+


### Description

用 PVRShell 库和操作系统窗口打交道的库。


## IntroducingPVRUtils

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/03_introducingpvrutils_introducingpvrutils.png" %}

用一个简单的顶点着色器和片段着色器 渲染一个 `.POD` 场景。基于 PVRUtils 库实现。
PVRUtils UIRenderer 库可用来在屏幕上显示简单的字符串。


### API

* OpenGL ES 2.0+


## IntroducingUIRenderer

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/04_introducinguirenderer_introducinguirenderer.png" %}

高级文字绘制。用 PVRUtils 函数库，UIRenderer。


### API

* OpenGL ES 2.0


### Description

可以创建 “Sprites” (2D elements)，还包括：2D 变换，3D 变换。


## IntroducingPVRCamera

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/05_introducingpvrcamera_introducingpvrcamera.png" %}

用 PVRCamera 库从硬件摄像头获取数据，并进行相应的 shader 颜色反转。


### API

* OpenGL ES 2.0+


## BinaryShaders

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/binaryshaders_binaryshaders.png" %}

演示怎么存储和价值二进制形式的 OpenGLES shaders。


### API

* OpenGL ES 3.0+


### Description

用 `glGetProgramBinary` and `glProgramBinary` 实现。


## Bumpmap 凹凸映射

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/bumpmap_bumpmap.png" %}

用 PowerVR Framework，实现法线贴图的凹凸贴图。


### API

* Vulkan


## DeferredShading

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/deferredshading_deferredshading.png" %}

基于 Pixel Local Storage (PLS) 实现延迟渲染。


### API

* OpenGL ES 3.0+


### Description

延迟渲染。先渲染几何体，然后再把只能看到的部分重新渲染计算光照。
基于 PowerVR，开发者可以用 fast on-chip memory 替代 render。
需要扩展：`GL_EXT_shader_pixel_local_storage` for PLS.


### Controls

* Action1- Pause
* Action2- Orbit camera


## GameOfLife

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/gameoflife_gameoflife.png" %}

基于 GPGPU (GPU Compute) 实现 John Conway’s Game of Life。


### API

* OpenGL ES 3.0+


### Controls

* Action1 to reset board configuration.
* Up/Down to change zoom levels.
* Left/Right to change board configuration.


## GaussianBlur

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/gaussianblur_gaussianblur.png" %}

基于 compute shaders 实现 高斯模糊 算法。


### API

* OpenGL ES 3.0+


### Description

实现 19x19 高斯模糊，算法优化过，适于大规模卷积运算。


## IMG_framebuffer_downsample 纹理下采样

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/imgframebufferdownsample_imgframebufferdownsample.png" %}

扩展 `GL_IMG_framebuffer_downsample`。实现自动纹理下采样。


### API

* OpenGL ES 2.0+


### Description

`glFramebufferTexture2DDownsampleIMG`。适用于 post processing 技术。


## IMGTextureFilterCubic

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/imgtexturefiltercubic_imgtexturefiltercubic.png" %}

扩展 `GL_IMG_texture_filter_cubic` 实现 cubic texture filtering。


### API

* OpenGL ES 2.0+


### Description

左边是传统的 bilinear texture filtering，右边是 cubic texture filtering。


## ImageBasedLighting 光照

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/imagebasedlighting_imagebasedlighting.png" %}

基于 Image Based Lighting (IBL) 实现 Physically Based Rendering (PBR)。


### API

* OpenGL ES 3.1+


### Description

This example has two scenes using Metallic-Roughness PBR workflow. It features two scenes, a GLTF model rederered with albedo, metallic roughness and emissive map, and a collection of spheres showcasing different metallic and non metallic non-texture values. The examples uses a Diffuse map pre-computed offline from the environment map, using the lambert diffuse BRDF, and two specular maps (also calculated offline): A Pre-Filtered Environment map for different roughness values, and an Environment BRDF including the rest of the equation.
Full documentation on [https://docs.imgtec.com/PBR_with_IBL_for_PVR/topics/pbr_ibl_introduction.html](https://docs.imgtec.com/PBR_with_IBL_for_PVR/topics/pbr_ibl_introduction.html)


### Controls

* Left/Right to change the scene
* Action1 to pause.


## Multithreading

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/multithreading_multithreading.png" %}

采用 PowerVR Framework，把一个数据流的资源异步传到应用程序中。


### API

OpenGL ES 3.0+


## MultiviewVR

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/multiviewvr_multiviewvr.png" %}

渲染一个立体的 VR 硬件场景。基于扩展：`GL_OVR_multiview`。


### API

* OpenGL ES 3.0+


### Description

采用两个 FBO。一个低分辨率，一个高分辨率。VR 设备一般中心需要高分辨率，边缘会被拉伸，采用低分辨率。


## Navigation2D

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/navigation2d_navigation2d.png" %}

基于原始的 Open Street Map (OSM) 数据，实现 2D 导航地图。


### API

* OpenGL ES 2.0+


### Description

* 用 ear-clipping 生成三角形。
* 反锯齿。


## Navigation3D

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/navigation3d_navigation3d.png" %}

基于 raw OSM data 实现 3D 地图导航。


### API

* OpenGL ES 2.0+


### Description

* 基于 GRLAA 实现反锯齿。


## OpenCLExample

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/openclexample_openclexample.png" %}

演示 小图片 卷积 OpenCL 核。


### API

* OpenGL ES 2.0+
* OpenCL


### Description

OpenCL / OpenGL 交互 (or if necessary, CPU fallback)，在 GPU 上，用 OpenCL 处理图片。

几个 3x3 卷积：

* 高斯模糊 高斯模糊
* erode/dilate 腐蚀 / 膨胀
* edge detection 边缘检测
* emboss 浮雕。


### Controls

* Left/Right- Change the convolution filter


## PVRScopeExample

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/pvrscopeexample_pvrscopeexample.png" %}

PVRScope 使用演示。


### API

* OpenGL ES 2.0+


### Description

采用 PBR-style shader 基于 GPU 实时统计数据。


### Controls

* Quit- Close demo
* Up/Down- Select a counter from the available list of HW counters
* Action1- Add/remove selected counter to the graph


## PVRScopeRemote

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/pvrscoperemote_pvrscoperemote.png" %}

演示 PVRScope 的远程通信能力。


### API

* OpenGL ES 2.0+


### Description

PVRTune 必须连接上一个目标设备 PVRPerfServer 实例。
可以实现 Albedo（反照率）, Metallicity（金属度） and Glossiness（光泽度） 的实时编辑和预览。


### Controls

* Quit- Close demo
* PVRTune- Control example variables through PVRTune


## 粒子系统

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/particlesystem_particlesystem.png" %}

基于 GPGPU 实现一个 粒子系统。


### API

* OpenGL ES 3.1+


### Controls

* Quit- Close demo
* Left/Right- Decrease/increase number of particles
* Up/Down- Switch between GPU compute and CPU particle system implementation.


## PostProcessing

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/postprocessing_postprocessing.png" %}

heavily-optimised bloom post-processing 实现。


### API

* OpenGL ES 3.0+


### Description

* 一个高斯模糊参考实现
* 线性 sampler-optimised 高斯模糊实现
* 基于滑动平均计算的高斯模糊
* 线性 sampler-optimised 高斯模糊实现，基于 negligible value truncated，同样的效果只需要更少的数据。
* Hybrid 高斯模糊 using the truncated separated 高斯模糊 along with a sliding average-based 高斯模糊
* Kawase Blur - Framebuffer post-processing effects in “DOUBLE-S.T.E.A.L.” aka “Wreckless”.
* Dual Filter - Bandwidth-efficient rendering - siggraph2015-mmg-marius.
* Tent Filter - Next generation post-processing in “Call Of Duty Advanced Warfare”.

Other than the Dual Filter and Tent Filter, the bloom post-processing implementations follow a similar high-level pattern:
1. Downsampling the brighter regions of an input image to a lower resolution.
2. Several post-process passes, each working from the output of the previous pass, rendering to intermediate textures.
3. The resulting blurred image is then composited onto the original image to create a smooth bloom around the brighter regions.


### Controls

* Left/Right - Cycle through the various bloom implementations
* Up/Down - Increase/decrease the size of the bloom intensity
* Action1 - Pause
* Action2 - Enable/disable rendering of bloom only
* Quit - Close the application


## Skinning 蒙皮和骨骼

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/skinning_skinning.png" %}

蒙皮的凹凸贴图角色与非蒙皮的凹凸贴图对象的组合。


### API

* OpenGL ES 3.0+


### Description

PVRAssets 和 POD 文件支持使用完全变换矩阵进行蒙皮，或者使用缩放和平移向量进行四元数旋转。提供的 POD 文件包含矩阵动画。着色器存储缓冲区对象用于支持动态数量的骨骼。


### Controls

* Action1/2/3- Pause
* Esc- Close

-----

<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.imgtec.com/PBR_with_IBL_for_PVR/topics/pbr_ibl_introduction.html]({% include relref.html url="/backup/2021-01-16-shader-windows-powervr_opengles_examples.md/docs.imgtec.com/bca9d913.html" %})
