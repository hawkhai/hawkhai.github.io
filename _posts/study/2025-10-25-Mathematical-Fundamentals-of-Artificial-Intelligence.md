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
date: 2025-10-11 01:50:53 +0800
archived: true
layoutclear: true
---

非常好的问题 👍

数学里像这样写的符号：

$$
\lVert \boldsymbol{x} \rVert
$$

叫做 **“范数”（norm）** 。

---


### 🌟 简单理解

它表示向量 $\boldsymbol{x}$ 的 **长度（模）** ，也可以理解为“到原点的距离”。

---


### 📘 举个例子

如果
$$
\boldsymbol{x} =
\begin{bmatrix}
x_1\x_2\x_3
\end{bmatrix}
$$

那么它的 **二范数（Euclidean norm，欧几里得范数）** 就是：

$$
\lVert \boldsymbol{x} \rVert = \sqrt{x_1^2 + x_2^2 + x_3^2}
$$

也就是我们熟悉的三维空间中“向量的长度”。

---


### ⚙️ 一般形式

不同的范数定义不同，常见的几种是：

| 名称          | 记号                                    | 定义                  | 含义   |   |          |
| ----------- | ------------------------------------- | ------------------- | ---- | - | -------- |
| 二范数（欧几里得范数） | $\lVert \boldsymbol{x} \rVert_2$      | $\sqrt{\sum x_i^2}$ | 向量长度 |   |          |
| 一范数         | $\lVert \boldsymbol{x} \rVert_1$      | $\sum               \| x_i  \| $ | 各分量绝对值之和 |
| 无穷范数        | $\lVert \boldsymbol{x} \rVert_\infty$ | $\max               \| x_i  \| $ | 最大绝对值    |

---


### 💡 所以

在你的式子中：

$$
\lVert \boldsymbol{x}\rVert^2
$$

表示的是 **向量长度的平方** ，即
$$
\boldsymbol{x}^\mathsf{T}\boldsymbol{x} = x_1^2 + x_2^2 + \dots + x_n^2
$$

---

是否希望我顺带讲一下“为什么用双竖线而不是单竖线”？

我们来严格推导：

---


### 1️⃣ 设定符号

设
$$
\boldsymbol{x} =
\begin{bmatrix}
x_1\x_2\\vdots\x_n
\end{bmatrix}
\in \mathbb{R}^n
$$

那么
$$
\lVert \boldsymbol{x}\rVert^2 = \boldsymbol{x}^\mathsf{T}\boldsymbol{x}
= \sum_{i=1}^n x_i^2
$$

---


### 2️⃣ 对每个分量求偏导

我们要计算
$$
\frac{\partial \lVert \boldsymbol{x}\rVert^2}{\partial \boldsymbol{x}}
$$

$$
\begin{bmatrix}
\frac{\partial \lVert \boldsymbol{x}\rVert^2}{\partial x_1} &
\frac{\partial \lVert \boldsymbol{x}\rVert^2}{\partial x_2} &
\cdots &
\frac{\partial \lVert \boldsymbol{x}\rVert^2}{\partial x_n}
\end{bmatrix}
$$

因为
$$
\lVert \boldsymbol{x}\rVert^2 = \sum_{i=1}^n x_i^2
$$

对每个分量：
$$
\frac{\partial \lVert \boldsymbol{x}\rVert^2}{\partial x_i} = 2x_i
$$

---


### 3️⃣ 写成向量形式

于是梯度为：
$$
\frac{\partial \lVert \boldsymbol{x}\rVert^2}{\partial \boldsymbol{x}}
= [2x_1, 2x_2, \dots, 2x_n]
= 2
\begin{bmatrix}
x_1\x_2\\vdots\x_n
\end{bmatrix}^{!!\mathsf{T}}
$$

如果我们采用列向量形式表示梯度（在机器学习中常用这种 convention），
则：
$$
\nabla_{\boldsymbol{x}} \lVert \boldsymbol{x}\rVert^2 = 2\boldsymbol{x}
$$

---

✅ **结论：**
$$
\boxed{\displaystyle \frac{\partial \lVert \boldsymbol{x}\rVert^2}{\partial \boldsymbol{x}} = 2\boldsymbol{x}}
$$

---


### 4️⃣ 矩阵形式的验证（更一般）

若 $\boldsymbol{x}\in\mathbb{R}^n$，有：
$$
\lVert \boldsymbol{x}\rVert^2 = \boldsymbol{x}^\mathsf{T}\boldsymbol{x}
$$
利用矩阵求导公式：
$$
\frac{\partial (\boldsymbol{x}^\mathsf{T}\boldsymbol{x})}{\partial \boldsymbol{x}}
= (\mathbf{I}+\mathbf{I})\boldsymbol{x} = 2\boldsymbol{x}
$$
与上面结果一致。


