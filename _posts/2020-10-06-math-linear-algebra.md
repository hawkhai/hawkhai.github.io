---
layout: post
title: "NOTE -- 线性代数的本质"
location: "珠海"
categories: ["数学之美"]
tags: [数学之美]
mathjax: true
toc: true
---

线性代数存在完整的空间意义，平时的写法只是一种简写。

线性代数的本质 <https://www.bilibili.com/video/BV1ys411472E>

线性代数里面“线性”两个字究竟是啥意思？**线性变换就是保持网格线平行和等距分布，并且保持原点不动的一类变换。**

$$
\underbrace{\left[\begin{array}{cc}
1 & 1 \\
0 & 1
\end{array}\right]}_{\text {Shear }}(\underbrace{\left[\begin{array}{cc}
0 & -1 \\
1 & 0
\end{array}\right]}_{\text {Rotation }}\left[\begin{array}{l}
x \\
y
\end{array}\right])=\underbrace{\left[\begin{array}{cc}
1 & -1 \\
1 & 0
\end{array}\right]}_{\text {Composition }}
\left[\begin{array}{l}
x \\
y
\end{array}\right]
$$

齐次坐标，数字图像平移、伸缩、旋转等计算，可以通过 Composition 加快计算速度。


## 行列式

行列式是线性变换的伸缩因子。

$$
\operatorname{det}\left(\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]\right)=a d-b c
$$


## 线性方程组

{% include image.html url="/images/linear-algebra/20201006145304.png" %}


## 点积


## 抽象向量空间


## 克莱姆法则


## toP10


## 参考

- [1] [线性代数的本质 <img src="{% include relref.html url="/assets/bilibili.svg" %}" class="bilibili" />](https://www.bilibili.com/video/BV1ys411472E)
