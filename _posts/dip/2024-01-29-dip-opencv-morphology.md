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



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-01-29-dip-opencv-morphology.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/m0_70885101/article/details/126339673]({% include relrefx.html url="/backup/2024-01-29-dip-opencv-morphology.md/blog.csdn.net/f59d9bfc.html" %})
