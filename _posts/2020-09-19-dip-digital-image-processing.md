---
layout: post
title: "“数字图像处理”笔记 -- Digital Image Processing (DIP)"
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

[空间变换网络（STN）原理 + 2D 图像空间变换 + 齐次坐标系讲解](https://www.cnblogs.com/think90/p/11556725.html)


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
资料：[空间变换网络（STN）原理 + 2D 图像空间变换 + 齐次坐标系讲解](https://blog.csdn.net/Rosemary_tu/article/details/84069878)


### 仿射变换 & 透视变换

{% include image.html url="/images/digital-image-processing/20190104135139626.png" noshadow=1 %}
{% include image.html url="/images/digital-image-processing/20190104135201258.png" noshadow=1 %}
{% include image.html url="/images/digital-image-processing/20190104135229160.png" noshadow=1 %}
{% include image.html url="/images/digital-image-processing/20190104135246701.png" noshadow=1 %}


## toP14


### zz


## 参考

- [1] [bilibili](https://www.bilibili.com/video/BV1tx41147Tx?from=search&seid=2305003300792844801)
- [2] [标题自动编号](https://www.cnblogs.com/36bian/p/7609304.html)
