---
layout: post
title: "数学笔记 -- 线性代数的本质"
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
---

线性代数存在完整的空间意义，平时的写法只是一种简写。

线性代数的本质 <https://www.bilibili.com/video/BV1ys411472E>

线性代数里面“线性”两个字究竟是啥意思？ **线性变换就是保持网格线平行和等距分布，并且保持原点不动的一类变换。**

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

{% include image.html url="/assets/images/201006-math-linear-algebra/20201006145304.png" %}


## 点积


## 叉乘 Cross product

{% include image.html url="/assets/images/201006-math-linear-algebra/220px-cross_product.gif" url2="/assets/images/201006-math-linear-algebra/220px-right_hand_rule_cross_product.svg.png" %}
{% include image.html url="/assets/images/201006-math-linear-algebra/220px-cross_product_parallelogram.svg.png" url2="/assets/images/201006-math-linear-algebra/220px-cross_product_vector.svg.png" %}


## 抽象向量空间


## 克莱姆法则


## toP10


## 编程与线性代数

模型的作用就是把一部分复杂性隐藏到模型中，使得模型的使用者可以更加简单地解决问题。曾经有人质疑 C++ 太复杂，C++ 之父 Bjarne Stroustrup 这样回答：

> Complexity will go somewhere: if not the language then the application code.

线性代数的核心：向量模型。给定三维坐标系中的一点 $$(x_0, y_0, z_0)$$ 和一个平面 $$a*x + b*y + c*z + d = 0$$，求点到平面的垂直距离？

{% include image.html url="/assets/images/201006-math-linear-algebra/rr3qru.jpeg" %}

根据平面方程，平面的法向量 $$(Normal Vector)$$ 是 $$v=(a, b, c)$$，设从平面上任意一点 $$(x, y, z)$$ 到 $$(x_0, y_0, z_0)$$ 的向量为 $$w$$，
那么通过内积 $$dot\_product(w, v)$$ 算出 $$w$$ 到 $$v$$ 的投影向量 $$p$$，其大小就是 $$(x_0, y_0, z_0)$$ 到平面 $$a*x + b*y + c*z + d = 0$$ 的垂直距离。
这里用到了向量模型的基本概念：法向量，投影向量，内积，整个问题解决过程简洁明快。


## 最小二乘法

<https://www.bilibili.com/video/BV15zPBevERL/>

* 几何角度：向量空间中的投影
* 统计角度：参数估计与最优性
* 分析角度：凸优化的极值问题


## 参考

- [1] [线性代数的本质 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1ys411472E)
- [2] [数学对于程式设计来说重要吗？程式设计大佬眼里的线性代数](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/637653/)
- [3] [数学对于编程来说重要吗？编程眼里的线性代数](https://cloud.tencent.com/developer/news/319028)
- [4] [编程大佬眼中的线性代数，到底是什么样的？](https://www.eet-china.com/mp/a24399.html)
- [5] [编程与线性代数](https://www.sohu.com/a/283978289_701814)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-10-06-math-linear-algebra.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1ys411472E]({% include relrefx.html url="/backup/2020-10-06-math-linear-algebra.md/www.bilibili.com/c113c40a.html" %})
- [https://www.bilibili.com/video/BV15zPBevERL/]({% include relrefx.html url="/backup/2020-10-06-math-linear-algebra.md/www.bilibili.com/bb2719d9.html" %})
- [https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/637653/]({% include relrefx.html url="/backup/2020-10-06-math-linear-algebra.md/codertw.com/12bf289a.html" %})
- [https://cloud.tencent.com/developer/news/319028]({% include relrefx.html url="/backup/2020-10-06-math-linear-algebra.md/cloud.tencent.com/a7a13242.html" %})
- [https://www.eet-china.com/mp/a24399.html]({% include relrefx.html url="/backup/2020-10-06-math-linear-algebra.md/www.eet-china.com/98597c33.html" %})
- [https://www.sohu.com/a/283978289_701814]({% include relrefx.html url="/backup/2020-10-06-math-linear-algebra.md/www.sohu.com/aba00d75.html" %})
