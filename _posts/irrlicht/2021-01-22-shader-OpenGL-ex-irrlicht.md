---
layout: post
title: "图形学笔记 -- Irrlicht OpenGL 扩展支持 整理文档"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL", "Irrlicht"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

$$NV/AMD/ATI \leadsto EXT \leadsto ARB \leadsto GL$$

一个 3D 引擎为了更好的性能，就只能适配这些不同的硬件。Irrlicht 用到的 284 个 API。
这些 API 就像后山上的野花，**一簇一簇的**，这个也是 状态机 C 风格函数接口的特点。

开始觉得很难，学了一段时间的 OpenGL，觉得也就那样，尝试改造 3D 引擎，发现一千多个 API，常用的 284 个，而且 OpenGL & OpenGL ES 存在巨大差异，不同硬件之间还存在差异，唏嘘不已。

* GLES 扩展 333 个：<https://www.khronos.org/registry/OpenGL/index_es.php>
* OpenGL 扩展 554 个：<https://www.khronos.org/registry/OpenGL/index_gl.php>
* *docs.GL* <http://docs.gl/>
* *MicrosoftDocs OpenGL* <https://github.com/MicrosoftDocs/win32/tree/docs/desktop-src/OpenGL>

OpenGL ES & OpenGL 存在大量 API 交叉的情况，为了兼容，很多 API 采用 wglGetProcAddress 函数指针的形式。包含厂商后缀的都是 wglGetProcAddress，$$\color{pink}{ogladdr}$$。分了五类：

* 只支持 GLES: $$\color{blue}{gles}$$（大概 36 个）
* 只支持 OpenGL & wglGetProcAddress: $$\color{pink}{ogladdr}$$（大概 140 个）
* 只支持 OpenGL: $$\color{red}{ogl}$$（大概 43 个）
* 两个都支持 OpenGL & wglGetProcAddress: $$\color{blue}{gles}\&\color{pink}{ogladdr}$$（大概 27 个）
* 两个都支持：$$\color{blue}{gles}\&\color{red}{ogl}$$（大概 38 个）

{'$$\color{blue}{gles}$$': 36, '$$\color{blue}{gles}\&\color{pink}{ogladdr}$$': 27, '$$\color{pink}{ogladdr}$$': 140, '$$\color{red}{ogl}$$': 43, '$$\color{blue}{gles}\&\color{red}{ogl}$$': 38}


## 遮挡查询 occlusion query

* **glBeginOcclusionQueryNV**, **glBeginQueryARB** $$\bbox[yellow]{Queries}$$  $$\color{pink}{ogladdr}$$ // extGlBeginQuery
* **glDeleteOcclusionQueriesNV**, **glDeleteQueriesARB** $$\bbox[yellow]{Queries}$$  $$\color{pink}{ogladdr}$$ // extGlDeleteQueries
* **glEndOcclusionQueryNV**, **glEndQueryARB** $$\bbox[yellow]{Queries}$$  $$\color{pink}{ogladdr}$$ // extGlEndQuery
* **glGenOcclusionQueriesNV**, **glGenQueriesARB** $$\bbox[yellow]{Queries}$$  $$\color{pink}{ogladdr}$$ // extGlGenQueries
* **glGetOcclusionQueryivNV**, **glGetQueryObjectivARB** $$\bbox[yellow]{Queries}$$  $$\color{pink}{ogladdr}$$ // extGlGetQueryObjectiv
* **glGetOcclusionQueryuivNV**, **glGetQueryObjectuivARB** $$\bbox[yellow]{Queries}$$  $$\color{pink}{ogladdr}$$ // extGlGetQueryObjectuiv
* **glGetQueryivARB** $$\bbox[yellow]{Queries}$$  $$\color{pink}{ogladdr}$$ // extGlGetQueryiv
* **glIsOcclusionQueryNV**, **glIsQueryARB** $$\bbox[yellow]{Queries}$$  $$\color{pink}{ogladdr}$$ // extGlIsQuery


## OpenGL WGL

