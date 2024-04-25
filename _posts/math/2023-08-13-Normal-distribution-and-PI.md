---
layout: post
title: "人工智能 -- 正态分布中为什么有 π？"
author:
location: "珠海"
categories: ["人工智能"]
tags: ["人工智能"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "草履虫"
---

美国诺贝尔物理学奖得主费曼 (Feymann) 每次看到一个有的数学公式的时候，就会问：圆在哪里？这个推导中使用到了，也就是告诉我们正态分布密度公式中有个，其根源来在于二维正态分布中的等高线恰好是个圆。

[3Blue1Brown 为什么正态分布里会有一个 π？（不止是积分技巧） {% include relref_bili.html %}](https://www.bilibili.com/video/BV1wu411W7uU/)
Why π is in the normal distribution (beyond integral tricks)
感觉 e 和 pi 的大量出现并不是巧合，而是人类理解能力的局限性导致的。
人们大量使用强对称性，导致了 pi 的大量出现；
人们大量使用不超过 4 阶的运算（即自增、加法、乘法、指数），导致了 e 的大量出现。

{% include image.html url="/assets/images/230813-normal-distribution-and~5d/6402172626.png" %}


## 第一部分 通过升维进行积分求曲面的体积


## 第二部分 用传统的积分思路再次求一次积分

[为什么正态分布中会有一个 π {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/A9XCDnDI6lZlCoudh-cryg)
[姊妹篇：为什么正态分布中会有一个 e {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/TBNa4xfoIYhgDJKzs-tqwQ)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-08-13-Normal-distribution-and-PI.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1wu411W7uU/]({% include relrefx.html url="/backup/2023-08-13-Normal-distribution-and-PI.md/www.bilibili.com/1395b8cf.html" %})
- [https://mp.weixin.qq.com/s/A9XCDnDI6lZlCoudh-cryg]({% include relrefx.html url="/backup/2023-08-13-Normal-distribution-and-PI.md/mp.weixin.qq.com/b92a3ed9.html" %})
- [https://mp.weixin.qq.com/s/TBNa4xfoIYhgDJKzs-tqwQ]({% include relrefx.html url="/backup/2023-08-13-Normal-distribution-and-PI.md/mp.weixin.qq.com/c9b96a38.html" %})
