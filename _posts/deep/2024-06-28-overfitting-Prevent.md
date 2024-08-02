---
layout: post
title: "机器学习 -- 防止模型过拟合（overfitting）！"
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
---

其实正则化的本质很简单，就是对某一问题加以先验的限制或约束以达到某种特定目的的一种手段或操作。
在算法中使用正则化的目的是防止模型出现过拟合。
一提到正则化，很多同学可能马上会想到常用的 L1 范数和 L2 范数，在汇总之前，我们先看下 LP 范数是什么？


## LP 范数

范数简单可以理解为用来表征向量空间中的距离，而距离的定义很抽象，只要满足 **非负、自反、三角不等式** 就可以称之为距离。
LP 范数不是一个范数，而是一组范数，其定义如下：

{% include image.html url="/assets/images/240628-overfitting-prevent/6401.png" %}

$p$ 的范围是 $\[1,∞)$。p 在 $(0,1)$ 范围内定义的并不是范数，因为违反了三角不等式。
根据 $p$ 的变化，范数也有着不同的变化，借用一个经典的有关 P 范数的变化图如下：

{% include image.html url="/assets/images/240628-overfitting-prevent/6402.jfif" %}

上图表示了 p 从 0 到正无穷变化时，单位球（unit ball）的变化情况。在 P 范数下定义的单位球都是凸集，但是当 0<p<1 时，在该定义下的 unit ball 并不是凸集（这个我们之前提到，当 0<p<1 时并不是范数）。
那问题来了，L0 范数是啥玩意？
L0 范数表示向量中非零元素的个数，用公式表示如下：

{% include image.html url="/assets/images/240628-overfitting-prevent/6403.png" %}

我们可以通过最小化 L0 范数，来寻找最少最优的稀疏特征项。但不幸的是，L0 范数的最优化问题是一个 NP hard 问题（L0 范数同样是非凸的）。因此，在实际应用中我们经常对 L0 进行凸松弛，理论上有证明，L1 范数是 L0 范数的最优凸近似，因此通常使用 L1 范数来代替直接优化 L0 范数。


## L1 范数

根据 LP 范数的定义我们可以很轻松的得到 L1 范数的数学形式：

{% include image.html url="/assets/images/240628-overfitting-prevent/6404.png" %}

通过上式可以看到，L1 范数就是向量各元素的绝对值之和，也被称为是 "稀疏规则算子 "（Lasso regularization）。那么问题来了，为什么我们希望稀疏化？稀疏化有很多好处，最直接的两个：
* 特征选择
* 可解释性


## L2 范数

L2 范数是最熟悉的，它就是欧几里得距离，公式如下：

{% include image.html url="/assets/images/240628-overfitting-prevent/6405.png" %}

L2 范数有很多名称，有人把它的回归叫“岭回归”（Ridge Regression），也有人叫它“权值衰减”（Weight Decay）。
以 L2 范数作为正则项可以得到稠密解，即每个特征对应的参数 $w$ 都很小，接近于 0 但是不为 0；
此外，L2 范数作为正则化项，可以防止模型为了迎合训练集而过于复杂造成过拟合的情况，从而提高模型的泛化能力。


## L1 范数和 L2 范数的区别

引入 PRML 一个经典的图来说明下 L1 和 L2 范数的区别，如下图所示：

{% include image.html url="/assets/images/240628-overfitting-prevent/6406.jfif" %}

如上图所示，蓝色的圆圈表示问题可能的解范围，橘色的表示正则项可能的解范围。而整个目标函数（原问题 + 正则项）有解当且仅当两个解范围相切。从上图可以很容易地看出，由于 L2 范数解范围是圆，所以相切的点有很大可能不在坐标轴上，而由于 L1 范数是菱形（顶点是凸出来的），其相切的点更可能在坐标轴上，而坐标轴上的点有一个特点，其只有一个坐标分量不为零，其他坐标分量为零，即是稀疏的。所以有如下结论，L1 范数可以导致稀疏解，L2 范数导致稠密解。

从贝叶斯先验的角度看，当训练一个模型时，仅依靠当前的训练数据集是不够的，为了实现更好的泛化能力，往往需要加入先验项，而加入正则项相当于加入了一种先验。
* L1 范数相当于加入了一个 Laplacean 先验；
* L2 范数相当于加入了一个 Gaussian 先验。

如下图所示：

{% include image.html url="/assets/images/240628-overfitting-prevent/6407.jfif" %}


## Dropout

Dropout 是深度学习中经常采用的一种正则化方法。它的做法可以简单的理解为在 DNNs 训练的过程中以概率 $p$ 丢弃部分神经元，即使得被丢弃的神经元输出为 0。Dropout 可以实例化的表示为下图：

{% include image.html url="/assets/images/240628-overfitting-prevent/6408.jfif" %}

