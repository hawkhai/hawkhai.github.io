---
layout: post
title: "特效编程笔记 -- Irrlicht OpenGL 扩展支持 整理文档"
author:
location: "珠海"
categories: ["特效"]
tags: ["特效", "OpenGL", "Irrlicht"]
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

OpenGL ES & OpenGL 存在大量 API 交叉的情况，为了兼容，很多 API 采用 wglGetProcAddress 函数指针的形式。包含厂商后缀的都是 wglGetProcAddress，<font color="#FF00FF">ogladdr</font>。分了五类：

* 只支持 GLES: <font color="#0000FF">gles</font>（大概 36 个）
* 只支持 OpenGL & wglGetProcAddress: <font color="#FF00FF">ogladdr</font>（大概 140 个）
* 只支持 OpenGL: <font color="red">ogl</font>（大概 43 个）
* 两个都支持 OpenGL & wglGetProcAddress: <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>（大概 27 个）
* 两个都支持：<font color="#0000FF">gles</font>&<font color="red">ogl</font>（大概 38 个）

{'<font color="#0000FF">gles</font>': 36, '<font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>': 27, '<font color="#FF00FF">ogladdr</font>': 140, '<font color="red">ogl</font>': 43, '<font color="#0000FF">gles</font>&<font color="red">ogl</font>': 38}


## 遮挡查询 occlusion query

* **glBeginOcclusionQueryNV**, **glBeginQueryARB** <font color="#FF00FF">ogladdr</font> // extGlBeginQuery
* **glDeleteOcclusionQueriesNV**, **glDeleteQueriesARB** <font color="#FF00FF">ogladdr</font> // extGlDeleteQueries
* **glEndOcclusionQueryNV**, **glEndQueryARB** <font color="#FF00FF">ogladdr</font> // extGlEndQuery
* **glGenOcclusionQueriesNV**, **glGenQueriesARB** <font color="#FF00FF">ogladdr</font> // extGlGenQueries
* **glGetOcclusionQueryivNV**, **glGetQueryObjectivARB** <font color="#FF00FF">ogladdr</font> // extGlGetQueryObjectiv
* **glGetOcclusionQueryuivNV**, **glGetQueryObjectuivARB** <font color="#FF00FF">ogladdr</font> // extGlGetQueryObjectuiv
* **glGetQueryivARB** <font color="#FF00FF">ogladdr</font> // extGlGetQueryiv
* **glIsOcclusionQueryNV**, **glIsQueryARB** <font color="#FF00FF">ogladdr</font> // extGlIsQuery


## OpenGL WGL

* **wglCreateContext** <font color="red">ogl</font>
* **wglDeleteContext** <font color="red">ogl</font>
* **wglGetCurrentDC** <font color="red">ogl</font>
* **wglGetProcAddress** <font color="red">ogl</font>
* **wglMakeCurrent** <font color="red">ogl</font>
* **wglChoosePixelFormatARB** <font color="#FF00FF">ogladdr</font> // ? 请求并选择一个匹配的像素格式
* **wglCreateContextAttribsARB** <font color="#FF00FF">ogladdr</font> // ? 创建和使用 OpenGL
* **wglGetExtensionsStringARB** <font color="#FF00FF">ogladdr</font> // ? 检查是否支持 WGL_ARB_extensions_string 扩展
* **wglSwapIntervalEXT** <font color="#FF00FF">ogladdr</font> // extGlSwapInterval 是否启用垂直同步


## GLES EGL

* **eglBindAPI** <font color="#0000FF">gles</font>
* **eglChooseConfig** <font color="#0000FF">gles</font>
* **eglCreateContext** <font color="#0000FF">gles</font>
* **eglCreateWindowSurface** <font color="#0000FF">gles</font>
* **eglDestroyContext** <font color="#0000FF">gles</font>
* **eglDestroySurface** <font color="#0000FF">gles</font>
* **eglGetConfigAttrib** <font color="#0000FF">gles</font>
* **eglGetConfigs** <font color="#0000FF">gles</font>
* **eglGetDisplay** <font color="#0000FF">gles</font>
* **eglGetError** <font color="#0000FF">gles</font>
* **eglInitialize** <font color="#0000FF">gles</font>
* **eglMakeCurrent** <font color="#0000FF">gles</font>
* **eglSwapBuffers** <font color="#0000FF">gles</font>
* **eglSwapInterval** <font color="#0000FF">gles</font>
* **eglTerminate** <font color="#0000FF">gles</font>