* **wglCreateContext** $$\color{red}{ogl}$$
* **wglDeleteContext** $$\color{red}{ogl}$$
* **wglGetCurrentDC** $$\color{red}{ogl}$$
* **wglGetProcAddress** $$\color{red}{ogl}$$
* **wglMakeCurrent** $$\color{red}{ogl}$$
* **wglChoosePixelFormatARB** $$\color{pink}{ogladdr}$$ // ? 请求并选择一个匹配的像素格式
* **wglCreateContextAttribsARB** $$\color{pink}{ogladdr}$$ // ? 创建和使用 OpenGL
* **wglGetExtensionsStringARB** $$\color{pink}{ogladdr}$$ // ? 检查是否支持 WGL_ARB_extensions_string 扩展
* **wglSwapIntervalEXT** $$\color{pink}{ogladdr}$$ // extGlSwapInterval 是否启用垂直同步


## GLES EGL

* **eglBindAPI** $$\color{blue}{gles}$$
* **eglChooseConfig** $$\color{blue}{gles}$$
* **eglCreateContext** $$\color{blue}{gles}$$
* **eglCreateWindowSurface** $$\color{blue}{gles}$$
* **eglDestroyContext** $$\color{blue}{gles}$$
* **eglDestroySurface** $$\color{blue}{gles}$$
* **eglGetConfigAttrib** $$\color{blue}{gles}$$
* **eglGetConfigs** $$\color{blue}{gles}$$
* **eglGetDisplay** $$\color{blue}{gles}$$
* **eglGetError** $$\color{blue}{gles}$$
* **eglInitialize** $$\color{blue}{gles}$$
* **eglMakeCurrent** $$\color{blue}{gles}$$
* **eglSwapBuffers** $$\color{blue}{gles}$$
* **eglSwapInterval** $$\color{blue}{gles}$$
* **eglTerminate** $$\color{blue}{gles}$$


## glUniform 系列

* **glUniform1fv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniform1iv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniform1uiv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniform2fv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniform2iv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniform2uiv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniform3fv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniform3iv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniform3uiv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniform4fv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniform4iv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniform4uiv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniformMatrix2fv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniformMatrix2x3fv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniformMatrix2x4fv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniformMatrix3fv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniformMatrix3x2fv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniformMatrix3x4fv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniformMatrix4fv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
* **glUniformMatrix4x2fv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniformMatrix4x3fv** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$
* **glUniform1fvARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniform1fv
* **glUniform1ivARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniform1iv
* **glUniform2fvARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniform2fv
* **glUniform2ivARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniform2iv
* **glUniform3fvARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniform3fv
* **glUniform3ivARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniform3iv
* **glUniform4fvARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniform4fv
* **glUniform4ivARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniform4iv
* **glUniformMatrix2fvARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniformMatrix2fv
* **glUniformMatrix3fvARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniformMatrix3fv
* **glUniformMatrix4fvARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlUniformMatrix4fv
* **glGetActiveUniformARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlGetActiveUniformARB
* **glGetUniformLocationARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlGetUniformLocationARB
* **glGetActiveUniform** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glGetUniformLocation** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$


## 模板测试

* **glClearStencil** $$\bbox[yellow]{Rendering}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
* **glStencilFunc** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
* **glStencilMask** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
* **glStencilOp** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
* **glStencilFuncSeparate** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$
* **glStencilOpSeparate** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$
* **glStencilFuncSeparateATI** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // extGlStencilFuncSeparate
* **glStencilOpSeparateATI** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // extGlStencilOpSeparate


## general functions

* **glActiveTexture** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glCompressedTexImage2D** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glCompressedTexSubImage2D** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glActiveTextureARB** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$ // irrGlActiveTexture
* **glClientActiveTextureARB** $$\bbox[yellow]{GL2 Textures}$$  $$\color{pink}{ogladdr}$$ // irrGlClientActiveTexture
* **glPointParameterfARB** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // extGlPointParameterf
* **glPointParameterfvARB** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // extGlPointParameterfv


## shader programming

