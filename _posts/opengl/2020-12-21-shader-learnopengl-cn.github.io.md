---
layout: post
title: "图形学笔记 -- LearnOpenGL CN 学习笔记（原书复习）"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
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

这本书非常好。记录了这本书的学习笔记。[300% 阅读]
[LearnOpenGL CN {% include relref_github.html %}](https://learnopengl-cn.github.io/)

<https://ke.qq.com/course/package/25480?flowToken=1019441>


## 入门 Getting Started

[Polytonic/Glitter {% include relref_github.html %}](https://github.com/Polytonic/Glitter)
一个简单的样板项目，它已经提前配置了所有相关的库。

Functionality           | Library
----------------------- | ------------------------------------------
Mesh Loading            | [assimp {% include relref_github.html %}](https://github.com/assimp/assimp)
Physics                 | [bullet {% include relref_github.html %}](https://github.com/bulletphysics/bullet3)
OpenGL Function Loader  | [glad {% include relref_github.html %}](https://github.com/Dav1dde/glad)
Windowing and Input     | [glfw {% include relref_github.html %}](https://github.com/glfw/glfw)
OpenGL Mathematics      | [glm {% include relref_github.html %}](https://github.com/g-truc/glm)
Texture Loading         | [stb {% include relref_github.html %}](https://github.com/nothings/stb)

```glsl
while(!glfwWindowShouldClose(window))
{
    // 输入
    processInput(window);

    // 渲染
    // 清除颜色缓冲
    glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    // 记得激活着色器
    glUseProgram(shaderProgram);

    // 更新 uniform 颜色
    float timeValue = glfwGetTime();
    float greenValue = sin(timeValue) / 2.0f + 0.5f;
    int vertexColorLocation = glGetUniformLocation(shaderProgram, "ourColor");
    glUniform4f(vertexColorLocation, 0.0f, greenValue, 0.0f, 1.0f);

    // 绘制三角形
    glBindVertexArray(VAO);
    glDrawArrays(GL_TRIANGLES, 0, 3);

    // 交换缓冲并查询 IO 事件
    glfwSwapBuffers(window);
    glfwPollEvents();
}
```


### 重组 (Swizzling)

```glsl
vec2 someVec;
vec4 differentVec = someVec.xyxx;
vec3 anotherVec = differentVec.zyw;
vec4 otherVec = someVec.xxxx + anotherVec.yxzy;

vec2 vect = vec2(0.5, 0.7);
vec4 result = vec4(vect, 0.0, 0.0);
vec4 otherResult = vec4(result.xyz, 1.0);
```


### stb_image 编译

创建一个新的 C++ 文件，输入以下代码：

```cpp
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
```


### 生成一个纹理

```cpp
unsigned int texture;
glGenTextures(1, &texture);
glBindTexture(GL_TEXTURE_2D, texture);
// 为当前绑定的纹理对象设置环绕、过滤方式
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
// 加载并生成纹理
int width, height, nrChannels;
unsigned char *data = stbi_load("container.jpg", &width, &height, &nrChannels, 0);
if (data)
{
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
    glGenerateMipmap(GL_TEXTURE_2D); // 多级渐远纹理 (Mipmap)
}
else
{
    std::cout << "Failed to load texture" << std::endl;
}
stbi_image_free(data);
```

```glsl
glActiveTexture(GL_TEXTURE0);
glBindTexture(GL_TEXTURE_2D, texture1);
glActiveTexture(GL_TEXTURE1);
glBindTexture(GL_TEXTURE_2D, texture2);
glBindVertexArray(VAO);

glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
```


### 向量 & 矩阵

计算长度 (Length)：
$$
||\color{red}{\bar{v}}|| = \sqrt{\color{green}x^2 + \color{blue}y^2}
$$

标准化 (Normalizing)：
$$
\hat{n} = \frac{\bar{v}}{||\bar{v}||}
$$

位移矩阵：

$$
\begin{bmatrix}  \color{red}1 & \color{red}0 & \color{red}0 & \color{red}{T_x} \\ \color{green}0 & \color{green}1 & \color{green}0 & \color{green}{T_y} \\ \color{blue}0 & \color{blue}0 & \color{blue}1 & \color{blue}{T_z} \\ \color{purple}0 & \color{purple}0 & \color{purple}0 & \color{purple}1 \end{bmatrix} \cdot \begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix} = \begin{pmatrix} x + \color{red}{T_x} \\ y + \color{green}{T_y} \\ z + \color{blue}{T_z} \\ 1 \end{pmatrix}
$$

万向节死锁（Gimbal Lock）：<https://v.youku.com/v_show/id_XNzkyOTIyMTI=.html>

任意旋转轴：

$$
\begin{bmatrix} \cos \theta + \color{red}{R_x}^2(1 - \cos \theta) & \color{red}{R_x}\color{green}{R_y}(1 - \cos \theta) - \color{blue}{R_z} \sin \theta & \color{red}{R_x}\color{blue}{R_z}(1 - \cos \theta) + \color{green}{R_y} \sin \theta & 0 \\ \color{green}{R_y}\color{red}{R_x} (1 - \cos \theta) + \color{blue}{R_z} \sin \theta & \cos \theta + \color{green}{R_y}^2(1 - \cos \theta) & \color{green}{R_y}\color{blue}{R_z}(1 - \cos \theta) - \color{red}{R_x} \sin \theta & 0 \\ \color{blue}{R_z}\color{red}{R_x}(1 - \cos \theta) - \color{green}{R_y} \sin \theta & \color{blue}{R_z}\color{green}{R_y}(1 - \cos \theta) + \color{red}{R_x} \sin \theta & \cos \theta + \color{blue}{R_z}^2(1 - \cos \theta) & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$


### 坐标系统

一旦所有顶点被变换到裁剪空间，最终的操作 —— 透视除法 (Perspective Division) 将会执行，在这个过程中我们将位置向量的 x，y，z 分量分别除以向量的齐次 w 分量；透视除法是将 4D 裁剪空间坐标变换为 3D 标准化设备坐标的过程。这一步会在每一个顶点着色器运行的最后被自动执行。


### Z 缓冲

OpenGL 存储它的所有深度信息于一个 Z 缓冲 (Z-buffer) 中，也被称为深度缓冲 (Depth Buffer)。GLFW 会自动为你生成这样一个缓冲（就像它也有一个颜色缓冲来存储输出图像的颜色）。深度值存储在每个片段里面（作为片段的 z 值），当片段想要输出它的颜色时，OpenGL 会将它的深度值和 z 缓冲进行比较，如果当前的片段在其它片段之后，它将会被丢弃，否则将会覆盖。这个过程称为深度测试 (Depth Testing)，它是由 OpenGL 自动完成的。

* [OpenGL 深度缓冲区 Z 缓冲区 介绍 {% include relref_csdn.html %}](https://blog.csdn.net/zsc2014030403015/article/details/51719990)
* 深度其实就是该象素点在 3d 世界中距离摄象机的距离（绘制坐标），深度缓存中存储着每个象素点（绘制在屏幕上的）的深度值！
* 绘制半透明物体时，需注意：在绘制半透明物体时前，还需要利用 glDepthMask(GL_FALSE) 将深度缓冲区设置为只读形式，否则可能出现画面错误。


### FPS 风格的摄像机

$$
LookAt = \begin{bmatrix} \color{red}{R_x} & \color{red}{R_y} & \color{red}{R_z} & 0 \\ \color{green}{U_x} & \color{green}{U_y} & \color{green}{U_z} & 0 \\ \color{blue}{D_x} & \color{blue}{D_y} & \color{blue}{D_z} & 0 \\ 0 & 0 & 0  & 1 \end{bmatrix} * \begin{bmatrix} 1 & 0 & 0 & -\color{purple}{P_x} \\ 0 & 1 & 0 & -\color{purple}{P_y} \\ 0 & 0 & 1 & -\color{purple}{P_z} \\ 0 & 0 & 0  & 1 \end{bmatrix}
$$


## 光照 Lighting


### 法线矩阵 (Normal Matrix)

不等比缩放的模型矩阵对法向量的影响。每当我们应用一个不等比缩放时（注意：等比缩放不会破坏法线，因为法线的方向没被改变，仅仅改变了法线的长度，而这很容易通过标准化来修复），法向量就不会再垂直于对应的表面了，这样光照就会被破坏。

```glsl
Normal = mat3(transpose(inverse(model))) * aNormal;
```

> 即使是对于着色器来说，逆矩阵也是一个开销比较大的运算，因此，只要可能就应该避免在着色器中进行逆矩阵运算，它们必须为你场景中的每个顶点都进行这样的处理。用作学习目这样做是可以的，但是对于一个对效率有要求的应用来说，在绘制之前你最好用 CPU 计算出法线矩阵，然后通过 uniform 把值传递给着色器（像模型矩阵一样）。


### 材质

```glsl
#version 330 core
struct Material {
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float shininess;
};

uniform Material material;

// c++ 部分
lightingShader.setVec3("material.ambient",  1.0f, 0.5f, 0.31f);
lightingShader.setVec3("material.diffuse",  1.0f, 0.5f, 0.31f);
lightingShader.setVec3("material.specular", 0.5f, 0.5f, 0.5f);
lightingShader.setFloat("material.shininess", 32.0f);
```


### 平行光

```glsl
struct Light {
    // vec3 position; // 使用定向光就不再需要了
    vec3 direction;

    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};
...
void main()
{
    vec3 lightDir = normalize(-light.direction);
    ...
}

// c++ 部分
lightingShader.setVec3("light.direction", -0.2f, -1.0f, -0.3f);

if(lightVector.w == 0.0) // 注意浮点数据类型的误差
  // 执行定向光照计算
else if(lightVector.w == 1.0)
  // 根据光源的位置做光照计算（与上一节一样）
```


## 模型加载 Model Loading


## 高级 Advanced OpenGL


### 深度冲突 (Z-fighting)

* 永远不要把多个物体摆得太靠近，以至于它们的一些三角形会重叠。never place objects too close to each other in a way that some of their triangles closely overlap.
* 尽可能将近平面设置远一些。set the near plane as far as possible.
* 使用更高精度的深度缓冲。use a higher precision depth buffer.


### 物体轮廓

```cpp
glEnable(GL_DEPTH_TEST);
glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE); // 模板测试和深度测试都通过时 REPLACE

glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT);

glStencilMask(0x00); // 记得保证我们在绘制地板的时候不会更新模板缓冲
normalShader.use();
DrawFloor()

glStencilFunc(GL_ALWAYS, 1, 0xFF);
glStencilMask(0xFF); // 开启模板测试，把两个箱子写入 Stencil
DrawTwoContainers();

glStencilFunc(GL_NOTEQUAL, 1, 0xFF);
glStencilMask(0x00); // 关闭模板测试
glDisable(GL_DEPTH_TEST);
shaderSingleColor.use();
DrawTwoScaledUpContainers(); // 再次根据 Stencil 绘制箱子，GL_NOTEQUAL 1
glStencilMask(0xFF);
glEnable(GL_DEPTH_TEST);
```

当绘制一个有不透明和透明物体的场景的时候，大体的原则如下：

* 先绘制所有不透明的物体。
* 对所有透明的物体排序。
* 按顺序绘制所有透明的物体。


### 帧缓冲 framebuffers

核处理：你在网上找到的大部分核将所有的权重加起来之后都应该会等于 1，如果它们加起来不等于 1，这就意味着最终的纹理颜色将会比原纹理值更亮或者更暗了。

```cpp
// framebuffer configuration
// -------------------------
unsigned int framebuffer;
glGenFramebuffers(1, &framebuffer);
glBindFramebuffer(GL_FRAMEBUFFER, framebuffer);

// create a color attachment texture
unsigned int textureColorbuffer;
glGenTextures(1, &textureColorbuffer);
glBindTexture(GL_TEXTURE_2D, textureColorbuffer);
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, SCR_WIDTH, SCR_HEIGHT, 0, GL_RGB, GL_UNSIGNED_BYTE, NULL);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, textureColorbuffer, 0);

// create a renderbuffer object for depth and stencil attachment (we won't be sampling these)
unsigned int rbo;
glGenRenderbuffers(1, &rbo);
glBindRenderbuffer(GL_RENDERBUFFER, rbo);
glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH24_STENCIL8, SCR_WIDTH, SCR_HEIGHT); // use a single renderbuffer object for both a depth AND stencil buffer.
glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_STENCIL_ATTACHMENT, GL_RENDERBUFFER, rbo); // now actually attach it

// now that we actually created the framebuffer and added all attachments we want to check if it is actually complete now
if (glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE)
    cout << "ERROR::FRAMEBUFFER:: Framebuffer is not complete!" << endl;
glBindFramebuffer(GL_FRAMEBUFFER, 0);

// render loop
// -----------
while (!glfwWindowShouldClose(window))
{
    // render
    // ------
    // bind to framebuffer and draw scene as we normally would to color texture
    glBindFramebuffer(GL_FRAMEBUFFER, framebuffer);
    glEnable(GL_DEPTH_TEST); // enable depth testing (is disabled for rendering screen-space quad)

    // make sure we clear the framebuffer's content
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    shader.use();
    glm::mat4 model = glm::mat4(1.0f);
    glm::mat4 view = camera.GetViewMatrix();
    glm::mat4 projection = glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f);
    shader.setMat4("view", view);
    shader.setMat4("projection", projection);

    // cubes
    glBindVertexArray(cubeVAO);
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, cubeTexture);
    model = glm::translate(model, glm::vec3(-1.0f, 0.0f, -1.0f));
    shader.setMat4("model", model);
    glDrawArrays(GL_TRIANGLES, 0, 36);
    model = glm::mat4(1.0f);
    model = glm::translate(model, glm::vec3(2.0f, 0.0f, 0.0f));
    shader.setMat4("model", model);
    glDrawArrays(GL_TRIANGLES, 0, 36);

    // floor
    glBindVertexArray(planeVAO);
    glBindTexture(GL_TEXTURE_2D, floorTexture);
    shader.setMat4("model", glm::mat4(1.0f));
    glDrawArrays(GL_TRIANGLES, 0, 6);
    glBindVertexArray(0);

    // now bind back to default framebuffer and draw a quad plane with the attached framebuffer color texture
    glBindFramebuffer(GL_FRAMEBUFFER, 0);
    glDisable(GL_DEPTH_TEST); // disable depth test so screen-space quad isn't discarded due to depth test.
    // clear all relevant buffers
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f); // set clear color to white (not really necessary actually, since we won't be able to see behind the quad anyways)
    glClear(GL_COLOR_BUFFER_BIT);

    screenShader.use();
    glBindVertexArray(quadVAO);
    glBindTexture(GL_TEXTURE_2D, textureColorbuffer); // use the color attachment texture as the texture of the quad plane
    glDrawArrays(GL_TRIANGLES, 0, 6);

    // glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
    // -------------------------------------------------------------------------------
    glfwSwapBuffers(window);
    glfwPollEvents();
}
```


## 屏幕空间环境光遮蔽 SSAO

在 2007 年，Crytek 公司发布了一款叫做屏幕空间环境光遮蔽 (Screen-Space Ambient Occlusion, SSAO) 的技术，并用在了他们的看家作孤岛危机上。这一技术使用了屏幕空间场景的深度而不是真实的几何体数据来确定遮蔽量。这一做法相对于真正的环境光遮蔽不但速度快，而且还能获得很好的效果，使得它成为近似实时环境光遮蔽的标准。


## PBR 基于物理的渲染 (Physically Based Rendering)

高等数学真的是无处不在，一些聪明绝顶的人构想出来的方程，我们这种不那么聪明的人一看就脑壳痛。大概讲的是，基于物理的渲染，会更逼真：基于微平面的表面模型，能量守恒，应用基于物理的双向反射分布函数。没时间学了，先就这样了。


## todo

Advanced Lighting
PBR
In Practice
Guest Articles
Code repository
Translations
About

看到这里，就基本上没看了：
https://learnopengl-cn.github.io/
05%20Advanced%20Lighting/03%20Shadows/02%20Point%20Shadows/


## Refs

- [1] [Welcome to songho.ca](http://www.songho.ca/index.html)
- [2] [songho.ca OpenGL](http://www.songho.ca/opengl/index.html)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relrefx.html url="/assets/reviewjs/blogs/2020-12-21-shader-learnopengl-cn.github.io.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://learnopengl-cn.github.io/]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/learnopengl-cn.github.io/e0710dd2.html" %})
- [https://ke.qq.com/course/package/25480?flowToken=1019441]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/ke.qq.com/3fd1c97a.html" %})
- [https://github.com/Polytonic/Glitter]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/e303322e.html" %})
- [https://github.com/assimp/assimp]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/01f8d32b.html" %})
- [https://github.com/bulletphysics/bullet3]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/863fe200.html" %})
- [https://github.com/Dav1dde/glad]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/18cd3ae8.html" %})
- [https://github.com/glfw/glfw]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/0f399271.html" %})
- [https://github.com/g-truc/glm]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/277752ea.html" %})
- [https://github.com/nothings/stb]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/6439e35a.html" %})
- [https://v.youku.com/v_show/id_XNzkyOTIyMTI=.html]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/v.youku.com/6f3e2a8f.html" %})
- [https://blog.csdn.net/zsc2014030403015/article/details/51719990]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/blog.csdn.net/cdb6b2c2.html" %})
- [http://www.songho.ca/index.html]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/www.songho.ca/564bb2d2.html" %})
- [http://www.songho.ca/opengl/index.html]({% include relrefx.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/www.songho.ca/d4f46261.html" %})