## glUniform 系列

* **glUniform1fv** <font color="#0000FF">gles</font>
* **glUniform1iv** <font color="#0000FF">gles</font>
* **glUniform1uiv** <font color="#FF00FF">ogladdr</font>
* **glUniform2fv** <font color="#0000FF">gles</font>
* **glUniform2iv** <font color="#0000FF">gles</font>
* **glUniform2uiv** <font color="#FF00FF">ogladdr</font>
* **glUniform3fv** <font color="#0000FF">gles</font>
* **glUniform3iv** <font color="#0000FF">gles</font>
* **glUniform3uiv** <font color="#FF00FF">ogladdr</font>
* **glUniform4fv** <font color="#0000FF">gles</font>
* **glUniform4iv** <font color="#0000FF">gles</font>
* **glUniform4uiv** <font color="#FF00FF">ogladdr</font>
* **glUniformMatrix2fv** <font color="#0000FF">gles</font>
* **glUniformMatrix2x3fv** <font color="#FF00FF">ogladdr</font>
* **glUniformMatrix2x4fv** <font color="#FF00FF">ogladdr</font>
* **glUniformMatrix3fv** <font color="#0000FF">gles</font>
* **glUniformMatrix3x2fv** <font color="#FF00FF">ogladdr</font>
* **glUniformMatrix3x4fv** <font color="#FF00FF">ogladdr</font>
* **glUniformMatrix4fv** <font color="#0000FF">gles</font>
* **glUniformMatrix4x2fv** <font color="#FF00FF">ogladdr</font>
* **glUniformMatrix4x3fv** <font color="#FF00FF">ogladdr</font>
* **glUniform1fvARB** <font color="#FF00FF">ogladdr</font> // extGlUniform1fv
* **glUniform1ivARB** <font color="#FF00FF">ogladdr</font> // extGlUniform1iv
* **glUniform2fvARB** <font color="#FF00FF">ogladdr</font> // extGlUniform2fv
* **glUniform2ivARB** <font color="#FF00FF">ogladdr</font> // extGlUniform2iv
* **glUniform3fvARB** <font color="#FF00FF">ogladdr</font> // extGlUniform3fv
* **glUniform3ivARB** <font color="#FF00FF">ogladdr</font> // extGlUniform3iv
* **glUniform4fvARB** <font color="#FF00FF">ogladdr</font> // extGlUniform4fv
* **glUniform4ivARB** <font color="#FF00FF">ogladdr</font> // extGlUniform4iv
* **glUniformMatrix2fvARB** <font color="#FF00FF">ogladdr</font> // extGlUniformMatrix2fv
* **glUniformMatrix3fvARB** <font color="#FF00FF">ogladdr</font> // extGlUniformMatrix3fv
* **glUniformMatrix4fvARB** <font color="#FF00FF">ogladdr</font> // extGlUniformMatrix4fv
* **glGetActiveUniformARB** <font color="#FF00FF">ogladdr</font> // extGlGetActiveUniformARB
* **glGetUniformLocationARB** <font color="#FF00FF">ogladdr</font> // extGlGetUniformLocationARB
* **glGetActiveUniform** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glGetUniformLocation** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>


## 模板测试

* **glClearStencil** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
* **glStencilFunc** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
* **glStencilMask** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
* **glStencilOp** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
* **glStencilFuncSeparate** <font color="#FF00FF">ogladdr</font>
* **glStencilOpSeparate** <font color="#FF00FF">ogladdr</font>
* **glStencilFuncSeparateATI** <font color="#FF00FF">ogladdr</font> // extGlStencilFuncSeparate
* **glStencilOpSeparateATI** <font color="#FF00FF">ogladdr</font> // extGlStencilOpSeparate


## general functions

