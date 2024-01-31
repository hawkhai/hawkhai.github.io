---
layout: post
title: "图像处理笔记 3/2 -- OpenCV 形态学处理"
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

<https://blog.csdn.net/m0_70885101/article/details/126339673>


## 腐蚀

cv2.erode
{% include image.html url="/assets/images/240129-dip-opencv-morphology/21ab6dbf19954ff7966c07491a316d4f.png" %}


## 膨胀

cv2.dilate
{% include image.html url="/assets/images/240129-dip-opencv-morphology/085381176c6d47eb90afbd09e51c8a05.png" %}


## 开运算 = 腐蚀 + 膨胀

cv2.morphologyEx MORPH_OPEN
{% include image.html url="/assets/images/240129-dip-opencv-morphology/b601c9072bae4923b5d58f88d7c92bc6.png" %}


## 闭运算 = 膨胀 + 腐蚀

cv2.morphologyEx MORPH_CLOSE
{% include image.html url="/assets/images/240129-dip-opencv-morphology/fe75d8b8114942ceaff8e0d88bb632a8.png" %}


## 梯度 = 原图 - 腐蚀

cv2.morphologyEx MORPH_GRADIENT
腐蚀之后原图像边缘变小了，原图 - 腐蚀 就可以得到腐蚀掉的部分，即边缘。

{% include image.html url="/assets/images/240129-dip-opencv-morphology/1f3a5be1e0074ddf81d34d66b46f381d.png" %}


## 顶帽 = 原图 - 开运算

cv2.morphologyEx MORPH_TOPHAT
开运算的效果是去除图像外的噪点，原图 - 开运算 就得到了去掉的噪点。

{% include image.html url="/assets/images/240129-dip-opencv-morphology/3b561c8bfb624c439b9e8a9e8d2ac912.png" %}


## 黑帽 = 原图 - 闭运算

cv2.morphologyEx MORPH_BLACKHAT
闭运算可以将图像内部的噪点去除，那么原图 - 闭运算 的结果就是图像内部的噪点。

{% include image.html url="/assets/images/240129-dip-opencv-morphology/f023634b0d2a464ba18be75334587f38.png" %}


## 基于 OpenCV 的图像修复技术

<https://blog.csdn.net/m0_49047167/article/details/107178467>


### 算法 INPAINT_TELEA 介绍

基于快速行进算法（FMM），从待修补区域的边界向区域内部前进，先填充区域边界像素。
选待修补区域小的领域，使用领域归一化加权和更新修复像素。（先修复待修改区域的边界，依据边界外正常的像素向内修复）

Fast Marching Method
这篇文章提出的是基于快速行进算法的图像修复，其主要思想则是基于沿图像梯度传播平滑估计器。图像的平滑主要来自于受损图像领域的加权平均。同时将缺失的区域视为水平集，并用 FMM（Fast Marching Method）来描述为图像信息的传播。

{% include image.html url="/assets/images/240129-dip-opencv-morphology/20200707122132904.png" %}


### 算法 INPAINT_NS 介绍

通过匹配待修复区域的梯度相邻来延伸等光强线，灰度相等的点连成线，通过填充颜色使区域内的灰度值变化最小。

{% include image.html url="/assets/images/240129-dip-opencv-morphology/20200707122306491.png" %}

Navier-Stokes based 方法
论文摘要：这种方法利用了经典流体动力学中的思想，将等照度线连续的从待修补区域周围传播到修补区域中去。主要的观点在于将图像强度视为了二维不可压缩流的流函数（stream function），其中图像强度的拉普拉斯量为流体的旋量、并将它通过矢量场定义的流函数输运到待修补区域。最终得到的算法会通过连续照度来匹配受损区域的梯度矢量。它直接依赖于流体力学中的纳维叶斯托克斯方程，具有较强的理论和数值优势。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-01-29-dip-opencv-morphology.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/m0_70885101/article/details/126339673]({% include relrefx.html url="/backup/2024-01-29-dip-opencv-morphology.md/blog.csdn.net/f59d9bfc.html" %})
- [https://blog.csdn.net/m0_49047167/article/details/107178467]({% include relrefx.html url="/backup/2024-01-29-dip-opencv-morphology.md/blog.csdn.net/895f6395.html" %})
