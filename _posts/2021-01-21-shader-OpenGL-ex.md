---
layout: post
title: "特效编程笔记 -- OpenGL 的 Windows 组件 和 扩展"
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

<https://riptutorial.com/zh-CN/opengl>
OpenGL 是由一些充满智慧的人设计的，他们拥有丰富的图形程序设计 API 设计经验。


## WGL

WGL（可以发音为 wiggle）代表“Windows-GL”，如“Windows 和 OpenGL 之间的接口” - 来自 Windows API 的一组函数，用于与 OpenGL 通信。WGL 函数具有 wgl 前缀，其标记具有 WGL_ 前缀。

Microsoft 系统支持的默认 OpenGL 版本为 1.1。这是一个非常旧的版本（最近的版本是 4.5）。获取最新版本的方法是更新图形驱动程序，但您的图形卡必须支持这些新版本。

可以在此处找到 WGL 功能的完整列表。
[from](https://docs.microsoft.com/zh-cn/windows/win32/opengl/wgl-functions)

```
wglCopyContext
wglCreateContext
wglCreateLayerContext
wglDeleteContext
wglDescribeLayerPlane
wglGetCurrentContext
wglGetCurrentDC
wglGetLayerPaletteEntries
wglGetProcAddress
wglMakeCurrent
wglRealizeLayerPalette
wglSetLayerPaletteEntries
wglShareLists
wglSwapLayerBuffers
wglUseFontBitmaps
wglUseFontOutlines
```


## 图形设备接口（GDI）

GDI（今天更新为 GDI+）是一个 2D 绘图界面，允许您在 Windows 中绘制窗口。
您需要 GDI 来初始化 OpenGL 并允许它与它交互（但实际上不会使用 GDI 本身）。

在 GDI 中，每个窗口都有一个设备上下文（DC），用于在调用函数时标识绘图目标（将其作为参数传递）。
但是，OpenGL 使用自己的渲染上下文（RC）。因此，DC 将用于创建 RC。


## 渲染上下文

我们可以简单地创建渲染上下文：

```cpp
/* RENDERING CONTEXT */
HGLRC rc = wglCreateContext(dc);
wglMakeCurrent(dc, rc);
/* ***************** */
```

请注意，一次只能有一个线程使用 RC。如果你希望稍后从另一个线程使用它，你必须 wglMakeCurrent 那里调用 wglMakeCurrent 来再次激活它（这将在它当前处于活动状态的线程上停用它，依此类推）。


## OpenGL 扩展

对 OpenGL 的原始功能的任何添加都称为扩展。通常，它们可以使某些事情变得合法，扩展参数值范围，扩展 GLSL，甚至添加全新的功能。

有三个主要的扩展组：供应商，EXT 和 ARB。供应商扩展来自特定供应商，它们具有供应商特定标记，如 AMD 或 NV。
EXT 扩展由多个供应商共同完成。一段时间后，它们可能会成为 ARB 扩展，这些都是官方支持的 ARB 和 ARB 批准的扩展。

要获取所有扩展的函数指针类型和函数原型， 并且如前所述，来自 OpenGL 1.2 和更高版本的所有函数指针类型，必须从 OpenGL 注册表下载头文件。
如上所述，对于新应用程序，最好使用核心配置文件，因此最好包括 GL/glcorearb.h 而不是 GL/gl.h 和 GL/glext.h（如果您使用的是 GL/glcorearb.h 那么请不包括 GL/gl.h）。

在 GL/wglext.h 中还有 WGL 的扩展。例如，获取所有支持的扩展列表的函数实际上是一个扩展本身，即 wglGetExtensionsStringARB（它返回一个大字符串，其中包含所有支持的扩展的空格分隔列表）。

获取扩展也是通过 wglGetProcAddress 处理的，所以我们可以像以前一样使用我们的包装器。


## Windows wglGetProcAddress

<https://www.khronos.org/opengl/wiki/Load_OpenGL_Functions>

So in order to get the address of any GL function one can try with wglGetProcAddress and if it fails, try again with the Win32's GetProcAddress:

```cpp
void *GetAnyGLFuncAddress(const char *name)
{
    void *p = (void *)wglGetProcAddress(name);
    if(p == 0 ||
        (p == (void*)0x1) || (p == (void*)0x2) || (p == (void*)0x3) ||
        (p == (void*)-1) )
    {
        HMODULE module = LoadLibraryA("opengl32.dll");
        p = (void *)GetProcAddress(module, name);
    }

    return p;
}
```


## OpenGL ARB

[from {% include relref_csdn.html %}](https://blog.csdn.net/qq_31243065/article/details/105466436)
这样 OpenGL 体系结构审核委员会 (ARB, OpenGL Architecture Reiview Board) 就诞生了。

```cpp
GLint nNum;
glGetIntegerv(GL_NUM_EXTENSIONS, &nNum); // 跟上一个示例一样，获取扩展支持数量

// 遍历所有扩展
for (GLint i = 0; i < nNum; ++i) {
    // 判断是否支持扩展名为: WGL_EXT_swap_control 的扩展
    if (strcmp("WGL_EXT_swap_control", (const char *)glGetStringi(GL_EXTENSIONS, i)) == 0)
    {
        // 支持则获取这个扩展函数的函数指针
        wglSwapIntervalExt = (PFNWGLSWAPINTERVALEXTPROC)wglGetProcAddress("wglSwapIntervalExt");
        if (wglSwapIntervalExt != NULL) {
            // 调用设置这个扩展
            wglSwapIntervalExt(1);
        }
     }
}
```


## OpenGL 扩展识别示例

前缀 | 提 供 商
---- | ----
SGI_ | Silicon Graphics
ATI_ | ATI Tenchnologies
AMD_ | Advanced Micro Devices
NV_ | NVIDIA
IBM_ | IBM
WGL_ | Microsoft
EXT_ | Cross-Vendor
ARB_ | ARB Approved

[第十二课：OpenGL 扩展 {% include relref_csdn.html %}](https://blog.csdn.net/qq_22822335/article/details/50682294)

ARB vs EXT vs …
扩展的名字暗示了它的适用范围：

* GL_: 所有平台；
* GLX_: 只有 Linux 和 Mac 下可使用（X11）；
* WGL_: 只有 Windows 下可使用。
* EXT: 通用的扩展。
* ARB: 已经被 OpenGL 架构评审委员会的所有成员接受（EXT 扩展没多久后就经常被提升为 ARB）的扩展。
* NV/AMD/INTEL: 顾名思义。


## OpenGL ES & OpenGL API

OpenGL ES & OpenGL 存在大量 API 交叉的情况。分了五类：

* 只支持 GLES: gles
* 只支持 OpenGL & wglGetProcAddress: ogladdr
* 只支持 OpenGL: ogl
* 两个都支持 OpenGL & wglGetProcAddress: gles&ogladdr
* 两个都支持: gles&ogl

Irrlicht 用到的 284 个 API：

<dl>
<dt>eglBindAPI gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglBindAPI(EGLenum api);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglChooseConfig gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglChooseConfig(EGLDisplay dpy, const EGLint* attrib_list, EGLConfig* configs, EGLint config_size, EGLint* num_config);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglCreateContext gles</dt>
<dd>EglAPI EGLContext EglAPIENTRY eglCreateContext(EGLDisplay dpy, EGLConfig config, EGLContext share_context, const EGLint* attrib_list);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglCreateWindowSurface gles</dt>
<dd>EglAPI EGLSurface EglAPIENTRY eglCreateWindowSurface(EGLDisplay dpy, EGLConfig config, EGLNativeWindowType win, const EGLint* attrib_list);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglDestroyContext gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglDestroyContext(EGLDisplay dpy, EGLContext ctx);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglDestroySurface gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglDestroySurface(EGLDisplay dpy, EGLSurface surface);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglGetConfigAttrib gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglGetConfigAttrib(EGLDisplay dpy, EGLConfig config, EGLint attribute, EGLint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglGetConfigs gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglGetConfigs(EGLDisplay dpy, EGLConfig* configs, EGLint config_size, EGLint* num_config);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglGetDisplay gles</dt>
<dd>EglAPI EGLDisplay EglAPIENTRY eglGetDisplay(EGLNativeDisplayType display_id);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglGetError gles</dt>
<dd>EglAPI EGLint EglAPIENTRY eglGetError(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglInitialize gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglInitialize(EGLDisplay dpy, EGLint* major, EGLint* minor);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglMakeCurrent gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglMakeCurrent(EGLDisplay dpy, EGLSurface draw, EGLSurface read, EGLContext ctx);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglSwapBuffers gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglSwapBuffers(EGLDisplay dpy, EGLSurface surface);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglSwapInterval gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglSwapInterval(EGLDisplay dpy, EGLint interval);</dd>
<dd></dd>
</dl>
<dl>
<dt>eglTerminate gles</dt>
<dd>EglAPI EGLBoolean EglAPIENTRY eglTerminate(EGLDisplay dpy);</dd>
<dd></dd>
</dl>
<dl>
<dt>glActiveTexture gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glActiveTexture(GLenum texture);</dd>
<dd></dd>
</dl>
<dl>
<dt>glActiveTextureARB ogladdr</dt>
<dd>glAPI void APIENTRY glActiveTextureARB(GLenum texture);</dd>
<dd></dd>
</dl>
<dl>
<dt>glAlphaFunc ogl</dt>
<dd>WINzGDIAPI void APIENTRY glAlphaFunc(GLenum efunc, GLclampf ref);</dd>
<dd></dd>
</dl>
<dl>
<dt>glAttachObjectARB ogladdr</dt>
<dd>glAPI void APIENTRY glAttachObjectARB(GLhandleARB containerObj, GLhandleARB obj);</dd>
<dd></dd>
</dl>
<dl>
<dt>glAttachShader gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glAttachShader(GLuint program, GLuint shader);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBeginOcclusionQueryNV ogladdr</dt>
<dd>glAPI void APIENTRY glBeginOcclusionQueryNV(GLuint id);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBeginQueryARB ogladdr</dt>
<dd>glAPI void APIENTRY glBeginQueryARB(GLenum target, GLuint id);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindAttribLocation gles</dt>
<dd>glAPICALL void glAPIENTRY glBindAttribLocation(GLuint program, GLuint index, const GLchar* name);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindBuffer gles</dt>
<dd>glAPICALL void glAPIENTRY glBindBuffer(GLenum target, GLuint buffer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindBufferARB ogladdr</dt>
<dd>glAPI void APIENTRY glBindBufferARB(GLenum target, GLuint buffer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindFramebuffer gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glBindFramebuffer(GLenum target, GLuint framebuffer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindFramebufferEXT ogladdr</dt>
<dd>glAPI void APIENTRY glBindFramebufferEXT(GLenum target, GLuint framebuffer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindProgramARB ogladdr</dt>
<dd>glAPI void APIENTRY glBindProgramARB(GLenum target, GLuint program);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindProgramNV ogladdr</dt>
<dd>glAPI void APIENTRY glBindProgramNV(GLenum target, GLuint id);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindRenderbuffer ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glBindRenderbuffer(GLenum target, GLuint renderbuffer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindRenderbufferEXT ogladdr</dt>
<dd>glAPI void APIENTRY glBindRenderbufferEXT(GLenum target, GLuint renderbuffer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindTexture gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glBindTexture(GLenum target, GLuint texture);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBindTextures ogladdr</dt>
<dd>glAPI void APIENTRY glBindTextures(GLuint first, GLsizei count, const GLuint* textures);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendEquation gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glBlendEquation(GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendEquationEXT ogladdr</dt>
<dd>glAPI void APIENTRY glBlendEquationEXT(GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendEquationIndexedAMD ogladdr</dt>
<dd>glAPI void APIENTRY glBlendEquationIndexedAMD(GLuint buf, GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendEquationSeparate ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glBlendEquationSeparate(GLenum modeRGB, GLenum modeAlpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendEquationSeparateEXT ogladdr</dt>
<dd>glAPI void APIENTRY glBlendEquationSeparateEXT(GLenum modeRGB, GLenum modeAlpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendEquationSeparateIndexedAMD ogladdr</dt>
<dd>glAPI void APIENTRY glBlendEquationSeparateIndexedAMD(GLuint buf, GLenum modeRGB, GLenum modeAlpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendEquationSeparateiARB ogladdr</dt>
<dd>glAPI void APIENTRY glBlendEquationSeparateiARB(GLuint buf, GLenum modeRGB, GLenum modeAlpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendEquationiARB ogladdr</dt>
<dd>glAPI void APIENTRY glBlendEquationiARB(GLuint buf, GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendFunc gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glBlendFunc(GLenum sfactor, GLenum dfactor);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendFuncIndexedAMD ogladdr</dt>
<dd>glAPI void APIENTRY glBlendFuncIndexedAMD(GLuint buf, GLenum src, GLenum dst);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendFuncSeparate gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glBlendFuncSeparate(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendFuncSeparateEXT ogladdr</dt>
<dd>glAPI void APIENTRY glBlendFuncSeparateEXT(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendFuncSeparateIndexedAMD ogladdr</dt>
<dd>glAPI void APIENTRY glBlendFuncSeparateIndexedAMD(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendFuncSeparateiARB ogladdr</dt>
<dd>glAPI void APIENTRY glBlendFuncSeparateiARB(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBlendFunciARB ogladdr</dt>
<dd>glAPI void APIENTRY glBlendFunciARB(GLuint buf, GLenum src, GLenum dst);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBufferData gles</dt>
<dd>glAPICALL void glAPIENTRY glBufferData(GLenum target, GLsizeiptr size, const void* data, GLenum usage);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBufferDataARB ogladdr</dt>
<dd>glAPI void APIENTRY glBufferDataARB(GLenum target, GLsizeiptrARB size, const void* data, GLenum usage);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBufferSubData gles</dt>
<dd>glAPICALL void glAPIENTRY glBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, const void* data);</dd>
<dd></dd>
</dl>
<dl>
<dt>glBufferSubDataARB ogladdr</dt>
<dd>glAPI void APIENTRY glBufferSubDataARB(GLenum target, GLintptrARB offset, GLsizeiptrARB size, const void* data);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCheckFramebufferStatus gles&ogladdr</dt>
<dd>glAPICALL GLenum glAPIENTRY glCheckFramebufferStatus(GLenum target);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCheckFramebufferStatusEXT ogladdr</dt>
<dd>glAPI GLenum APIENTRY glCheckFramebufferStatusEXT(GLenum target);</dd>
<dd></dd>
</dl>
<dl>
<dt>glClear gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glClear(GLbitfield mask);</dd>
<dd></dd>
</dl>
<dl>
<dt>glClearColor gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glClearDepth ogl</dt>
<dd>WINzGDIAPI void APIENTRY glClearDepth(GLclampd depth);</dd>
<dd></dd>
</dl>
<dl>
<dt>glClearDepthf gles</dt>
<dd>glAPICALL void glAPIENTRY glClearDepthf(GLfloat d);</dd>
<dd></dd>
</dl>
<dl>
<dt>glClearStencil gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glClearStencil(GLint s);</dd>
<dd></dd>
</dl>
<dl>
<dt>glClientActiveTextureARB ogladdr</dt>
<dd>glAPI void APIENTRY glClientActiveTextureARB(GLenum texture);</dd>
<dd></dd>
</dl>
<dl>
<dt>glClipPlane ogl</dt>
<dd>WINzGDIAPI void APIENTRY glClipPlane(GLenum plane, const GLdouble *equation);</dd>
<dd></dd>
</dl>
<dl>
<dt>glColor4ub ogl</dt>
<dd>WINzGDIAPI void APIENTRY glColor4ub(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glColorMask gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha);</dd>
<dd></dd>
</dl>
<dl>
<dt>glColorMaskIndexedEXT ogladdr</dt>
<dd>glAPI void APIENTRY glColorMaskIndexedEXT(GLuint index, GLboolean r, GLboolean g, GLboolean b, GLboolean a);</dd>
<dd></dd>
</dl>
<dl>
<dt>glColorMaterial ogl</dt>
<dd>WINzGDIAPI void APIENTRY glColorMaterial(GLenum face, GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glColorPointer ogl</dt>
<dd>WINzGDIAPI void APIENTRY glColorPointer(GLint size, GLenum type, GLsizei stride, const GLvoid *pointer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCompileShader gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glCompileShader(GLuint shader);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCompileShaderARB ogladdr</dt>
<dd>glAPI void APIENTRY glCompileShaderARB(GLhandleARB shaderObj);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCompressedTexImage2D gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void* data);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCompressedTexSubImage2D gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void* data);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCopyTexSubImage2D gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCreateFramebuffers ogladdr</dt>
<dd>glAPI void APIENTRY glCreateFramebuffers(GLsizei n, GLuint* framebuffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCreateProgram gles&ogladdr</dt>
<dd>glAPICALL GLuint glAPIENTRY glCreateProgram(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCreateProgramObjectARB ogladdr</dt>
<dd>glAPI GLhandleARB APIENTRY glCreateProgramObjectARB(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCreateShader gles&ogladdr</dt>
<dd>glAPICALL GLuint glAPIENTRY glCreateShader(GLenum type);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCreateShaderObjectARB ogladdr</dt>
<dd>glAPI GLhandleARB APIENTRY glCreateShaderObjectARB(GLenum shaderType);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCreateTextures ogladdr</dt>
<dd>glAPI void APIENTRY glCreateTextures(GLenum target, GLsizei n, GLuint* textures);</dd>
<dd></dd>
</dl>
<dl>
<dt>glCullFace gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glCullFace(GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteBuffers gles</dt>
<dd>glAPICALL void glAPIENTRY glDeleteBuffers(GLsizei n, const GLuint* buffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteBuffersARB ogladdr</dt>
<dd>glAPI void APIENTRY glDeleteBuffersARB(GLsizei n, const GLuint* buffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteFramebuffers gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glDeleteFramebuffers(GLsizei n, const GLuint* framebuffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteFramebuffersEXT ogladdr</dt>
<dd>glAPI void APIENTRY glDeleteFramebuffersEXT(GLsizei n, const GLuint* framebuffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteObjectARB ogladdr</dt>
<dd>glAPI void APIENTRY glDeleteObjectARB(GLhandleARB obj);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteOcclusionQueriesNV ogladdr</dt>
<dd>glAPI void APIENTRY glDeleteOcclusionQueriesNV(GLsizei n, const GLuint* ids);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteProgram gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glDeleteProgram(GLuint program);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteProgramsARB ogladdr</dt>
<dd>glAPI void APIENTRY glDeleteProgramsARB(GLsizei n, const GLuint* programs);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteProgramsNV ogladdr</dt>
<dd>glAPI void APIENTRY glDeleteProgramsNV(GLsizei n, const GLuint* programs);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteQueriesARB ogladdr</dt>
<dd>glAPI void APIENTRY glDeleteQueriesARB(GLsizei n, const GLuint* ids);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteRenderbuffers ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glDeleteRenderbuffers(GLsizei n, const GLuint* renderbuffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteRenderbuffersEXT ogladdr</dt>
<dd>glAPI void APIENTRY glDeleteRenderbuffersEXT(GLsizei n, const GLuint* renderbuffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteShader gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glDeleteShader(GLuint shader);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDeleteTextures gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glDeleteTextures(GLsizei n, const GLuint *textures);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDepthFunc gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glDepthFunc(GLenum efunc);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDepthMask gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glDepthMask(GLboolean flag);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDisable gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glDisable(GLenum cap);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDisableClientState ogl</dt>
<dd>WINzGDIAPI void APIENTRY glDisableClientState(GLenum array);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDisableIndexedEXT ogladdr</dt>
<dd>glAPI void APIENTRY glDisableIndexedEXT(GLenum target, GLuint index);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDisableVertexAttribArray gles</dt>
<dd>glAPICALL void glAPIENTRY glDisableVertexAttribArray(GLuint index);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDrawArrays gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glDrawArrays(GLenum mode, GLint first, GLsizei count);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDrawBuffer ogl</dt>
<dd>WINzGDIAPI void APIENTRY glDrawBuffer(GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDrawBuffersARB ogladdr</dt>
<dd>glAPI void APIENTRY glDrawBuffersARB(GLsizei n, const GLenum* bufs);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDrawBuffersATI ogladdr</dt>
<dd>glAPI void APIENTRY glDrawBuffersATI(GLsizei n, const GLenum* bufs);</dd>
<dd></dd>
</dl>
<dl>
<dt>glDrawElements gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glDrawElements(GLenum mode, GLsizei count, GLenum type, const void *indices);</dd>
<dd></dd>
</dl>
<dl>
<dt>glEnable gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glEnable(GLenum cap);</dd>
<dd></dd>
</dl>
<dl>
<dt>glEnableClientState ogl</dt>
<dd>WINzGDIAPI void APIENTRY glEnableClientState(GLenum array);</dd>
<dd></dd>
</dl>
<dl>
<dt>glEnableIndexedEXT ogladdr</dt>
<dd>glAPI void APIENTRY glEnableIndexedEXT(GLenum target, GLuint index);</dd>
<dd></dd>
</dl>
<dl>
<dt>glEnableVertexAttribArray gles</dt>
<dd>glAPICALL void glAPIENTRY glEnableVertexAttribArray(GLuint index);</dd>
<dd></dd>
</dl>
<dl>
<dt>glEndOcclusionQueryNV ogladdr</dt>
<dd>glAPI void APIENTRY glEndOcclusionQueryNV(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>glEndQueryARB ogladdr</dt>
<dd>glAPI void APIENTRY glEndQueryARB(GLenum target);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFlush gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glFlush(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFogf ogl</dt>
<dd>WINzGDIAPI void APIENTRY glFogf(GLenum pname, GLfloat param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFogfv ogl</dt>
<dd>WINzGDIAPI void APIENTRY glFogfv(GLenum pname, const GLfloat *params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFogi ogl</dt>
<dd>WINzGDIAPI void APIENTRY glFogi(GLenum pname, GLint param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFramebufferRenderbuffer ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glFramebufferRenderbuffer(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFramebufferRenderbufferEXT ogladdr</dt>
<dd>glAPI void APIENTRY glFramebufferRenderbufferEXT(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFramebufferTexture ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glFramebufferTexture(GLenum target, GLenum attachment, GLuint texture, GLint level);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFramebufferTexture2D gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glFramebufferTexture2D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFramebufferTexture2DEXT ogladdr</dt>
<dd>glAPI void APIENTRY glFramebufferTexture2DEXT(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level);</dd>
<dd></dd>
</dl>
<dl>
<dt>glFrontFace gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glFrontFace(GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenBuffers gles</dt>
<dd>glAPICALL void glAPIENTRY glGenBuffers(GLsizei n, GLuint* buffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenBuffersARB ogladdr</dt>
<dd>glAPI void APIENTRY glGenBuffersARB(GLsizei n, GLuint* buffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenFramebuffers gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glGenFramebuffers(GLsizei n, GLuint* framebuffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenFramebuffersEXT ogladdr</dt>
<dd>glAPI void APIENTRY glGenFramebuffersEXT(GLsizei n, GLuint* framebuffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenOcclusionQueriesNV ogladdr</dt>
<dd>glAPI void APIENTRY glGenOcclusionQueriesNV(GLsizei n, GLuint* ids);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenProgramsARB ogladdr</dt>
<dd>glAPI void APIENTRY glGenProgramsARB(GLsizei n, GLuint* programs);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenProgramsNV ogladdr</dt>
<dd>glAPI void APIENTRY glGenProgramsNV(GLsizei n, GLuint* programs);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenQueriesARB ogladdr</dt>
<dd>glAPI void APIENTRY glGenQueriesARB(GLsizei n, GLuint* ids);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenRenderbuffers ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glGenRenderbuffers(GLsizei n, GLuint* renderbuffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenRenderbuffersEXT ogladdr</dt>
<dd>glAPI void APIENTRY glGenRenderbuffersEXT(GLsizei n, GLuint* renderbuffers);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenTextures gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glGenTextures(GLsizei n, GLuint *textures);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenerateMipmap gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glGenerateMipmap(GLenum target);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenerateMipmapEXT ogladdr</dt>
<dd>glAPI void APIENTRY glGenerateMipmapEXT(GLenum target);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenerateTextureMipmap ogladdr</dt>
<dd>glAPI void APIENTRY glGenerateTextureMipmap(GLuint texture);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGenerateTextureMipmapEXT ogladdr</dt>
<dd>glAPI void APIENTRY glGenerateTextureMipmapEXT(GLuint texture, GLenum target);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetActiveUniform gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glGetActiveUniform(GLuint program, GLuint index, GLsizei bufSize, GLsizei* length, GLint* size, GLenum* type, GLchar* name);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetActiveUniformARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetActiveUniformARB(GLhandleARB programObj, GLuint index, GLsizei maxLength, GLsizei* length, GLint* size, GLenum* type, GLcharARB* name);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetAttachedObjectsARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetAttachedObjectsARB(GLhandleARB containerObj, GLsizei maxCount, GLsizei* count, GLhandleARB* obj);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetAttachedShaders gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glGetAttachedShaders(GLuint program, GLsizei maxCount, GLsizei* count, GLuint* shaders);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetBufferParameterivARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetBufferParameterivARB(GLenum target, GLenum pname, GLint* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetBufferPointervARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetBufferPointervARB(GLenum target, GLenum pname, void** params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetBufferSubDataARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetBufferSubDataARB(GLenum target, GLintptrARB offset, GLsizeiptrARB size, void* data);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetError gles&ogl</dt>
<dd>glAPICALL GLenum glAPIENTRY glGetError(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetFloatv gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glGetFloatv(GLenum pname, GLfloat *data);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetInfoLogARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetInfoLogARB(GLhandleARB obj, GLsizei maxLength, GLsizei* length, GLcharARB* infoLog);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetIntegerv gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glGetIntegerv(GLenum pname, GLint *data);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetObjectParameterivARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetObjectParameterivARB(GLhandleARB obj, GLenum pname, GLint* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetOcclusionQueryivNV ogladdr</dt>
<dd>glAPI void APIENTRY glGetOcclusionQueryivNV(GLuint id, GLenum pname, GLint* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetOcclusionQueryuivNV ogladdr</dt>
<dd>glAPI void APIENTRY glGetOcclusionQueryuivNV(GLuint id, GLenum pname, GLuint* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetProgramInfoLog gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glGetProgramInfoLog(GLuint program, GLsizei bufSize, GLsizei* length, GLchar* infoLog);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetProgramiv gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glGetProgramiv(GLuint program, GLenum pname, GLint* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetQueryObjectivARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetQueryObjectivARB(GLuint id, GLenum pname, GLint* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetQueryObjectuivARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetQueryObjectuivARB(GLuint id, GLenum pname, GLuint* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetQueryivARB ogladdr</dt>
<dd>glAPI void APIENTRY glGetQueryivARB(GLenum target, GLenum pname, GLint* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetShaderInfoLog gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glGetShaderInfoLog(GLuint shader, GLsizei bufSize, GLsizei* length, GLchar* infoLog);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetShaderiv gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glGetShaderiv(GLuint shader, GLenum pname, GLint* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetString gles&ogl</dt>
<dd>glAPICALL CPGLubyte glAPIENTRY glGetString(GLenum name);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetTexImage ogl</dt>
<dd>WINzGDIAPI void APIENTRY glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type, GLvoid *pixels);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetTextureImage ogladdr</dt>
<dd>glAPI void APIENTRY glGetTextureImage(GLuint texture, GLint level, GLenum format, GLenum type, GLsizei bufSize, void* pixels);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetTextureImageEXT ogladdr</dt>
<dd>glAPI void APIENTRY glGetTextureImageEXT(GLuint texture, GLenum target, GLint level, GLenum format, GLenum type, void* pixels);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetUniformLocation gles&ogladdr</dt>
<dd>glAPICALL GLint glAPIENTRY glGetUniformLocation(GLuint program, const GLchar* name);</dd>
<dd></dd>
</dl>
<dl>
<dt>glGetUniformLocationARB ogladdr</dt>
<dd>glAPI GLint APIENTRY glGetUniformLocationARB(GLhandleARB programObj, const GLcharARB* name);</dd>
<dd></dd>
</dl>
<dl>
<dt>glHint gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glHint(GLenum target, GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glIsBufferARB ogladdr</dt>
<dd>glAPI GLboolean APIENTRY glIsBufferARB(GLuint buffer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glIsEnabled gles&ogl</dt>
<dd>glAPICALL GLboolean glAPIENTRY glIsEnabled(GLenum cap);</dd>
<dd></dd>
</dl>
<dl>
<dt>glIsOcclusionQueryNV ogladdr</dt>
<dd>glAPI GLboolean APIENTRY glIsOcclusionQueryNV(GLuint id);</dd>
<dd></dd>
</dl>
<dl>
<dt>glIsQueryARB ogladdr</dt>
<dd>glAPI GLboolean APIENTRY glIsQueryARB(GLuint id);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLightModelfv ogl</dt>
<dd>WINzGDIAPI void APIENTRY glLightModelfv(GLenum pname, const GLfloat *params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLightModeli ogl</dt>
<dd>WINzGDIAPI void APIENTRY glLightModeli(GLenum pname, GLint param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLightf ogl</dt>
<dd>WINzGDIAPI void APIENTRY glLightf(GLenum light, GLenum pname, GLfloat param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLightfv ogl</dt>
<dd>WINzGDIAPI void APIENTRY glLightfv(GLenum light, GLenum pname, const GLfloat *params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLineWidth gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glLineWidth(GLfloat width);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLinkProgram gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glLinkProgram(GLuint program);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLinkProgramARB ogladdr</dt>
<dd>glAPI void APIENTRY glLinkProgramARB(GLhandleARB programObj);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLoadIdentity ogl</dt>
<dd>WINzGDIAPI void APIENTRY glLoadIdentity(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLoadMatrixf ogl</dt>
<dd>WINzGDIAPI void APIENTRY glLoadMatrixf(const GLfloat *m);</dd>
<dd></dd>
</dl>
<dl>
<dt>glLoadProgramNV ogladdr</dt>
<dd>glAPI void APIENTRY glLoadProgramNV(GLenum target, GLuint id, GLsizei len, const GLubyte* program);</dd>
<dd></dd>
</dl>
<dl>
<dt>glMapBufferARB ogladdr</dt>
<dd>glAPI PVOID APIENTRY glMapBufferARB(GLenum target, GLenum access);</dd>
<dd></dd>
</dl>
<dl>
<dt>glMaterialf ogl</dt>
<dd>WINzGDIAPI void APIENTRY glMaterialf(GLenum face, GLenum pname, GLfloat param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glMaterialfv ogl</dt>
<dd>WINzGDIAPI void APIENTRY glMaterialfv(GLenum face, GLenum pname, const GLfloat *params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glMatrixMode ogl</dt>
<dd>WINzGDIAPI void APIENTRY glMatrixMode(GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glMultMatrixf ogl</dt>
<dd>WINzGDIAPI void APIENTRY glMultMatrixf(const GLfloat *m);</dd>
<dd></dd>
</dl>
<dl>
<dt>glNamedFramebufferTexture ogladdr</dt>
<dd>glAPI void APIENTRY glNamedFramebufferTexture(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level);</dd>
<dd></dd>
</dl>
<dl>
<dt>glNamedFramebufferTextureEXT ogladdr</dt>
<dd>glAPI void APIENTRY glNamedFramebufferTextureEXT(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level);</dd>
<dd></dd>
</dl>
<dl>
<dt>glNormalPointer ogl</dt>
<dd>WINzGDIAPI void APIENTRY glNormalPointer(GLenum type, GLsizei stride, const GLvoid *pointer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPixelStorei gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glPixelStorei(GLenum pname, GLint param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPointParameterfARB ogladdr</dt>
<dd>glAPI void APIENTRY glPointParameterfARB(GLenum pname, GLfloat param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPointParameterfvARB ogladdr</dt>
<dd>glAPI void APIENTRY glPointParameterfvARB(GLenum pname, const GLfloat* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPointSize ogl</dt>
<dd>WINzGDIAPI void APIENTRY glPointSize(GLfloat size);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPolygonMode ogl</dt>
<dd>WINzGDIAPI void APIENTRY glPolygonMode(GLenum face, GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPolygonOffset gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glPolygonOffset(GLfloat factor, GLfloat units);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPopAttrib ogl</dt>
<dd>WINzGDIAPI void APIENTRY glPopAttrib(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPopMatrix ogl</dt>
<dd>WINzGDIAPI void APIENTRY glPopMatrix(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>glProgramLocalParameter4fvARB ogladdr</dt>
<dd>glAPI void APIENTRY glProgramLocalParameter4fvARB(GLenum target, GLuint index, const GLfloat* params);</dd>
<dd></dd>
</dl>
<dl>
<dt>glProgramParameteriARB ogladdr</dt>
<dd>glAPI void APIENTRY glProgramParameteriARB(GLuint program, GLenum pname, GLint value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glProgramParameteriEXT ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glProgramParameteriEXT(GLuint program, GLenum pname, GLint value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glProgramStringARB ogladdr</dt>
<dd>glAPI void APIENTRY glProgramStringARB(GLenum target, GLenum format, GLsizei len, const void* string);</dd>
<dd></dd>
</dl>
<dl>
<dt>glProvokingVertex ogladdr</dt>
<dd>glAPI void APIENTRY glProvokingVertex(GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glProvokingVertexEXT ogladdr</dt>
<dd>glAPI void APIENTRY glProvokingVertexEXT(GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPushAttrib ogl</dt>
<dd>WINzGDIAPI void APIENTRY glPushAttrib(GLbitfield mask);</dd>
<dd></dd>
</dl>
<dl>
<dt>glPushMatrix ogl</dt>
<dd>WINzGDIAPI void APIENTRY glPushMatrix(void);</dd>
<dd></dd>
</dl>
<dl>
<dt>glReadBuffer gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glReadBuffer(GLenum src);</dd>
<dd></dd>
</dl>
<dl>
<dt>glReadPixels gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels);</dd>
<dd></dd>
</dl>
<dl>
<dt>glRectf ogl</dt>
<dd>WINzGDIAPI void APIENTRY glRectf(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2);</dd>
<dd></dd>
</dl>
<dl>
<dt>glRenderbufferStorage ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glRenderbufferStorage(GLenum target, GLenum internalformat, GLsizei width, GLsizei height);</dd>
<dd></dd>
</dl>
<dl>
<dt>glRenderbufferStorageEXT ogladdr</dt>
<dd>glAPI void APIENTRY glRenderbufferStorageEXT(GLenum target, GLenum internalformat, GLsizei width, GLsizei height);</dd>
<dd></dd>
</dl>
<dl>
<dt>glScissor gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glScissor(GLint x, GLint y, GLsizei width, GLsizei height);</dd>
<dd></dd>
</dl>
<dl>
<dt>glShadeModel ogl</dt>
<dd>WINzGDIAPI void APIENTRY glShadeModel(GLenum mode);</dd>
<dd></dd>
</dl>
<dl>
<dt>glShaderSource gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glShaderSource(GLuint shader, GLsizei count, const GLchar* const* string, const GLint* length);</dd>
<dd></dd>
</dl>
<dl>
<dt>glShaderSourceARB ogladdr</dt>
<dd>glAPI void APIENTRY glShaderSourceARB(GLhandleARB shaderObj, GLsizei count, const GLcharARB** string, const GLint* length);</dd>
<dd></dd>
</dl>
<dl>
<dt>glStencilFunc gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glStencilFunc(GLenum efunc, GLint ref, GLuint mask);</dd>
<dd></dd>
</dl>
<dl>
<dt>glStencilFuncSeparate ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glStencilFuncSeparate(GLenum face, GLenum efunc, GLint ref, GLuint mask);</dd>
<dd></dd>
</dl>
<dl>
<dt>glStencilFuncSeparateATI ogladdr</dt>
<dd>glAPI void APIENTRY glStencilFuncSeparateATI(GLenum frontfunc, GLenum backfunc, GLint ref, GLuint mask);</dd>
<dd></dd>
</dl>
<dl>
<dt>glStencilMask gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glStencilMask(GLuint mask);</dd>
<dd></dd>
</dl>
<dl>
<dt>glStencilOp gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glStencilOp(GLenum fail, GLenum zfail, GLenum zpass);</dd>
<dd></dd>
</dl>
<dl>
<dt>glStencilOpSeparate ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glStencilOpSeparate(GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass);</dd>
<dd></dd>
</dl>
<dl>
<dt>glStencilOpSeparateATI ogladdr</dt>
<dd>glAPI void APIENTRY glStencilOpSeparateATI(GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexCoordPointer ogl</dt>
<dd>WINzGDIAPI void APIENTRY glTexCoordPointer(GLint size, GLenum type, GLsizei stride, const GLvoid *pointer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexEnvf ogl</dt>
<dd>WINzGDIAPI void APIENTRY glTexEnvf(GLenum target, GLenum pname, GLfloat param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexEnvi ogl</dt>
<dd>WINzGDIAPI void APIENTRY glTexEnvi(GLenum target, GLenum pname, GLint param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexGeni ogl</dt>
<dd>WINzGDIAPI void APIENTRY glTexGeni(GLenum coord, GLenum pname, GLint param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexImage2D gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glTexImage2D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexParameterf gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glTexParameterf(GLenum target, GLenum pname, GLfloat param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexParameteri gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glTexParameteri(GLenum target, GLenum pname, GLint param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexStorage2D ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glTexStorage2D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexStorage3D ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glTexStorage3D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTexSubImage2D gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureParameterf ogladdr</dt>
<dd>glAPI void APIENTRY glTextureParameterf(GLuint texture, GLenum pname, GLfloat param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureParameterfv ogladdr</dt>
<dd>glAPI void APIENTRY glTextureParameterfv(GLuint texture, GLenum pname, const GLfloat* param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureParameteri ogladdr</dt>
<dd>glAPI void APIENTRY glTextureParameteri(GLuint texture, GLenum pname, GLint param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureParameteriv ogladdr</dt>
<dd>glAPI void APIENTRY glTextureParameteriv(GLuint texture, GLenum pname, const GLint* param);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureStorage2D ogladdr</dt>
<dd>glAPI void APIENTRY glTextureStorage2D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureStorage2DEXT ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glTextureStorage2DEXT(GLuint texture, GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureStorage3D ogladdr</dt>
<dd>glAPI void APIENTRY glTextureStorage3D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureStorage3DEXT ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glTextureStorage3DEXT(GLuint texture, GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureSubImage2D ogladdr</dt>
<dd>glAPI void APIENTRY glTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void* pixels);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTextureSubImage2DEXT ogladdr</dt>
<dd>glAPI void APIENTRY glTextureSubImage2DEXT(GLuint texture, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void* pixels);</dd>
<dd></dd>
</dl>
<dl>
<dt>glTranslatef ogl</dt>
<dd>WINzGDIAPI void APIENTRY glTranslatef(GLfloat x, GLfloat y, GLfloat z);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform1fv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniform1fv(GLint location, GLsizei count, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform1fvARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniform1fvARB(GLint location, GLsizei count, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform1iv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniform1iv(GLint location, GLsizei count, const GLint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform1ivARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniform1ivARB(GLint location, GLsizei count, const GLint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform1uiv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniform1uiv(GLint location, GLsizei count, const GLuint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform2fv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniform2fv(GLint location, GLsizei count, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform2fvARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniform2fvARB(GLint location, GLsizei count, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform2iv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniform2iv(GLint location, GLsizei count, const GLint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform2ivARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniform2ivARB(GLint location, GLsizei count, const GLint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform2uiv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniform2uiv(GLint location, GLsizei count, const GLuint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform3fv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniform3fv(GLint location, GLsizei count, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform3fvARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniform3fvARB(GLint location, GLsizei count, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform3iv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniform3iv(GLint location, GLsizei count, const GLint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform3ivARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniform3ivARB(GLint location, GLsizei count, const GLint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform3uiv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniform3uiv(GLint location, GLsizei count, const GLuint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform4fv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniform4fv(GLint location, GLsizei count, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform4fvARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniform4fvARB(GLint location, GLsizei count, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform4iv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniform4iv(GLint location, GLsizei count, const GLint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform4ivARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniform4ivARB(GLint location, GLsizei count, const GLint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniform4uiv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniform4uiv(GLint location, GLsizei count, const GLuint* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix2fv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniformMatrix2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix2fvARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniformMatrix2fvARB(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix2x3fv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniformMatrix2x3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix2x4fv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniformMatrix2x4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix3fv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniformMatrix3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix3fvARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniformMatrix3fvARB(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix3x2fv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniformMatrix3x2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix3x4fv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniformMatrix3x4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix4fv gles</dt>
<dd>glAPICALL void glAPIENTRY glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix4fvARB ogladdr</dt>
<dd>glAPI void APIENTRY glUniformMatrix4fvARB(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix4x2fv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniformMatrix4x2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUniformMatrix4x3fv ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUniformMatrix4x3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUnmapBufferARB ogladdr</dt>
<dd>glAPI GLboolean APIENTRY glUnmapBufferARB(GLenum target);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUseProgram gles&ogladdr</dt>
<dd>glAPICALL void glAPIENTRY glUseProgram(GLuint program);</dd>
<dd></dd>
</dl>
<dl>
<dt>glUseProgramObjectARB ogladdr</dt>
<dd>glAPI void APIENTRY glUseProgramObjectARB(GLhandleARB programObj);</dd>
<dd></dd>
</dl>
<dl>
<dt>glVertexAttribPointer gles</dt>
<dd>glAPICALL void glAPIENTRY glVertexAttribPointer(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void* pointer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glVertexPointer ogl</dt>
<dd>WINzGDIAPI void APIENTRY glVertexPointer(GLint size, GLenum type, GLsizei stride, const GLvoid *pointer);</dd>
<dd></dd>
</dl>
<dl>
<dt>glViewport gles&ogl</dt>
<dd>glAPICALL void glAPIENTRY glViewport(GLint x, GLint y, GLsizei width, GLsizei height);</dd>
<dd></dd>
</dl>
<dl>
<dt>wglChoosePixelFormatARB ogladdr</dt>
<dd>MYzABRCALL BOOL WINAPI wglChoosePixelFormatARB(HDC hdc, const int* piAttribIList, const FLOAT* pfAttribFList, UINT nMaxFormats, int* piFormats, UINT* nNumFormats);</dd>
<dd></dd>
</dl>
<dl>
<dt>wglCreateContext ogl</dt>
<dd>WINzGDIAPI HGLRC WINAPI wglCreateContext(HDC);</dd>
<dd></dd>
</dl>
<dl>
<dt>wglCreateContextAttribsARB ogladdr</dt>
<dd>MYzABRCALL HGLRC WINAPI wglCreateContextAttribsARB(HDC hDC, HGLRC hShareContext, const int* attribList);</dd>
<dd></dd>
</dl>
<dl>
<dt>wglDeleteContext ogl</dt>
<dd>WINzGDIAPI BOOL  WINAPI wglDeleteContext(HGLRC);</dd>
<dd></dd>
</dl>
<dl>
<dt>wglGetCurrentDC ogl</dt>
<dd>WINzGDIAPI HDC   WINAPI wglGetCurrentDC(VOID);</dd>
<dd></dd>
</dl>
<dl>
<dt>wglGetExtensionsStringARB ogladdr</dt>
<dd>MYzABRCALL CPCHAR WINAPI wglGetExtensionsStringARB(HDC hdc);</dd>
<dd></dd>
</dl>
<dl>
<dt>wglGetProcAddress ogl</dt>
<dd>WINzGDIAPI PROC  WINAPI wglGetProcAddress(LPCSTR);</dd>
<dd></dd>
</dl>
<dl>
<dt>wglMakeCurrent ogl</dt>
<dd>WINzGDIAPI BOOL  WINAPI wglMakeCurrent(HDC, HGLRC);</dd>
<dd></dd>
</dl>
<dl>
<dt>wglSwapIntervalEXT ogladdr</dt>
<dd>MYzABRCALL BOOL WINAPI wglSwapIntervalEXT(int interval);</dd>
<dd></dd>
</dl>


## Irrlicht API 分组

$$NV/AMD/INTEL/ATI \leadsto EXT \leadsto ARB \leadsto GL$$


### NV - NVIDIA

1. glBeginOcclusionQueryNV ogladdr
2. glBindProgramNV ogladdr
3. glDeleteOcclusionQueriesNV ogladdr
4. glDeleteProgramsNV ogladdr
5. glEndOcclusionQueryNV ogladdr
6. glGenOcclusionQueriesNV ogladdr
7. glGenProgramsNV ogladdr
8. glGetOcclusionQueryivNV ogladdr
9. glGetOcclusionQueryuivNV ogladdr
10. glIsOcclusionQueryNV ogladdr
11. glLoadProgramNV ogladdr


### ATI - ATI Tenchnologies

1. glDrawBuffersATI ogladdr
2. ~~glStencilFuncSeparateATI ogladdr~~
3. ~~glStencilOpSeparateATI ogladdr~~


### AMD - Advanced Micro Devices

1. glBlendEquationIndexedAMD ogladdr
2. glBlendEquationSeparateIndexedAMD ogladdr
3. glBlendFuncIndexedAMD ogladdr
4. glBlendFuncSeparateIndexedAMD ogladdr


### EXT - 通用扩展 Cross-Vendor

1. ~~glBindFramebufferEXT ogladdr~~
2. ~~glBindRenderbufferEXT ogladdr~~
3. ~~glBlendEquationEXT ogladdr~~
4. ~~glBlendEquationSeparateEXT ogladdr~~
5. ~~glBlendFuncSeparateEXT ogladdr~~
6. ~~glCheckFramebufferStatusEXT ogladdr~~
7. glColorMaskIndexedEXT ogladdr
8. ~~glDeleteFramebuffersEXT ogladdr~~
9. ~~glDeleteRenderbuffersEXT ogladdr~~
10. glDisableIndexedEXT ogladdr
11. glEnableIndexedEXT ogladdr
12. ~~glFramebufferRenderbufferEXT ogladdr~~
13. ~~glFramebufferTexture2DEXT ogladdr~~
14. ~~glGenFramebuffersEXT ogladdr~~
15. ~~glGenRenderbuffersEXT ogladdr~~
16. ~~glGenerateMipmapEXT ogladdr~~
17. ~~glGenerateTextureMipmapEXT ogladdr~~
18. ~~glGetTextureImageEXT ogladdr~~
19. ~~glNamedFramebufferTextureEXT ogladdr~~
20. glProgramParameteriEXT ogladdr
21. ~~glProvokingVertexEXT ogladdr~~
22. ~~glRenderbufferStorageEXT ogladdr~~
23. ~~glTextureStorage2DEXT ogladdr~~
24. ~~glTextureStorage3DEXT ogladdr~~
25. ~~glTextureSubImage2DEXT ogladdr~~
26. wglSwapIntervalEXT ogladdr


### ARB - ARB Approved

1. ~~glActiveTextureARB ogladdr~~
2. glAttachObjectARB ogladdr
3. glBeginQueryARB ogladdr
4. ~~glBindBufferARB ogladdr~~
5. glBindProgramARB ogladdr
6. glBlendEquationSeparateiARB ogladdr
7. glBlendEquationiARB ogladdr
8. glBlendFuncSeparateiARB ogladdr
9. glBlendFunciARB ogladdr
10. ~~glBufferDataARB ogladdr~~
11. ~~glBufferSubDataARB ogladdr~~
12. glClientActiveTextureARB ogladdr
13. ~~glCompileShaderARB ogladdr~~
14. glCreateProgramObjectARB ogladdr
15. glCreateShaderObjectARB ogladdr
16. ~~glDeleteBuffersARB ogladdr~~
17. glDeleteObjectARB ogladdr
18. glDeleteProgramsARB ogladdr
19. glDeleteQueriesARB ogladdr
20. glDrawBuffersARB ogladdr
21. glEndQueryARB ogladdr
22. ~~glGenBuffersARB ogladdr~~
23. glGenProgramsARB ogladdr
24. glGenQueriesARB ogladdr
25. ~~glGetActiveUniformARB ogladdr~~
26. glGetAttachedObjectsARB ogladdr
27. glGetBufferParameterivARB ogladdr
28. glGetBufferPointervARB ogladdr
29. glGetBufferSubDataARB ogladdr
30. glGetInfoLogARB ogladdr
31. glGetObjectParameterivARB ogladdr
32. glGetQueryObjectivARB ogladdr
33. glGetQueryObjectuivARB ogladdr
34. glGetQueryivARB ogladdr
35. ~~glGetUniformLocationARB ogladdr~~
36. glIsBufferARB ogladdr
37. glIsQueryARB ogladdr
38. ~~glLinkProgramARB ogladdr~~
39. glMapBufferARB ogladdr
40. glPointParameterfARB ogladdr
41. glPointParameterfvARB ogladdr
42. glProgramLocalParameter4fvARB ogladdr
43. glProgramParameteriARB ogladdr
44. glProgramStringARB ogladdr
45. ~~glShaderSourceARB ogladdr~~
46. ~~glUniform1fvARB ogladdr~~
47. ~~glUniform1ivARB ogladdr~~
48. ~~glUniform2fvARB ogladdr~~
49. ~~glUniform2ivARB ogladdr~~
50. ~~glUniform3fvARB ogladdr~~
51. ~~glUniform3ivARB ogladdr~~
52. ~~glUniform4fvARB ogladdr~~
53. ~~glUniform4ivARB ogladdr~~
54. ~~glUniformMatrix2fvARB ogladdr~~
55. ~~glUniformMatrix3fvARB ogladdr~~
56. ~~glUniformMatrix4fvARB ogladdr~~
57. glUnmapBufferARB ogladdr
58. glUseProgramObjectARB ogladdr
59. wglChoosePixelFormatARB ogladdr
60. wglCreateContextAttribsARB ogladdr
61. wglGetExtensionsStringARB ogladdr


### OpenGL & ES - 所有平台

1. eglBindAPI gles
2. eglChooseConfig gles
3. eglCreateContext gles
4. eglCreateWindowSurface gles
5. eglDestroyContext gles
6. eglDestroySurface gles
7. eglGetConfigAttrib gles
8. eglGetConfigs gles
9. eglGetDisplay gles
10. eglGetError gles
11. eglInitialize gles
12. eglMakeCurrent gles
13. eglSwapBuffers gles
14. eglSwapInterval gles
15. eglTerminate gles
16. glActiveTexture gles&ogladdr
17. glAlphaFunc ogl
18. glAttachShader gles&ogladdr
19. glBindAttribLocation gles
20. glBindBuffer gles
21. glBindFramebuffer gles&ogladdr
22. glBindRenderbuffer ogladdr
23. glBindTexture gles&ogl
24. glBindTextures ogladdr
25. glBlendEquation gles&ogladdr
26. glBlendEquationSeparate ogladdr
27. glBlendFunc gles&ogl
28. glBlendFuncSeparate gles&ogladdr
29. glBufferData gles
30. glBufferSubData gles
31. glCheckFramebufferStatus gles&ogladdr
32. glClear gles&ogl
33. glClearColor gles&ogl
34. glClearDepth ogl
35. glClearDepthf gles
36. glClearStencil gles&ogl
37. glClipPlane ogl
38. glColor4ub ogl
39. glColorMask gles&ogl
40. glColorMaterial ogl
41. glColorPointer ogl
42. glCompileShader gles&ogladdr
43. glCompressedTexImage2D gles&ogladdr
44. glCompressedTexSubImage2D gles&ogladdr
45. glCopyTexSubImage2D gles&ogl
46. glCreateFramebuffers ogladdr
47. glCreateProgram gles&ogladdr
48. glCreateShader gles&ogladdr
49. glCreateTextures ogladdr
50. glCullFace gles&ogl
51. glDeleteBuffers gles
52. glDeleteFramebuffers gles&ogladdr
53. glDeleteProgram gles&ogladdr
54. glDeleteRenderbuffers ogladdr
55. glDeleteShader gles&ogladdr
56. glDeleteTextures gles&ogl
57. glDepthFunc gles&ogl
58. glDepthMask gles&ogl
59. glDisable gles&ogl
60. glDisableClientState ogl
61. glDisableVertexAttribArray gles
62. glDrawArrays gles&ogl
63. glDrawBuffer ogl
64. glDrawElements gles&ogl
65. glEnable gles&ogl
66. glEnableClientState ogl
67. glEnableVertexAttribArray gles
68. glFlush gles&ogl
69. glFogf ogl
70. glFogfv ogl
71. glFogi ogl
72. glFramebufferRenderbuffer ogladdr
73. glFramebufferTexture ogladdr
74. glFramebufferTexture2D gles&ogladdr
75. glFrontFace gles&ogl
76. glGenBuffers gles
77. glGenFramebuffers gles&ogladdr
78. glGenRenderbuffers ogladdr
79. glGenTextures gles&ogl
80. glGenerateMipmap gles&ogladdr
81. glGenerateTextureMipmap ogladdr
82. glGetActiveUniform gles&ogladdr
83. glGetAttachedShaders gles&ogladdr
84. glGetError gles&ogl
85. glGetFloatv gles&ogl
86. glGetIntegerv gles&ogl
87. glGetProgramInfoLog gles&ogladdr
88. glGetProgramiv gles&ogladdr
89. glGetShaderInfoLog gles&ogladdr
90. glGetShaderiv gles&ogladdr
91. glGetString gles&ogl
92. glGetTexImage ogl
93. glGetTextureImage ogladdr
94. glGetUniformLocation gles&ogladdr
95. glHint gles&ogl
96. glIsEnabled gles&ogl
97. glLightModelfv ogl
98. glLightModeli ogl
99. glLightf ogl
100. glLightfv ogl
101. glLineWidth gles&ogl
102. glLinkProgram gles&ogladdr
103. glLoadIdentity ogl
104. glLoadMatrixf ogl
105. glMaterialf ogl
106. glMaterialfv ogl
107. glMatrixMode ogl
108. glMultMatrixf ogl
109. glNamedFramebufferTexture ogladdr
110. glNormalPointer ogl
111. glPixelStorei gles&ogl
112. glPointSize ogl
113. glPolygonMode ogl
114. glPolygonOffset gles&ogl
115. glPopAttrib ogl
116. glPopMatrix ogl
117. glProvokingVertex ogladdr
118. glPushAttrib ogl
119. glPushMatrix ogl
120. glReadBuffer gles&ogl
121. glReadPixels gles&ogl
122. glRectf ogl
123. glRenderbufferStorage ogladdr
124. glScissor gles&ogl
125. glShadeModel ogl
126. glShaderSource gles&ogladdr
127. glStencilFunc gles&ogl
128. glStencilFuncSeparate ogladdr
129. glStencilMask gles&ogl
130. glStencilOp gles&ogl
131. glStencilOpSeparate ogladdr
132. glTexCoordPointer ogl
133. glTexEnvf ogl
134. glTexEnvi ogl
135. glTexGeni ogl
136. glTexImage2D gles&ogl
137. glTexParameterf gles&ogl
138. glTexParameteri gles&ogl
139. glTexStorage2D ogladdr
140. glTexStorage3D ogladdr
141. glTexSubImage2D gles&ogl
142. glTextureParameterf ogladdr
143. glTextureParameterfv ogladdr
144. glTextureParameteri ogladdr
145. glTextureParameteriv ogladdr
146. glTextureStorage2D ogladdr
147. glTextureStorage3D ogladdr
148. glTextureSubImage2D ogladdr
149. glTranslatef ogl
150. glUniform1fv gles
151. glUniform1iv gles
152. glUniform1uiv ogladdr
153. glUniform2fv gles
154. glUniform2iv gles
155. glUniform2uiv ogladdr
156. glUniform3fv gles
157. glUniform3iv gles
158. glUniform3uiv ogladdr
159. glUniform4fv gles
160. glUniform4iv gles
161. glUniform4uiv ogladdr
162. glUniformMatrix2fv gles
163. glUniformMatrix2x3fv ogladdr
164. glUniformMatrix2x4fv ogladdr
165. glUniformMatrix3fv gles
166. glUniformMatrix3x2fv ogladdr
167. glUniformMatrix3x4fv ogladdr
168. glUniformMatrix4fv gles
169. glUniformMatrix4x2fv ogladdr
170. glUniformMatrix4x3fv ogladdr
171. glUseProgram gles&ogladdr
172. glVertexAttribPointer gles
173. glVertexPointer ogl
174. glViewport gles&ogl
175. wglCreateContext ogl
176. wglDeleteContext ogl
177. wglGetCurrentDC ogl
178. wglGetProcAddress ogl
179. wglMakeCurrent ogl

-----
<p class='reviewtip'>2021-01-22: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://riptutorial.com/zh-CN/opengl]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/riptutorial.com/d14cbeb5.html" %})
- [https://docs.microsoft.com/zh-cn/windows/win32/opengl/wgl-functions]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/docs.microsoft.com/2204bf30.html" %})
- [https://www.khronos.org/opengl/wiki/Load_OpenGL_Functions]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/www.khronos.org/108527e1.html" %})
- [https://blog.csdn.net/qq_31243065/article/details/105466436]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/blog.csdn.net/213dac02.html" %})
- [https://blog.csdn.net/qq_22822335/article/details/50682294]({% include relref.html url="/backup/2021-01-21-shader-OpenGL-ex.md/blog.csdn.net/ea7981bb.html" %})