* **glGenProgramsNV**, **glGenProgramsARB** $$\color{pink}{ogladdr}$$ // extGlGenPrograms
* **glBindProgramNV**, **glBindProgramARB** $$\color{pink}{ogladdr}$$ // extGlBindProgram
* **glLoadProgramNV** $$\color{pink}{ogladdr}$$ // extGlLoadProgram
* **glProgramStringARB** $$\color{pink}{ogladdr}$$ // extGlProgramString, 貌似跟上面一个用途一样
* **glDeleteProgramsNV**, **glDeleteProgramsARB** $$\color{pink}{ogladdr}$$ // extGlDeletePrograms
* **glProgramLocalParameter4fvARB** $$\color{pink}{ogladdr}$$ // extGlProgramLocalParameter4fv
* **glCreateProgramObjectARB** $$\color{pink}{ogladdr}$$ // extGlCreateProgramObject
* **glCreateShaderObjectARB** $$\color{pink}{ogladdr}$$ // extGlCreateShaderObject
<hr/>
* **glCreateProgram** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glDeleteProgram** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glLinkProgram** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glUseProgram** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
<hr/>
* **glCreateShader** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glDeleteShader** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glCompileShader** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glAttachShader** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
<hr/>
* **glGetAttachedShaders** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glGetProgramInfoLog** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$ // extGlGetProgramInfoLog
* **glGetShaderInfoLog** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glGetProgramiv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$ // extGlGetProgramiv
* **glGetShaderiv** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glShaderSource** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
<hr/>
* **glShaderSourceARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlShaderSourceARB
* **glCompileShaderARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlCompileShaderARB
* **glLinkProgramARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlLinkProgramARB
* **glGetInfoLogARB** $$\color{pink}{ogladdr}$$ // extGlGetInfoLog
* **glGetObjectParameterivARB** $$\color{pink}{ogladdr}$$ // extGlGetObjectParameteriv
* **glUseProgramObjectARB** $$\color{pink}{ogladdr}$$ // extGlUseProgramObject
* **glAttachObjectARB** $$\color{pink}{ogladdr}$$ // extGlAttachObject
* **glDeleteObjectARB** $$\color{pink}{ogladdr}$$ // extGlDeleteObject
* **glGetAttachedObjectsARB** $$\color{pink}{ogladdr}$$ // extGlGetAttachedObjects


## framebuffer objects

* **glGenFramebuffers** $$\bbox[yellow]{Frame Buffers}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glBindFramebuffer** $$\bbox[yellow]{Frame Buffers}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glCheckFramebufferStatus** $$\bbox[yellow]{Frame Buffers}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glFramebufferTexture2D** $$\bbox[yellow]{Frame Buffers}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
* **glDeleteFramebuffers** $$\bbox[yellow]{Frame Buffers}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$ // irrGlDeleteFramebuffers
* **glGenerateMipmap** $$\bbox[yellow]{Frame Buffers}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
<hr/>
* **glGenFramebuffersEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlGenFramebuffers
* **glBindFramebufferEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlBindFramebuffer
* **glCheckFramebufferStatusEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlCheckFramebufferStatus
* **glFramebufferTexture2DEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlFramebufferTexture2D
* **glDeleteFramebuffersEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlDeleteFramebuffers
<hr/>
* **glBindRenderbuffer** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$
* **glDeleteRenderbuffers** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$
* **glGenRenderbuffers** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$
* **glRenderbufferStorage** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$
* **glFramebufferRenderbuffer** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$
* **glFramebufferTexture** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$
<hr/>
* **glBindRenderbufferEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlBindRenderbuffer
* **glDeleteRenderbuffersEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlDeleteRenderbuffers
* **glGenRenderbuffersEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlGenRenderbuffers
* **glRenderbufferStorageEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlRenderbufferStorage
* **glFramebufferRenderbufferEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlFramebufferRenderbuffer
* **glGenerateMipmapEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlGenerateMipmap
<hr/>
* **glDrawBuffer** $$\bbox[yellow]{Rendering}$$  $$\color{red}{ogl}$$
* **glDrawBuffersATI** $$\bbox[yellow]{Frame Buffers}$$ , **glDrawBuffersARB** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // irrGlDrawBuffers


## vertex buffer object

