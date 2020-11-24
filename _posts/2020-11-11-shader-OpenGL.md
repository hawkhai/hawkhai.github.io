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
顶点着色器、几何着色器、片段着色器。又酷又通透，身心愉悦 ——

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


## P2 GLFW 窗口

生成窗口，支持 OpenGL 上下文。


## P3 GLAD

用户画图。


## P4 顶点数组对象 VAO 顶点缓冲对象 VBO

* 顶点数组对象：Vertex Array Object，VAO
* 顶点缓冲对象：Vertex Buffer Object，VBO
* 索引缓冲对象：Element Buffer Object，EBO 或 Index Buffer Object，IBO

输入：3D 坐标；输出：2D 像素。

{% include image.html url="/images/OpenGL-GLSL/20201112141055.png" %}


## P5 FragmentShader 片段着色器

1. 将着色器源码存入字符串
2. 创建着色器对象
3. 将源码字符串赋予着色器对象
4. 编译着色器
5. 创建着色器程序对象
6. 将编译好的着色器附加到程序对象上
7. 链接生成程序


## P6 VertexShader 顶点着色器


## P7 索引缓冲对象 EBO


## P8 GLSL 数据传输


## 一个 VAO 对应多个 VBO

{% include image.html url="/images/OpenGL-GLSL/20201119170155.png" %}
{% include image.html url="/images/OpenGL-GLSL/v2-2f7beaffce2851a26a5bcba77e29120a_720w.jpg" %}


## todo

类封装。


## 运行结果

{% include image.html url="/images/OpenGL-GLSL/20201112210930.png" %}
