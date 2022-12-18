---
layout: post
title: "图像处理笔记 2/2 -- 彩色图像基础知识 (DIP)"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---


## RGB, HSV, Lab, HSL, YUV

[from {% include relref_csdn.html %}](https://blog.csdn.net/qq_41731507/article/details/113868152)
The geometric derivation of the cylindrical HSL and HSV representations of an RGB "colorcube".
{% include image.html url="/assets/images/200927-dip-color-image/Hsl-and-hsv.svg.png" %}


### RGB vs. CMYK

RGB 色彩空间采用物理三基色表示，因而物理意义很清楚，适合彩色显象管工作。
RGB 模式是一种发光屏幕的加色模式，CMYK 模式是一种颜色反光的印刷减色模式。

{% include image.html url="/assets/images/200927-dip-color-image/2021021917230853.png" %}
{% include image.html url="/assets/images/200927-dip-color-image/3801213fb80e7bec54e780b79f66ae389b504fc23d06.webp" %}


### HSV vs. HSL vs. HSI

HSV 类似于人类感觉颜色的方式。
在圆锥的顶点（即原点）处，V=0，H 和 S 无定义，代表黑色。
圆锥的顶面中心处 S=0，V=1，H 无定义，代表白色。
GIMP（HSV 用于颜色选择，HSL 用于颜色调整）

{% include image.html url="/assets/images/200927-dip-color-image/296px-HSL_color_solid_cylinder_saturation_gray.png"
url2="/assets/images/200927-dip-color-image/296px-HSV_color_solid_cylinder_saturation_gray.png" %}

{% include image.html url="/assets/images/200927-dip-color-image/20210219172903677.jpg" %}
{% include image.html url="/assets/images/200927-dip-color-image/20161108103240445.jpg" %}

#### HSV 颜色模型

色调 H（Hue）：与光波的波长有关，它表示人的感官对不同颜色的感受，如红色、绿色、蓝色等，它也可表示一定范围的颜色，如暖色、冷色等。

饱和度 S（Saturation）：表示颜色的纯度，纯光谱色是完全饱和的，加入白光会稀释饱和度。饱和度越大，颜色看起来就会越鲜艳，反之亦然。

亮度 I（Intensity）：对应成像亮度和图像灰度，是颜色的明亮程度。

明度 V：明度表示颜色明亮的程度，对于光源色，明度值与发光体的光亮度有关；对于物体色，此值和物体的透射比或反射比有关。通常取值范围为 0%（黑）到 100%（白）。

{% include image.html url="/assets/images/200927-dip-color-image/1353461596_7598.jpg" %}

$\text{HSV}$ 即使用**色相（Hue）、饱和度（Saturation）、明度（Value）**来表示色彩的一种方式。

- 色相：将颜色使用 $0^{\circ}$ 到 $360^{\circ}$ 表示，就是平常所说的颜色名称，如红色、蓝色。色相与数值按下表对应：

    | 红          | 黄           | 绿            | 青色          | 蓝色          | 品红          | 红            |
    | ----------- | ------------ | ------------- | ------------- | ------------- | ------------- | ------------- |
    | $0^{\circ}$ | $60^{\circ}$ | $120^{\circ}$ | $180^{\circ}$ | $240^{\circ}$ | $300^{\circ}$ | $360^{\circ}$ |

- 饱和度：是指色彩的纯度，饱和度越低则颜色越黯淡（$0\leq S < 1$）；
- 明度：即颜色的明暗程度。数值越高越接近白色，数值越低越接近黑色（$0\leq V < 1$）；

#### HSI 颜色模型

根据视觉的主观感受对颜色进行描述。亮度（Intensity）、色度（Hue）、饱和度（Saturation）。

RGB 转换到 HSI 空间。

{% include image.html url="/assets/images/200927-dip-color-image/17162015-b37e8ea4a16544e4b4f732d36172add3.jpg" %}

{% include image.html url="/assets/images/200927-dip-color-image/9a093de900836fccfdb1d6de768343b2.png" %}

#### HSV 与 HSI 区别

HSV 里面的 v 指的是 RGB 里面的最大的值，$v = max(max(r,g),b)$，
而 HSI 的 I 是平均值，$I=(r+g+b) / 3$，
另外两个分量应该是一样的，如果只是需要 h 或者 s 的话可以用 matlab 自带的 rgb2hsv 了。


### YUV

多用于电视信号，人眼对亮度更敏感。Y 表示亮度，U、V 表示色差信号。
彩色电视采用 YUV 空间正是为了用亮度信号 Y 解决彩色电视机与黑白电视机的相容问题，使黑白电视机也能接收彩色电视信号。


### Lab

Lab 颜色被设计来接近人类视觉。它致力于感知均匀性，它的 L 分量密切匹配人类亮度感知。

Lab 颜色由亮度或者光亮度分量 Lab 和 a、b 两个色度分量组成。
其中 a 在的正向数值越大表示越红，在负值越大则表示越绿；
b 在正向数值越大表示越黄，在负向的在数值越大表示越蓝：
- L\* 代表亮度
- a\* 代表从绿色到红色的分量
- b\* 代表从蓝色到黄色的分量

{% include image.html url="/assets/images/200927-dip-color-image/6114414-8bbd10752e22cbd2.webp" %}


## 平滑 & 锐化


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

- [1] [bilibili {% include relref_bili.html %}](https://www.bilibili.com/video/BV1tx41147Tx)
- [2] [标题自动编号 {% include relref_cnblogs.html %}](https://www.cnblogs.com/36bian/p/7609304.html)
- [3] [课程目录 {% include relref_cnblogs.html %}](https://www.cnblogs.com/-wenli/p/11744405.html)
- [4] [数字图像处理实现·资料丰富 {% include relref_cnblogs.html %}](https://www.cnblogs.com/wojianxin/tag/%E6%95%B0%E5%AD%97%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86/default.html)
- [5] [opencv 图像变换原理详解 图像平移 图像旋转 图像缩放 {% include relref_cnblogs.html %}](https://www.cnblogs.com/wojianxin/p/12591410.html)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-09-27-dip-color-image.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/qq_41731507/article/details/113868152]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/blog.csdn.net/f0629609.html" %})
- [https://blog.csdn.net/chenaiyanmie/article/details/80246108]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/blog.csdn.net/8f1617a3.html" %})
- [https://www.originlab.com/doc/Origin-Help/Continuous-WaveTrans]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/www.originlab.com/1c8787ea.html" %})
- [https://blog.csdn.net/newchenxf/article/details/51719597]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/blog.csdn.net/55caa543.html" %})
- [https://www.cnblogs.com/buaaxhzh/p/9138307.html]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/www.cnblogs.com/d90fb3c3.html" %})
- [https://www.bilibili.com/video/BV1tx41147Tx]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/www.bilibili.com/57d122ce.html" %})
- [https://www.cnblogs.com/36bian/p/7609304.html]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/www.cnblogs.com/9c1872d6.html" %})
- [https://www.cnblogs.com/-wenli/p/11744405.html]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/www.cnblogs.com/98804d9b.html" %})
- [https://www.cnblogs.com/wojianxin/tag/%E6%95%B0%E5%AD%97%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86/default.html]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/www.cnblogs.com/5292bd07.html" %})
- [https://www.cnblogs.com/wojianxin/p/12591410.html]({% include relrefx.html url="/backup/2020-09-27-dip-color-image.md/www.cnblogs.com/5c2ee41d.html" %})
