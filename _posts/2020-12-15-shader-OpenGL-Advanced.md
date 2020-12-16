---
layout: post
title: "特效编程笔记 -- OpenGL 图形学 / 高级 OpenGL：深度测试、面剔除、帧缓冲 等"
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
cluster: "LearnOpenGL"
---

深度测试、鼠标点击选取模型、模板测试、混合、剔除面、帧缓冲、高级数据，高级 GLSL、集合说色器、实例化、抗锯齿等。

前面的简单，看到后面，慢慢的有难度了，stencil 模板測試，要看好久才能理解。


## 深度测试

$$
\begin{equation} F_{depth} = \frac{z - near}{far - near} \end{equation}
$$

$$
\begin{equation} F_{depth} = \frac{1/z - 1/near}{1/far - 1/near} \end{equation}
$$


## 鼠标点击选取模型

就要把屏幕坐标一步一步还原成世界坐标。

```cpp
Model ourModel("E:/kSource/LearnOpenGLz/LearnOpenGL-og/resources/objects/nanosuit/nanosuit.obj");
glfwGetCursorPos(window, &winX, &winY);
glReadPixels((int)winX, 600 - (int)winY, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT, &winZ);
float x = (2.0f*winX) / 800.0f - 1.0f;
float y = 1.0f - (2.0f*winY) / 600.0f;
float z = winZ * 2.0 - 1.0f;
float w = near * far / (near*winZ - far * winZ + far);
glm::vec4 wolrdPostion = glm::inverse(view)*glm::inverse(projection)*w*glm::vec4(x, y, z, 1);

// 遍历模型，根据距离判断哪个被选中了。
float _distance=glm::distance(_modelsIter->second.first+glm::vec3(0,7.5,0),glm::vec3(wolrdPostion));
```


### [Mouse Picking with Ray Casting](https://antongerdelan.net/opengl/raycasting.html)

Instead of starting with a mesh in local space, we are starting with a 2d mouse cursor position in viewport space. We work backwards through the transformation by using inverse matrices, and arrive with a ray in world space.

It can be useful to click on, or "pick" a 3d object in our scene using the mouse cursor. One way of doing this is to project a 3d ray from the mouse, through the camera, into the scene, and then check if that ray intersects with any objects. This is usually called ray casting. This is an entirely mathematical exercise - we don't use any OpenGL code or draw any graphics - this means that it will apply to any 3d application the same way. The mathematical subject is usually called geometric intersection testing.

{% include image.html url="/assets/images/201215-shader-opengl-advanced/newtranspipe.png" %}


## stencil 模板測試

1. 启用模板缓冲的写入。
2. 渲染物体，更新模板缓冲的内容。
3. 禁用模板缓冲的写入。
4. 渲染（其它）物体，这次根据模板缓冲的内容丢弃特定的片段。

```cpp
// 开启
glEnable(GL_DEPTH_TEST);
glEnable(GL_STENCIL_TEST); // 启用蒙板测试
glStencilOp(GL_KEEP,GL_KEEP,GL_REPLACE);

while (True):
    // 每次绘制。
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT);

    if selected: // 如果选中了。
        glStencilFunc(GL_ALWAYS,1,0xFF); // 所有片段都要写入模板缓冲
        glStencilMask(0xFF); // 设置模板缓冲为可写状态
        _modelsIter->second.second.Draw(modelShader); // 绘制模型

        glStencilFunc(GL_NOTEQUAL,1,0xFF);
        glStencilMask(0x00); // 禁止修改模板缓冲
        ...; // 模型放大一点
        _modelsIter->second.second.Draw(stencilShader); // 绘制边界
        glStencilMask(0xFF); // 设置模板缓冲为可写状态

    else: // 如果没选中。
        glStencilFunc(GL_ALWAYS,1,0xFF);
        _modelsIter->second.second.Draw(modelShader); // 绘制模型
```

{% include video.html url="/assets/images/201215-shader-opengl-advanced/grabmodelselect.mp4" %}

* [Android OpenGL ES 系列连载：（11）模板测试 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/115230970)

glStencilFunc 是用来规定是否通过了 stencil test 的规则。
向 stencil buffer 中写内容的规则，是 glStencilOp 规定的。


### glStencilFunc(GLenum func,GLint ref, GLuint mask)

* [模板缓存 {% include relref_csdn.html %}](https://blog.csdn.net/korekara88730/article/details/42213217)
* 第一个参数可以选择 GL_NEVER，GL_LESS，GL_LEQUAL，GL_GREATER，GL_GEQUAL，GL_EQUAL，GL_NOTEQUAL 和 GL_ALWAYS。初始化的值是 GL_ALWAYS。
    模板缓存中的值得 与 mask 参数作与， 然后再与 ref 参数作比较，得出的比较结果，和第一个 enum 参数比较，如何符合 enum 的规则，则认为是通过了模板缓存，反之不通过。


### glStencilOp(GLenum fail, GLenum zfail, GLenum zpass )

在开启模板缓存后， 绘制内容时，会做两件事：

1. 检测当前像素是否通过了 stencil test。测试规则是 glStencilFunc 规定的。
2. 当前像素如何修改 stencil buffer 的值。规则是 glStencilFunc 和 glStencilOp 共同规定的。


## 混合

$$
\begin{equation}\bar{C}_{result} = \bar{\color{green}C}_{source} * \color{green}F_{source} + \bar{\color{red}C}_{destination} * \color{red}F_{destination}\end{equation}
$$

* $$\bar{\color{green}C}_{source}$$：源颜色向量。这是源自纹理的颜色向量。
* $$\bar{\color{red}C}_{destination}$$：目标颜色向量。这是当前储存在颜色缓冲中的颜色向量。
* $$\color{green}F_{source}$$：源因子值。指定了 alpha 值对源颜色的影响。
* $$\color{red}F_{destination}$$：目标因子值。指定了 alpha 值对目标颜色的影响。


## 面剔除

```cpp
glEnable(GL_CULL_FACE);
glCullFace(GL_BACK);
glFrontFace(GL_CW);
```


## 帧缓冲 Framebuffers

当创建一个附件的时候，我们有两个选项：
1. 纹理
2. 渲染缓冲对象（Renderbuffer Object）


## 参考资料

- [1] [Mouse Picking with Ray Casting](https://antongerdelan.net/opengl/raycasting.html)
- [2] [OpenGL Projection Matrix](http://www.songho.ca/opengl/gl_projectionmatrix.html)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://antongerdelan.net/opengl/raycasting.html]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/antongerdelan.net/fdb6a2ef.html" %})
- [2] [https://zhuanlan.zhihu.com/p/115230970]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/zhuanlan.zhihu.com/45793866.html" %})
- [3] [https://blog.csdn.net/korekara88730/article/details/42213217]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/blog.csdn.net/e53c4341.html" %})
- [4] [http://www.songho.ca/opengl/gl_projectionmatrix.html]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/www.songho.ca/7c7467ff.html" %})