* **glActiveTexture** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glCompressedTexImage2D** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glCompressedTexSubImage2D** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glActiveTextureARB** <font color="#FF00FF">ogladdr</font> // irrGlActiveTexture
* **glClientActiveTextureARB** <font color="#FF00FF">ogladdr</font> // irrGlClientActiveTexture
* **glPointParameterfARB** <font color="#FF00FF">ogladdr</font> // extGlPointParameterf
* **glPointParameterfvARB** <font color="#FF00FF">ogladdr</font> // extGlPointParameterfv


## shader programming

* **glGenProgramsNV**, **glGenProgramsARB** <font color="#FF00FF">ogladdr</font> // extGlGenPrograms
* **glBindProgramNV**, **glBindProgramARB** <font color="#FF00FF">ogladdr</font> // extGlBindProgram
* **glLoadProgramNV** <font color="#FF00FF">ogladdr</font> // extGlLoadProgram
* **glProgramStringARB** <font color="#FF00FF">ogladdr</font> // extGlProgramString, 貌似跟上面一个用途一样
* **glDeleteProgramsNV**, **glDeleteProgramsARB** <font color="#FF00FF">ogladdr</font> // extGlDeletePrograms
* **glProgramLocalParameter4fvARB** <font color="#FF00FF">ogladdr</font> // extGlProgramLocalParameter4fv
* **glCreateProgramObjectARB** <font color="#FF00FF">ogladdr</font> // extGlCreateProgramObject
* **glCreateShaderObjectARB** <font color="#FF00FF">ogladdr</font> // extGlCreateShaderObject
<hr/>
* **glCreateProgram** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glDeleteProgram** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glLinkProgram** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glUseProgram** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
<hr/>
* **glCreateShader** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glDeleteShader** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glCompileShader** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glAttachShader** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
<hr/>
* **glGetAttachedShaders** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glGetProgramInfoLog** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font> // extGlGetProgramInfoLog
* **glGetShaderInfoLog** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glGetProgramiv** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font> // extGlGetProgramiv
* **glGetShaderiv** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glShaderSource** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
<hr/>
* **glShaderSourceARB** <font color="#FF00FF">ogladdr</font> // extGlShaderSourceARB
* **glCompileShaderARB** <font color="#FF00FF">ogladdr</font> // extGlCompileShaderARB
* **glLinkProgramARB** <font color="#FF00FF">ogladdr</font> // extGlLinkProgramARB
* **glGetInfoLogARB** <font color="#FF00FF">ogladdr</font> // extGlGetInfoLog
* **glGetObjectParameterivARB** <font color="#FF00FF">ogladdr</font> // extGlGetObjectParameteriv
* **glUseProgramObjectARB** <font color="#FF00FF">ogladdr</font> // extGlUseProgramObject
* **glAttachObjectARB** <font color="#FF00FF">ogladdr</font> // extGlAttachObject
* **glDeleteObjectARB** <font color="#FF00FF">ogladdr</font> // extGlDeleteObject
* **glGetAttachedObjectsARB** <font color="#FF00FF">ogladdr</font> // extGlGetAttachedObjects


## framebuffer objects

* **glGenFramebuffers** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glBindFramebuffer** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glCheckFramebufferStatus** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glFramebufferTexture2D** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
* **glDeleteFramebuffers** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font> // irrGlDeleteFramebuffers
* **glGenerateMipmap** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
<hr/>
* **glGenFramebuffersEXT** <font color="#FF00FF">ogladdr</font> // irrGlGenFramebuffers
* **glBindFramebufferEXT** <font color="#FF00FF">ogladdr</font> // irrGlBindFramebuffer
* **glCheckFramebufferStatusEXT** <font color="#FF00FF">ogladdr</font> // irrGlCheckFramebufferStatus
* **glFramebufferTexture2DEXT** <font color="#FF00FF">ogladdr</font> // irrGlFramebufferTexture2D
* **glDeleteFramebuffersEXT** <font color="#FF00FF">ogladdr</font> // irrGlDeleteFramebuffers
<hr/>
* **glBindRenderbuffer** <font color="#FF00FF">ogladdr</font>
* **glDeleteRenderbuffers** <font color="#FF00FF">ogladdr</font>
* **glGenRenderbuffers** <font color="#FF00FF">ogladdr</font>
* **glRenderbufferStorage** <font color="#FF00FF">ogladdr</font>
* **glFramebufferRenderbuffer** <font color="#FF00FF">ogladdr</font>
* **glFramebufferTexture** <font color="#FF00FF">ogladdr</font>
<hr/>
* **glBindRenderbufferEXT** <font color="#FF00FF">ogladdr</font> // irrGlBindRenderbuffer
* **glDeleteRenderbuffersEXT** <font color="#FF00FF">ogladdr</font> // irrGlDeleteRenderbuffers
* **glGenRenderbuffersEXT** <font color="#FF00FF">ogladdr</font> // irrGlGenRenderbuffers
* **glRenderbufferStorageEXT** <font color="#FF00FF">ogladdr</font> // irrGlRenderbufferStorage
* **glFramebufferRenderbufferEXT** <font color="#FF00FF">ogladdr</font> // irrGlFramebufferRenderbuffer
* **glGenerateMipmapEXT** <font color="#FF00FF">ogladdr</font> // irrGlGenerateMipmap
<hr/>
* **glDrawBuffer** <font color="red">ogl</font>
* **glDrawBuffersATI**, **glDrawBuffersARB** <font color="#FF00FF">ogladdr</font> // irrGlDrawBuffers


