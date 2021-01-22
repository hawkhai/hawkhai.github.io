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

Andrey Kurenkov

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/failures.png" %}


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

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-398f4d3580c1a683.webp" caption="自组织映射神经网络" %}

自组织映射神经网络：将输入的一个大向量映射到一个神经输出的网格中，在其中，每个输出都是一个聚类。相邻的神经元表示同样的聚类。


### 神经网络迎来信念网络

玻尔兹曼机器就是类似神经网络的网络，并有着和感知器（Perceptrons）非常相似的单元，但该机器并不是根据输入和权重来计算输出，在给定相连单元值和权重的情况下，网络中的每个单元都能计算出自身概率，取得值为 1 或 0。
因此，这些单元都是随机的 —— 它们依循的是概率分布而非一种已知的决定性方式。
玻尔兹曼部分和概率分布有关，它需要考虑系统中粒子的状态，这些状态本身基于粒子的能量和系统本身的热力学温度。
这一分布不仅决定了玻尔兹曼机器的数学方法，也决定了其推理方法 —— 网络中的单元本身拥有能量和状况，学习是由最小化系统能量和热力学直接刺激完成的。
虽然不太直观，但这种基于能量的推理演绎实际上恰是一种基于能量的模型实例，并能够适用于基于能量的学习理论框架，而很多学习算法都能用这样的框架进行表述。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-c8de5df311b235b7.webp" caption="一个简单的信念网络" %}

一个简单的信念，或者说贝叶斯网络 —— 玻尔兹曼机器基本上就是如此，但有着非直接 / 对称联系和可训练式权重，能够学习特定模式下的概率。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-d987d7aca07b0579.webp" caption="玻尔兹曼机器实例" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-25de789aee57ee80.webp" caption="An explanation of belief nets" %}


## 90 年代的兴衰 —— 强化学习与递归神经网络 (2000s-2010s)

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-b5dd96d6bbcb1bd9.webp" caption="强化学习" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-4fbb0ee4d4a611f6.webp" caption="双摆控制问题" %}

双摆控制问题 —— 单摆问题进阶版本，是一个经典的控制和强化学习任务。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-2d0584dfda47216e.webp" caption="西洋双陆棋游戏中，掌握专家级别水平的神经网络" %}


### 神经网络变得呆头呆脑

要解决理解语音的问题，研究人员试图修改神经网络来处理一系列输入（就像语音中的那样）而不是批量输入（像图片中那样）。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-a7db517568c2e635.webp" caption="时延神经网络" %}

将神经元回路接回神经网络，赋予神经网络记忆就被优雅地解决了。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-55be164812717615.webp" caption="递归神经网络图。还记得之前的玻尔兹曼机吗？大吃一惊吧！那些是递归性神经网络。" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-beefa436cd189c44.webp" caption="通过时间概念反向传播的直观图解" %}


### 新的冬日黎明

用它们来工作是十分麻烦的 —— 电脑不够快、算法不够聪明，人们不开心。


## 深度学习终迎伟大复兴

试问机器学习领域的任何一人，是什么让神经网络研究进行下来，对方很可能提及这几个名字中的一个或全部：Geoffrey Hinton，加拿大同事 Yoshua Bengio 以及脸书和纽约大学的 Yann LeCun。


### 深度学习的密谋

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-4d6b2da090e95ad2.webp" caption="受限的玻尔兹曼机器" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-319fedf1a3c8fbe3.webp" caption="Hinton 引入的层式预训练" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-9197a5a2839b4498.webp" caption="关于非监督式预训练的另一种看法，利用自动代码取代 RBM" %}


### 蛮力的重要性

大型训练数据集与快速腭化计算的蛮力方法是一个关键。

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-3b81b0bae7b4864c.webp" caption="谷歌最著名的神经网络学习猫。这是输入到一个神经元中最佳的一张" %}


### 深度学习的上升

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-540672fd868ac270.webp" caption="不同的激活函数。ReLU 是修正线性单元" %}

深度学习 = 许多训练数据 + 并行计算 + 规模化、灵巧的的算法

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-088afe4fb9bd4415.webp" %}

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/1496926-8d610fda7cec0db6.webp" %}


### 后记：现状

{% include image.html url="/assets/images/201226-a-brief-history-of-neur~fe/118309788_31_2017120708490293.jpg" caption="LTSM RNNs 的死灰复燃以及分布式表征的代表" %}


## 参考

- [1] [深度｜神经网络和深度学习简史（第一部分）：从感知机到 BP 算法 {% include relref_jianshu.html %}](https://www.jianshu.com/p/f90d923b73b5)
- [2] [深度｜神经网络和深度学习简史（第二部分）：BP 算法之后的又一突破 —— 信念网络 {% include relref_jianshu.html %}](https://www.jianshu.com/p/9dc4c2320732)
- [3] [深度｜神经网络和深度学习简史（第三部分）：90 年代的兴衰 —— 强化学习与递归神经网络 {% include relref_jianshu.html %}](https://www.jianshu.com/p/5db8170d4bcb)
- [4] [深度｜神经网络和深度学习简史（第四部分）：深度学习终迎伟大复兴 {% include relref_jianshu.html %}](https://www.jianshu.com/p/e1bac195f06d)
- [5] <http://www.360doc.com/content/17/1207/08/1609415_710706921.shtml>
- [6] <https://www.skynettoday.com/overviews/neural-net-history>
- [7] <https://www.andreykurenkov.com/writing/life/lessons-learned-from-failures/>

-----
<p class='reviewtip'>2021-01-22: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.jianshu.com/p/f90d923b73b5]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.jianshu.com/041824b2.html" %})
- [https://www.jianshu.com/p/9dc4c2320732]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.jianshu.com/b7378314.html" %})
- [https://www.jianshu.com/p/5db8170d4bcb]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.jianshu.com/4ca64f65.html" %})
- [https://www.jianshu.com/p/e1bac195f06d]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.jianshu.com/f80ec7b0.html" %})
- [http://www.360doc.com/content/17/1207/08/1609415_710706921.shtml]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.360doc.com/68c30233.shtml" %})
- [https://www.skynettoday.com/overviews/neural-net-history]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.skynettoday.com/3fb22ab6.html" %})
- [https://www.andreykurenkov.com/writing/life/lessons-learned-from-failures/]({% include relref.html url="/backup/2020-12-26-A-brief-history-of-neural-networks-and-deep-learning.md/www.andreykurenkov.com/8920000a.html" %})