我们可以从两个方面去直观地理解 Dropout 的正则化效果：
* 在 Dropout 每一轮训练过程中随机丢失神经元的操作相当于多个 DNNs 进行取平均，因此用于预测时具有 vote 的效果。

* 减少神经元之间复杂的共适应性。当隐藏层神经元被随机删除之后，使得全连接网络具有了一定的稀疏化，从而有效地减轻了不同特征的协同效应。也就是说，有些特征可能会依赖于固定关系的隐含节点的共同作用，而通过 Dropout 的话，就有效地组织了某些特征在其他特征存在下才有效果的情况，增加了神经网络的鲁棒性。


## Batch Normalization

批规范化（Batch Normalization）严格意义上讲属于归一化手段，主要用于加速网络的收敛，但也具有一定程度的正则化效果。

这里借鉴下魏秀参博士的知乎回答中对 covariate shift 的解释（[link {% include relref_zhihu.html %}](https://www.zhihu.com/question/38102762)）。

注以下内容引自魏秀参博士的知乎回答：

大家都知道在统计机器学习中的一个经典假设是“源空间（source domain）和目标空间（target domain）的数据分布（distribution）是一致的”。如果不一致，那么就出现了新的机器学习问题，如 transfer learning/domain adaptation 等。而 covariate shift 就是分布不一致假设之下的一个分支问题，它是指源空间和目标空间的条件概率是一致的，但是其边缘概率不同。大家细想便会发现，的确，对于神经网络的各层输出，由于它们经过了层内操作作用，其分布显然与各层对应的输入信号分布不同，而且差异会随着网络深度增大而增大，可是它们所能“指示”的样本标记（label）仍然是不变的，这便符合了 covariate shift 的定义。

BN 的基本思想其实相当直观，因为神经网络在做非线性变换前的激活输入值（X=WU+B，U 是输入）随着网络深度加深，其分布逐渐发生偏移或者变动（即上述的 covariate shift）。之所以训练收敛慢，一般是整体分布逐渐往非线性函数的取值区间的上下限两端靠近（对于 Sigmoid 函数来说，意味着激活输入值 X=WU+B 是大的负值或正值），所以这导致后向传播时低层神经网络的梯度消失，这是训练深层神经网络收敛越来越慢的本质原因。而 BN 就是通过一定的规范化手段，把每层神经网络任意神经元这个输入值的分布强行拉回到均值为 0 方差为 1 的标准正态分布，避免因为激活函数导致的梯度弥散问题。所以与其说 BN 的作用是缓解 covariate shift，倒不如说 BN 可缓解梯度弥散问题。


## 归一化、标准化 & 正则化

正则化我们以及提到过了，这里简单提一下归一化和标准化。

归一化（Normalization）：归一化的目标是找到某种映射关系，将原数据映射到 $[a,b]$ 区间上。一般 $a,b$ 会取 $[−1,1],[0,1]$ 这些组合。

一般有两种应用场景：
* 把数变为 (0, 1) 之间的小数。
* 把有量纲的数转化为无量纲的数。

常用 min-max normalization：
{% include image.html url="/assets/images/240628-overfitting-prevent/6409.png" %}

标准化（Standardization）：用大数定理将数据转化为一个标准正态分布，标准化公式为：

{% include image.html url="/assets/images/240628-overfitting-prevent/64010.png" %}


## 归一化和标准化的区别：

我们可以这样简单地解释：

归一化的缩放是“拍扁”统一到区间（仅由极值决定），而标准化的缩放是更加“弹性”和“动态”的，和整体样本的分布有很大的关系。

值得注意：
* 归一化：缩放仅仅跟最大、最小值的差别有关。
* 标准化：缩放和每个点都有关系，通过方差（variance）体现出来。与归一化对比，标准化中所有数据点都有贡献（通过均值和标准差造成影响）。


## 为什么要标准化和归一化？

提升模型精度：归一化后，不同维度之间的特征在数值上有一定比较性，可以大大提高分类器的准确性。

加速模型收敛：标准化后，最优解的寻优过程明显会变得平缓，更容易正确的收敛到最优解。如下图所示：

{% include image.html url="/assets/images/240628-overfitting-prevent/764050-20180630165521390-1050850446.png" %}
{% include image.html url="/assets/images/240628-overfitting-prevent/64011.png" %}


## Reference

* 参考链接：<http://www.cnblogs.com/maybe2030/>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-06-28-overfitting-Prevent.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.zhihu.com/question/38102762]({% include relrefx.html url="/backup/2024-06-28-overfitting-Prevent.md/www.zhihu.com/cd798378.html" %})
- [http://www.cnblogs.com/maybe2030/]({% include relrefx.html url="/backup/2024-06-28-overfitting-Prevent.md/www.cnblogs.com/1e7ae9f9.html" %})
