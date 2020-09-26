---
layout: post
title: "“数字图像处理”笔记 -- 傅里叶变换"
location: "珠海"
categories: ["图像处理"]
tags: [图像处理]
mathjax: true
toc: true
mermaid: true
---


## 数学推导 傅里叶级数与傅里叶变换

傅里叶分析之掐死教程 <https://zhuanlan.zhihu.com/p/19763358>

{% include image.html url="/images/fourier-transform/40cf849e55ed95732a60b52d4019d609_r.jpg" %}

Part1. 三角函数的正交性 <https://www.bilibili.com/video/BV1Et411R78v>

Part2. 周期为 $2\varPi$ 的函数展开 <https://www.bilibili.com/video/BV17t411d7hm>

Part3. 周期为 $2L$ 的函数展开 <https://www.bilibili.com/video/BV1wb411K7Kp>

Part4. 傅里叶级数的复数形式 <https://www.bilibili.com/video/BV13b411P7mU>

Part5. 从傅里叶级数推导傅里叶变换 <https://www.bilibili.com/video/BV1jt411U7Bp>

Part6. 总结与闲话 <https://www.bilibili.com/video/BV1St41117fH>


### 复数的物理意义是什么？

<https://www.zhihu.com/question/23234701/answer/26017000>

转载文章：<https://blog.csdn.net/Ciellee/article/details/108304531>

我们脑袋瓜不太好，看不到世界的真相。高维空间我们也感知不到，只能通过投射到三维，甚至二维，直观感受其投影。
数学是我们最有力的分析工具。事情直接处理很难，升维或者变维后却变的很简单，处理完后再变换回去，搞定。

三维到二维的投影。

{% include image.html url="/images/fourier-transform/20200901103813238.png" %}


## 参考

- [1] [bilibili](https://space.bilibili.com/230105574/channel/detail?cid=67768)
- [2] [课程目录](https://www.cnblogs.com/-wenli/p/11744405.html)
