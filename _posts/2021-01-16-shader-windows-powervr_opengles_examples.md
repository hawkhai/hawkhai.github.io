---
layout: post
title: "特效编程笔记 -- PowerVR SDK OpenGLES Examples"
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

最好的资料基本上是这些 GPU 厂商给的 demo，为了演示其芯片的能力，给的示例既全面又工整。


## HelloAPI

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/01_helloapi_helloapi.png" %}

Draws a basic triangle to the screen.
绘制一个基本的三角形。


### API

* OpenGL ES 2.0+


### Description

A basic tutorial that guides the user, step-by-step, through the process of drawing a basic triangle to the screen.

This includes:

initialising a window using raw OpenGL ES

drawing a triangle with a simple shader

terminating the window - depending on the platform, either after a few seconds, or when the user closes the window.


### Controls


## IntroducingPVRShell

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/02_introducingpvrshell_introducingpvrshell.png" %}

基本的 PVRShell 使用。


### API

* OpenGL ES 2.0+


### Description

和操作系统窗口打交道的库。

When using the PVR Shell, the application uses the class `pvr::Shell` as its base class, and is constructed and returned from a `pvr::newDemo` function.


### Controls


## IntroducingPVRUtils

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/03_introducingpvrutils_introducingpvrutils.png" %}

This example introduces the PVRShell library.

This example shows basic use of the PVRShell library. The PowerVR Shell handles all OS specific initialisation code. It has several built-in command-line features which allow for the specifying of attributes such as window width/height, quitting after a number of frames, taking screenshots and others.

When using the PVR Shell, the application uses the class pvr::Shell as its base class, and is constructed and returned from a pvr::newDemo function.

This example renders a `.POD` scene using a a simple vertex and fragment shader, making use of the PVRUtils library for various utility functions.


### API

* OpenGL ES 2.0+


### Description

This example demonstrates how to make the most of the PVRUtils library for handling API-agnostic utility functions such as loading shaders and creating buffers. Various API-specific utility functions are also provided such as the OpenGL ES-specific EGL context creation. The PVRUtils UIRenderer library is also used to display simple text on screen.


### Controls


## IntroducingUIRenderer

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/04_introducinguirenderer_introducinguirenderer.png" %}

This example introduces the UIRenderer from the PVRUtils library for advanced Text tasks.


### API

* OpenGL ES 2.0


### Description

The UIRenderer allows the user to create “Sprites” (2D elements) which can be grouped in 2D and/or 3D groups to be displayed as UIs or world text. This includes:

* 2D transformations (pixel and/or NDC coordinates) both single, and in a group

* anchoring on different parts of the screen or the group

* 3D transformations of groups of sprites

In this example, UIRendererer is used to display images and Unicode text, screen aligned, and with 3D transformations.


### Controls


## IntroducingPVRCamera

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/05_introducingpvrcamera_introducingpvrcamera.png" %}

Uses the PVRCamera library to get the hardware camera of a device, and applies a simple colour inversion shader.


### API

* OpenGL ES 2.0+


### Description

The PVRCamera library provides a very simple, unified API to access the video feed of an iOS or Android device as an OpenGL ES texture. This example displays the texture on the screen using a very simple shader that inverts the colours.

Note: On desktop platforms, the camera interface returns a dummy static texture to aid development. On Android N and above, the Camera permission must be given to the application.


### Controls


## BinaryShaders

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/binaryshaders_binaryshaders.png" %}

This examples shows how to store an OpenGLES shaders into a binary format and load it.


### API

* OpenGL ES 3.0+


### Description

This examples uses glGetProgramBinary and glProgramBinary to store a shader program into a binary buffer and then load it into a different shader program to be used.


### Controls


## Bumpmap

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/bumpmap_bumpmap.png" %}

This example demonstrates using a normal map to implement bumpmapping using the PowerVR Framework.


### API

* Vulkan


### Description

Bumpmapping is a technique for simulating bumps and wrinkles on the surface of an object. This is achieved by perturbing the surface normals of the object and using the perturbed normal during the illumination calculations. The result is an apparently bumpy surface rather than a perfectly smooth surface, although the surface of the underlying object is not actually changed.