* **glGenBuffers** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}$$
* **glBindBuffer** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}$$
* **glBufferData** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}$$
* **glBufferSubData** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}$$
* **glDeleteBuffers** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}$$
<hr/>
* **glGenBuffersARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlGenBuffers
* **glBindBufferARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlBindBuffer
* **glBufferDataARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlBufferData
* **glDeleteBuffersARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlDeleteBuffers
<hr/>
* **glBufferSubDataARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlBufferSubData
* **glGetBufferSubDataARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlGetBufferSubData
* **glMapBufferARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlMapBuffer
* **glUnmapBufferARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlUnmapBuffer
* **glIsBufferARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlIsBuffer
* **glGetBufferParameterivARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlGetBufferParameteriv
* **glGetBufferPointervARB** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlGetBufferPointerv
* **glProvokingVertexEXT** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$ // extGlProvokingVertex
* **glProvokingVertex** $$\bbox[yellow]{Buffer Objects}$$  $$\color{pink}{ogladdr}$$
    * specifiy the vertex to be used as the source of data for flat shaded varyings。
    * 指定哪个点的数据作为平面着色的数据源。[from {% include relref_cnblogs.html %}](https://www.cnblogs.com/striver-zhu/p/4539160.html)
* **glProgramParameteriEXT** $$\bbox[yellow]{Shaders}$$ , **glProgramParameteriARB** $$\bbox[yellow]{Shaders}$$  $$\color{pink}{ogladdr}$$ // extGlProgramParameteri
    * glProgramParameteri — specify a parameter for a program object。


## 纹理

* **glTextureSubImage2D** $$\bbox[yellow]{Textures}$$ , **glTexSubImage2D** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
    * specify a two-dimensional texture subimage.
* **glTextureStorage2D** $$\bbox[yellow]{Textures}$$ , **glTexStorage2D** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
    * glTexStorage2D, glTextureStorage2D — simultaneously specify storage for all levels of a two-dimensional or one-dimensional array texture.
* **glTextureStorage3D** $$\bbox[yellow]{Textures}$$ , **glTexStorage3D** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
    * glTexStorage3D, glTextureStorage3D — simultaneously specify storage for all levels of a three-dimensional, two-dimensional array or cube-map array texture.
* **glGetTextureImage** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
    * 红宝书 p206 获取纹理数据。
    * 从纹理 texture 中获取图像数据。level 表示细节层次的层数。format 和 type 表示所需数据的像素格式和数据类型。pixels 可以被理解为用户内存中的一个地址，用来存储图像数据，或者如果当前有缓存对象绑定到 GL_PIXEL_PACK_BUFFER，这里设置的就是图像数据传递到缓存对象时的数据偏移地址。
* **glGetTexImage** $$\bbox[yellow]{Textures}$$  $$\color{red}{ogl}$$
    * glGetTexImage — return a texture image.
* **glTextureStorage2DEXT** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$ // extGlTextureStorage2D
* **glTextureSubImage2DEXT** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$ // extGlTextureSubImage2D
* **glTextureStorage3DEXT** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$ // extGlTextureStorage3D
* **glGetTextureImageEXT** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$ // extGlGetTextureImage
<hr/>
* **glNamedFramebufferTexture** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$
    * glFramebufferTexture — attach a level of a texture object as a logical buffer of a framebuffer object。
* **glNamedFramebufferTextureEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // extGlNamedFramebufferTexture
* **glTextureParameterf** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
    * set texture parameters。
* **glTextureParameterfv** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
* **glTextureParameteri** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
* **glTextureParameteriv** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
    * set texture parameters。
<hr/>
* **glCreateTextures** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
    * create texture objects。Create a new 2D texture object。
* **glCreateFramebuffers** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$
    * create framebuffer objects。
* **glBindTextures** $$\bbox[yellow]{Textures}$$  $$\color{pink}{ogladdr}$$
    * bind one or more named textures to a sequence of consecutive texture units。
<hr/>
* **glGenTextures** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * generate texture names。
    * 生成纹理的函数。函数根据纹理参数返回 n 个纹理索引。纹理名称集合不必是一个连续的整数集合。
* **glBindTexture** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * bind a named texture to a texturing target。
    * 允许建立一个绑定到目标纹理的有名称的纹理。
* **glDeleteTextures** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * delete named textures。
<hr/>
* **glGenerateTextureMipmap** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$
* **glGenerateTextureMipmapEXT** $$\bbox[yellow]{Frame Buffers}$$  $$\color{pink}{ogladdr}$$ // extGlGenerateTextureMipmap
    * glGenerateMipmap, glGenerateTextureMipmap — generate mipmaps for a specified texture object。


## 深度测试

* **glClearDepthf** $$\bbox[yellow]{Rendering}$$  $$\color{blue}{gles}$$
    * specify the clear value for the depth buffer。
* **glClearDepth** $$\bbox[yellow]{Rendering}$$  $$\color{red}{ogl}$$
    * specify the clear value for the depth buffer。
    * 设置深度缓存的清除值。
* **glDepthFunc** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * specify the value used for depth buffer comparisons。
    * 通过目标像素与当前像素在 z 方向上值大小的比较是否满足参数指定的条件，来决定在深度（z 方向）上是否绘制该目标像素。该函数只有启用“深度测试”时才有效，参考 glEnable(GL_DEPTH_TEST) 和 glDisable(GL_DEPTH_TEST)。
* **glDepthMask** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * enable or disable writing into the depth buffer。


## 颜色混合 Blend indexed

* **glDisableIndexedEXT** $$\color{pink}{ogladdr}$$ // irrGlDisableIndexed
* **glEnableIndexedEXT** $$\color{pink}{ogladdr}$$ // irrGlEnableIndexed
* **glColorMaskIndexedEXT** $$\color{pink}{ogladdr}$$ // irrGlColorMaskIndexed
    * glColorMask — enable and disable writing of frame buffer color components。
<hr/>
* **glBlendFuncIndexedAMD**, **glBlendFunciARB** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // irrGlBlendFuncIndexed
* **glBlendFuncSeparateIndexedAMD**, **glBlendFuncSeparateiARB** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // irrGlBlendFuncSeparateIndexed
* **glBlendEquationIndexedAMD**, **glBlendEquationiARB** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // irrGlBlendEquationIndexed
* **glBlendEquationSeparateIndexedAMD**, **glBlendEquationSeparateiARB** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // irrGlBlendEquationSeparateIndexed
<hr/>
* **glBlendEquationEXT** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // irrGlBlendEquation
* **glBlendEquationSeparateEXT** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // ?
* **glBlendFuncSeparateEXT** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$ // irrGlBlendFuncSeparate
<hr/>
* **glBlendEquation** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
    * specify the equation used for both the RGB blend equation and the Alpha blend equation。
    * 设置 BLEND 方程式。
* **glBlendEquationSeparate** $$\bbox[yellow]{State Management}$$  $$\color{pink}{ogladdr}$$
    * 对 RGB 和 Alpha 分别设置 BLEND 方程式。
* **glBlendFuncSeparate** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{pink}{ogladdr}$$
    * specify pixel arithmetic for RGB and alpha components separately。
    * 对 RGB 和 Alpha 分别设置 BLEND 函数。
* **glBlendFunc** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * 设置 BLEND 函数。


## GLES Only

* **glBindAttribLocation** $$\bbox[yellow]{Shaders}$$  $$\color{blue}{gles}$$
    * Associates a generic vertex attribute index with a named attribute variable。
    * 指定属性变量名和通用属性索引之间的关联。
* **glDisableVertexAttribArray** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}$$
    * 禁用 index 指定的通用顶点属性数组。
    * Enable or disable a generic vertex attribute array。
