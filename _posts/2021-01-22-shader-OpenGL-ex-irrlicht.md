---
layout: post
title: "特效编程笔记 -- Irrlicht OpenGL 扩展支持 整理文档"
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

$$NV/AMD/INTEL/ATI \leadsto EXT \leadsto ARB \leadsto GL$$

一个 3D 引擎为了更好的性能，就只能适配这些不同的硬件。Irrlicht 用到的 284 个 API。
这些 API 就像后山上的野花，**一簇一簇的**，这个是也是 状态机 C 风格的函数接口的特点决定的。


## 遮挡查询 occlusion query

* glBeginOcclusionQueryNV, glBeginQueryARB // extGlBeginQuery
* glDeleteOcclusionQueriesNV, glDeleteQueriesARB // extGlDeleteQueries
* glEndOcclusionQueryNV, glEndQueryARB // extGlEndQuery
* glGenOcclusionQueriesNV, glGenQueriesARB // extGlGenQueries
* glGetOcclusionQueryivNV, glGetQueryObjectivARB // extGlGetQueryObjectiv
* glGetOcclusionQueryuivNV, glGetQueryObjectuivARB // extGlGetQueryObjectuiv
* glGetQueryivARB // extGlGetQueryiv
* glIsOcclusionQueryNV, glIsQueryARB // extGlIsQuery


## OpenGL WGL

* wglCreateContext ogl
* wglDeleteContext ogl
* wglGetCurrentDC ogl
* wglGetProcAddress ogl
* wglMakeCurrent ogl
* wglChoosePixelFormatARB // ?
* wglCreateContextAttribsARB // ?
* wglGetExtensionsStringARB // ?
* wglSwapIntervalEXT // extGlSwapInterval


## GLES EGL

* eglBindAPI gles
* eglChooseConfig gles
* eglCreateContext gles
* eglCreateWindowSurface gles
* eglDestroyContext gles
* eglDestroySurface gles
* eglGetConfigAttrib gles
* eglGetConfigs gles
* eglGetDisplay gles
* eglGetError gles
* eglInitialize gles
* eglMakeCurrent gles
* eglSwapBuffers gles
* eglSwapInterval gles
* eglTerminate gles


## glUniform 系列

* glUniform1fv gles
* glUniform1iv gles
* glUniform1uiv ogladdr
* glUniform2fv gles
* glUniform2iv gles
* glUniform2uiv ogladdr
* glUniform3fv gles
* glUniform3iv gles
* glUniform3uiv ogladdr
* glUniform4fv gles
* glUniform4iv gles
* glUniform4uiv ogladdr
* glUniformMatrix2fv gles
* glUniformMatrix2x3fv ogladdr
* glUniformMatrix2x4fv ogladdr
* glUniformMatrix3fv gles
* glUniformMatrix3x2fv ogladdr
* glUniformMatrix3x4fv ogladdr
* glUniformMatrix4fv gles
* glUniformMatrix4x2fv ogladdr
* glUniformMatrix4x3fv ogladdr
* glUniform1fvARB // extGlUniform1fv
* glUniform1ivARB // extGlUniform1iv
* glUniform2fvARB // extGlUniform2fv
* glUniform2ivARB // extGlUniform2iv
* glUniform3fvARB // extGlUniform3fv
* glUniform3ivARB // extGlUniform3iv
* glUniform4fvARB // extGlUniform4fv
* glUniform4ivARB // extGlUniform4iv
* glUniformMatrix2fvARB // extGlUniformMatrix2fv
* glUniformMatrix3fvARB // extGlUniformMatrix3fv
* glUniformMatrix4fvARB // extGlUniformMatrix4fv
* glGetActiveUniformARB // extGlGetActiveUniformARB
* glGetUniformLocationARB // extGlGetUniformLocationARB
* glGetActiveUniform gles&ogladdr
* glGetUniformLocation gles&ogladdr


### 模板测试

* glClearStencil gles&ogl
* glStencilFunc gles&ogl
* glStencilFuncSeparate ogladdr
* glStencilMask gles&ogl
* glStencilOp gles&ogl
* glStencilOpSeparate ogladdr
* glStencilFuncSeparateATI // extGlStencilFuncSeparate
* glStencilOpSeparateATI // extGlStencilOpSeparate


## shader programming

