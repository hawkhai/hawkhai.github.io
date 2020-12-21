---
layout: post
title: "特效编程笔记 -- LearnOpenGL CN 学习笔记（原书复习）"
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

这本书非常好。记录了这本书的学习笔记。[300% 阅读]
[LearnOpenGL CN {% include relref_github.html %}](https://learnopengl-cn.github.io/)

<https://ke.qq.com/course/package/25480?flowToken=1019441>


## 入门 Getting Started

[Polytonic/Glitter {% include relref_github.html %}](https://github.com/Polytonic/Glitter)
一个简单的样板项目，它已经提前配置了所有相关的库。

![alt 属性文本](https://camo.githubusercontent.com/96a40083ee00e5319de5d18a6d262c4f3f2bc3200afe03f06fdf5053b174840c/687474703a2f2f692e696d6775722e636f6d2f4d446f327273792e6a7067 " 可选标题 ")

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


## todo

https://learnopengl-cn.github.io/
02%20Lighting/03%20Materials/

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://learnopengl-cn.github.io/]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/learnopengl-cn.github.io/e0710dd2.html" %})
- [2] [https://ke.qq.com/course/package/25480?flowToken=1019441]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/ke.qq.com/3fd1c97a.html" %})
- [3] [https://github.com/Polytonic/Glitter]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/e303322e.html" %})
- [4] [https://camo.githubusercontent.com/96a40083ee00e5319de5d18a6d262c4f3f2bc3200afe03f06fdf5053b174840c/687474703a2f2f692e696d6775722e636f6d2f4d446f327273792e6a7067]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/camo.githubusercontent.com/b2f16552.html" %})
- [5] [https://github.com/assimp/assimp]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/01f8d32b.html" %})
- [6] [https://github.com/bulletphysics/bullet3]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/863fe200.html" %})
- [7] [https://github.com/Dav1dde/glad]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/18cd3ae8.html" %})
- [8] [https://github.com/glfw/glfw]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/0f399271.html" %})
- [9] [https://github.com/g-truc/glm]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/277752ea.html" %})
- [10] [https://github.com/nothings/stb]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/github.com/6439e35a.html" %})
- [11] [https://v.youku.com/v_show/id_XNzkyOTIyMTI=.html]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/v.youku.com/6f3e2a8f.html" %})
- [12] [https://blog.csdn.net/zsc2014030403015/article/details/51719990]({% include relref.html url="/backup/2020-12-21-shader-learnopengl-cn.github.io.md/blog.csdn.net/cdb6b2c2.html" %})