## 机器学习中常见函数的导数

标量对向量求导

标量 $y$ 对 $n$ 维向量 $\boldsymbol{x}=\left(x_1, \cdots, x_n\right)^{\mathrm{T}}$ 的导数，有：

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=\left(\frac{\partial y}{\partial x_1}, \cdots, \frac{\partial y}{\partial x_n}\right)^{\mathrm{T}}
$$

根据上式，很容易得到下面结论：

- $\frac{\partial\lVert\boldsymbol{x}\rVert^2}{\partial \boldsymbol{x}}=2 \boldsymbol{x}$
- $f(\boldsymbol{x})=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x}, \frac{\partial f(\boldsymbol{x})}{\partial \boldsymbol{x}}=(\mathbf{A} + \mathbf{A}^{\mathrm{T}}) \boldsymbol{x}$（当 $\mathbf{A}$ 对称时为 $2 \mathbf{A} \boldsymbol{x}$）
- $f(\boldsymbol{x})=\boldsymbol{\beta}^{\mathrm{T}} \boldsymbol{x}, \frac{\partial f(\boldsymbol{x})}{\partial \boldsymbol{x}}=\boldsymbol{\beta}$
- $f(\boldsymbol{x})=\lVert\boldsymbol{x}-\boldsymbol{a}\rVert, \frac{\partial f(\boldsymbol{x})}{\partial \boldsymbol{x}}=\frac{\boldsymbol{x}-\boldsymbol{a}}{\lVert\boldsymbol{x}-\boldsymbol{a}\rVert}$（当 $\boldsymbol{x} \neq \boldsymbol{a}$ 时）


## 高斯正交化

{% include image.html url="/assets/images/251025-mathematical-fundamenta~5a/23492424.png" %}


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
\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} e^{-x^2-y^2} \mathrm{~d} x \mathrm{~d} y=\int_0^{2 \pi} \int_0^{+\infty} e^{-r^2} r \mathrm{~d} r \mathrm{~d} \theta=\int_0^{2 \pi}\left(-\left.\frac{e^{-r^2}}{2}\right|_0 ^{+\infty}\right) d \theta=\int_0^{2 \pi} \frac{1}{2} \mathrm{~d} \theta=\pi
$$


## n 重积分

上面介绍的二重积分可以推广到 ( n )（( n \ge 3 )）重积分。

n 重积分的一般形式

$$
\iiint\cdots\int_D f(x_1, x_2, \dots, x_n) \, dx_1 \, dx_2 \cdots dx_n
$$

多重积分转化为累次积分

多重积分常用的一种计算方法是 **转化为累次积分** 。其一般形式为：

$$
\iiint\cdots\int_D f(x_1, x_2, \dots, x_n) \, dx_1 \, dx_2 \cdots dx_n
=
\int_{a_1}^{b_1}
dx_1
\int_{a_2(x_1)}^{b_2(x_1)}
dx_2
\cdots
\int_{a_n(x_1,\dots,x_{n-1})}^{b_n(x_1,\dots,x_{n-1})}
f(x_1, x_2, \dots, x_n) \, dx_n
$$

变量变换法（换元法）

另一种常用的计算多重积分的方法是 **换元法** 。

假设对 ( n ) 重积分进行如下的变换：

$$
x = \varphi(y)
\quad\text{ 或 }\quad
\begin{cases}
x_1 = \varphi_1(y_1, y_2, \dots, y_n) \\
x_2 = \varphi_2(y_1, y_2, \dots, y_n) \\
\vdots \\
x_n = \varphi_n(y_1, y_2, \dots, y_n)
\end{cases}
$$

若该变换的雅可比行列式（Jacobian determinant）不为零，即：

$$
\det\left( \frac{\partial x}{\partial y} \right) \ne 0
$$

则多重积分的变换公式为：

$$
\iiint\cdots\int_D f(x) \, dx
=
\iiint\cdots\int_{D'}
f(\varphi(y))
\left|
\det\left( \frac{\partial x}{\partial y} \right)
\right| dy
$$

---

✅ **说明：**

* ( D ) 为原积分区域；( D' ) 为经过变量变换后的积分区域。
* (\displaystyle \frac{\partial x}{\partial y}) 表示雅可比矩阵。
* 积分符号前的点表示多重积分（例如三重、四重、n 重）。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-10-25-Mathematical-Fundamentals-of-Artificial-Intelligence.md.js" %}'></script></p>
