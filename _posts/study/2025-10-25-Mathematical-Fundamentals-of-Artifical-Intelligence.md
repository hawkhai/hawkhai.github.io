---
layout: post
title: "人工智能 -- 人工智能数学基础"
author: qhai
location: "珠海"
categories: ["人工智能"]
tags: ["人工智能"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
permalink:
date: 2025-10-11 01:50:53 +0800
archived: true
layoutclear: true
---


## 机器学习中常见函数的导数

标量对向量求导

标量 y 对 n 维向量 $\boldsymbol{x}=\left(x_1, \cdots, x_n\right)^{\mathrm{T}}$ 的导数，有：

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=\left(\frac{\partial y}{\partial x_1}, \cdots, \frac{\partial y}{\partial x_n}\right)^{\mathrm{T}}
$$

根据上式，很容易得到下面结论：

- $\frac{\partial\|\boldsymbol{x}\|^2}{\partial \boldsymbol{x}}=2 \boldsymbol{x}$
- $f(\boldsymbol{x})=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x}, \frac{\partial f(\boldsymbol{x})}{\partial \boldsymbol{x}}=2 \mathbf{A} \boldsymbol{x}$
- $f(\boldsymbol{x})=\boldsymbol{\beta}^{\mathrm{T}} \boldsymbol{x}, \frac{\partial f(\boldsymbol{x})}{\partial \boldsymbol{x}}=\boldsymbol{\beta}$
- $f(\boldsymbol{x})=\|\boldsymbol{x}-\boldsymbol{a}\|, \frac{\partial f(\boldsymbol{x})}{\partial \boldsymbol{x}}=\frac{\boldsymbol{x}-\boldsymbol{a}}{\|\boldsymbol{x}-\boldsymbol{a}\|}$


## 高斯正交化

{% include image.html url="/assets/images/251025-mathematical-fundamenta~18/23492424.png" %}


## 多重积分

显然，极坐标系下的二重积分也可以类似直角坐标系那样，采用分步积分法求解。下面我们给出一个典型例子，利用极坐标变换公式求解一个二重积分。

例 2-11 计算二重积分
$$
\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} e^{-x^2-y^2} \mathrm{~d} x \mathrm{~d} y
$$

将该积分采用极坐标变换之后，在极坐标系中，积分区域 D 为
$$
D=\{(r, \theta) \mid 0 \leq \theta \leq 2 \pi, 0 \leq r<+\infty\}
$$
于是有
$$
\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} e^{-x^2-y^2} \mathrm{~d} x \mathrm{~d} y=\int_0^{2 \pi} \int_0^{+\infty} e^{-r^2} r \mathrm{~d} x \mathrm{~d} y=\int_0^{2 \pi}\left(-\left.\frac{e^{-r^2}}{2}\right|_0 ^{+\infty}\right) d \theta=\int_0^{2 \pi} \frac{1}{2} \mathrm{~d} \theta=\pi
$$

## 下面是整理后的 **Markdown (MD)** 文档，包含正确的数学公式（LaTeX 语法），可直接在支持公式渲染的 Markdown 编辑器或 GitHub 上使用。

---

## n 重积分

上面介绍的二重积分可以推广到 ( n )（( n \ge 3 )）重积分。

n 重积分的一般形式

[
\iiint!!\cdots!!\int_D f(x_1, x_2, \dots, x_n) , dx_1 , dx_2 \cdots dx_n
]

多重积分转化为累次积分

多重积分常用的一种计算方法是**转化为累次积分**。其一般形式为：

[
\iiint!!\cdots!!\int_D f(x_1, x_2, \dots, x_n), dx_1, dx_2 \cdots dx_n
======================================================================

\int_{a_1}^{b_1}
!!dx_1
\int_{a_2(x_1)}^{b_2(x_1)}
!!dx_2
\cdots
\int_{a_n(x_1,\dots,x_{n-1})}^{b_n(x_1,\dots,x_{n-1})}
f(x_1, x_2, \dots, x_n), dx_n
]

变量变换法（换元法）

另一种常用的计算多重积分的方法是**换元法**。

假设对 ( n ) 重积分进行如下的变换：

[
x = \varphi(y)
\quad\text{或}\quad
\begin{cases}
x_1 = \varphi_1(y_1, y_2, \dots, y_n) \
x_2 = \varphi_2(y_1, y_2, \dots, y_n) \
\vdots \
x_n = \varphi_n(y_1, y_2, \dots, y_n)
\end{cases}
]

若该变换的雅可比行列式（Jacobian determinant）不为零，即：

[
\det!\left( \frac{\partial x}{\partial y} \right) \ne 0
]

则多重积分的变换公式为：

[
\iiint!!\cdots!!\int_D f(x), dx
===============================

\iiint!!\cdots!!\int_{D'}
f(\varphi(y)) ,
\left|
\det!\left( \frac{\partial x}{\partial y} \right)
\right| dy
]

---

✅ **说明：**

* ( D ) 为原积分区域；( D' ) 为经过变量变换后的积分区域。
* (\displaystyle \frac{\partial x}{\partial y}) 表示雅可比矩阵。
* 积分符号前的点表示多重积分（例如三重、四重、n重）。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-10-25-Mathematical-Fundamentals-of-Artifical-Intelligence.md.js" %}'></script></p>
