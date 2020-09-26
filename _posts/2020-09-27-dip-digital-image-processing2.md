---
layout: post
title: "“数字图像处理”笔记 β -- 彩色图像基础知识 (DIP)"
location: "珠海"
categories: ["图像处理"]
tags: [图像处理]
mathjax: true
toc: true
mermaid: true
---

第十一章 $\Rightarrow$ 第十四章


## 色彩空间

{% include image.html url="/images/digital-image-processing2/20161108103240445.jpg" %}


### HSI 颜色模型

根据视觉的主观感受对颜色进行描述。亮度（Intensity）、色度（Hue）、饱和度（Saturation）。

RGB 转换到 HSI 空间。

{% include image.html url="/images/digital-image-processing2/17162015-b37e8ea4a16544e4b4f732d36172add3.jpg" %}


### YUV 颜色模型

多用于电视信号，人眼对亮度更敏感。Y 表示亮度，U、V 表示色差信号。


### CMYK 颜色模型

减色合成法。


### Lab 颜色模型

{% include image.html url="/images/digital-image-processing2/481745a5d7cd4c5eb99f62be8bbd1cbd.png" %}

Lab 颜色由亮度或者光亮度分量 Lab 和 a、b 两个色度分量组成。其中 a 在的正向数值越大表示越红，在负值越大则表示越绿；b 在正向数值越大表示越黄，在负向的在数值越大表示越蓝。


## toP45


## 参考

- [1] [bilibili](https://www.bilibili.com/video/BV1tx41147Tx)
- [2] [标题自动编号](https://www.cnblogs.com/36bian/p/7609304.html)
- [3] [课程目录](https://www.cnblogs.com/-wenli/p/11744405.html)
