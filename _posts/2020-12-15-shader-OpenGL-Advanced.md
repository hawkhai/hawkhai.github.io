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
codeprint:
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
glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE);

while (True):
    // 每次绘制。
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT);

    if selected: // 如果选中了。
        glStencilMask(0xFF); // 设置模板缓冲为可写状态

        glStencilFunc(GL_ALWAYS,1,0xFF); // 所有片段都要写入模板缓冲
        model.Draw(modelShader); // 绘制模型

        glStencilMask(0x00); // 禁止修改模板缓冲

        glStencilFunc(GL_NOTEQUAL,1,0xFF); // 不等于 1 才写入。
        float scale=1.02; // 模型放大一点
        model.Draw(stencilShader); // 绘制边界，就把模型边框绘制出来的

        glStencilMask(0xFF); // 设置模板缓冲为可写状态

    else: // 如果没选中。
        glStencilFunc(GL_ALWAYS,1,0xFF);
        _modelsIter->second.second.Draw(modelShader); // 绘制模型
```

{% include image.html url="/assets/images/201215-shader-opengl-advanced/grabmodelselect.gif" %}

* [Android OpenGL ES 系列连载：模板测试 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/115230970)
* [模板缓存 {% include relref_csdn.html %}](https://blog.csdn.net/korekara88730/article/details/42213217)

伪代码：

```cpp
// stencil test 比较的时候需要 mask
status = glStencilFunc.func((stencilbuf[x,y] & glStencilFunc.mask), (glStencilFunc.ref & glStencilFunc.mask));
status |= depth_test_result;
if (status == stencil_test_fail) stencilop = glStencilOp.sfailop;
else if (status == stencil_test_pass & depth_test_fail) stencilop = glStencilOp.dpfailop;
else if (status == stencil_test_pass & depth_test_pass) stencilop = glStencilOp.dppassop;
// stencil test 结束后的操作不需要 mask
stencil_new_value = stencilop(stencilbuf[x,y]);
// 写入 stencil buffer 的时候需要另一个 mask
stencilbuf[x,y] = (stencil_new_value & glStencilMask.mask) | (stencilbuf[x,y] & (~glStencilMask.mask));
```


## 混合

$$
\begin{equation}\bar{C}_{result} = \bar{\color{green}C}_{source} * \color{green}F_{source} + \bar{\color{red}C}_{destination} * \color{red}F_{destination}\end{equation}
$$

* $$\bar{\color{green}C}_{source}$$：源颜色向量。这是源自纹理的颜色向量。
* $$\bar{\color{red}C}_{destination}$$：目标颜色向量。这是当前储存在颜色缓冲中的颜色向量。
* $$\color{green}F_{source}$$：源因子值。指定了 alpha 值对源颜色的影响。
* $$\color{red}F_{destination}$$：目标因子值。指定了 alpha 值对目标颜色的影响。

```cpp
glEnable(GL_BLEND);
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
```

* 关闭深度测试，新的颜色会直接替换掉颜色缓冲区存在的老的颜色。
* 开启深度测试，用深度值来判断，离近裁剪面越近的颜色会替换原有的颜色。
* 开启混合：glEnable(GL_BLEND)，会将目标颜色和源颜色按照混合方程式来计算最终的颜色。


## 面剔除

```cpp
glEnable (GL_CULL_FACE); // 开启正背面剔除，默认剔除背面
glDisable(GL_CULL_FACE); // 关闭正背面剔除
// 选择剔除正面还是背面，mode：GL_FRONT（正面）GL_BACK（背面）GL_FRONT_AND_BACK（正背面）
void glCullFace(GLenum mode);
// 设置正面，mode：GL_CW（顺时针）GL_CCW（逆时针）
void glFrontFace(GLenum mode);
```


## 帧缓冲 Framebuffers

当创建一个附件的时候，我们有两个选项：
1. 纹理
2. 渲染缓冲对象（Renderbuffer Object）

* [OpenGL 之 帧缓冲 使用实践 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/l5eYzkYAzR-m21-iYBoyCw)
* [帧缓冲的基础知识](https://riptutorial.com/zh-CN/opengl/example/23675/%E5%B8%A7%E7%BC%93%E5%86%B2%E7%9A%84%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86)

前面的简单，后面的慢慢有难度了，基本原理简单，代码是怎么做到的，就是一大坨代码。

```cpp
unsigned int FBO; // 创建一个帧缓冲对象
glGenFramebuffers(1, &FBO);
glBindFramebuffer(GL_FRAMEBUFFER, FBO); // 开启 glBindFramebuffer

unsigned int texColorBuffer = 0;
glGenTextures(1, &texColorBuffer); // 纹理附件
glBindTexture(GL_TEXTURE_2D, texColorBuffer);
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 600, 450, 0, GL_RGB, GL_UNSIGNED_BYTE, NULL);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

// 它附加到帧缓冲上
glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, texColorBuffer, 0);

unsigned int RBO; // 缓冲对象附件
glGenRenderbuffers(1, &RBO);
glBindRenderbuffer(GL_RENDERBUFFER, RBO);
glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH24_STENCIL8, 600, 450);

// 把帧缓冲对象附加上
glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_STENCIL_ATTACHMENT, GL_RENDERBUFFER, RBO);

if (glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE)
    std::cout << "ERROR::FRAMEBUFFER:: Framebuffer is not complete!" << std::endl;

glBindFramebuffer(GL_FRAMEBUFFER, 0); // 关闭 glBindFramebuffer

// 用这个帧缓纹理创建一个网格 texColorBuffer
Mesh mesh = getMesh(texColorBuffer);

while (!glfwWindowShouldClose(window))
{
    glBindFramebuffer(GL_FRAMEBUFFER, FBO); // 开启 glBindFramebuffer

    // 将内容绘制到自定义帧缓冲的纹理附件
    ... // 一大坨代码

    // 使用纹理绘制窗户
    glBindFramebuffer(GL_FRAMEBUFFER, 0); // 关闭 glBindFramebuffer

    mesh.Draw(caoShader); // mesh 用到的就是上面绘制的帧缓冲
}

glDeleteFramebuffers(1, &FBO);
```

{% include image.html url="/assets/images/201215-shader-opengl-advanced/grabframebuffer-256.gif" %}


## 参考资料

- [1] [Mouse Picking with Ray Casting](https://antongerdelan.net/opengl/raycasting.html)
- [2] [OpenGL Projection Matrix](http://www.songho.ca/opengl/gl_projectionmatrix.html)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://antongerdelan.net/opengl/raycasting.html]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/antongerdelan.net/fdb6a2ef.html" %})
- [2] [https://zhuanlan.zhihu.com/p/115230970]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/zhuanlan.zhihu.com/45793866.html" %})
- [3] [https://blog.csdn.net/korekara88730/article/details/42213217]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/blog.csdn.net/e53c4341.html" %})
- [4] [https://mp.weixin.qq.com/s/l5eYzkYAzR-m21-iYBoyCw]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/mp.weixin.qq.com/6c5f2acd.html" %})
- [5] [https://riptutorial.com/zh-CN/opengl/example/23675/%E5%B8%A7%E7%BC%93%E5%86%B2%E7%9A%84%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/riptutorial.com/404c0ecf.html" %})
- [6] [http://www.songho.ca/opengl/gl_projectionmatrix.html]({% include relref.html url="/backup/2020-12-15-shader-OpenGL-Advanced.md/www.songho.ca/7c7467ff.html" %})