## vertex buffer object

* **glGenBuffers** <font color="#0000FF">gles</font>
* **glBindBuffer** <font color="#0000FF">gles</font>
* **glBufferData** <font color="#0000FF">gles</font>
* **glBufferSubData** <font color="#0000FF">gles</font>
* **glDeleteBuffers** <font color="#0000FF">gles</font>
<hr/>
* **glGenBuffersARB** <font color="#FF00FF">ogladdr</font> // extGlGenBuffers
* **glBindBufferARB** <font color="#FF00FF">ogladdr</font> // extGlBindBuffer
* **glBufferDataARB** <font color="#FF00FF">ogladdr</font> // extGlBufferData
* **glDeleteBuffersARB** <font color="#FF00FF">ogladdr</font> // extGlDeleteBuffers
<hr/>
* **glBufferSubDataARB** <font color="#FF00FF">ogladdr</font> // extGlBufferSubData
* **glGetBufferSubDataARB** <font color="#FF00FF">ogladdr</font> // extGlGetBufferSubData
* **glMapBufferARB** <font color="#FF00FF">ogladdr</font> // extGlMapBuffer
* **glUnmapBufferARB** <font color="#FF00FF">ogladdr</font> // extGlUnmapBuffer
* **glIsBufferARB** <font color="#FF00FF">ogladdr</font> // extGlIsBuffer
* **glGetBufferParameterivARB** <font color="#FF00FF">ogladdr</font> // extGlGetBufferParameteriv
* **glGetBufferPointervARB** <font color="#FF00FF">ogladdr</font> // extGlGetBufferPointerv
* **glProvokingVertexEXT** <font color="#FF00FF">ogladdr</font> // extGlProvokingVertex
* **glProvokingVertex** <font color="#FF00FF">ogladdr</font>
    * specifiy the vertex to be used as the source of data for flat shaded varyings。
    * 指定哪个点的数据作为平面着色的数据源。[from {% include relref_cnblogs.html %}](https://www.cnblogs.com/striver-zhu/p/4539160.html)
* **glProgramParameteriEXT**, **glProgramParameteriARB** <font color="#FF00FF">ogladdr</font> // extGlProgramParameteri
    * glProgramParameteri — specify a parameter for a program object。


## 纹理

* **glTextureSubImage2D**, **glTexSubImage2D** <font color="#FF00FF">ogladdr</font>
    * specify a two-dimensional texture subimage.
* **glTextureStorage2D**, **glTexStorage2D** <font color="#FF00FF">ogladdr</font>
    * glTexStorage2D, glTextureStorage2D — simultaneously specify storage for all levels of a two-dimensional or one-dimensional array texture.
* **glTextureStorage3D**, **glTexStorage3D** <font color="#FF00FF">ogladdr</font>
    * glTexStorage3D, glTextureStorage3D — simultaneously specify storage for all levels of a three-dimensional, two-dimensional array or cube-map array texture.
* **glGetTextureImage** <font color="#FF00FF">ogladdr</font>
    * 红宝书 p206 获取纹理数据。
    * 从纹理 texture 中获取图像数据。level 表示细节层次的层数。format 和 type 表示所需数据的像素格式和数据类型。pixels 可以被理解为用户内存中的一个地址，用来存储图像数据，或者如果当前有缓存对象绑定到 GL_PIXEL_PACK_BUFFER，这里设置的就是图像数据传递到缓存对象时的数据偏移地址。
* **glGetTexImage** <font color="red">ogl</font>
    * glGetTexImage — return a texture image.
* **glTextureStorage2DEXT** <font color="#FF00FF">ogladdr</font> // extGlTextureStorage2D
* **glTextureSubImage2DEXT** <font color="#FF00FF">ogladdr</font> // extGlTextureSubImage2D
* **glTextureStorage3DEXT** <font color="#FF00FF">ogladdr</font> // extGlTextureStorage3D
* **glGetTextureImageEXT** <font color="#FF00FF">ogladdr</font> // extGlGetTextureImage
<hr/>
* **glNamedFramebufferTexture** <font color="#FF00FF">ogladdr</font>
    * glFramebufferTexture — attach a level of a texture object as a logical buffer of a framebuffer object。
* **glNamedFramebufferTextureEXT** <font color="#FF00FF">ogladdr</font> // extGlNamedFramebufferTexture
* **glTextureParameterf** <font color="#FF00FF">ogladdr</font>
    * set texture parameters。
* **glTextureParameterfv** <font color="#FF00FF">ogladdr</font>
* **glTextureParameteri** <font color="#FF00FF">ogladdr</font>
* **glTextureParameteriv** <font color="#FF00FF">ogladdr</font>
    * set texture parameters。
<hr/>
* **glCreateTextures** <font color="#FF00FF">ogladdr</font>
    * create texture objects。Create a new 2D texture object。
* **glCreateFramebuffers** <font color="#FF00FF">ogladdr</font>
    * create framebuffer objects。
* **glBindTextures** <font color="#FF00FF">ogladdr</font>
    * bind one or more named textures to a sequence of consecutive texture units。
<hr/>
* **glGenTextures** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * generate texture names。
    * 生成纹理的函数。函数根据纹理参数返回 n 个纹理索引。纹理名称集合不必是一个连续的整数集合。
* **glBindTexture** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * bind a named texture to a texturing target。
    * 允许建立一个绑定到目标纹理的有名称的纹理。
* **glDeleteTextures** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * delete named textures。
<hr/>
* **glGenerateTextureMipmap** <font color="#FF00FF">ogladdr</font>
* **glGenerateTextureMipmapEXT** <font color="#FF00FF">ogladdr</font> // extGlGenerateTextureMipmap
    * glGenerateMipmap, glGenerateTextureMipmap — generate mipmaps for a specified texture object。


## 深度测试

* **glClearDepthf** <font color="#0000FF">gles</font>
    * specify the clear value for the depth buffer。
* **glClearDepth** <font color="red">ogl</font>
    * specify the clear value for the depth buffer。
    * 设置深度缓存的清除值。
* **glDepthFunc** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * specify the value used for depth buffer comparisons。
    * 通过目标像素与当前像素在 z 方向上值大小的比较是否满足参数指定的条件，来决定在深度（z 方向）上是否绘制该目标像素。该函数只有启用“深度测试”时才有效，参考 glEnable(GL_DEPTH_TEST) 和 glDisable(GL_DEPTH_TEST)。
* **glDepthMask** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * enable or disable writing into the depth buffer。


## 颜色混合 Blend indexed

* **glDisableIndexedEXT** <font color="#FF00FF">ogladdr</font> // irrGlDisableIndexed
* **glEnableIndexedEXT** <font color="#FF00FF">ogladdr</font> // irrGlEnableIndexed
* **glColorMaskIndexedEXT** <font color="#FF00FF">ogladdr</font> // irrGlColorMaskIndexed
    * glColorMask — enable and disable writing of frame buffer color components。
<hr/>
* **glBlendFuncIndexedAMD**, **glBlendFunciARB** <font color="#FF00FF">ogladdr</font> // irrGlBlendFuncIndexed
* **glBlendFuncSeparateIndexedAMD**, **glBlendFuncSeparateiARB** <font color="#FF00FF">ogladdr</font> // irrGlBlendFuncSeparateIndexed
* **glBlendEquationIndexedAMD**, **glBlendEquationiARB** <font color="#FF00FF">ogladdr</font> // irrGlBlendEquationIndexed
* **glBlendEquationSeparateIndexedAMD**, **glBlendEquationSeparateiARB** <font color="#FF00FF">ogladdr</font> // irrGlBlendEquationSeparateIndexed
<hr/>
* **glBlendEquationEXT** <font color="#FF00FF">ogladdr</font> // irrGlBlendEquation
* **glBlendEquationSeparateEXT** <font color="#FF00FF">ogladdr</font> // ?
* **glBlendFuncSeparateEXT** <font color="#FF00FF">ogladdr</font> // irrGlBlendFuncSeparate
<hr/>
* **glBlendEquation** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
    * specify the equation used for both the RGB blend equation and the Alpha blend equation。
    * 设置 BLEND 方程式。
* **glBlendEquationSeparate** <font color="#FF00FF">ogladdr</font>
    * 对 RGB 和 Alpha 分别设置 BLEND 方程式。
* **glBlendFuncSeparate** <font color="#0000FF">gles</font>&<font color="#FF00FF">ogladdr</font>
    * specify pixel arithmetic for RGB and alpha components separately。
    * 对 RGB 和 Alpha 分别设置 BLEND 函数。
* **glBlendFunc** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * 设置 BLEND 函数。


## GLES Only

* **glBindAttribLocation** <font color="#0000FF">gles</font>
    * Associates a generic vertex attribute index with a named attribute variable。
    * 指定属性变量名和通用属性索引之间的关联。
* **glDisableVertexAttribArray** <font color="#0000FF">gles</font>
    * 禁用 index 指定的通用顶点属性数组。
    * Enable or disable a generic vertex attribute array。
* **glEnableVertexAttribArray** <font color="#0000FF">gles</font>
    * Enable or disable a generic vertex attribute array。
* **glVertexAttribPointer** <font color="#0000FF">gles</font>
    * define an array of generic vertex attribute data。


## OpenGL Only

* **glDisableClientState** <font color="red">ogl</font>
    * enable or disable client-side capability。
    * The glEnableClientState and glDisableClientState functions enable and disable arrays respectively.
* **glEnableClientState** <font color="red">ogl</font>
    * enable or disable client-side capability。
* **glClipPlane** <font color="red">ogl</font>
    * 定义一个裁剪平面。
    * specify a plane against which all geometry is clipped。
* **glColor4ub** <font color="red">ogl</font>
    * Sets the current color.
* **glColorMaterial** <font color="red">ogl</font>
    * cause a material color to track the current color。
* **glColorPointer** <font color="red">ogl</font>
    * define an array of colors。
* **glFogf** <font color="red">ogl</font>
    * The glFogf and function specifies fog parameters.
* **glFogfv** <font color="red">ogl</font>
    * The glFogfv function specifies fog parameters.
* **glFogi** <font color="red">ogl</font>
    * The glFogi function specifies fog parameters.
* **glLightModelfv** <font color="red">ogl</font>
    * The glLightModelfv function sets lighting model parameters.
* **glLightModeli** <font color="red">ogl</font>
    * The glLightModeli function sets lighting model parameters.
* **glLightf** <font color="red">ogl</font>
    * The glLightf function returns light source parameter values.
* **glLightfv** <font color="red">ogl</font>
    * The glLightfv function returns light source parameter values.
* **glNormalPointer** <font color="red">ogl</font>
    * define an array of normals。
* **glPointSize** <font color="red">ogl</font>
    * specify the diameter of rasterized points。
* **glPolygonMode** <font color="red">ogl</font>
    * select a polygon rasterization mode。
* **glRectf** <font color="red">ogl</font>
    * draw a rectangle。
* **glAlphaFunc** <font color="red">ogl</font>
    * specify the alpha test function。
* **glVertexPointer** <font color="red">ogl</font>
    * define an array of vertex data。
* **glTranslatef** <font color="red">ogl</font>
    * multiply the current matrix by a translation matrix。
* **glTexCoordPointer** <font color="red">ogl</font>
    * define an array of texture coordinates。
* **glTexEnvf** <font color="red">ogl</font>
    * The glTexEnvf function sets a texture environment parameter.
* **glTexEnvi** <font color="red">ogl</font>
    * set texture environment parameters。
* **glTexGeni** <font color="red">ogl</font>
    * control the generation of texture coordinates。
* **glShadeModel** <font color="red">ogl</font>
    * select flat or smooth shading。
* **glPushAttrib** <font color="red">ogl</font>
    * push and pop the server attribute stack。
* **glPushMatrix** <font color="red">ogl</font>
    * push and pop the current matrix stack。
* **glPopAttrib** <font color="red">ogl</font>
    * push and pop the server attribute stack。
* **glPopMatrix** <font color="red">ogl</font>
    * push and pop the current matrix stack。
* **glLoadIdentity** <font color="red">ogl</font>
    * replace the current matrix with the identity matrix。
* **glLoadMatrixf** <font color="red">ogl</font>
    * replace the current matrix with the specified matrix。
* **glMaterialf** <font color="red">ogl</font>
    * specify material parameters for the lighting model。
* **glMaterialfv** <font color="red">ogl</font>
    * 指定用于光照计算的当前材质属性。
* **glMatrixMode** <font color="red">ogl</font>
    * specify which matrix is the current matrix。
* **glMultMatrixf** <font color="red">ogl</font>
    * multiply the current matrix with the specified matrix。


## 都支持的基本 API

* **glReadBuffer** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * select a color buffer source for pixels。
* **glReadPixels** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * read a block of pixels from the frame buffer。
* **glDrawArrays** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * render primitives from array data。
* **glDrawElements** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * render primitives from array data。
* **glEnable** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * enable or disable server-side GL capabilities。
* **glDisable** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * enable or disable server-side GL capabilities。
* **glIsEnabled** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * test whether a capability is enabled。
* **glClear** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * clear buffers to preset values。
* **glClearColor** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * specify clear values for the color buffers。
* **glFrontFace** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * define front- and back-facing polygons。
* **glCullFace** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * specify whether front- or back-facing facets can be culled。
* **glFlush** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * 强制刷新缓冲。
    * force execution of GL commands in finite time。
* **glViewport** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * set the viewport。
* **glGetString** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    *  return a string describing the current GL connection。
* **glGetError** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * return error information。
* **glGetFloatv** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * return the value or values of a selected parameter。
* **glGetIntegerv** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * return the value or values of a selected parameter。
* **glHint** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * specify implementation-specific hints。
    * 指定特定于实现的提示。
* **glTexParameterf** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * set texture parameters。
    * 纹理过滤函数。
* **glTexParameteri** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * set texture parameters。
    * 纹理过滤函数。
* **glLineWidth** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * specify the width of rasterized lines。
    * 设置线段的宽度。
* **glScissor** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * define the scissor box。
    * 剪裁测试用于限制绘制区域。
* **glCopyTexSubImage2D** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * copy a two-dimensional texture subimage。
    * 复制二维纹理子图像。
* **glColorMask** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * enable and disable writing of color buffer components。
    * 启用和禁用帧缓冲区颜色分量的写入。
* **glPolygonOffset** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * set the scale and units used to calculate depth values。
    * 设置计算深度值的拉伸比和单位。
* **glPixelStorei** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * set pixel storage modes。
    * 设置像素存储模式。
* **glTexImage2D** <font color="#0000FF">gles</font>&<font color="red">ogl</font>
    * specify a two-dimensional texture image。
    * 指定一个二维的纹理图片。

<hr class='reviewline'/>
<p class='reviewtip'>2021-01-25: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.khronos.org/registry/OpenGL/index_es.php]({% include relref.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/www.khronos.org/bb75bed1.php" %})
- [https://www.khronos.org/registry/OpenGL/index_gl.php]({% include relref.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/www.khronos.org/a9a79c0a.php" %})
- [http://docs.gl/]({% include relref.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/docs.gl/378832af.html" %})
- [https://www.cnblogs.com/striver-zhu/p/4539160.html]({% include relref.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/www.cnblogs.com/7b349b94.html" %})
