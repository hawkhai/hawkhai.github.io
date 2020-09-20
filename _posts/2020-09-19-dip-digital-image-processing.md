---
layout: post
title: "“数字图像处理”笔记 -- 基础知识 Digital Image Processing (DIP)"
location: "珠海"
categories: ["图像处理"]
tags: [图像处理]
mathjax: true
toc: true
---


## 数字图像处理概述

数字图像处理 - Digital Image Processing (DIP)


### 图像和图形区别

* 图形是指令的集合，比如 `Point1.LineTo(Point2)`。
* 图像是一个数值矩阵。


### 索引图像 vs 真色彩图像

* 索引图像，有颜色表调色板索引。矩阵存储的是索引号。
* 真色彩图像，矩阵直接存储色彩像素信息。

> **UltraEdit** 软件。基本的编辑文本、十六进制、ASCII 码、语法加亮、代码折叠、代码单词拼写检查等。


## 几何变换


### 齐次坐标

齐次坐标就是将一个原本是 $n$ 维的向量用一个 $n+1$ 维向量来表示，是指一个用于投影几何里的坐标系统。

$$
\left[\begin{array}{l}
x^{\prime} \\
y^{\prime} \\
1
\end{array}\right]
=
\left[\begin{array}{lll}
1 & 0 & \Delta x \\
0 & 1 & \Delta y \\
0 & 0 & 1
\end{array}\right]
\left[\begin{array}{l}
x \\
y \\
1
\end{array}\right]
=
\left[\begin{array}{c}
x+\Delta x \\
y+\Delta y \\
1
\end{array}\right]
\tag{ 平移 }
$$

$$
T=\left[\begin{array}{cccc}
1 & 0 & \Delta x \\
0 & 1 & \Delta y \\
0 & 0 & 1
\end{array}\right]
\tag{ 平移 }
$$

$$
S=\left[\begin{array}{cccc}
S_{x} & 0 & 0 \\
0 & S_{y} & 0 \\
0 & 0 & 1
\end{array}\right]
\tag{ 缩放 }
$$

$$
R=\left[\begin{array}{cccc}
\cos \gamma & \sin \gamma & 0 \\
-\sin \gamma & \cos \gamma & 0 \\
0 & 0 & 1
\end{array}\right]
\tag{ 旋转 }
$$

$$
H
=
\left[\begin{array}{ccc}
-1 & 0 & f \text {Width} \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
\tag{ 水平镜像 }
$$

$$
V
=
\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & -1 & f \text {Height} \\
0 & 0 & 1
\end{array}\right]
\tag{ 垂直镜像 }
$$

$$
Z
=
\left[\begin{array}{ccc}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{array}\right]
\tag{ 转置 }
$$

PPT: <https://wenku.baidu.com/view/1bdcc12227c52cc58bd63186bceb19e8b8f6ecbc.html>

资料：空间变换网络（STN）原理 + 2D 图像空间变换 + 齐次坐标系讲解。<sup>[疑似转载](https://www.cnblogs.com/think90/p/11556725.html)</sup>
<sup>[**貌似原版**](https://blog.csdn.net/Rosemary_tu/article/details/84069878)</sup>


### 仿射变换 & 透视变换

扩展到三维，也是成立的。

$$
\left[\begin{array}{l}
x^{\prime} \\
y^{\prime} \\
z^{\prime} \\
1
\end{array}\right]
=
\left[\begin{array}{llll}
1 & 0 & 0 & \Delta x \\
0 & 1 & 0 & \Delta y \\
0 & 0 & 1 & \Delta z \\
0 & 0 & 0 & 1
\end{array}\right]
\left[\begin{array}{l}
x \\
y \\
z \\
1
\end{array}\right]
=
\left[\begin{array}{c}
x+\Delta x \\
y+\Delta y \\
z+\Delta z \\
1
\end{array}\right]
$$

{z% include image.html url="/images/digital-image-processing/20190104135139626.png" noshadow=1 %}
{z% include image.html url="/images/digital-image-processing/20190104135201258.png" noshadow=1 %}
{z% include image.html url="/images/digital-image-processing/20190104135229160.png" noshadow=1 %}
{z% include image.html url="/images/digital-image-processing/20190104135246701.png" noshadow=1 %}


## 图像增强 & 灰度变化

点运算：$$g(x, y) = T[f(x, y)]$$


## 图像平滑处理

领域处理方法，空域卷积滤波。

中值滤波法。中值滤波法是一种非线性平滑技术，它将每一像素点的灰度值设置为该点某邻域窗口内的所有像素点灰度值的中值。


##  图像锐化

微分运算，梯度锐化，边缘检测。

$$
\nabla f(x, y)=\left[G_{x}, G_{y}\right]^{T}=\left[\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right]^{T}
$$

这个矢量的幅度为：

$$\operatorname{mag}(\nabla f)=g(x, y)=\sqrt{\frac{\partial^{2} f}{\partial x^{2}}+\frac{\partial^{2} f}{\partial y^{2}}}$$

方向角为：

$$\phi(x, y)=\arctan \left|\frac{\partial f}{\partial y} / \frac{\partial f}{\partial x}\right|$$

数字图像中，更多的使用差分来近似导数，最简单的梯度近似表达式如下：

$$\begin{array}{l}
G_{x}=f(x, y)-f(x-1, y) \\
G_{y}=f(x, y)-f(x, y-1)
\end{array}$$


### 拉普拉斯算子

二阶微分，拉普拉斯算子。

$$\begin{array}{l}
\nabla^2 f=\frac{\partial^{2} f}{\partial x^{2}}+\frac{\partial^{2} f}{\partial y^{2}} \\
\frac{\partial^{2} f}{\partial x^{2}}=f(x+1)+f(x-1)-2 f(x) \\
\frac{\partial^{2} f}{\partial y^{2}}=f(y+1)+f(y-1)-2 f(y) \\
\end{array}$$

$$
\nabla^2 f=[f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)]-4f(x,y)\tag{ 两个分向量相加 }
$$

原始图像和拉普拉斯图像叠加，可以边缘加强。

$$
g(x)=
\begin{cases}
f(x, y)-\nabla^{2} f(x, y) & \text{ 中心系数为负 } \\
f(x, y)+\nabla^{2} f(x, y) & \text{ 中心系数为正 }
\end{cases}
$$

边缘检测，LOG 算子（高斯-拉普拉斯算子 / Laplacian of Gaussian, LoG）中心点的距离与位置加权系数的关系：

{% include image.html url="/images/digital-image-processing/bki-20131208210655-949753613.png" noshadow=1
url2="/images/digital-image-processing/logx.png" %}
{% include image.html url="/images/digital-image-processing/v2-f824bd5eae07235ebf531fa0b546ba98_720w.jpg" %}

推演过程。高斯二阶导如下图的绿色线，蓝色线是高斯一阶导数，红色则是高斯函数。

{% include image.html url="/images/digital-image-processing/20170315204708636.png" %}


### 高频提升滤波器

$$
g(x,y)=af(x,y)\pm \nabla f(x,y)
$$


## toP24


### zz


## 参考

- [1] [bilibili](https://www.bilibili.com/video/BV1tx41147Tx?from=search&seid=2305003300792844801)
- [2] [标题自动编号](https://www.cnblogs.com/36bian/p/7609304.html)
