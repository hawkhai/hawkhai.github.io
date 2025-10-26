---
layout: post
title: "图像处理笔记 -- 数字图像处理 (DIP)"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## 色彩模型

面向设备的色彩模型
RGB
CMYK

面向色彩感知的色彩模型
HSI
LAB


### RGB 模型 —— 面向输出显示设备

RGB 模型是基于仿生学原理，人的视网膜有三种细胞，分别对红、绿、蓝三种颜色敏感（其中绿色最敏感）。这三种颜色的光通过相加，可以混合出绝大部分肉眼能看到的颜色。
使用最广泛的色彩模型。非常适合在输出显示场合使用，如彩色电视机的显像管、计算机的显示器。

国际照度委员会规定 3 种基本色的波长为 R:700nm，G:546.1nm，B:435.8nm。

{% include image.html url="/assets/images/251022-dip-digital-image-proce~aa/2381.png" %}


### CMYK 模型 —— 面向输出印刷设备

CMYK 色彩系统是一种用于印刷的模式，分别是指青（Cyan）、品红（Magenta）、黄（Yellow）和黑（Black）。

CMYK 模式在本质上与 RGB 颜色模式没有什么区别，只是产生色彩的原理不同。RGB 颜色合成是通过颜色相加。而 CMYK 是通过颜色相减产生其它颜色。
RGB 与 CMYK 没有一一对应的转换关系，转换过程会与显示器设置、印刷油墨设置以及分色设置有关。

在处理图像时，一般不采用 CMYK 模式，因为：①这种模式的图像文件占用的存储空间较大；②色域范围比 RGB 小得多。

{% include image.html url="/assets/images/251022-dip-digital-image-proce~aa/3948.png" %}


### 亮度

亮度表示某种颜色在人眼视觉上引起的明暗程度，它由光的强度（能量）决定：光的强亮越大，景物就越亮；光的强度越小，景物就越暗。

对于灰度图象而言，亮度就是图像的灰度值。


### 色调

色调（色相）表示光的颜色，它由光的波长决定。例如自然界中的七色光就分别对应着不同的色调，每种色调分别对应着不同的波长。

在通常的使用中，色调是由颜色名称标识的，比如红、橙或绿色。


### 饱和度

饱和度指颜色的纯度（鲜艳程度），它由主波长的纯光谱色与白光的比例决定，也就是说，夹杂白光的多少。越接近光谱色、白光比例越小，则饱和度越高，色彩越鲜艳醒目；距离光谱色越远、白光比例越大，饱和度越低，色彩越平淡晦暗，越不鲜艳。
如对白光来讲，它的色饱和度为 0（没有色彩），纯色的色饱和度是 100%，指该彩色中不含白光。


### HSI 色彩模型

最直观的色彩描述方法。用色调（Hue）、色饱和度（Saturation）和亮度（Intensity）来描述色彩。它与人类颜色视觉感知非常接近，但独立于设备（设备造不出来，仅存在于软件中）。

这个模型有两个特点：I 分量与图像的彩色信息无关；其二，H 和 S 分量与人感受颜色的方式是紧密相连的。这些特点使得 HSI 模型比 RGB 色彩空间更符合人的视觉特性，非常适合于借助人的视觉系统来感知彩色特性的图像处理算法。

{% include image.html url="/assets/images/251022-dip-digital-image-proce~aa/hsi.png" %}


### LAB 色彩模型

一种能够描述颜色感觉的标准语言，能够用数学方法唯一精确定义颜色刺激所产生的感觉，这种模型就是 LAB 模型。

L 表示亮度，A 赋予了从红到绿的所有颜色，B 赋予了从黄到蓝的所有颜色，该模型覆盖了全部的可见光色谱。

该模型与设备无关（仅存在于数学 / 软件中）。 没有提供直接显示的格式，必须要转换到其它色彩空间来显示。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-10-22-dip-digital-image-processing.md.js" %}'></script></p>
