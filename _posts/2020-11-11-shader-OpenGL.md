---
layout: post
title: "“特效编程”笔记 -- 计算机图形学 OPENGL 入门"
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
---

以前随便找点代码，改吧改吧就能跑，今天算是入门学习了一下。
顶点着色器、几何着色器、片段着色器。又酷又通透，身心愉悦——

本文源码 <a href="{% include relref.html url="/source/shader/shaderdemo.cpp" %}" target="_blank">shaderdemo.cpp</a>


## 历史

1988 年 5 月，Pixar 公布了第三版 RenderMan 规范，将「着色器」的使用推广到了我们目前所知的各大应用领域。

随着图形处理器的进步，OpenGL 和 Direct3D 等主要的图形软件库都开始支持着色器。
第一批支持着色器的 GPU 仅支持像素着色器，但随着开发者逐渐认识到着色器的强大，很快便出现了顶点着色器。
2000 年，第一款支持可编程像素着色器的显卡 Nvidia GeForce 3（NV20）问世。Direct3D 10 和 OpenGL 3.2 则引入了几何着色器。

{% include image.html url="/images/OpenGL-GLSL/faa27c0e4a3a4b7eb3436c016ce606f1.jpeg"
caption= "利用 gpu 渲染一个巨人的图像" %}

[计算机图形学 OPENGL 入门 {% include relref_svgbili.html %}](https://www.bilibili.com/video/BV1px41197A5)

<https://ke.qq.com/course/package/25480?flowToken=1019441>

<https://learnopengl-cn.github.io/>


## P1 状态机上下文 & 软件环境

状态机：当前绘制状态、光照设置、纹理设置、材质设置。

```cpp
void setVertexEnv() {
    float vertices[] = {
        -0.5f, -0.5f, 0.0f, // left, down
        0.5f, -0.5f, 0.0f, // right, down
        -0.5f, 0.5f, 0.0f, // left, top
        0.5f, 0.5f, 0.0f, // right, top
    };
    unsigned int indices[] = {
        0, 1, 2,
        1, 2, 3,
    };

    unsigned int VAO; // VAO: vertex array object
    unsigned int VBO; // VBO: vertex buffer object
    unsigned int EBO;

    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);

    // 绑定当前上下文
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);

    // 往显卡写值，分配显存空间。
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    // 告诉显卡，值的结构。
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
}
```


## P2 GLFW 窗口

生成窗口，支持 OpenGL 上下文。


## P3 GLAD

用户画图。

```cpp
#include "stdafx.h"
#include <math.h>
#include "LearnOpenGL.h"
#include "glad/glad.h"
#include "GLFW/glfw3.h"

#pragma comment(lib, "glfw3.lib")

#define GLSL(src) "#version 400 core\n" #src "\n\0"

int g_vertexShaderId = 0;
int g_fragShaderId = 0;
int g_shaderProgId = 0;
int g_uColorLocation = 0;

void setVertexEnv();
void createVertexShader();
void createFragShader();
void createShaderProg();
void drawContent();

int learnOpenGL() {

    // 初始化
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 0);

    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow* window = glfwCreateWindow(400, 300, "OpenGL", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        glfwTerminate();
        return -1;
    }

    setVertexEnv();
    createVertexShader();
    createFragShader();
    createShaderProg();

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE); // GL_FILL

    // 渲染引擎
    while (!glfwWindowShouldClose(window)) {

        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        drawContent();

        glfwPollEvents();
        glfwSwapBuffers(window);
    }

    // 退出
    glfwTerminate();
    return 0;
}
```

```cpp
void createShaderProg() {
    // 创建着色器程序对象
    g_shaderProgId = glCreateProgram();
    // 将编译好的着色器附加到程序对象上
    glAttachShader(g_shaderProgId, g_vertexShaderId);
    glAttachShader(g_shaderProgId, g_fragShaderId);
    // 链接生成程序
    glLinkProgram(g_shaderProgId);

    g_uColorLocation = glGetUniformLocation(g_shaderProgId, "ourColor");
}
```

```cpp
void drawContent() {

    glUseProgram(g_shaderProgId); // 使用程序

    // in out： GPU & GPU 数据传输
    // 全局 CPU 和 GPU 传数据 uniform
    float xtime = glfwGetTime();
    glUniform4f(g_uColorLocation, 0.0f, 0.0f, sin(xtime), 1.0);

    //glDrawArrays(GL_TRIANGLES, 0, 6); // 画三角
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
}
```


## P4 顶点数组对象 VAO 顶点缓冲对象 VBO

* 顶点数组对象：Vertex Array Object，VAO
* 顶点缓冲对象：Vertex Buffer Object，VBO
* 索引缓冲对象：Element Buffer Object，EBO 或 Index Buffer Object，IBO

输入：3D 坐标；输出：2D 像素。

```cpp
float vertices[] = {
    -0.5f, -0.5f, 0.0f, // left, down
    0.5f, -0.5f, 0.0f, // right, down
    -0.5f, 0.5f, 0.0f, // left, top
    0.5f, 0.5f, 0.0f, // right, top
};
unsigned int indices[] = {
    0, 1, 2,
    1, 2, 3,
};
```

{% include image.html url="/images/OpenGL-GLSL/20201112141055.png" %}


## P5 FragmentShader 片段着色器

1. 将着色器源码存入字符串
2. 创建着色器对象
3. 将源码字符串赋予着色器对象
4. 编译着色器
5. 创建着色器程序对象
6. 将编译好的着色器附加到程序对象上
7. 链接生成程序

```cpp
// 片段着色器
void createFragShader() {
    // 将着色器源码存入字符串
    const char* fragShaderSource = GLSL(
        out vec4 FragColor;
        in vec4 vertexsColor;
        uniform vec4 ourColor;
        void main() {
            FragColor = ourColor; // vertexsColor
        });

    // 创建着色器对象
    g_fragShaderId = glCreateShader(GL_FRAGMENT_SHADER);
    // 将源码字符串赋予着色器对象
    glShaderSource(g_fragShaderId, 1, &fragShaderSource, NULL);
    // 编译着色器
    glCompileShader(g_fragShaderId);
}
```


## P6 VertexShader 顶点着色器

```cpp

// 顶点着色器
void createVertexShader() {

    const char* vertexShaderSource = GLSL(
        layout(location = 0) in vec3 aPos;
        out vec4 vertexsColor;
        void main() {
            vertexsColor = vec4(0.0f, 1.0f, 0.0f, 1.0f);
            gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0f);
        });

    g_vertexShaderId = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(g_vertexShaderId, 1, &vertexShaderSource, NULL);
    glCompileShader(g_vertexShaderId);
}
```


## P7 索引缓冲对象 EBO


## P8 GLSL 数据传输


## 运行结果

{% include image.html url="/images/OpenGL-GLSL/20201112210930.png" %}
