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

$$NV/AMD/INTEL/ATI \leadsto EXT \leadsto ARB \leadsto GL$$

一个 3D 引擎为了更好的性能，就只能适配这些不同的硬件。Irrlicht 用到的 284 个 API。
这些 API 就像后山上的野花，**一簇一簇的**，这个也是 状态机 C 风格函数接口的特点。

开始觉得很难，学了一段时间的 OpenGL，觉得也就那样，尝试改造 3D 引擎，发现一千多个 API，常用的 284 个，而且 OpenGL & OpenGL ES 存在巨大差异，不同硬件之间还存在差异，唏嘘不已。

* **GLES 扩展 333 个：<https://www.khronos.org/registry/OpenGL/index_es.php>
* **OpenGL 扩展 554 个：<https://www.khronos.org/registry/OpenGL/index_gl.php>

OpenGL ES & OpenGL 存在大量 API 交叉的情况，为了兼容，很多 API 采用 wglGetProcAddress 函数指针的形式。包含厂商后缀的都是 wglGetProcAddress，ogladdr。分了五类：

* **只支持 GLES: gles（大概 36 个）
* **只支持 OpenGL & wglGetProcAddress: ogladdr（大概 140 个）
* **只支持 OpenGL: ogl（大概 43 个）
* **两个都支持 OpenGL & wglGetProcAddress: gles&ogladdr（大概 27 个）
* **两个都支持：gles&ogl（大概 38 个）

{'gles': 36, 'gles&ogladdr': 27, 'ogladdr': 140, 'ogl': 43, 'gles&ogl': 38}


## 遮挡查询 occlusion query

* **glBeginOcclusionQueryNV**, **glBeginQueryARB** // extGlBeginQuery
* **glDeleteOcclusionQueriesNV**, **glDeleteQueriesARB** // extGlDeleteQueries
* **glEndOcclusionQueryNV**, **glEndQueryARB** // extGlEndQuery
* **glGenOcclusionQueriesNV**, **glGenQueriesARB** // extGlGenQueries
* **glGetOcclusionQueryivNV**, **glGetQueryObjectivARB** // extGlGetQueryObjectiv
* **glGetOcclusionQueryuivNV**, **glGetQueryObjectuivARB** // extGlGetQueryObjectuiv
* **glGetQueryivARB** // extGlGetQueryiv
* **glIsOcclusionQueryNV**, **glIsQueryARB** // extGlIsQuery


## OpenGL WGL

* **wglCreateContext** ogl
* **wglDeleteContext** ogl
* **wglGetCurrentDC** ogl
* **wglGetProcAddress** ogl
* **wglMakeCurrent** ogl
* **wglChoosePixelFormatARB** // ? 请求并选择一个匹配的像素格式
* **wglCreateContextAttribsARB** // ? 创建和使用 OpenGL
* **wglGetExtensionsStringARB** // ? 检查是否支持 WGL_ARB_extensions_string 扩展
* **wglSwapIntervalEXT** // extGlSwapInterval 是否启用垂直同步


## GLES EGL

* **eglBindAPI** gles
* **eglChooseConfig** gles
* **eglCreateContext** gles
* **eglCreateWindowSurface** gles
* **eglDestroyContext** gles
* **eglDestroySurface** gles
* **eglGetConfigAttrib** gles
* **eglGetConfigs** gles
* **eglGetDisplay** gles
* **eglGetError** gles
* **eglInitialize** gles
* **eglMakeCurrent** gles
* **eglSwapBuffers** gles
* **eglSwapInterval** gles
* **eglTerminate** gles


## glUniform 系列