* **glEnableVertexAttribArray** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}$$
    * Enable or disable a generic vertex attribute array。
* **glVertexAttribPointer** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}$$
    * define an array of generic vertex attribute data。


## OpenGL Only

* **glDisableClientState** $$\bbox[yellow]{Client Arrays}$$  $$\color{red}{ogl}$$
    * enable or disable client-side capability。
    * The glEnableClientState and glDisableClientState functions enable and disable arrays respectively.
* **glEnableClientState** $$\bbox[yellow]{Client Arrays}$$  $$\color{red}{ogl}$$
    * enable or disable client-side capability。
* **glClipPlane** $$\bbox[yellow]{GL2 Rasterization}$$  $$\color{red}{ogl}$$
    * 定义一个裁剪平面。
    * specify a plane against which all geometry is clipped。
* **glColor4ub** $$\bbox[yellow]{Immediate Mode}$$  $$\color{red}{ogl}$$
    * Sets the current color.
* **glColorMaterial** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * cause a material color to track the current color。
* **glColorPointer** $$\bbox[yellow]{Client Arrays}$$  $$\color{red}{ogl}$$
    * define an array of colors。
* **glFogf** $$\bbox[yellow]{GL2 Rasterization}$$  $$\color{red}{ogl}$$
    * The glFogf and function specifies fog parameters.
