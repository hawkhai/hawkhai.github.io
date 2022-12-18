---
layout: post
title: "图形学 -- QUALCOMM Adreno™ SDK Tutorials 动态图概览"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
toc: true
toclistyle: none
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

QUALCOMM Adreno™ SDK Readme ReleaseSpecific/IntroductionToAdrenoSDK.htm


## About Tutorials and Samples

Samples are a little bit more complex than tutorials.

很多学习资料都不如这些 sdk 啊，dx 啊 什么的 自带的 Samples 例子好。截图备份一下。[皮毛渲染 {% include relref_github.html %}](https://chengkehan.github.io/Fur.html)

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/shaderdemo.bmp" caption="SDKHelp/ShaderDemo.htm" %}


## OpenGL ES 2.0 Tutorials

ReleaseSpecific/Tutorials.htm
SDKHelp/OpenGLES2.0Samples.htm

Bloom
DepthOfField
ImageEffects
Lighting
MotionBlur
NormalMapping
NPR
ParallaxMapping
PointSprites
ProceduralTexture
ProjectiveShadows
Reflections
ShadowMap
ShadowVolume
ShallowWater
SkinnedMesh
SkinnedMesh2


### 01_CreateWindow

Shows how to use EGL to create an empty rendering window.


### 02_ConfigureFrameBuffer

Shows how to configure the framebuffer for 16 and 32-bit displays. Detects the current resolution and configures the framebuffer accordingly.


### 03_DrawTriangle

Shows how to render a triangle with a simple vertex and fragment shader.


### 04_PortraitAndLandscape

Shows how to render geometry in landscape and portrait mode. Press the * key to change the orientation.


### 05_NonInterleavedVBO

Shows how to use vertex buffer objects where each vertex attribute is stored in a seperate buffer.


### 06_InterleavedVBO

Shows how to use interleaved vertex buffer objects.


### 07_Transforms

Shows how to transform a 3D object with model, view, and projection matrix transforms. This program shows how to pass transforms into a shader program and use them in a vertex shader.


### 08_SimpleTexture

Shows how to do simple texture mapping.


### 09_CompressedTexture

Shows how to do texture mapping with the ATC compressed texture format.


### 10_TextureProperties

Shows how to use various texture properties.


### 11_MultiTexture

Shows how to do multi-texturing. It applies 2 textures to the object, a wood texture and a scrolling clouds texture on top of it.


### 12_CubemapTexture

Shows how to use cubemap textures.


### 13_CompressedVertices

Shows how to compress vertex data with 16-bit floats and the GL_INT_10_10_10_2 extension.


### 14_StencilBuffer

Shows how to use the stencil buffer to limit render regions.


### 15_RenderToTexture

Shows how to render to an offscreen texture using a frame buffer object. The scene is rendered to the color buffer and also to an offscreen texture. The texture is then displayed in the upper right corner.


## OpenGL ES 3.0 Tutorials

SDKHelp/OpenGLES3.0Samples.htm


### 16_RenderToTexture30

Tutorial to show how to use FBOs to render to a texture using OpenGL ES 3.0.


### 17_FBOTextureFormats30

Tutorial showing different texture formats when rendering to a simple texture using an FBO.


### 18_InterleavedVBO-DrawArraysInstanced30

Tutorial showing how to render a simple quad using a vertex buffer object (VBO). This version uses glDrawArraysInstanced.


### 19_InterleavedVBO-DrawRangeElements30

Tutorial showing how to render a simple quad using a vertex buffer object (VBO). This version uses glDrawRangeElements.


### 20_Texture2DArray30

Tutorial showing how to render a simple quad using a vertex buffer object (VBO). This version uses glDrawArraysInstanced.


### 21_PixelBufferObject30

Tutorial to show how to use pixel buffer objects.


### 22_TransformFeedback30

Tutorial to show how to use transform feedback to return the number of rendered primitives.


### 23_BlitFramebuffer30

Tutorial to show how to blit from one framebuffer to another.


### 24_MultisampleFramebuffer30

Tutorial showing how to use multiple framebuffers.


### 25_FramebufferTextureLayer

Tutorial showing how to specify a single texture layer as the GL_COLOR_ATTACHMENT0 for a framebuffer object.

CascadedShadowMaps
CompressedGeometry
DepthOfField
HDRTexture
NonPhotorealisticRendering
PointSprites
PhysicallyBasedLighting
ShadowMap
SkyDome
TextureSynthesis
ToneMapping


## Tools and Utilities

ReleaseSpecific/ToolsAndUtilities.htm


### SDK Browser


### OpenGL ES 2.0 / 3.0 Emulators


### ES_Control


### Binary Shader Compilation


### TextureCompressionToolSuite


### FBXModelConverter


### Texture Converter


### Qstrip


### FontMaker


### MeshConverter


### ResourcePacker


### ShaderPreprocessor


### VGFontParser


### Texcompress


### PC2AndroidBridge

<p class="counter-reset h2counter"></p>


## Accel.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/accel_d.webp" %}


## AdrenoShaders.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/adrenoshaders_d.webp" %}


## BandwidthTest.exe


## BlitFramebufferOGLES30.exe


## Bloom.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/bloom_d.webp" %}


## CascadedShadowMaps.exe


## ClothSimCLGLES.exe


## CompressedGeometry.exe


## CompressedTexture.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/compressedtexture_d.png" %}


## CompressedVertices.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/compressedvertices_d.webp" %}


## ComputeShader.exe


## Concurrency.exe


## ConfigureFrameBuffer.exe


## CreateWindow.exe


## CubemapReflection.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/cubemapreflection_d.webp" %}


## CubemapTexture.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/cubemaptexture_d.webp" %}


## DepthOfField.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/depthoffield_d.webp" %}


## DepthOfFieldOGLES30.exe


## DeviceQuery.exe


## Disintegrate.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/disintegrate_d.webp" %}


## DotProduct.exe


## DrawTriangle.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/drawtriangle_d.webp" %}


## ES_Control.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/es_control.webp" %}


## FboMultiSample.exe


## FboNoAttachment.exe


## FboShadow.exe


## FBOTextureFormatsOGLES30.exe


## FbxModelConverter.exe


## FFT1D.exe


## FFT2D.exe


## FontMaker.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/fontmaker.webp" %}


## FrameBufferTextureLayerOGLES30.exe


## Gyro.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/gyro_d.webp" %}


## HDRTexture.exe


## ImageBoxFilter.exe


## ImageEffects.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/imageeffects_d.webp" %}


## ImageMedianFilter.exe


## ImageRecursiveGaussianFilter.exe


## ImageSobelFilter.exe


## InterleavedVBO2OGLES30.exe


## InterleavedVBO.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/interleavedvbo_d.webp" %}


## InterleavedVBOOGLES30.exe


## InteropCLGLES.exe


## Lighting.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/lighting_d.webp" %}


## MatrixMatrixMul.exe


## MatrixTranspose.exe


## MatrixVectorMul.exe


## MeshConverter.exe


## MotionBlur.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/motionblur_d.webp" %}


## MultiSample.exe


## MultisampleFramebufferOGLES30.exe


## MultiTexture.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/multitexture_d.webp" %}


## NonInterleavedVBO.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/noninterleavedvbo_d.webp" %}


## NormalMapping.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/normalmapping_d_3.webp" %}


## NPR30.exe


## NPR.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/npr_d.webp" %}


## ParallaxMapping.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/parallaxmapping_d_2.webp" %}


## ParallelPrefixSum.exe


## ParticleSystem.exe


## ParticleSystemCLGLES.exe


## PC2Android.exe


## PhysicallyBasedLighting.exe


## PixelBufferObjectsOGLES30.exe


## PointSprites.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/pointsprites_d.webp" %}


## PortraitAndLandscape.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/portraitandlandscape_d.webp" %}


## PostProcessCLGLES.exe


## ProceduralTexture.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/proceduraltexture_d_2.webp" %}


## ProjectiveShadows.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/projectiveshadows_d.webp" %}


## QCompress.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/qcompress.webp" %}


## RenderToTexture.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/rendertotexture_d.webp" %}


## RenderToTextureOGLES30.exe


## ResourcePacker.exe


## Robot.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/robot_d_2.webp" %}


## ShaderPreprocessor.exe


## ShadowMap30.exe


## ShadowMap.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/shadowmap_d.webp" %}


## ShadowVolume.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/shadowvolume_d.webp" %}


## SILS.exe


## SimpleTexture.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/simpletexture_d.webp" %}


## Skinning2.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/skinning2_d.webp" %}


## Skinning.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/skinning_d.webp" %}


## SkyDome.exe


## SSO.exe


## StencilBuffer.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/stencilbuffer_d.webp" %}


## SWE.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/swe_d_2.webp" %}


## Texture2DArrayOGLES30.exe


## TextureProperties.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/textureproperties_d.webp" %}


## TextureSynthesis.exe


## ToneMapping.exe


## TransformFeedbackOGLES30.exe


## Transforms.exe

{% include image.html url="/assets/images/210108-gles-qualcomm-adreno/transforms_d.webp" %}


## VectorAdd.exe



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-08-gles-qualcomm-Adreno.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://chengkehan.github.io/Fur.html]({% include relrefx.html url="/backup/2021-01-08-gles-qualcomm-Adreno.md/chengkehan.github.io/2d825edb.html" %})
