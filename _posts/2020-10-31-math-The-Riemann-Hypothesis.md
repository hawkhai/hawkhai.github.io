---
layout: post
title: "数学之美 -- 黎曼猜想"
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
---

> 数学中的皇冠 —— 数论 —— 2000 年来一直没有任何实际应用，是最纯粹的数学。直到计算机，尤其是现代密码学的出现，才让数论第一次走出数学，走进了人们的生活中。

如果真的有神的话，那么数学就是神的语言。**心事浩茫连广宇，于无声处听惊雷。**

大概讲的是，一个牛逼的函数，对于任意输入数字 x，可以直接算出小于 x 的所有质数个数。

黎曼素数计数函数：

$$J(x)=Li(x)-\sum_{\rho}Li(x^{\rho})-\ln 2 +\int_x^\infty\frac{dt}{t(t^2-1)\ln t}$$

当代入的非平凡零点越多，越准确。

{% include image.html url="/images/math-riemann/zk.gif" %}

而黎曼猜想说的是，这些非平凡零点的所有实部都是 1/2。

严伯钧说：能完全理解黎曼猜想，至少是一个数学专业的博士生水平。一切的起点：欧拉乘积公式，对于全体质数的某种运算，可以转移成对于全体自然数的某种运算。

[黎曼猜想，及其解释（上） {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/25055731)

[黎曼猜想，及其解释（下） {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/25222934)


## 马同学

[黎曼猜想到底是什么意思？](https://www.matongxue.com/madocs/2101)

[黎曼猜想（Riemann hypothesis）是什么？有什么用？ {% include relref_zhihu.html %}](https://www.zhihu.com/question/295619713)


## 李永乐老师

* [1+2+3+4+...=-1/12？李永乐老师讲黎曼猜想（1） {% include relref_bili.html %}](https://www.bilibili.com/video/BV1MW411S7Tg)

    欧拉级数 解析延拓

* [质数有多重要？数学家欧拉和高斯是如何研究质数的？李永乐老师讲黎曼猜想（2） {% include relref_bili.html %}](https://www.bilibili.com/video/BV1HW411S77f)

* [悬赏 100 万美元的“黎曼猜想”有多难？李永乐老师讲什么是黎曼猜想（3） {% include relref_bili.html %}](https://www.bilibili.com/video/BV1rW411m7GL)

    **复数到复数的函数，四维空间才可以表示出来。**


## 科技袁人

* [黎曼猜想合集-总有一天，人类会骄傲地发出这串数字：2,3,5,7,11…… {% include relref_bili.html %}](https://www.bilibili.com/video/BV1vt411b72q)

    质数的分布函数

* [黎曼猜想合集-总有一天，人类会骄傲地发出这串数字：2,3,5,7,11…… {% include relref_bili.html %}](https://www.bilibili.com/video/BV1vt411b72q?p=2)

    论小于给定数值的质数个数

    质数定理


## 袁岚峰

* [理解黎曼猜想（一）背景 \| 袁岚峰 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/47346148)
* [理解黎曼猜想（二）两个自然数互质的概率是多少？ \| 袁岚峰 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/47978393)
* [理解黎曼猜想（三）你真的相信全体自然数的和等于 -1/12 吗？ \| 袁岚峰 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/48750070)
* [理解黎曼猜想（四）得救之道，就在其中 \| 袁岚峰 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/49454034)
* [理解黎曼猜想（五）宇宙的密码 \| 袁岚峰 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/50421799)
* [理解黎曼猜想（六）朝闻道 \| 袁岚峰 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/51566599)


## 3Blue1Brown

[【官方双语】黎曼 ζ 函数与解析延拓的可视化 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1tx411y7VG)


## CSDN 其它文章

* [黎曼猜想（一）欧拉乘积式](https://blog.csdn.net/fztsilly/article/details/106525876)
* [黎曼猜想（二）全体自然数之和等于 -1/12 和解析延拓](https://blog.csdn.net/fztsilly/article/details/106549849)
* [黎曼猜想（三）黎曼猜想](https://blog.csdn.net/fztsilly/article/details/106548223)
* [《终结篇》全体自然数的和等于 -1/12??? 我觉得我还可以再抢救一下](https://blog.csdn.net/qq_40155097/article/details/86670230)


## 实际应用

和密码学关系重大。