* **glFogfv** $$\bbox[yellow]{GL2 Rasterization}$$  $$\color{red}{ogl}$$
    * The glFogfv function specifies fog parameters.
* **glFogi** $$\bbox[yellow]{GL2 Rasterization}$$  $$\color{red}{ogl}$$
    * The glFogi function specifies fog parameters.
* **glLightModelfv** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * The glLightModelfv function sets lighting model parameters.
* **glLightModeli** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * The glLightModeli function sets lighting model parameters.
* **glLightf** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * The glLightf function returns light source parameter values.
* **glLightfv** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * The glLightfv function returns light source parameter values.
* **glNormalPointer** $$\bbox[yellow]{Client Arrays}$$  $$\color{red}{ogl}$$
    * define an array of normals。
* **glPointSize** $$\bbox[yellow]{State Management}$$  $$\color{red}{ogl}$$
    * specify the diameter of rasterized points。
* **glPolygonMode** $$\bbox[yellow]{State Management}$$  $$\color{red}{ogl}$$
    * select a polygon rasterization mode。
* **glRectf** $$\bbox[yellow]{GL2 Rasterization}$$  $$\color{red}{ogl}$$
    * draw a rectangle。
* **glAlphaFunc** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * specify the alpha test function。
* **glVertexPointer** $$\bbox[yellow]{Client Arrays}$$  $$\color{red}{ogl}$$
    * define an array of vertex data。
* **glTranslatef** $$\bbox[yellow]{Matrix State}$$  $$\color{red}{ogl}$$
    * multiply the current matrix by a translation matrix。
* **glTexCoordPointer** $$\bbox[yellow]{Client Arrays}$$  $$\color{red}{ogl}$$
    * define an array of texture coordinates。
* **glTexEnvf** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * The glTexEnvf function sets a texture environment parameter.
* **glTexEnvi** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * set texture environment parameters。
* **glTexGeni** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * control the generation of texture coordinates。
* **glShadeModel** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * select flat or smooth shading。
* **glPushAttrib** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * push and pop the server attribute stack。
* **glPushMatrix** $$\bbox[yellow]{Matrix State}$$  $$\color{red}{ogl}$$
    * push and pop the current matrix stack。
* **glPopAttrib** $$\bbox[yellow]{Fixed Function}$$  $$\color{red}{ogl}$$
    * push and pop the server attribute stack。
* **glPopMatrix** $$\bbox[yellow]{Matrix State}$$  $$\color{red}{ogl}$$
    * push and pop the current matrix stack。
* **glLoadIdentity** $$\bbox[yellow]{Matrix State}$$  $$\color{red}{ogl}$$
    * replace the current matrix with the identity matrix。
* **glLoadMatrixf** $$\bbox[yellow]{Matrix State}$$  $$\color{red}{ogl}$$
    * replace the current matrix with the specified matrix。
* **glMaterialf** $$\bbox[yellow]{Immediate Mode}$$  $$\color{red}{ogl}$$
    * specify material parameters for the lighting model。
* **glMaterialfv** $$\bbox[yellow]{Immediate Mode}$$  $$\color{red}{ogl}$$
    * 指定用于光照计算的当前材质属性。
* **glMatrixMode** $$\bbox[yellow]{Matrix State}$$  $$\color{red}{ogl}$$
    * specify which matrix is the current matrix。