* **glUniform1fv** gles
* **glUniform1iv** gles
* **glUniform1uiv** ogladdr
* **glUniform2fv** gles
* **glUniform2iv** gles
* **glUniform2uiv** ogladdr
* **glUniform3fv** gles
* **glUniform3iv** gles
* **glUniform3uiv** ogladdr
* **glUniform4fv** gles
* **glUniform4iv** gles
* **glUniform4uiv** ogladdr
* **glUniformMatrix2fv** gles
* **glUniformMatrix2x3fv** ogladdr
* **glUniformMatrix2x4fv** ogladdr
* **glUniformMatrix3fv** gles
* **glUniformMatrix3x2fv** ogladdr
* **glUniformMatrix3x4fv** ogladdr
* **glUniformMatrix4fv** gles
* **glUniformMatrix4x2fv** ogladdr
* **glUniformMatrix4x3fv** ogladdr
* **glUniform1fvARB** // extGlUniform1fv
* **glUniform1ivARB** // extGlUniform1iv
* **glUniform2fvARB** // extGlUniform2fv
* **glUniform2ivARB** // extGlUniform2iv
* **glUniform3fvARB** // extGlUniform3fv
* **glUniform3ivARB** // extGlUniform3iv
* **glUniform4fvARB** // extGlUniform4fv
* **glUniform4ivARB** // extGlUniform4iv
* **glUniformMatrix2fvARB** // extGlUniformMatrix2fv
* **glUniformMatrix3fvARB** // extGlUniformMatrix3fv
* **glUniformMatrix4fvARB** // extGlUniformMatrix4fv
* **glGetActiveUniformARB** // extGlGetActiveUniformARB
* **glGetUniformLocationARB** // extGlGetUniformLocationARB
* **glGetActiveUniform** gles&ogladdr
* **glGetUniformLocation** gles&ogladdr


## 模板测试

* **glClearStencil** gles&ogl
* **glStencilFunc** gles&ogl
* **glStencilMask** gles&ogl
* **glStencilOp** gles&ogl
* **glStencilFuncSeparate** ogladdr
* **glStencilOpSeparate** ogladdr
* **glStencilFuncSeparateATI** // extGlStencilFuncSeparate
* **glStencilOpSeparateATI** // extGlStencilOpSeparate


## general functions

* **glActiveTexture** gles&ogladdr
* **glCompressedTexImage2D** gles&ogladdr
* **glCompressedTexSubImage2D** gles&ogladdr
* **glActiveTextureARB** // irrGlActiveTexture
* **glClientActiveTextureARB** // irrGlClientActiveTexture
* **glPointParameterfARB** // extGlPointParameterf
* **glPointParameterfvARB** // extGlPointParameterfv


## shader programming

* **glGenProgramsNV**, **glGenProgramsARB** // extGlGenPrograms
* **glBindProgramNV**, **glBindProgramARB** // extGlBindProgram
* **glLoadProgramNV** // extGlLoadProgram
* **glProgramStringARB** // extGlProgramString, 貌似跟上面一个用途一样
* **glDeleteProgramsNV**, **glDeleteProgramsARB** // extGlDeletePrograms
* **glProgramLocalParameter4fvARB** // extGlProgramLocalParameter4fv
* **glCreateProgramObjectARB** // extGlCreateProgramObject
* **glCreateShaderObjectARB** // extGlCreateShaderObject
<hr/>
* **glCreateProgram** gles&ogladdr
* **glDeleteProgram** gles&ogladdr
* **glLinkProgram** gles&ogladdr
* **glUseProgram** gles&ogladdr
<hr/>
* **glCreateShader** gles&ogladdr
* **glDeleteShader** gles&ogladdr
* **glCompileShader** gles&ogladdr
* **glAttachShader** gles&ogladdr
<hr/>
* **glGetAttachedShaders** gles&ogladdr
* **glGetProgramInfoLog** gles&ogladdr // extGlGetProgramInfoLog
* **glGetShaderInfoLog** gles&ogladdr
* **glGetProgramiv** gles&ogladdr // extGlGetProgramiv
* **glGetShaderiv** gles&ogladdr
* **glShaderSource** gles&ogladdr
<hr/>
* **glShaderSourceARB** // extGlShaderSourceARB
* **glCompileShaderARB** // extGlCompileShaderARB
* **glLinkProgramARB** // extGlLinkProgramARB
* **glGetInfoLogARB** // extGlGetInfoLog
* **glGetObjectParameterivARB** // extGlGetObjectParameteriv
* **glUseProgramObjectARB** // extGlUseProgramObject
* **glAttachObjectARB** // extGlAttachObject
* **glDeleteObjectARB** // extGlDeleteObject
* **glGetAttachedObjectsARB** // extGlGetAttachedObjects


## framebuffer objects

