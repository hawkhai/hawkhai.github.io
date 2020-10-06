---
layout: post
title: "“数字图像处理”笔记 -- 傅里叶变换"
location: "珠海"
categories: ["图像处理"]
tags: [图像处理]
mathjax: true
toc: true
mermaid: truez
---


## 数学推导 傅里叶级数与傅里叶变换

傅里叶分析之掐死教程 <https://zhuanlan.zhihu.com/p/19763358>

{% include image.html url="/images/fourier-transform/40cf849e55ed95732a60b52d4019d609_r.jpg" %}

Part1. 三角函数的正交性 <https://www.bilibili.com/video/BV1Et411R78v>

Part2. 周期为 $2\varPi$ 的函数展开 <https://www.bilibili.com/video/BV17t411d7hm>

Part3. 周期为 $2L$ 的函数展开 <https://www.bilibili.com/video/BV1wb411K7Kp>

Part4. 傅里叶级数的复数形式 <https://www.bilibili.com/video/BV13b411P7mU>

Part5. 从傅里叶级数推导傅里叶变换 <https://www.bilibili.com/video/BV1jt411U7Bp>

Part6. 总结与闲话 <https://www.bilibili.com/video/BV1St41117fH>


### 复数的物理意义

[复数的物理意义是什么？](https://www.zhihu.com/question/23234701/answer/26017000)

转载文章：[傅里叶变换分析之掐死教程](https://blog.csdn.net/Ciellee/article/details/108304531)

高维空间我们感知不到，只能通过投射到三维，甚至二维，直观感受其投影。
数学是我们最有力的分析工具。事情直接处理很难，升维或者变维后却变的很简单，处理完后再变换回去，搞定。

三维到二维的投影。欧拉公式所描绘的，是一个随着时间变化，在复平面上做圆周运动的点，随着时间的改变，在时间轴上就成了一条螺旋线。如果只看它的实数部分，也就是螺旋线在左侧的投影，就是一个最基础的余弦函数。而右侧的投影则是一个正弦函数。

{% include image.html url="/images/fourier-transform/20200901103813238.png" %}


### 傅里叶变换（Fourier Transformation）

{% include image.html url="/images/fourier-transform/419cd0b2e965aca25d5f8a5a6362d728_720w.jpg" %}

[傅里叶级数和傅里叶变换是什么关系？](https://www.zhihu.com/question/21665935)

**[马同学原版·从傅里叶级数到傅里叶变换](https://www.matongxue.com/madocs/712)**

周期函数，可以通过傅里叶级数画出频域图；增长周期，频域图变得越来越密集；当周期无限大，得到傅里叶变换，频域图变为连续的曲线。

{% include image.html url="/images/fourier-transform/v2-8f5dc83df22c3296f312139d2d3c74bb_720w.jpg" %}

傅里叶级数的本质是将一个周期的信号分解成无限多分开的（离散的）正弦波。

傅里叶变换实际上是对一个周期无限大的函数进行傅里叶变换。
是将一个时域非周期的连续信号，转换为一个在频域非周期的连续信号。

{% include image.html url="/images/fourier-transform/ece53f825c6de629befba3de12f929a7_720w.jpg" %}

[形象展示傅里叶变换 <sup><img src="{% include relref.html url="/assets/bilibili.svg" %}" /></sup>](https://www.bilibili.com/video/BV1pW411J7s8)

**这个视频形象 [傅里叶级数与傅里叶变换 <sup><img src="{% include relref.html url="/assets/bilibili.svg" %}" /></sup>](https://www.bilibili.com/video/BV11W411H7Uz)**

傅里叶变换是将函数分解到频率不同、幅值恒为 1 的单位圆上；拉普拉斯变换是将函数分解到频率幅值都在变化的圆上。
因为拉普拉斯变换的基有两个变量，因此更灵活，适用范围更广。

[拉普拉斯变换可视化 <sup><img src="{% include relref.html url="/assets/bilibili.svg" %}" /></sup>](https://www.bilibili.com/video/BV1Yb411G7u2)

[3D 动画详细解释傅里叶与拉普拉斯变换 <sup><img src="{% include relref.html url="/assets/bilibili.svg" %}" /></sup>](https://www.bilibili.com/video/BV1MJ41147PH)

最后这个“海螺图”还是有点没看懂。?

{% include image.html url="/images/fourier-transform/f116ae26859bdc80b28ea0f8f894ccc0_720w.jpg" %}


## 傅里叶变换理解

一个频率相当于一个维度，当维度变成无穷多维度，然后频率叠加就是密度。？

{% include image.html url="/images/fourier-transform/v2-bad520e27c839917cf27d76e1206bb70_1440w.jpg" %}

[以初中数学基础理解傅里叶变换 <sup><img src="{% include relref.html url="/assets/bilibili.svg" %}" /></sup>](https://www.bilibili.com/video/BV1TJ41157FZ)

[形象理解二维傅里叶变换](https://zhuanlan.zhihu.com/p/110026009)

{% include image.html url="/images/fourier-transform/v2-73ad89919f066942a612107925152c8c_720w.jpg" %}

中心低频贡献了图像的主体，周围高频提供图像的细节和边缘。

{% include image.html url="/images/fourier-transform/v2-39eb0e4cd7fa4f0cd927bc97fc1c1674_720w.jpg" %}

[为什么用图像二维傅里叶变换的相位谱进行反变换，能够大致得到原图的形状，而幅度谱则不行呢？](https://www.zhihu.com/question/23718291/answer/1057562032)

k 空间中的 phase 保留的是位置信息，如果没有幅度或者，幅度错误，只是对比度会不同；而 mag 保留的是强度信息，没有 phase 的话，强度相加也是按照周期性相加。

因此：k 空间中的幅度决定强度信息，相位决定位置位置信息。


## 应用举例

PDF <a href="{% include relref.html url="/source/2D-Fourier-transforms.pdf" %}"
target="_blank">2D Fourier transforms and applications</a>
from http://www.robots.ox.ac.uk/~az/lectures/ia/lect2.pdf


### 螺旋 CT 成像

[连原子都能看清的 CT 成像 <sup><img src="{% include relref.html url="/assets/bilibili.svg" %}" /></sup>](https://www.bilibili.com/video/BV1w54y1R7LT)

{% include image.html url="/images/fourier-transform/20201006194100.png" %}


### 指纹去噪

{% include image.html url="/images/fourier-transform/v2-5b1db77b17cc490cae1e9670bb34eeeb_720w.jpg" %}


### 天体表面去噪

{% include image.html url="/images/fourier-transform/v2-2c6301e214b1766e2b4173c2a0593bb2_720w.jpg" %}


## 参考

- [1] [bilibili <sup><img src="{% include relref.html url="/assets/bilibili.svg" %}" /></sup>](https://space.bilibili.com/230105574/channel/detail?cid=67768)
- [2] [课程目录](https://www.cnblogs.com/-wenli/p/11744405.html)
- [3] [公式图形实时显示](https://www.desmos.com/calculator)
