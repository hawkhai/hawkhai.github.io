---
layout: post
title: "MATHEMATICS -- 生成模型数学 —— 概率论基础"
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


## 信息熵

描述信息源各可能事件发生的不确定性。

$$
H(X)=-\sum_{i=1}^n P\left(x_i\right) \log _2 P\left(x_i\right)
$$

信息量是对某个已经发生的事件而计算的，当我们设定的是某一个随机变量，其包含所有事件发生的可能，那么信息熵的定义就是，这些事件，在概率发生的情况下，带来的平均信息量。

$$
H(X)=-\sum_{i=1}^n P\left(x_i\right) \log _2 P\left(x_i\right)=-\mathbb{E}\left[\log _2 P(X)\right]
$$


## KL 散度（相对熵）

一种用于衡量两个概率分布之间的差异的指标。

$$
K L(q \| p)=\sum q(x) \log \frac{q(x)}{p(x)}=\int q(x) \log \frac{q(x)}{p(x)} d x
$$

其表示的是概率分布 $q$ 跟概率分布 $p$ 的相似性。

我们把 KL 散度的公式转化一下，

$$
\begin{aligned}
K L(q \| p) & =\sum q(x) \log \frac{q(x)}{p(x)} \\
& =\sum q(x)[\log q(x)-\log p(x)]
\end{aligned}
$$

我们可以发现这个公式跟信息熵的公式相当之像，
如果从信息熵的角度去看的话（$\log$ 底数取 $2$），其就可以表达成两个概率分布的信息熵的差值。

性质：非负性，$K L(q \|\| p) \geq 0$。等于 $0$ 时表示两个概率分布相等。

性质：非对称性，$K L(q \|\| p) \neq K L(p \|\| q)$。


## 变分自动编码器和变分贝叶斯方法

[Kullback-Leibler(KL) 散度介绍 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/100676922)
<https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained>

在最一般的意义上，神经网络是函数近似器。这意味着你可以使用神经网络来学习各种复杂的功能。使神经网络学习的关键是使用目标函数，该函数可以告知网络运行状况。你可以通过最小化目标函数的损失来训练神经网络。

我们可以使用 KL 散度来最小化近似分布时的信息损失量。将 KL 散度与神经网络相结合，可以让我们学习非常复杂的数据近似分布。一种常见的解决方法称为“变分自编码器”，它学习了近似数据集中信息的最佳方法。

更一般的是变分贝叶斯方法领域。
蒙特卡洛模拟可以有效解决一系列概率问题。尽管蒙特卡洛模拟可以帮助解决贝叶斯推理所需的许多难解积分，但即使这些方法在计算上也非常昂贵。包括变分自动编码器在内的变分贝叶斯方法使用 KL 散度来生成最佳近似分布，从而可以对非常困难的积分进行更有效的推断。


## Refs

* <https://blog.csdn.net/sdksdf/article/details/138322038>
* <https://www.bilibili.com/video/BV1Hw4m117Ka/>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-09-27-Probability-Theory-Review.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://zhuanlan.zhihu.com/p/100676922]({% include relrefx.html url="/backup/2024-09-27-Probability-Theory-Review.md/zhuanlan.zhihu.com/7d705530.html" %})
- [https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained]({% include relrefx.html url="/backup/2024-09-27-Probability-Theory-Review.md/www.countbayesie.com/d077bc2b.html" %})
- [https://blog.csdn.net/sdksdf/article/details/138322038]({% include relrefx.html url="/backup/2024-09-27-Probability-Theory-Review.md/blog.csdn.net/bf4201a9.html" %})
- [https://www.bilibili.com/video/BV1Hw4m117Ka/]({% include relrefx.html url="/backup/2024-09-27-Probability-Theory-Review.md/www.bilibili.com/9d6cf4b5.html" %})