* glCreateProgram gles&ogladdr
* glDeleteProgram gles&ogladdr
* glLinkProgram gles&ogladdr
* glUseProgram gles&ogladdr
* glCreateShader gles&ogladdr
* glDeleteShader gles&ogladdr
* glCompileShader gles&ogladdr
* glAttachShader gles&ogladdr
* glGetAttachedShaders gles&ogladdr
* glGetProgramInfoLog gles&ogladdr // extGlGetProgramInfoLog
* glGetShaderInfoLog gles&ogladdr
* glGetProgramiv gles&ogladdr // extGlGetProgramiv
* glGetShaderiv gles&ogladdr
* glGenProgramsNV, glGenProgramsARB // extGlGenPrograms
* glBindProgramNV, glBindProgramARB // extGlBindProgram
* glDeleteProgramsNV, glDeleteProgramsARB // extGlDeletePrograms
* glLoadProgramNV // extGlLoadProgram
* glCreateProgramObjectARB // extGlCreateProgramObject
* glCreateShaderObjectARB // extGlCreateShaderObject
* glLinkProgramARB // extGlLinkProgramARB
* glCompileShaderARB // extGlCompileShaderARB
* glUseProgramObjectARB // extGlUseProgramObject
* glProgramParameteriEXT, glProgramParameteriARB // extGlProgramParameteri
* glProgramLocalParameter4fvARB // extGlProgramLocalParameter4fv
* glShaderSource gles&ogladdr
* glProgramStringARB // extGlProgramString
* glShaderSourceARB // extGlShaderSourceARB


## ATI framebuffer objects

* glGenFramebuffers gles&ogladdr
* glActiveTexture gles&ogladdr
* glBindFramebuffer gles&ogladdr
* glCheckFramebufferStatus gles&ogladdr
* glFramebufferTexture2D gles&ogladdr
* glDeleteFramebuffers gles&ogladdr // irrGlDeleteFramebuffers

* glCreateFramebuffers ogladdr
* glBindRenderbuffer ogladdr
* glNamedFramebufferTexture ogladdr
* glFramebufferRenderbuffer ogladdr
* glFramebufferTexture ogladdr
* glDeleteRenderbuffers ogladdr
* glRenderbufferStorage ogladdr
* glGenRenderbuffers ogladdr

* glGenFramebuffersEXT // irrGlGenFramebuffers
* glBindFramebufferEXT // irrGlBindFramebuffer
* glDeleteFramebuffersEXT // irrGlDeleteFramebuffers
* glCheckFramebufferStatusEXT // irrGlCheckFramebufferStatus
* glNamedFramebufferTextureEXT // extGlNamedFramebufferTexture
* glFramebufferRenderbufferEXT // irrGlFramebufferRenderbuffer
* glFramebufferTexture2DEXT // irrGlFramebufferTexture2D

* glBindRenderbufferEXT // irrGlBindRenderbuffer
* glDeleteRenderbuffersEXT // irrGlDeleteRenderbuffers
* glGenRenderbuffersEXT // irrGlGenRenderbuffers
* glRenderbufferStorageEXT // irrGlRenderbufferStorage

* glBindBuffer gles
* glBufferData gles
* glBufferSubData gles
* glDeleteBuffers gles
* glGenBuffers gles

* glDrawBuffersATI, glDrawBuffersARB // irrGlDrawBuffers

* glMapBufferARB // extGlMapBuffer
* glUnmapBufferARB // extGlUnmapBuffer
* glBufferDataARB // extGlBufferData
* glBufferSubDataARB // extGlBufferSubData
* glBindBufferARB // extGlBindBuffer
* glDeleteBuffersARB // extGlDeleteBuffers
* glGenBuffersARB // extGlGenBuffers
* glIsBufferARB // extGlIsBuffer
* glGetBufferParameterivARB // extGlGetBufferParameteriv
* glGetBufferPointervARB // extGlGetBufferPointerv
* glGetBufferSubDataARB // extGlGetBufferSubData

* glDrawBuffer ogl
* glReadBuffer gles&ogl
* glReadPixels gles&ogl


## 深度测试

* glClearDepthf gles
* glClearDepth ogl
* glDepthFunc gles&ogl
* glDepthMask gles&ogl


## AMD indexed

glBlendEquationIndexedAMD, glBlendEquationiARB // irrGlBlendEquationIndexed
glBlendEquationSeparateIndexedAMD, glBlendEquationSeparateiARB // irrGlBlendEquationSeparateIndexed
glBlendFuncIndexedAMD, glBlendFunciARB // irrGlBlendFuncIndexed
glBlendFuncSeparateIndexedAMD, glBlendFuncSeparateiARB // irrGlBlendFuncSeparateIndexed


