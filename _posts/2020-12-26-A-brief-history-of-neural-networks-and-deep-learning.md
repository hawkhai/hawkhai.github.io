---
layout: post
title: "深度学习笔记 -- 神经网络和深度学习简史"
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
codeprint:
---


## 从感知机到 BP 算法 (1950s-1980s)


### 线性回归

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-49b2056bce556a9f.webp" %}


### 虚假承诺的荒唐

弗兰克·罗森布拉特 (Frank Rosenblatt) 的感知机 Perceptron。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-b60ac8f45aa04acd.webp" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-2bbcf4426450d0d5.webp" %}

算法如下：

1. 从感知机有随机的权重和一个训练集开始。
2. 对于训练集中一个实例的输入值，计算感知机的输出值。
3. 如若感知机的输出值和实例中默认正确的输出值不同：
    1. 若输出值应该为 0 但实际为 1，减少输入值是 1 的例子的权重。
    2. 若输出值应该为 1 但实际为 0，增加输入值是 1 的例子的权重。
4. 对于训练集中下一个例子做同样的事，重复步骤 2-4 直到感知机不再出错。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-1186dc0019dcad1c.webp" caption="康奈尔航天实验室的 Mark I 感知机，第一台感知机的硬件" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-8ec85f25af21973b.webp" caption="多层输出的神经网络" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-b0d88af8286f3390.webp" %}

感知机局限性的视觉化。找到一个线性函数，输入 X，Y 时可以正确地输出 + 或 -，就是在 2D 图表上画一条从 + 中分离出 - 的线；很显然，就第三幅图显示的情况来看，这是不可能的。


### 人工智能冬天的复苏

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-8a52ea9061ab08cf.webp" caption="有两个隐藏层的神经网络" %}

多个隐藏层是件好事，原因在于隐藏层可以找到数据内在特点，后续层可以在这些特点（而不是嘈杂庞大的原始数据）基础上进行操作。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-29346594822d1d69.webp" caption="传统的特征的手工提取过程的视觉化" %}

我们可以利用微积分将一些导致输出层任何训练集误差的原因分配给前一隐藏层的每个神经元，如果还有另外一层隐藏层，我们可以将这些原因再做分配，以此类推 —— 我们在反向传播这些误差。
典型的随机梯度下降，找出最小化误差的最佳权值。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-2df4f9146fd3f6b8.webp" caption="反向传播的基本思想" %}


## BP 算法之后的又一突破 —— 信念网络 (1980s-2000s)


### 神经网络获得视觉

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-c23cd3e0638a4a79.webp" caption="一个神经网络工作原理的可视化过程" %}

多加了这两层 —— （卷积层和汇集层） —— 是卷积神经网络（CNNs/ConvNets）和普通旧神经网络的主要区别。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-24e4c608f0bd9a3d.webp" caption="卷积神经网络（CNN）的操作过程" %}


### 神经网络进入无监督学习时期

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-fe8ce0619ea7212f.webp" caption="自编码神经网络" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-66dfa1ff54744574.webp" caption="更明确地了解自编码压缩" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-4d3633f89c7f2fda.webp" caption="聚类，一种很常用的非监督式学习应用" %}


## 90 年代的兴衰 —— 强化学习与递归神经网络 (2000s-2010s)


## 深度学习终迎伟大复兴


## 参考

- [1] [深度｜神经网络和深度学习简史（第一部分）：从感知机到 BP 算法 {% include relref_jianshu.html %}](https://www.jianshu.com/p/f90d923b73b5)
- [2] [深度｜神经网络和深度学习简史（第二部分）：BP 算法之后的又一突破 —— 信念网络 {% include relref_jianshu.html %}](https://www.jianshu.com/p/9dc4c2320732)
- [3] [深度｜神经网络和深度学习简史（第三部分）：90 年代的兴衰 —— 强化学习与递归神经网络 {% include relref_jianshu.html %}](https://www.jianshu.com/p/5db8170d4bcb)
- [4] [深度｜神经网络和深度学习简史第四部分：深度学习终迎伟大复兴 {% include relref_jianshu.html %}](https://www.jianshu.com/p/e1bac195f06d)
- [5] <http://www.360doc.com/content/17/1207/08/1609415_710706921.shtml>
- [6] <https://www.skynettoday.com/overviews/neural-net-history>

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://www.jianshu.com/p/f90d923b73b5]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.jianshu.com/041824b2.html" %})
- [2] [https://www.jianshu.com/p/9dc4c2320732]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.jianshu.com/b7378314.html" %})
- [3] [https://www.jianshu.com/p/5db8170d4bcb]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.jianshu.com/4ca64f65.html" %})
- [4] [https://www.jianshu.com/p/e1bac195f06d]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.jianshu.com/f80ec7b0.html" %})
- [5] [http://www.360doc.com/content/17/1207/08/1609415_710706921.shtml]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.360doc.com/68c30233.shtml" %})
- [6] [https://www.skynettoday.com/overviews/neural-net-history]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.skynettoday.com/3fb22ab6.html" %})