* **glGenFramebuffers** gles&ogladdr
* **glBindFramebuffer** gles&ogladdr
* **glCheckFramebufferStatus** gles&ogladdr
* **glFramebufferTexture2D** gles&ogladdr
* **glDeleteFramebuffers** gles&ogladdr // irrGlDeleteFramebuffers
* **glGenerateMipmap** gles&ogladdr
<hr/>
* **glGenFramebuffersEXT** // irrGlGenFramebuffers
* **glBindFramebufferEXT** // irrGlBindFramebuffer
* **glCheckFramebufferStatusEXT** // irrGlCheckFramebufferStatus
* **glFramebufferTexture2DEXT** // irrGlFramebufferTexture2D
* **glDeleteFramebuffersEXT** // irrGlDeleteFramebuffers
<hr/>
* **glBindRenderbuffer** ogladdr
* **glDeleteRenderbuffers** ogladdr
* **glGenRenderbuffers** ogladdr
* **glRenderbufferStorage** ogladdr
* **glFramebufferRenderbuffer** ogladdr
* **glFramebufferTexture** ogladdr
<hr/>
* **glBindRenderbufferEXT** // irrGlBindRenderbuffer
* **glDeleteRenderbuffersEXT** // irrGlDeleteRenderbuffers
* **glGenRenderbuffersEXT** // irrGlGenRenderbuffers
* **glRenderbufferStorageEXT** // irrGlRenderbufferStorage
* **glFramebufferRenderbufferEXT** // irrGlFramebufferRenderbuffer
* **glGenerateMipmapEXT** // irrGlGenerateMipmap
<hr/>
* **glDrawBuffer** ogl
* **glDrawBuffersATI**, **glDrawBuffersARB** // irrGlDrawBuffers


## vertex buffer object

* **glGenBuffers** gles
* **glBindBuffer** gles
* **glBufferData** gles
* **glBufferSubData** gles
* **glDeleteBuffers** gles
<hr/>
* **glGenBuffersARB** // extGlGenBuffers
* **glBindBufferARB** // extGlBindBuffer
* **glBufferDataARB** // extGlBufferData
* **glDeleteBuffersARB** // extGlDeleteBuffers
<hr/>
* **glBufferSubDataARB** // extGlBufferSubData
* **glGetBufferSubDataARB** // extGlGetBufferSubData
* **glMapBufferARB** // extGlMapBuffer
* **glUnmapBufferARB** // extGlUnmapBuffer
* **glIsBufferARB** // extGlIsBuffer
* **glGetBufferParameterivARB** // extGlGetBufferParameteriv
* **glGetBufferPointervARB** // extGlGetBufferPointerv
* **glProvokingVertexEXT** // extGlProvokingVertex
* **glProvokingVertex** ogladdr
* **glProgramParameteriEXT**, **glProgramParameteriARB** // extGlProgramParameteri


## 纹理

* **glTextureSubImage2D** ogladdr
* **glTexSubImage2D** gles&ogl
* **glTextureStorage2D** ogladdr
* **glTexStorage2D** ogladdr
* **glTextureStorage3D** ogladdr
* **glTexStorage3D** ogladdr
* **glGetTextureImage** ogladdr
* **glGetTexImage** ogl
* **glTextureStorage2DEXT** // extGlTextureStorage2D
* **glTextureSubImage2DEXT** // extGlTextureSubImage2D
* **glTextureStorage3DEXT** // extGlTextureStorage3D
* **glGetTextureImageEXT** // extGlGetTextureImage
<hr/>
* **glNamedFramebufferTexture** ogladdr
* **glNamedFramebufferTextureEXT** // extGlNamedFramebufferTexture
* **glTextureParameterf** ogladdr
* **glTextureParameterfv** ogladdr
* **glTextureParameteri** ogladdr
* **glTextureParameteriv** ogladdr
<hr/>
* **glCreateTextures** ogladdr
* **glCreateFramebuffers** ogladdr
* **glBindTextures** ogladdr
<hr/>
* **glGenTextures** gles&ogl
* **glBindTexture** gles&ogl
* **glDeleteTextures** gles&ogl
<hr/>
* **glGenerateTextureMipmap** ogladdr
* **glGenerateTextureMipmapEXT** // extGlGenerateTextureMipmap


## 深度测试

* **glClearDepthf** gles
* **glClearDepth** ogl
* **glDepthFunc** gles&ogl
* **glDepthMask** gles&ogl


## 颜色混合 Blend indexed

