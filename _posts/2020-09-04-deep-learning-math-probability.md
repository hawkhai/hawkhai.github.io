---
layout: post
title: "“深度学习”笔记 -- 数学×概率分布（Probability Distribution）"
author:
location: "珠海"
categories: ["深度学习"]
tags: ["深度学习"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
---


## 离散分布

$F(x)$ 表示随机变量 $X\leq x$ 的概率值。如果 $X$ 的取值只有 $x_1 < x_2 < ... < x_n$，则：

$$F_X(x_i)=\sum_{j=1}^iP(x_j)$$

$$\sum_{k=1}^nP(x_i)=1$$


## 正态分布和二项分布

在离散分布中如果试验次数 n 值非常大，而且单次试验的概率 p 值又不是很小的情况下，正态分布可以用来近似的代替二项分布。一个粗略的使用正态分布的近似规则是：$n\cdot p\cdot(1-p)\geq9$。

从二项分布中获得 μ 和 σ 值的方法是

期望值 $\mu=n\cdot p$

标准差 $\sigma=\sqrt{n\cdot p\cdot(1-p)}$


## 参考

<div id="refer-anchor-1"></div>
- [1] [维基百科·概率分布](https://wiki.mbalib.com/wiki/%E6%A6%82%E7%8E%87%E5%88%86%E5%B8%83)

-----

<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>

- [1] [https://wiki.mbalib.com/wiki/%E6%A6%82%E7%8E%87%E5%88%86%E5%B8%83]({% include relref.html url="/backup/2020-09-04-deep-learning-math-probability.md/wiki.mbalib.com/b55ce3d48d28024e23275c167d27b9eb.html" %})
