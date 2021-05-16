---
layout: post
title: "图像处理笔记 -- The Fast Bilateral Solver 双边算子原理"
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

双边算子原理来自 Google Research Jon Barron 的 ECCV2016 论文 The Fast Bilateral Solver，
该论文获得了 ECCV 2016 年度最佳论文亚军，非常不错论文。

反正看不懂，也没时间研究，但是代码效果很吸引人。
很喜欢其中的自动上色部分。[Fast Bilateral Solver implementation with C++ and demos {% include relref_github.html %}](https://github.com/kuan-wang/The_Bilateral_Solver)
[论文 {% include relref_github.html %}](https://github.com/hawkhai/TheFastBilateralSolver/blob/master/report/The_Fast_Bilateral_Solver.pdf)
[源码 {% include relref_github.html %}](https://github.com/hawkhai/TheFastBilateralSolver/blob/master/code/FastBilateralSolver.ipynb)

{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/draw.png" %}
{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/colorized.png" %}

1. 边缘感知平滑 edge-aware smoothing
2. 自动着色 colorization
3. 深度超分辨率 depth superresolution

The Fast Bilateral Solver
Jonathan T. Barron & Ben Poole
Guillaume Dalle, MVA 2018-2019


## Algorithms


### Fast Bilateral Solver


### Domain transform


### Specific tasks and visualization

* Specific task 1: edge-aware smoothing
* Specific task 2: colorization
* Specific task 3: depth superresolution


## Applications


### Edge-aware smoothing

Test image with noise and a sharp edge

{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/11.png" url2="/assets/images/210514-dip-the-fast-bilateral-~79/12.png" %}


### Cartooning and sharpening

{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/13.png" %}
{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/14.png" %}
{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/15.png" %}
{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/16.png" %}


### Colorization

{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/17.png" %}
{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/18.png" %}


### Depth superresolution

Color photograph and disparity map from the Middlebury dataset.
来自 Middlebury 数据集 的 彩色图片 和 disparity map。

Artifial noise addition and downsampling of the depth map, followed by interpolated upsampling.
添加了人工噪点和下采样的深度图，然后插值的上采样。

{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/19.png" url2="/assets/images/210514-dip-the-fast-bilateral-~79/20.png" %}
{% include image.html url="/assets/images/210514-dip-the-fast-bilateral-~79/21.png" %}

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-14-dip-The-Fast-Bilateral-Solver.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/kuan-wang/The_Bilateral_Solver]({% include relrefx.html url="/backup/2021-05-14-dip-The-Fast-Bilateral-Solver.md/github.com/b229640a.html" %})