## EXT framebuffer objects

glBlendEquationEXT // irrGlBlendEquation
glBlendEquationSeparateEXT // ?
glBlendFuncSeparateEXT // irrGlBlendFuncSeparate

glColorMaskIndexedEXT // irrGlColorMaskIndexed

glDisableIndexedEXT // irrGlDisableIndexed
glEnableIndexedEXT // irrGlEnableIndexed

glGenerateMipmapEXT // irrGlGenerateMipmap
glGenerateTextureMipmapEXT // extGlGenerateTextureMipmap
glGetTextureImageEXT // extGlGetTextureImage

glProvokingVertexEXT // extGlProvokingVertex

glTextureStorage2DEXT // extGlTextureStorage2D
glTextureStorage3DEXT // extGlTextureStorage3D
glTextureSubImage2DEXT // extGlTextureSubImage2D

glActiveTextureARB // irrGlActiveTexture

glAttachObjectARB // extGlAttachObject

glClientActiveTextureARB // irrGlClientActiveTexture

glDeleteObjectARB // extGlDeleteObject

glGetAttachedObjectsARB // extGlGetAttachedObjects

glGetInfoLogARB // extGlGetInfoLog
glGetObjectParameterivARB // extGlGetObjectParameteriv

glPointParameterfARB // extGlPointParameterf
glPointParameterfvARB // extGlPointParameterfv

###

glTexStorage2D ogladdr
glTexStorage3D ogladdr
glTextureParameterf ogladdr
glTextureParameterfv ogladdr
glTextureParameteri ogladdr
glTextureParameteriv ogladdr
glTextureStorage2D ogladdr
glTextureStorage3D ogladdr
glTextureSubImage2D ogladdr


### gles&ogladdr

glBlendEquation gles&ogladdr

glBlendFuncSeparate gles&ogladdr


### GLES Only

glBindAttribLocation gles

glDisableVertexAttribArray gles
glEnableVertexAttribArray gles

glVertexAttribPointer gles


## OpenGL 扩展？

glBindTextures ogladdr
glBlendEquationSeparate ogladdr

glCreateTextures ogladdr

glGenerateTextureMipmap ogladdr
glProvokingVertex ogladdr

glGetTextureImage ogladdr


### GLES & OpenGL 扩展

glCompressedTexImage2D gles&ogladdr
glCompressedTexSubImage2D gles&ogladdr

glGenerateMipmap gles&ogladdr


## OpenGL Only

glGetTexImage ogl
glDisableClientState ogl

glEnableClientState ogl
glClipPlane ogl
glColor4ub ogl
glColorMaterial ogl
glColorPointer ogl
glFogf ogl
glFogfv ogl
glFogi ogl
glLightModelfv ogl
glLightModeli ogl
glLightf ogl
glLightfv ogl
glNormalPointer ogl
glPointSize ogl
glPolygonMode ogl
glPopAttrib ogl
glPopMatrix ogl
glRectf ogl
glAlphaFunc ogl
glVertexPointer ogl
glTranslatef ogl
glTexCoordPointer ogl
glTexEnvf ogl
glTexEnvi ogl
glTexGeni ogl
glShadeModel ogl
glPushAttrib ogl
glPushMatrix ogl
glLoadIdentity ogl
glLoadMatrixf ogl
glMaterialf ogl
glMaterialfv ogl
glMatrixMode ogl
glMultMatrixf ogl


## 都支持的

glFrontFace gles&ogl
glGenTextures gles&ogl

glPixelStorei gles&ogl
glPolygonOffset gles&ogl

glCullFace gles&ogl
glTexImage2D gles&ogl
glTexParameterf gles&ogl
glTexParameteri gles&ogl
glTexSubImage2D gles&ogl
glViewport gles&ogl

glHint gles&ogl
glIsEnabled gles&ogl
glLineWidth gles&ogl

glScissor gles&ogl

glGetError gles&ogl
glGetFloatv gles&ogl
glGetIntegerv gles&ogl

glClear gles&ogl
glClearColor gles&ogl

glDrawArrays gles&ogl
glDrawElements gles&ogl
glEnable gles&ogl
glFlush gles&ogl

glBlendFunc gles&ogl
glBindTexture gles&ogl
glColorMask gles&ogl
glCopyTexSubImage2D gles&ogl
glDeleteTextures gles&ogl

glDisable gles&ogl
glGetString gles&ogl

-----
<p class='reviewtip'>2021-01-22: review</p>
