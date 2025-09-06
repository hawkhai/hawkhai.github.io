---
layout: post
title: "MATHEMATICS --《线性代数》奇异值分解（SVD）"
author:
location: "珠海"
categories: ["数学"]
tags: ["数学"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
cluster: "机器学习的数学基础"
---

奇异值分解本质上是 **特征值分解的一个扩展** ，就是将一个 $$m×n$$ 的矩阵分解成三个矩阵相乘。

* 矩阵分解动画讲解，其实也很简单！ <https://www.bilibili.com/video/BV1zqYpzwEaQ/>
* 代数明珠--奇异值分解（SVD）生动动画演示！ <https://www.bilibili.com/video/BV1n5YyztEVk/>


## 特征值分解


### 特征值和特征向量

$$Av=λv$$

其中 A 是一个 n 维的方阵，v 是 n 维特征向量，λ 是个数字（特征值）。每一个特征值都对应一个特征向量。

上面式子也可以理解为：A 为对 v 向量的变换矩阵，由于 λ 仅仅是一个数值，所以这个变换 **只有拉伸没有旋转** 。


### 特征值分解

如果方阵 A 的秩为 m，那么就有 m 个特征值，也对应 m 个特征向量（正交）。每一个都满足表达式 Av=λv。
那么，就可以写成如下形式

{% include image.html url="/assets/images/240404-linear-algebraic-svd/6401.png" %}

$$AV=Vζ$$

V 是特征向量组成的矩阵，ζ 是对角线上元素为特征值的的对角阵。方程两边同时乘以 V 矩阵的逆得到：

$$A=VζV^{-1}$$

如果矩阵 A 不是方阵，那么就用到了奇异值分解。


## 奇异值分解


### 定义

$$A=UΣV^{-1}$$

A 是将要分解的大小为 m×n 的矩阵。U 是 m 维的方阵。V 是 n 维的方阵。
Σ 是除主对角线元素以外全为 0 的矩阵，大小为 m×n。示意图如下：

{% include image.html url="/assets/images/240404-linear-algebraic-svd/6402.png" %}


### 求解

还是按照特征值求解的思路，现在的矩阵 A 不是方阵，如果将其乘以自己的转置矩阵就变成了方阵，
是方阵就可以求其特征值和特征向量。

{% include image.html url="/assets/images/240404-linear-algebraic-svd/6403.png" %}

Σ 主对角线上的元素就是矩阵对应的奇异值，按从大到小的顺序排列，
奇异值越大代表其对应的特征向量包含的特征越多。利用这一点，可以对数据进行降维，压缩等应用。


### 奇异值分解代表的物理意义

一个矩阵可以理解为一个线性变换，如果矩阵是对角阵，那么对应的变换是 **拉伸** 。
如果矩阵是由正交向量组成的，那么对应的变换是 **旋转** 。
所以，奇异值分解就是将一个线性变换分解成先旋转，后拉伸，最后再旋转的一个过程。

{% include image.html url="/assets/images/240404-linear-algebraic-svd/6404.png" %}



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-04-04-Linear-Algebraic-SVD.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1zqYpzwEaQ/]({% include relrefx.html url="/backup/2024-04-04-Linear-Algebraic-SVD.md/www.bilibili.com/a9e69139.html" %})
- [https://www.bilibili.com/video/BV1n5YyztEVk/]({% include relrefx.html url="/backup/2024-04-04-Linear-Algebraic-SVD.md/www.bilibili.com/ca14073b.html" %})
