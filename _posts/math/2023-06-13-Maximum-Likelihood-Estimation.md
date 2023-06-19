---
layout: post
title: "机器学习 -- 极大似然估计（MLE，Maximum Likelihood Estimation）"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
cluster: "基础知识点"
---

小学生都能看懂的 **极大似然估计** 。

**极大似然估计（MLE，Maximum Likelihood Estimation）**
就是利用已知的样本结果，反推最有可能（最大概率）导致这样结果的参数值（模型已知，参数未知）。


## 举例说明

利用已知的样本信息，反推一个模型，模型的参数会使得这些样本出现的概率最大。

假设一个箱子里面有蓝色的球和黄色的球（很多），我们现在从箱子里面取 5 个球，结果是：蓝色、蓝色、黄色、蓝色、黄色。
然后询问，这个箱子里面蓝色球和黄色球的比例是多少？

很显然，答案是：$3:2$。


## 极大似然估计方法求解

假设比例是 $p$，那么每次取得蓝色小球的概率是 $p$，黄色小球的概率是 $1-p$。（独立同分布）

$$
x=
\begin{cases}
1, & \text { 蓝球 } \\
0, & \text { 黄球 }
\end{cases}
$$

取球的结果服从 $0-1$ 分布，可记为 $x-B(1,p)$，其概率函数为：

$$
\begin{aligned}
&P(x=1)=P(x=1|p)=p \\
&P(x=0)=P(x=0|p)=1-p
\end{aligned}
$$

对于取出的 5 个球，那么就是：

$$
\begin{aligned}
& P(x=1, x=1, x=0, x=1, x=0 ; p) \\
= & P(x=1) P(x=1) P(x=0) P(x=1) P(x=1) \\
= & p \cdot p \cdot(1-p) \cdot p \cdot(1-p)
\end{aligned}
$$

这个就是似然函数：

$$
\begin{aligned}
L(p) & =p \cdot p \cdot(1-p) \cdot p \cdot(1-p) \\
& =p^3(1-p)^2
\end{aligned}
$$

很明显 $p$ 不同，则 $L(p)$ 的计算结果不一样。
极大似然估计 就是为了求出，使得 $L(p)$ 取值最大的解。


## 求解

求极值，就是求导并令导数为 0。

由于是指数函数，所以两边加 $ln$。
乘法变加法，求导更容易，并且能保持单调性，就能保证最大值的位置不变。

$$
ln(L)=3ln(p)+2ln(1-p) \\
3/p-2/(1-p)=0
$$

所以，可得 $p=3/5$。


## 为什么呢

常用概率分布均是指数分布族，指数分布族可以保证似然是凹函数。
并且是全局严格凹函数（global strictly concave），所以极值点一定是极大值点。


## refs

* [极大似然估计（MLE）、贝叶斯估计、最大后验概率估计（MAP）区别 {% include relref_cnblogs.html %}](https://www.cnblogs.com/eilearn/p/9433911.html)
* [深度学习 — 过拟合问题 {% include relref_cnblogs.html %}](https://www.cnblogs.com/eilearn/p/9203186.html)
* [目标检测 — 评价指标 {% include relref_cnblogs.html %}](https://www.cnblogs.com/eilearn/p/9071440.html)
* [点估计 · 极大似然估计的理论与步骤 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1HU4y127kn/)
* [5 分钟-通俗易懂-极大似然估计 {% include relref_bili.html %}](https://www.bilibili.com/video/BV17K411z7fJ/)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-06-13-Maximum-Likelihood-Estimation.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/eilearn/p/9433911.html]({% include relrefx.html url="/backup/2023-06-13-Maximum-Likelihood-Estimation.md/www.cnblogs.com/e0fff013.html" %})
- [https://www.cnblogs.com/eilearn/p/9203186.html]({% include relrefx.html url="/backup/2023-06-13-Maximum-Likelihood-Estimation.md/www.cnblogs.com/0ee17131.html" %})
- [https://www.cnblogs.com/eilearn/p/9071440.html]({% include relrefx.html url="/backup/2023-06-13-Maximum-Likelihood-Estimation.md/www.cnblogs.com/74c44cb9.html" %})
- [https://www.bilibili.com/video/BV1HU4y127kn/]({% include relrefx.html url="/backup/2023-06-13-Maximum-Likelihood-Estimation.md/www.bilibili.com/3079c78a.html" %})
- [https://www.bilibili.com/video/BV17K411z7fJ/]({% include relrefx.html url="/backup/2023-06-13-Maximum-Likelihood-Estimation.md/www.bilibili.com/d30163ed.html" %})