* **glDisableIndexedEXT** // irrGlDisableIndexed
* **glEnableIndexedEXT** // irrGlEnableIndexed
* **glColorMaskIndexedEXT** // irrGlColorMaskIndexed
<hr/>
* **glBlendFuncIndexedAMD**, **glBlendFunciARB** // irrGlBlendFuncIndexed
* **glBlendFuncSeparateIndexedAMD**, **glBlendFuncSeparateiARB** // irrGlBlendFuncSeparateIndexed
* **glBlendEquationIndexedAMD**, **glBlendEquationiARB** // irrGlBlendEquationIndexed
* **glBlendEquationSeparateIndexedAMD**, **glBlendEquationSeparateiARB** // irrGlBlendEquationSeparateIndexed
<hr/>
* **glBlendEquationEXT** // irrGlBlendEquation
* **glBlendEquationSeparateEXT** // ?
* **glBlendFuncSeparateEXT** // irrGlBlendFuncSeparate
<hr/>
* **glBlendEquation** gles&ogladdr
* **glBlendFuncSeparate** gles&ogladdr
* **glBlendFunc** gles&ogl
* **glBlendEquationSeparate** ogladdr


## GLES Only

* **glBindAttribLocation** gles
* **glDisableVertexAttribArray** gles
* **glEnableVertexAttribArray** gles
* **glVertexAttribPointer** gles


## OpenGL Only

* **glDisableClientState** ogl
* **glEnableClientState** ogl
* **glClipPlane** ogl // 定义一个裁剪平面
* **glColor4ub** ogl
* **glColorMaterial** ogl
* **glColorPointer** ogl
* **glFogf** ogl
* **glFogfv** ogl
* **glFogi** ogl
* **glLightModelfv** ogl
* **glLightModeli** ogl
* **glLightf** ogl
* **glLightfv** ogl
* **glNormalPointer** ogl
* **glPointSize** ogl
* **glPolygonMode** ogl
* **glPopAttrib** ogl
* **glPopMatrix** ogl
* **glRectf** ogl
* **glAlphaFunc** ogl
* **glVertexPointer** ogl
* **glTranslatef** ogl
* **glTexCoordPointer** ogl
* **glTexEnvf** ogl
* **glTexEnvi** ogl
* **glTexGeni** ogl
* **glShadeModel** ogl
* **glPushAttrib** ogl
* **glPushMatrix** ogl
* **glLoadIdentity** ogl
* **glLoadMatrixf** ogl
* **glMaterialf** ogl
* **glMaterialfv** ogl
* **glMatrixMode** ogl
* **glMultMatrixf** ogl


## 都支持的基本 API

* **glReadBuffer** gles&ogl
* **glReadPixels** gles&ogl
* **glDrawArrays** gles&ogl
* **glDrawElements** gles&ogl
* **glEnable** gles&ogl
* **glDisable** gles&ogl
* **glIsEnabled** gles&ogl
* **glClear** gles&ogl
* **glClearColor** gles&ogl
* **glFrontFace** gles&ogl
* **glCullFace** gles&ogl
* **glFlush** gles&ogl
* **glViewport** gles&ogl
* **glGetString** gles&ogl
* **glGetError** gles&ogl
* **glGetFloatv** gles&ogl
* **glGetIntegerv** gles&ogl
* **glHint** gles&ogl // 指定特定于实现的提示
* **glTexParameterf** gles&ogl // 纹理过滤函数
* **glTexParameteri** gles&ogl // 纹理过滤函数
* **glLineWidth** gles&ogl
* **glScissor** gles&ogl // 剪裁测试用于限制绘制区域
* **glCopyTexSubImage2D** gles&ogl // 复制二维纹理子图像
* **glColorMask** gles&ogl // 启用和禁用帧缓冲区颜色分量的写入
* **glPolygonOffset** gles&ogl
* **glPixelStorei** gles&ogl
* **glTexImage2D** gles&ogl // 根据指定的参数，生成一个 2D 纹理

<hr class='reviewline'/>
<p class='reviewtip'>2021-01-23: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.khronos.org/registry/OpenGL/index_es.php]({% include relref.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/www.khronos.org/bb75bed1.php" %})
- [https://www.khronos.org/registry/OpenGL/index_gl.php]({% include relref.html url="/backup/2021-01-22-shader-OpenGL-ex-irrlicht.md/www.khronos.org/a9a79c0a.php" %})