* **glMultMatrixf** $$\bbox[yellow]{Matrix State}$$  $$\color{red}{ogl}$$
    * multiply the current matrix with the specified matrix。


## 都支持的基本 API

* **glReadBuffer** $$\bbox[yellow]{Rendering}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * select a color buffer source for pixels。
* **glReadPixels** $$\bbox[yellow]{Rendering}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * read a block of pixels from the frame buffer。
* **glDrawArrays** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * render primitives from array data。
* **glDrawElements** $$\bbox[yellow]{Buffer Objects}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * render primitives from array data。
* **glEnable** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * enable or disable server-side GL capabilities。
* **glDisable** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * enable or disable server-side GL capabilities。
* **glIsEnabled** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * test whether a capability is enabled。
* **glClear** $$\bbox[yellow]{Rendering}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * clear buffers to preset values。
* **glClearColor** $$\bbox[yellow]{Rendering}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * specify clear values for the color buffers。
* **glFrontFace** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * define front- and back-facing polygons。
* **glCullFace** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * specify whether front- or back-facing facets can be culled。
* **glFlush** $$\bbox[yellow]{Rendering}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * 强制刷新缓冲。
    * force execution of GL commands in finite time。
* **glViewport** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * set the viewport。
* **glGetString** $$\bbox[yellow]{Utility}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    *  return a string describing the current GL connection。
* **glGetError** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * return error information。
* **glGetFloatv** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * return the value or values of a selected parameter。
* **glGetIntegerv** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * return the value or values of a selected parameter。
* **glHint** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * specify implementation-specific hints。
    * 指定特定于实现的提示。
* **glTexParameterf** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * set texture parameters。
    * 纹理过滤函数。
* **glTexParameteri** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * set texture parameters。
    * 纹理过滤函数。
* **glLineWidth** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * specify the width of rasterized lines。
    * 设置线段的宽度。
* **glScissor** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * define the scissor box。
    * 剪裁测试用于限制绘制区域。
* **glCopyTexSubImage2D** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * copy a two-dimensional texture subimage。
    * 复制二维纹理子图像。
* **glColorMask** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * enable and disable writing of color buffer components。
    * 启用和禁用帧缓冲区颜色分量的写入。
* **glPolygonOffset** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * set the scale and units used to calculate depth values。
    * 设置计算深度值的拉伸比和单位。
* **glPixelStorei** $$\bbox[yellow]{State Management}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * set pixel storage modes。
    * 设置像素存储模式。
* **glTexImage2D** $$\bbox[yellow]{Textures}$$  $$\color{blue}{gles}\&\color{red}{ogl}$$
    * specify a two-dimensional texture image。
    * 指定一个二维的纹理图片。


## JS CODE for docs.gl

```js
var lip = $("li");
for (var i = 0; i < lip.length; i++) {
    var span = $(lip[i]).find("span");
    if (!span.length) continue;
    var subli = $(lip[i]).find("li");
    console.log("#", span.text(), subli.length);
    for (var j = 0; j < subli.length; j++) {
        var li = $(subli[j]);
        console.log(li.text(), span.text());
    }
}
```

[LaTeX/MathJax 字体美化 {% include relref_github.html %}](https://heartlessly.github.io/others/latex-mathjax-gong-shi-zi-ti-mei-hua/)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-22-shader-OpenGL-ex-irrlicht.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.khronos.org/registry/OpenGL/index_es.php]({% include relrefx.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/www.khronos.org/bb75bed1.php" %})
- [https://www.khronos.org/registry/OpenGL/index_gl.php]({% include relrefx.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/www.khronos.org/a9a79c0a.php" %})
- [http://docs.gl/]({% include relrefx.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/docs.gl/378832af.html" %})
- [https://github.com/MicrosoftDocs/win32/tree/docs/desktop-src/OpenGL]({% include relrefx.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/github.com/6b24f6cb.html" %})
- [https://www.cnblogs.com/striver-zhu/p/4539160.html]({% include relrefx.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/www.cnblogs.com/7b349b94.html" %})
- [https://heartlessly.github.io/others/latex-mathjax-gong-shi-zi-ti-mei-hua/]({% include relrefx.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/heartlessly.github.io/7ee13c5f.html" %})