This technique is used extensively in graphics applications to add perceived detail to models without adding further geometry, and could be considered the baseline for modern rendering.


### Controls


## DeferredShading

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/deferredshading_deferredshading.png" %}

This example demonstrates optimal deferred shading using Pixel Local Storage (PLS).


### API

* OpenGL ES 3.0+


### Description

Traditional rendering algorithms submit geometry and immediately apply shading effects to the rasterized primitives. Complex shading effects may require multiple draw calls (one per object per light) or render passes to produce the final pixel colour, with the geometry submitted every pass.

Deferred shading is an alternative rendering technique that submits the scene geometry once, storing per-pixel attributes into local video memory to be used in the subsequent rendering passes.

In these later passes, light volume primitives are rendered, and the per-pixel attributes contained in the buffer are retrieved at a 1:1 mapping ratio so that each pixel is shaded individually.

With the PowerVR architecture, the developer can use fast on-chip memory instead of the render target by using the Pixel Local Storage OpenGL ES extension.

Requires the extension `GL_EXT_shader_pixel_local_storage` for PLS.


### Controls

* Action1- Pause

* Action2- Orbit camera


## GameOfLife

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/gameoflife_gameoflife.png" %}

Implementation of John Conway’s Game of Life using GPGPU (GPU Compute).


### API

* OpenGL ES 3.0+


### Description

This example demonstrates how to implement John Conway’s Game of Life. It takes a starting texture
as an input and uses Compute to calculate the next generation. It then renders to screen the result.


### Controls

* Action1 to reset board configuration.

* Up/Down to change zoom levels.

* Left/Right to change board configuration.


## GaussianBlur

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/gaussianblur_gaussianblur.png" %}

Shows how to perform a extremely wide, highly optimised Gaussian Blur using compute shaders.


### API

* OpenGL ES 3.0+


### Description

This example demonstrates how to perform a 19x19 Gaussian Blur. It uses every input and output step
to blur an image by reading from an input using compute while blurring in one direction, and then writing to
the output with a fragment shader whilst blurring in the other direction.

This technique has been highly optimised for PowerVR and is very suitable for a very large convolution width.


### Controls


## IMG_framebuffer_downsample

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/imgframebufferdownsample_imgframebufferdownsample.png" %}

This example shows the power of the extension `GL_IMG_framebuffer_downsample` which enables automatic downsampling of textures.


### API

* OpenGL ES 2.0+


### Description

This example demonstrates the advantages of using the extension `GL_IMG_framebuffer_downsample`. A triangle is first rendered to a special FBO with a texture of half-size set as a downsampled texture using `glFramebufferTexture2DDownsampleIMG` and a full-size texture set as normal.

The application then renders to both the full-size texture and half-size texture, and the GPU automatically downsamples the colour attachment render. The left side of the rendered image samples from the full-size texture, and the right side samples from the half-size texture.

This extension can be extremely useful for various post processing techniques where it is desirable to generate downsampled images efficiently.


### Controls


## IMGTextureFilterCubic

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/imgtexturefiltercubic_imgtexturefiltercubic.png" %}

This example demonstrates the advantages of using the extension `GL_IMG_texture_filter_cubic` for cubic texture filtering


### API

* OpenGL ES 2.0+


### Description

This example shows the advantages of using cubic texture filtering using the extension `GL_IMG_texture_filter_cubic`. The left side of the image is rendered using traditional bilinear texture filtering with mipmapping. The right side of the image is rendered using cubic texture filtering.


### Controls


## ImageBasedLighting

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/imagebasedlighting_imagebasedlighting.png" %}

This example demonstrates Physically Based Rendering (PBR) with Image Based Lighting (IBL).


### API

* OpenGL ES 3.1+


### Description

