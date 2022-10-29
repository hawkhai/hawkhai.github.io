---
layout: post
title: "机器学习笔记 -- 人工智能领域的 10+ 大算法"
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

[神经网络*内部*发生了什么？ {% include relref_bili.html %}](https://www.bilibili.com/video/BV1s3411y7WN/)
{% include image.html url="/assets/images/221013-artificial-intelligence/20221016220307.png" %}

> 该看：8-1

* 机器学习：给定数据的预测问题。

* 监督学习：又标签，对于属于数据 X，预测 Y。
    * 分类：标签不连续。
    * 回归：标签连续。
    * K 近邻
    * SVM
    * 决策树
    * 朴素贝叶斯
    * 逻辑回归
    * XGBoost
    * Lightgbm
* 无监督学习：无标签，对于数据数据 X，能发现什么。
    * 聚类
    * 降维算法
    * EM 算法
* 强化学习：序列决策问题。
    * 马尔科夫决策方法（扫地机器人寻路）

[基本的机器学习算法 {% include relref_csdn.html %}](https://blog.csdn.net/qq_39783601/article/details/123365469)：
1. 线性回归算法 Linear Regression
2. 支持向量机算法 (Support Vector Machine, SVM)
3. 最近邻居 / k-近邻算法 (K-Nearest Neighbors, KNN)
4. 逻辑回归算法 Logistic Regression
5. 决策树算法 Decision Tree
6. k-平均算法 K-Means
7. 随机森林算法 Random Forest
8. 朴素贝叶斯算法 Naive Bayes
9. 降维算法 Dimensional Reduction
10. 梯度增强算法 Gradient Boosting

Boosting 和 AdaBoost
Boosting 是一种集成技术，它试图从多个弱分类器中创建一个强分类器。
妈妈卡号 邮政 2080


## 基础知识


### 超参数（Hyperparameter）

机器学习算法中的调优参数（tuning parameters），需要人为设定，称为超参数（Hyperparameter）。比如，正则化系数 λ，决策树模型中树的深度。

迭代次数 epoch，k 近邻法（kNN）中的 k（最相近的点的个数），决策树模型中树的深度等等都属于超参数。
梯度下降法中的学习速率 α，迭代次数 epoch，批量大小 batch-size，k 近邻法中的 k（最相近的点的个数），决策树模型中树的深度，树的数量或树的深度，矩阵分解中潜在因素的数量，学习率（多种模式），深层神经网络隐藏层数，k 均值聚类中的簇数等等。

超参数的优化：
有四种主要的策略可用于搜索最佳配置：照看（babysitting，又叫试错），网格搜索，随机搜索，贝叶斯优化。


### Bias（偏差）Variance（方差）

方差关乎数据，偏差关乎模型。
[Graphical illustration of bias and variance.](http://scott.fortmann-roe.com/docs/BiasVariance.html)
{% include image.html url="/assets/images/221013-artificial-intelligence/20221029125306.png" %}

偏差，就是模型的预测值与真实值偏了，距离之差是多少，模型平均预测值与真实值之间的距离。

方差，描述数据分布的分散程度。这里的数据分布，就是我们模型预测值的数据分布。从式子本身来看，是与真实值没有关系的。

高偏差：
1. 增加特征
2. 获得更多的特征
3. 增加多项式特征
4. 减少正则化程度

高方差：
1. 增加训练数据
2. 减少特征数量
3. 增加正则化程度


### scikit-learn

liblinear
libsvm

More esoteric: String kernel, chi-square kernel, histogram intersection kernel, ...
字符串距离，卡方核函数，直方相交核函数。

[sklearn](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) 包括了分类，回归，降维和聚类等四大机器学习算法，还包括了特征提取，数据处理和模型评估者三大模块。
sk-learn 库，基于上述的 numpy 和 Scipy 的库。包含大量用于传统机器学习和数据挖掘相关的算法，集成了常见的机器学习功能。
Scikit-learn 主要用于各种数据建模概念，如回归、分类、聚类、模型选择等。 该库是在 Numpy、Scipy 和 matplotlib 之上编写的。Scikit-learn 易于集成，可以继承其他机器学习库实现特定目标。
比如 Numpy 和 Pandas 用于数据分析，Plotly 用于可视化。
{% include image.html url="/assets/images/221013-artificial-intelligence/ml_map.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence/v2-43c13ca000a22bf0f9f9dc11ed0c4ee7_720w.webp" %}

* [sklearn 库主要模块功能和辅助函数 {% include relref_bili.html %}](https://www.bilibili.com/read/cv12252018/)
* [sklearn 库机器学习 python 使用教程 {% include relref_csdn.html %}](https://blog.csdn.net/weixin_51111267/article/details/122628057)
    * 1、分类学习 (classification)，属于监督型
        * 适用算法一：k 邻算法
        * 适用算法二：支持向量机 (SVC)
    * 2、回归学习 (regression)，属于监督型
        * 适用算法一：线性回归法
        * 适用算法二：支持向量机 (SVR)
    * 3、聚类学习 (clustering)，不属于监督型
    * 4、降维学习 (dimensionality reduction) 不属于监督型

**imgaug**：机器学习实验中的图像增强库，特别是卷积神经网络。支持以多种不同方式增强图像、关键点 / 地标、边界框、热图和分割图。
[Image augmentation for machine learning experiments.](https://imgaug.readthedocs.io/en/latest/)


### 归一化和标准化

标准化本质上都是对数据进行线性变换，并不会改变数据的分布类型。变量的原始分布是非正态的，变换之后依然是非正态的。也正是因为这一点，许多领域都会在分析前对数据进行标准化，因为它即可以无损数据的原有信息，同时还能赋予数据一些新的优良性质。

[note](https://www.lianxh.cn/news/ac0f7a163237d.html)
1. Z-score Normalization
    * z-score normalization 之后，数据会变成均值为 0 、标准差为 1 的分布。
2. Min-Max Normalization
    * 这种方法可以将数据范围映射到 [0，1] 区间内。
3. Mean Normalization

[那些算法需要归一化 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/488290289)
1. 涉及或隐含距离计算的算法，比如 K-means、KNN、PCA、SVM 等，一般需要进行归一化
2. 梯度下降算法，梯度下降的收敛速度取决于：参数的初始位置到 local minima 的距离，以及学习率 η 的大小
3. 采用 sigmoid 等有饱和区的激活函数，如果输入分布范围很广，参数初始化时没有适配好，
    很容易直接陷入饱和区，导致梯度消失，所以才会出现各种 BN，LN 等算法

那些算法不需要归一化
1. 与距离计算无关的概率模型，比如 Naive Bayes，不需要；
2. 与距离计算无关的基于树的模型，比如决策树、随机森林等，
    树中节点的选择只关注当前特征在哪里切分对分类更好，即只在意特征内部的相对大小，
    而与特征间的相对大小无关。
    使用 Z-Score 归一化会提高模型的准确率。
    其实归一化的作用就是由绝对变为了相对，所以可以说归一化对于树型模型不那么重要，
    是一个可选项或者说可以作为一个超参数在训练时进行选择。


## 线性回归

线性回归（Linear Regression）可能是最流行的机器学习算法。线性回归就是要找一条直线，并且让这条直线尽可能地拟合散点图中的数据点。它试图通过将直线方程与该数据拟合来表示自变量（x 值）和数值结果（y 值）。然后就可以用这条线来预测未来的值！

这种算法最常用的技术是最小二乘法（Least of squares）。这个方法计算出最佳拟合线，以使得与直线上每个数据点的垂直距离最小。总距离是所有数据点的垂直距离（绿线）的平方和。其思想是通过最小化这个平方误差或距离来拟合模型。

{% include image.html url="/assets/images/221013-artificial-intelligence/6401.jpg" %}


## 逻辑回归

逻辑回归（Logistic regression）与线性回归类似，但逻辑回归的结果只能有两个的值。如果说线性回归是在预测一个开放的数值，那逻辑回归更像是做一道是或不是的判断题。

逻辑函数中 Y 值的范围从 0 到 1，是一个概率值。逻辑函数通常呈 S 型，曲线把图表分成两块区域，因此适合用于分类任务。

{% include image.html url="/assets/images/221013-artificial-intelligence/6402.jpg" %}


## 决策树

如果说线性和逻辑回归都是把任务在一个回合内结束，那么决策树（Decision Trees）就是一个多步走的动作，它同样用于回归和分类任务中，不过场景通常更复杂且具体。

举个简单例子，老师面对一个班级的学生，哪些是好学生？如果简单判断考试 90 分就算好学生好像太粗暴了，不能唯分数论。那面对成绩不到 90 分的学生，我们可以从作业、出勤、提问等几个方面分开讨论。

{% include image.html url="/assets/images/221013-artificial-intelligence/6403.jpg" %}


## 朴素贝叶斯

朴素贝叶斯（Naive Bayes）是基于贝叶斯定理，即两个条件关系之间。它测量每个类的概率，每个类的条件概率给出 x 的值。这个算法用于分类问题，得到一个二进制“是 / 非”的结果。看看下面的方程式。

朴素贝叶斯分类器是一种流行的统计技术，经典应用是过滤垃圾邮件。

* 判别模型（Discriminative Model)
    * 线性回归、逻辑回归、感知机、决策树、支持向量机……
* 生成模型（Generative Model）
    * 朴素贝叶斯、HMM、深度信念网络（DBN）……

$$
P(Y|X)P(X)=P(X|Y)P(Y)
$$

* 最常用的 GaussianNB 是高斯贝叶斯分类器。它假设特征的条件概率分布满足高斯分布。
* MultinomialNB 是多项式贝叶斯分类器，它假设特征的条件概率分布满足多项式分布。
* BernoulliNB 是伯努利贝叶斯分类器。它假设特征的条件概率分布满足二项分布。


## 支持向量机

支持向量机（Support Vector Machine，SVM）是一种用于分类问题的监督算法。支持向量机试图在数据点之间绘制两条线，它们之间的边距最大。为此，我们将数据项绘制为 n 维空间中的点，其中，n 是输入特征的数量。在此基础上，支持向量机找到一个最优边界，称为超平面（Hyperplane），它通过类标签将可能的输出进行最佳分离。

超平面与最近的类点之间的距离称为边距。最优超平面具有最大的边界，可以对点进行分类，从而使最近的数据点与这两个类之间的距离最大化。

{% include image.html url="/assets/images/221013-artificial-intelligence/6405.jpg" %}

所以支持向量机想要解决的问题也就是如何把一堆数据做出区隔，它的主要应用场景有字符识别、面部识别、文本分类等各种识别。


## K- 最近邻算法（KNN）

K- 最近邻算法（K-Nearest Neighbors，KNN）非常简单。KNN 通过在整个训练集中搜索 K 个最相似的实例，即 K 个邻居，并为所有这些 K 个实例分配一个公共输出变量，来对对象进行分类。

K 的选择很关键：较小的值可能会得到大量的噪声和不准确的结果，而较大的值是不可行的。它最常用于分类，但也适用于回归问题。

用于评估实例之间相似性的距离可以是欧几里得距离（Euclidean distance）、曼哈顿距离（Manhattan distance）或明氏距离（Minkowski distance）。欧几里得距离是两点之间的普通直线距离。它实际上是点坐标之差平方和的平方根。

{% include image.html url="/assets/images/221013-artificial-intelligence/6406.jpg" caption="KNN 分类示例" %}

KNN 理论简单，容易实现，可用于文本分类、模式识别、聚类分析等。


### KD 树（K-D Tree）

k 近邻法最简单的实现是线性扫描（穷举搜索），即要计算输入实例与每一个训练实例的距离。计算并存储好以后，再查找 K 近邻。当训练集很大时，计算非常耗时。
为了提高 kNN 搜索的效率，可以考虑使用特殊的结构存储训练数据，以减小计算距离的次数。这里介绍的就是 KD 树。


## K- 均值

K- 均值（K-means）是通过对数据集进行分类来聚类的。例如，这个算法可用于根据购买历史将用户分组。它在数据集中找到 K 个聚类。K- 均值用于无监督学习，因此，我们只需使用训练数据 X，以及我们想要识别的聚类数量 K。

该算法根据每个数据点的特征，将每个数据点迭代地分配给 K 个组中的一个组。它为每个 K- 聚类（称为质心）选择 K 个点。基于相似度，将新的数据点添加到具有最近质心的聚类中。这个过程一直持续到质心停止变化为止。

{% include image.html url="/assets/images/221013-artificial-intelligence/6407.jpg" %}

生活中，K- 均值在欺诈检测中扮演了重要角色，在汽车、医疗保险和保险欺诈检测领域中广泛应用。


## 随机森林

随机森林（Random Forest）是一种非常流行的集成机器学习算法。这个算法的基本思想是，许多人的意见要比个人的意见更准确。在随机森林中，我们使用决策树集成（参见决策树）。

{% include image.html url="/assets/images/221013-artificial-intelligence/6408.jpg" %}

（a）在训练过程中，每个决策树都是基于训练集的引导样本来构建的。

（b）在分类过程中，输入实例的决定是根据多数投票做出的。

随机森林拥有广泛的应用前景，从市场营销到医疗保健保险，既可以用来做市场营销模拟的建模，统计客户来源、保留及流失，也可以用来预测疾病的风险和病患者的易感性。


## 降维

由于我们今天能够捕获的数据量之大，机器学习问题变得更加复杂。这就意味着训练极其缓慢，而且很难找到一个好的解决方案。这一问题，通常被称为“维数灾难”（Curse of dimensionality）。

降维（Dimensionality reduction）试图在不丢失最重要信息的情况下，通过将特定的特征组合成更高层次的特征来解决这个问题。主成分分析（Principal Component Analysis，PCA）是最流行的降维技术。

主成分分析通过将数据集压缩到低维线或超平面 / 子空间来降低数据集的维数。这尽可能地保留了原始数据的显著特征。
可以通过将所有数据点近似到一条直线来实现降维的示例。

{% include image.html url="/assets/images/221013-artificial-intelligence/6409.jpg" %}


## 人工神经网络（ANN）

人工神经网络（Artificial Neural Networks，ANN）可以处理大型复杂的机器学习任务。神经网络本质上是一组带有权值的边和节点组成的相互连接的层，称为神经元。在输入层和输出层之间，我们可以插入多个隐藏层。人工神经网络使用了两个隐藏层。除此之外，还需要处理深度学习。

人工神经网络的工作原理与大脑的结构类似。一组神经元被赋予一个随机权重，以确定神经元如何处理输入数据。通过对输入数据训练神经网络来学习输入和输出之间的关系。在训练阶段，系统可以访问正确的答案。

如果网络不能准确识别输入，系统就会调整权重。经过充分的训练后，它将始终如一地识别出正确的模式。
{% include image.html url="/assets/images/221013-artificial-intelligence/640x.jpg" %}
每个圆形节点表示一个人工神经元，箭头表示从一个人工神经元的输出到另一个人工神经元的输入的连接。

图像识别，就是神经网络中的一个著名应用。

现在，你已经了解了最流行的人工智能算法的基础介绍，并且，对它们的实际应用也有了一定认识。


## Adaboost

adaboost 是 bosting 的方法之一。
bosting 就是把若干个分类效果并不好的分类器综合起来考虑，会得到一个效果比较好的分类器。

[note {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/kbY8Y3BDmXTm2-wA3eLpMw)


## XGBoost



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-10-13-artificial-intelligence.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1s3411y7WN/]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/www.bilibili.com/9371f15d.html" %})
- [https://blog.csdn.net/qq_39783601/article/details/123365469]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/blog.csdn.net/a44029f7.html" %})
- [http://scott.fortmann-roe.com/docs/BiasVariance.html]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/scott.fortmann-roe.com/03c2a188.html" %})
- [https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/scikit-learn.org/3be777ad.html" %})
- [https://www.bilibili.com/read/cv12252018/]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/www.bilibili.com/197befec.html" %})
- [https://blog.csdn.net/weixin_51111267/article/details/122628057]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/blog.csdn.net/cda36618.html" %})
- [https://imgaug.readthedocs.io/en/latest/]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/imgaug.readthedocs.io/aeade3ec.html" %})
- [https://www.lianxh.cn/news/ac0f7a163237d.html]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/www.lianxh.cn/b9cac1b0.html" %})
- [https://zhuanlan.zhihu.com/p/488290289]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/zhuanlan.zhihu.com/b8d23c85.html" %})
- [https://mp.weixin.qq.com/s/kbY8Y3BDmXTm2-wA3eLpMw]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/mp.weixin.qq.com/4c1e2cb5.html" %})
