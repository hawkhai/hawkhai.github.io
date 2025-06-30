---
layout: post
title: "机器学习笔记 -- 3Blue1Brown 深度学习 Deep Learning（已完成）"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
kaliyun: true
cluster: "机器学习课程"
---

**深度学习 Deep Learning**
<https://space.bilibili.com/88461692/channel/seriesdetail?sid=1528929>
<https://www.3blue1brown.com/topics/neural-networks>


## 深度学习之神经网络的结构 Part 1 ver 2.0

<https://www.bilibili.com/video/BV1bx411M7Zx/>

But what is a Neural Network?
An overview of what a neural network is, introduced in the context of recognizing hand-written digits.
Chapter 1 2017 年 10 月 5 日


## 深度学习之梯度下降法 Part 2 ver 0.9 beta

<https://www.bilibili.com/video/BV1Ux411j7ri/>

Gradient descent, how neural networks learn
An overview of gradient descent in the context of neural networks.
This is a method used widely throughout machine learning for optimizing how a computer performs on certain tasks.
Chapter 2 2017 年 10 月 16 日

Analyzing our neural network
Chapter 3 2017 年 10 月 16 日


## 深度学习之反向传播算法 上 / 下 Part 3 ver 0.9 beta

<https://www.bilibili.com/video/BV16x411V7Qg/>

What is backpropagation really doing?
An overview of backpropagation, the algorithm behind how neural networks learn.
Chapter 4 2017 年 11 月 3 日

Backpropagation calculus
The math of backpropagation, the algorithm by which neural networks learn.
Chapter 5 2017 年 11 月 3 日

{% include image.html url="/assets/images/240629-artificial-intelligence~82/20240629130059.png" %}


## GPT 是什么？直观解释 Transformer \| 深度学习第 5 章

<https://www.bilibili.com/video/BV13z421U7cs/>
* Embedding
* Key
* Query
* Value
* Output
* Up-projection
* Down-projection
* Unembedding

GPT 的第一层：词嵌入为向量（embedding）
嵌入空间不仅代表词，还能包含上下文信息
GPT 的最后一层：向量解码为词（Unembedding）
带温度的 Softmax 函数

But what is a GPT? Visual intro to Transformers | Deep learning, chapter 5
A visual introduction to transformers. This chapter focusses on the overall structure, and word embeddings
2024 年 4 月 1 日


## 直观解释注意力机制，Transformer 的核心 \| 深度学习第 6 章

<https://www.bilibili.com/video/BV1TZ421j7Ke/>

朴素的理解两个词的注意力可能会理解为计算是两个词嵌入的直接的相似度，
但是其实是计算两个词分别在 QK 空间上的投影的相似度，因为如果不这么做，那么两个一样的词永远最相似。

因此 QK 两个矩阵其实表征了两个空间。即：查询空间 Q 和被查空间 K，
Q 用来映射每一个词 x 的方向，K 用来映射其他每个词的方向，一旦两个空间的映射结果一致则表示两个词匹配。

想真正弄清楚 Transformer 内部的大网络在做什么，推荐 Anthropic 的网页博文：
<https://transformer-circuits.pub/2021/framework/index.html>
我就是读了他的一篇文章后开始想，输出矩阵乘以值矩阵，其实就是嵌入空间到自身的一个低秩映射。
这样想之后，至少我的概念变得更清晰了。

Visualizing Attention, a Transformer's Heart | Chapter 6, Deep Learning
Demystifying attention, the key mechanism inside transformers and LLMs.
2024 年 4 月 7 日
© 2024 Grant Sanderson


## 何恺明 MIT 第一课 - 卷积神经网络

<https://www.bilibili.com/video/BV1sW421c7SK/>

{% include image.html url="/assets/images/240629-artificial-intelligence~82/20240629214909.png" %}

{% include image.html url="/assets/images/240629-artificial-intelligence~82/20240629221908.png" caption="every node can see every other node" %}

2017 Transformer 提出，截至到 2020 年的 ViT（Vision Transformer），最近 4 年都没有新的革命范式提出了，感觉图片中可能链接的都链接完了。

* GPT
* AlphaFold
* ViT


## Towards End-to-End Generative Modeling（走向端到端生成建模）

{% include image.html url="/assets/images/240629-artificial-intelligence~82/20250630154012.png" %}

Flow Matching



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-06-29-artificial-intelligence-3Blue1Brown.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://space.bilibili.com/88461692/channel/seriesdetail?sid=1528929]({% include relrefx.html url="/backup/2024-06-29-artificial-intelligence-3Blue1Brown.md/space.bilibili.com/02f3a0e4.html" %})
- [https://www.3blue1brown.com/topics/neural-networks]({% include relrefx.html url="/backup/2024-06-29-artificial-intelligence-3Blue1Brown.md/www.3blue1brown.com/8084f983.html" %})
- [https://www.bilibili.com/video/BV1bx411M7Zx/]({% include relrefx.html url="/backup/2024-06-29-artificial-intelligence-3Blue1Brown.md/www.bilibili.com/ddd13a59.html" %})
- [https://www.bilibili.com/video/BV1Ux411j7ri/]({% include relrefx.html url="/backup/2024-06-29-artificial-intelligence-3Blue1Brown.md/www.bilibili.com/4d897066.html" %})
- [https://www.bilibili.com/video/BV16x411V7Qg/]({% include relrefx.html url="/backup/2024-06-29-artificial-intelligence-3Blue1Brown.md/www.bilibili.com/a7bc9edf.html" %})
- [https://www.bilibili.com/video/BV13z421U7cs/]({% include relrefx.html url="/backup/2024-06-29-artificial-intelligence-3Blue1Brown.md/www.bilibili.com/590693b1.html" %})
- [https://www.bilibili.com/video/BV1TZ421j7Ke/]({% include relrefx.html url="/backup/2024-06-29-artificial-intelligence-3Blue1Brown.md/www.bilibili.com/c13fe51c.html" %})
- [https://transformer-circuits.pub/2021/framework/index.html]({% include relrefx.html url="/backup/2024-06-29-artificial-intelligence-3Blue1Brown.md/transformer-circuits.pub/7ca73ab6.html" %})
- [https://www.bilibili.com/video/BV1sW421c7SK/]({% include relrefx.html url="/backup/2024-06-29-artificial-intelligence-3Blue1Brown.md/www.bilibili.com/434313c5.html" %})