This example has two scenes using Metallic-Roughness PBR workflow. It features two scenes, a GLTF model rederered  with  albedo, metallic roughness and emissive map, and a collection of spheres showcasing different metallic and non metallic non-texture values.
The examples uses a Diffuse map pre-computed offline from the environment map, using the lambert diffuse BRDF, and two specular maps (also calculated offline): A Pre-Filtered Environment map for different roughness values, and an Environment BRDF including the rest of the equation.
Full documentation on .. __: [https://docs.imgtec.com/PBR_with_IBL_for_PVR/topics/pbr_ibl_introduction.html](https://docs.imgtec.com/PBR_with_IBL_for_PVR/topics/pbr_ibl_introduction.html)


### Controls

* Left/Right to change the scene

* Action1 to pause.


## Multithreading

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/multithreading_multithreading.png" %}

This example shows how to use the PowerVR Framework to stream assets asynchronously into an application.


### API

OpenGL ES 3.0+


### Description

This example will display a loading screen (using UIRenderer) while assets are being loaded in, and then
switch to displaying the statue from the Bumpmap demo.


### Controls


## MultiviewVR

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/multiviewvr_multiviewvr.png" %}

Render a scene stereoscopically intended for VR hardware using the `GL_OVR_multiview` extension.


### API

* OpenGL ES 3.0+


### Description

This example introduces the `GL_OVR_multiview extension` and shows how to use it to render the scene from two different eye locations.

Two sets of FBOs are being used, one low resolution and one high resolution. The intention is to render the centre of the screen in high resolution, and the edges of the screen (which will be distorted by the VR lenses) at a lower resolution. The end result is a split screen suitable for VR.


### Controls


## Navigation2D

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/navigation2d_navigation2d.png" %}

Demonstrates parsing, processing and rendering of raw OSM data as a 2D navigational map.


### API

* OpenGL ES 2.0+


### Description

The 2D navigation example shows the complete process of creating a navigational map from raw data, in this
case Open Street Map (OSM) data.

The example demonstrates:

* loading and parsing of the XML

* the processing of the raw data

* triangulation with the ear-clipping algorithm to generate triangles

* defining the roads

* batching everything into tiles as renderable polygons.

This example also shows several rendering techniques such as:

* anti-aliased lines with outline for roads

* UI elements for road names and places of interest

* an effective tile-based approach to batching and culling the geometry.


### Controls

Q- Quit- Close the application


## Navigation3D

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/navigation3d_navigation3d.png" %}

Demonstrates parsing, processing and rendering of raw OSM data as a 3D navigational map.


### API

* OpenGL ES 2.0+


### Description

The 3D navigation example demonstrates the entire process of creating a navigational map from raw XML data,
in this case using Open Street Map (OSM) data.

The example shows how to load and parse the XML. It then shows how to process the raw data into renderable polygons which can be used by the GPU. This is achieved through triangulation, which uses the ear-clipping algorithm to generate triangles from lists of points.

This example also shows several rendering techniques such as:

* anti-aliased lines with GRLAA for road outlines

* handling of UI elements for road names and places of interest

* an effective tile based approach to batching and culling the geometry.


### Controls

Q- Quit- Close the application


## OpenCLExample

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/openclexample_openclexample.png" %}

This example demonstrates using small image convolution OpenCL kernels.


### API

* OpenGL ES 2.0+

* OpenCL


### Description

This example shows how to structure an application with OpenCL / OpenGL interoperability (or if necessary, CPU fallback) to process images on the GPU using OpenCL.

Several 3x3 convolution filters are shown:

* Gaussian Blur

* erode/dilate

* edge detection

* emboss


### Controls

* Left/Right- Change the convolution filter


## PVRScopeExample

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/pvrscopeexample_pvrscopeexample.png" %}

Demonstrates the use of PVRScope and the example graphing code.


### API

* OpenGL ES 2.0+


### Description

This example uses a simple PBR-style shader, and shows the use of PVRScope to allow an application to return performance statistics from the GPU in real time. It uses the example graphing code to render a graph of the selected counters on the screen. For further details, refer to the PVRScope User Manual.


### Controls

* Quit- Close demo

* Up/Down- Select a counter from the available list of HW counters

* Action1- Add/remove selected counter to the graph


## PVRScopeRemote

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/pvrscoperemote_pvrscoperemote.png" %}

Demonstrates the use of PVRScope’s remote communication features.


### API

* OpenGL ES 2.0+


### Description

This example shows how to use the editable data and custom mark functionality of PVRScope. PVRTune must be running and connected to an instance of PVRPerfServer running on the target device for this example to function.

A simple physically-based shader is provided with properties of Albedo, Metallicity and Glossiness. These, together with the shaders, can be edited from the PVRTune GUI. This allows immediate modification of the appearance of the statue.


### Controls

* Quit- Close demo

* PVRTune- Control example variables through PVRTune


## ParticleSystem

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/particlesystem_particlesystem.png" %}

This example shows how to implement a simple particle system using GPGPU.


### API

* OpenGL ES 3.1+


### Description

Particle systems are techniques that use a large amount of sprites to simulate phenomena that would be difficult to reproduce with conventional rendering techniques.

This example uses GPGPU (GPU compute) to implement a particle system. This is a simple integration-based simulation which is advanced and then rendered every frame strictly on the GPU, without any CPU access of that data. It also highlights the interaction between the compute and the rendering part of a simulation.


### Controls

* Quit- Close demo

* Left/Right- Decrease/increase number of particles

* Up/Down- Switch between GPU compute and CPU particle system implementation.


## PostProcessing

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/postprocessing_postprocessing.png" %}

This example demonstrates a set of heavily-optimised bloom post-processing implementations.


### API

* OpenGL ES 3.0+


### Description

This example demonstrates a set of heavily optimised bloom post-processing implementations including:

* Reference implementation of a separated Gaussian Blur.

* Linear sampler-optimised separated Gaussian Blur.

* Sliding average compute-based separated Gaussian Blur.

* Linear sampler-optimised separated Gaussian Blur with samples of negligible value truncated. This means the approximate blurs can be achieved with far fewer samples.

* Hybrid Gaussian Blur using the truncated separated Gaussian Blur along with a sliding average-based Gaussian Blur.

* Kawase Blur - Framebuffer post-processing effects in “DOUBLE-S.T.E.A.L.” aka “Wreckless”.

* Dual Filter - Bandwidth-efficient rendering - siggraph2015-mmg-marius.

* Tent Filter - Next generation post-processing in “Call Of Duty Advanced Warfare”.

Other than the Dual Filter and Tent Filter, the bloom post-processing implementations follow a similar high-level pattern:

1.  Downsampling the brighter regions of an input image to a lower resolution.

2.  Several post-process passes, each working from the output of the previous pass, rendering to intermediate textures.

3.  The resulting blurred image is then composited onto the original image to create a smooth bloom around the brighter regions.


### Controls

* Left/Right - Cycle through the various bloom implementations

* Up/Down - Increase/decrease the size of the bloom intensity

* Action1 - Pause

* Action2 - Enable/disable rendering of bloom only

* Quit - Close the application


## Skinning

{% include image.html url="/assets/images/210116-shader-windows-powervr_~89/skinning_skinning.png" %}

This example shows a scene with a combination of a skinned, bumpmapped character with non-skinned, non-bumpmapped objects.


### API

* OpenGL ES 3.0+


### Description

Skinning is the act of animating a vertex over time given a set (palette) of matrices, and a known set of blend weights assigned to those matrices.

The Skinning example shows a skinned character in combination with bump mapping. For each frame, the matrix palette is recomputed based on time.

PVRAssets and POD files support skinning with either full transformation matrices, or Quaternion rotation with scaling and translation vectors. The provided POD file contains matrix animation. A shader storage buffer object is used to support a dynamic number of bones.


### Controls

* Action1/2/3- Pause

* Esc- Close

-----

<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.imgtec.com/PBR_with_IBL_for_PVR/topics/pbr_ibl_introduction.html]({% include relref.html url="/backup/2021-01-16-shader-windows-powervr_opengles_examples.md/docs.imgtec.com/bca9d913.html" %})
