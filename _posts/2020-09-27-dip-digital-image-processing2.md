---
layout: post
title: "“数字图像处理”笔记 2/2 -- 彩色图像基础知识 (DIP)"
location: "珠海"
categories: ["图像处理"]
tags: [图像处理]
mathjax: true
toc: true
mermaid: truez
---

第十一章 $\Rightarrow$ 第十四章


## 彩色图像处理

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


### 平滑 & 锐化


## 图像小波变换处理


### 墨西哥帽小波

傅立叶变换、Gabor 变换与小波变换 <https://blog.csdn.net/chenaiyanmie/article/details/80246108>

[Continuous Wavelet Transform](https://www.originlab.com/doc/Origin-Help/Continuous-WaveTrans)
The Mexican Hat wavelet is:
$$\psi(x)=\frac{2}{\sqrt{3}} \pi^{-1 / 4}\left(1-x^{2}\right) e^{-x^{2} / 2}$$

$$\psi(t)=\frac{1}{\sqrt{2 \pi} \sigma^{3}}\left(1-\frac{t^{2}}{\sigma^{2}}\right) e^{\frac{-t^{2}}{2 \sigma^{2}}}$$


## 图像压缩编码

JPEG 压缩原理与 DCT 离散余弦变换 <https://blog.csdn.net/newchenxf/article/details/51719597>

JPEG 图像压缩算法流程详解 <https://www.cnblogs.com/buaaxhzh/p/9138307.html>


## 参考

- [1] [<sup><img src="{% include relref.html url="/assets/bilibili.svg" %}" /></sup>](https://www.bilibili.com/video/BV1tx41147Tx)
- [2] [标题自动编号](https://www.cnblogs.com/36bian/p/7609304.html)
- [3] [课程目录](https://www.cnblogs.com/-wenli/p/11744405.html)
- [4] [数字图像处理实现·资料丰富](https://www.cnblogs.com/wojianxin/tag/%E6%95%B0%E5%AD%97%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86/default.html)
- [5] [opencv 图像变换原理详解 图像平移 图像旋转 图像缩放](https://www.cnblogs.com/wojianxin/p/12591410.html)
