---
layout: post
title: "机器学习笔记 -- 人工智能 机器学习 算法概览（已完成）"
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
cluster: "机器学习课程"
---

[神经网络*内部*发生了什么？ {% include relref_bili.html %}](https://www.bilibili.com/video/BV1s3411y7WN/)
{% include image.html url="/assets/images/221013-artificial-intelligence/20221016220307.png" %}

> 深度学习如皓月当空，传统机器学习算法都显得暗淡无光了，系统性的整理了机器学习算法，希望项目中能用上一两个。
> 数据收集、数据清洗、特征工程、数据建模。
> 数据和特征决定了机器学习的上限，而模型和算法只能逼近这个上限而已。

* 机器学习：给定数据的预测问题。

* 监督学习：有标签，对于属于数据 X，预测 Y。
    * 分类：标签不连续。
    * 回归：标签连续。
    * K 近邻
    * 支持向量机 SVM
    * 决策树
    * 朴素贝叶斯
    * 逻辑回归
    * 线性回归
    * 集成算法 Adaboost 等
    * XGBoost
    * **LightGBM**
* 无监督学习：无标签，对于数据数据 X，能发现什么。
    * 聚类
    * 降维算法
    * EM 算法
    * 关联规则
    * PageRank 等
* 强化学习：序列决策问题。
    * 马尔可夫决策方法（扫地机器人寻路）

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

{% include image.html url="/assets/images/221013-artificial-intelligence/IMG_e404fc02625449b5aa6c712a5d68da2b.png" %}
boxplot：箱型图又称为盒须图、盒式图或箱线图，是一种用作显示一组数据分散情
况资料的统计图。


### 卡尔曼滤波

{% include image.html url="/assets/images/221013-artificial-intelligence/20230612230555.png" caption="李永乐 · 人工智能" %}

1. 卡尔曼滤波器能够很好地解决线性的状态估计问题；
2. 在遇到非线性的状态估计问题时，可以利用扩展卡尔曼滤波器将非线性问题线性化，只是会有一些精度损失。
3. 粒子滤波的思想基于蒙特卡洛方法，利用粒子集来表示概率，可以用在任何形式的状态空间模型上。
    相比于其他滤波算法，粒子滤波在解决非线性、非高斯的问题上，有着较大的优越性。
    在无人驾驶领域，粒子滤波常被用于解决无人车的定位问题。

[卡尔曼滤波](https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/)
在介绍卡尔曼滤波器数学原理之前，先从感性上看一下它的工作原理。
简单来讲，卡尔曼滤波器就是根据上一时刻的状态，预测当前时刻的状态，将预测的状态与当前时刻的测量值进行加权，加权后的结果才认为是当前的实际状态，而不是仅仅听信当前的测量值。


### 超参数（Hyperparameter）

机器学习算法中的调优参数（tuning parameters），需要人为设定，称为超参数（Hyperparameter）。比如，正则化系数 λ，决策树模型中树的深度。

迭代次数 epoch，k 近邻法（kNN）中的 k（最相近的点的个数），决策树模型中树的深度等等都属于超参数。
梯度下降法中的学习速率 α，批量大小 batch-size，k 近邻法中的 k（最相近的点的个数），树的数量或树的深度，矩阵分解中潜在因素的数量，学习率（多种模式），深层神经网络隐藏层数，k 均值聚类中的簇数等等。

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

**imgaug** ：机器学习实验中的图像增强库，特别是卷积神经网络。支持以多种不同方式增强图像、关键点 / 地标、边界框、热图和分割图。
[Image augmentation for machine learning experiments.](https://imgaug.readthedocs.io/en/latest/)


### 归一化和标准化

标准化本质上都是对数据进行线性变换，并不会改变数据的分布类型。变量的原始分布是非正态的，变换之后依然是非正态的。也正是因为这一点，许多领域都会在分析前对数据进行标准化，因为它即可以无损数据的原有信息，同时还能赋予数据一些新的优良性质。

[note](https://www.lianxh.cn/news/ac0f7a163237d.html)
1. Z-score Normalization
    * z-score normalization 之后，数据会变成均值为 0、标准差为 1 的分布。
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


### 神经网络中怎么解决梯度消失问题

在深度网络中，网络参数的学习是通过反向传播的链式求导法则来求 Loss 对某个参数 的偏导数，然后进行参数更新的。因此造成梯度消失的原因主要有两个：
1. 当网络层 数很深，而当前的参数所在层又靠近网络的输入时，求导链就会非常长；
2. 如果其中的某些中间结果的值很小，并经过链式的累成作用，最终求得的梯度值就会接近于零，而导致参数得不到更新。

可通过以下方法解决梯度消失的问题：
1. 选用合适的激活函数。比如 ReLU 或者 Leaky ReLU。因为像 Sigmoid 和 Tanh 这样的激活函数，会出现比较大的梯度饱和区域，使得梯度的取值接近于 0。
2. 采用 Batch Normalization 层，对网络中计算得到中间值进行归一化，使得中 间计算结果的取值在均值为 0，方差为 1 这样的分布内。那么此时，在 sigmoid 和 tanh 中，函数取值处于中间变化较大的部分，梯度取值也相对较大，从而 可以防止过拟合。
3. 使用残差结构，残差结构相当于给靠近输入端的网络层提供了一个与靠近输出 端层的直连操作。在反向传播计算时，减少了梯度传播的路径长度，以缓解梯 度消失的问题。
4. 在 RNN 网络中，可以通过使用 LSTM（long-short term memory networks）长 短时记忆网络，来解决信息遗忘和梯度传播的问题。


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

{% include image.html url="/assets/images/221013-artificial-intelligence/20221101235640.png" %}

决策树算法主要包括三个部分：特征选择、树的生成、树的剪枝。常用算法有 ID3、C4.5、CART。


### 分割方法

[note {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/32877396)
* ID3(Iterative Dichotomiser)
    * “信息熵”，期望信息越小，信息熵越大，样本纯度越低。
* C4.5
    * C4.5 算法是 Ross 对 ID3 算法的改进。
* CART(Classification And Regression Tree)
    * 用基尼指数来选择属性（分类），或用均方差来选择属性（回归）。


### 决策树差异总结

* 划分标准的差异：
    ID3 使用信息增益偏向特征值多的特征，
    C4.5 使用信息增益率克服信息增益的缺点，偏向于特征值小的特征，
    CART 使用基尼指数克服 C4.5 需要求 log 的巨大计算量，偏向于特征值较多的特征。
* 使用场景的差异：ID3 和 C4.5 都只能用于分类问题，CART 可以用于分类和回归问题；
    ID3 和 C4.5 是多叉树，速度较慢，CART 是二叉树，计算速度很快；
* 样本数据的差异：ID3 只能处理离散数据且缺失值敏感，
    C4.5 和 CART 可以处理连续性数据且有多种方式处理缺失值；
    从样本量考虑的话，小样本建议 C4.5、大样本建议 CART。
    C4.5 处理过程中需对数据集进行多次扫描排序，处理成本耗时较高，而 CART 本身是一种大样本的统计方法，小样本处理下泛化误差较大；
* 样本特征的差异：ID3 和 C4.5 层级之间只使用一次特征，CART 可多次重复使用特征；
* 剪枝策略的差异：ID3 没有剪枝策略，C4.5 是通过悲观剪枝策略来修正树的准确性，而 CART 是通过代价复杂度剪枝。

* 特征选择。特征选择的目的是选取能够对训练集分类的特征。特征选择的关键是准则：信息增益、信息增益比、Gini 指数；
* 决策树的生成。通常是利用信息增益最大、信息增益比最大、Gini 指数最小作为特征选择的准则。从根节点开始，递归的生成决策树。
    相当于是不断选取局部最优特征，或将训练集分割为基本能够正确分类的子集；
* 决策树的剪枝。决策树的剪枝是为了防止树的过拟合，增强其泛化能力。包括预剪枝和后剪枝。


## 朴素贝叶斯

朴素贝叶斯（Naive Bayes）是基于贝叶斯定理，即两个条件关系之间。它测量每个类的概率，每个类的条件概率给出 x 的值。这个算法用于分类问题，得到一个二进制“是 / 非”的结果。看看下面的方程式。

$$
P(Y|X)P(X)=P(X|Y)P(Y)
$$

* 最常用的 GaussianNB 是高斯贝叶斯分类器。它假设特征的条件概率分布满足高斯分布。
* MultinomialNB 是多项式贝叶斯分类器，它假设特征的条件概率分布满足多项式分布。
* BernoulliNB 是伯努利贝叶斯分类器。它假设特征的条件概率分布满足二项分布。

朴素贝叶斯分类器是一种流行的统计技术，经典应用是过滤垃圾邮件。

* 判别模型（Discriminative Model)
    * 线性回归、逻辑回归、感知机、决策树、支持向量机……
* 生成模型（Generative Model）
    * 朴素贝叶斯、HMM、深度信念网络（DBN）……


## 支持向量机

支持向量机（Support Vector Machine，SVM）是一种用于分类问题的监督算法。支持向量机试图在数据点之间绘制两条线，它们之间的边距最大。为此，我们将数据项绘制为 n 维空间中的点，其中，n 是输入特征的数量。在此基础上，支持向量机找到一个最优边界，称为超平面（Hyperplane），它通过类标签将可能的输出进行最佳分离。

超平面与最近的类点之间的距离称为边距。最优超平面具有最大的边界，可以对点进行分类，从而使最近的数据点与这两个类之间的距离最大化。

[数学推导过程 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/77750026)
没看懂。mark

{% include image.html url="/assets/images/221013-artificial-intelligence/6405.jpg" %}

所以支持向量机想要解决的问题也就是如何把一堆数据做出区隔，它的主要应用场景有字符识别、面部识别、文本分类等各种识别。

{% include image.html url="/assets/images/221013-artificial-intelligence/IMG_990a02a6461e464b97d8fb217ef26f09.png" %}

n 为特征数，m 为训练样本数。
1. 如果相较于 m 而言，n 要大许多，即训练集数据量不够支持我们训练一个复
    杂的非线性模型，我们选用逻辑回归模型或者不带核函数的支持向量机。
2. 如果 n 较小，而且 m 大小中等，例如 n 在 1-1000 之间，而 m 在 10-10000 之
    间，使用高斯核函数的支持向量机。
3. 如果 n 较小，而 m 较大，例如 n 在 1-1000 之间，而 m 大于 50000，则使用支
    持向量机会非常慢，解决方案是创造、增加更多的特征，然后使用逻辑回归或不带核函数的支持向量机。


## K- 最近邻算法（KNN）

K- 最近邻算法（K-Nearest Neighbors，KNN）非常简单。KNN 通过在整个训练集中搜索 K 个最相似的实例，即 K 个邻居，并为所有这些 K 个实例分配一个公共输出变量，来对对象进行分类。

K 的选择很关键：较小的值可能会得到大量的噪声和不准确的结果，而较大的值是不可行的。它最常用于分类，但也适用于回归问题。

用于评估实例之间相似性的距离可以是欧几里得距离（Euclidean distance）、曼哈顿距离（Manhattan distance）或明氏距离（Minkowski distance）。欧几里得距离是两点之间的普通直线距离。它实际上是点坐标之差平方和的平方根。

{% include image.html url="/assets/images/221013-artificial-intelligence/6406.jpg" caption="KNN 分类示例" %}

KNN 理论简单，容易实现，可用于文本分类、模式识别、聚类分析等。


### KD 树（K-D Tree）

k 近邻法最简单的实现是线性扫描（穷举搜索），即要计算输入实例与每一个训练实例的距离。计算并存储好以后，再查找 K 近邻。当训练集很大时，计算非常耗时。
为了提高 kNN 搜索的效率，可以考虑使用特殊的结构存储训练数据，以减小计算距离的次数。就是 KD 树。


## K- 均值

K- 均值（K-means）是通过对数据集进行分类来聚类的。例如，这个算法可用于根据购买历史将用户分组。它在数据集中找到 K 个聚类。K- 均值用于无监督学习，因此，我们只需使用训练数据 X，以及我们想要识别的聚类数量 K。

该算法根据每个数据点的特征，将每个数据点迭代地分配给 K 个组中的一个组。它为每个 K- 聚类（称为质心）选择 K 个点。基于相似度，将新的数据点添加到具有最近质心的聚类中。这个过程一直持续到质心停止变化为止。

{% include image.html url="/assets/images/221013-artificial-intelligence/6407.jpg" %}

生活中，K- 均值在欺诈检测中扮演了重要角色，在汽车、医疗保险和保险欺诈检测领域中广泛应用。

聚类
主要算法
K-means、密度聚类、层次聚类


### 密度聚类

DBSCAN 密度聚类。
与划分和层次聚类方法不同，DBSCAN (Density-Based Spatial Clustering of
Applications with Noise) 是一个比较有代表性的基于密度的聚类算法。它将簇
定义为密度相连的点的最大集合，能够把具有足够高密度的区域划分为簇，并
可在噪声的空间数据库中发现任意形状的聚类。
{% include image.html url="/assets/images/221013-artificial-intelligence/20221105122214.png" %}


### 层次聚类

{% include image.html url="/assets/images/221013-artificial-intelligence/20221105123039.png" %}


## 随机森林

随机森林（Random Forest）是一种非常流行的集成机器学习算法。这个算法的基本思想是，许多人的意见要比个人的意见更准确。在随机森林中，我们使用决策树集成。

{% include image.html url="/assets/images/221013-artificial-intelligence/6408.jpg" %}

1. 在训练过程中，每个决策树都是基于训练集的引导样本来构建的。
2. 在分类过程中，输入实例的决定是根据多数投票做出的。

随机森林拥有广泛的应用前景，从市场营销到医疗保健保险，既可以用来做市场营销模拟的建模，统计客户来源、保留及流失，也可以用来预测疾病的风险和病患者的易感性。

优点：
* 由于每次不再考虑全部的属性，而是一个属性子集，所以相比于 Bagging 计算开销更小，训练效率更高；
* 由于增加了属性的扰动，随机森林中基学习器的性能降低，使得在随机森林在起始时候性能较差，但是随着基学习器的增多，
    随机森林通常会收敛于更低的泛化误差，相比于 Bagging；
* 两个随机性的引入，使得随机森林不容易陷入过拟合，具有很好的抗噪声能力；
* 对数据的适应能力强，可以处理离散和连续的，无需要规范化；
* 可以得到变量的重要性， 基于 oob 错误率（袋外错误率 out-of-bag error）和基于 Gini 系数的变化。
* 不同决策树可以由不同主机并行训练生成，效率很高。

缺点：
* 在噪声较大的时候容易过拟合。


### 集成学习

adaboost 是 bosting 的方法之一。
bosting 就是把若干个分类效果并不好的分类器综合起来考虑，会得到一个效果比较好的分类器。

[note {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/kbY8Y3BDmXTm2-wA3eLpMw)
[集成学习](http://c.biancheng.net/ml_alg/ensemble-learning.html)。
* Bagging Boosting Stacking
* AdaBoost（Adaptive Boosting，自适应增强），后一个模型的训练永远是在前一个模型的基础上完成！
* GBDT 算法 GBDT（Gradient Boosting Decision Tree）是一种迭代的决策树算
    法，该算法由多棵决策树组成，GBDT 的核心在于累加所有树的结果
    作为最终结果，所以 GBDT 中的树都是回归树，不是分类树，它是属
    于 Boosting 策略。GBDT 是被公认的泛化能力较强的算法。
* XGBoost 是大规模并行 boosting tree 的工具，它是目前最快最好的开源 boosting tree 工具包，
    比常见的工具包快 10 倍以上。XGBoost 和 GBDT 两者都是 boosting 方法，
    除了工程实现、解决问题上的一些差异外，最大的不同就是目标函数的定义。
*  [ **LightGBM** {% include relref_csdn.html %}](https://blog.csdn.net/a321123b/article/details/119451920) 由微软提出，主要用于解决 GDBT 在海量数据中遇到的问题，
    以便其可以更好更快地用于工业实践中，其相对 XGBoost 具有训练速度快、内存占用低的特点。
    LightGBM 与 XGBoost 相比，主要有以下几个改进：
    * 基于梯度的单边采样算法（Gradient-based One-Side Sampling, GOSS）；
    * 互斥特征捆绑算法（Exclusive Feature Bundling, EFB）；
    * 直方图算法（Histogram）；
    * 基于最大深度的 Leaf-wise 的垂直生长算法。


### GBDT 和随机森林区别

GBDT 和随机森林的相同点：
* 都是由多棵树组成；
* 最终的结果都由多棵树共同决定。

GBDT 和随机森林的不同点：
* 组成随机森林的可以是分类树、回归树；组成 GBDT 只能是回归树；
* 组成随机森林的树可以并行生成（Bagging）；GBDT 只能串行生成（Boosting）；这两种模型都用到了 Bootstrap 的思想。
* 对于最终的输出结果而言，随机森林使用多数投票或者简单平均；而 GBDT 则是将所有结果累加起来，或者加权累加起来；
* 随机森林对异常值不敏感，GBDT 对异常值非常敏感；
* 随机森林对训练集一视同仁权值一样，GBDT 是基于权值的弱分类器的集成；
* 随机森林通过减小模型的方差提高性能，GBDT 通过减少模型偏差提高性能。


## 降维

由于我们今天能够捕获的数据量之大，机器学习问题变得更加复杂。这就意味着训练极其缓慢，而且很难找到一个好的解决方案。这一问题，通常被称为“维数灾难”（Curse of dimensionality）。

降维（Dimensionality reduction）试图在不丢失最重要信息的情况下，通过将特定的特征组合成更高层次的特征来解决这个问题。主成分分析（Principal Component Analysis，PCA）是最流行的降维技术。

主成分分析通过将数据集压缩到低维线或超平面 / 子空间来降低数据集的维数。这尽可能地保留了原始数据的显著特征。
可以通过将所有数据点近似到一条直线来实现降维的示例。

{% include image.html url="/assets/images/221013-artificial-intelligence/6409.jpg" %}


### SVD（奇异值分解）

SVD 其实是众多矩阵分解的一种，除了在 PCA 上使用，也有用于推荐，在推荐领域的 svd 算法形式上并不能和标准的奇异值分解对应上，但其思路是相通的，具体可以参考协同过滤算法实现。

* SVD 分解可以将一个矩阵进行分解，对角矩阵对角线上的特征值递减存放，
    而且奇异值的减少特别的快，在很多情况下，前 $10%$ 甚至 $1%$ 的奇异值的和
    就占了全部的奇异值之和的 99% 以上的比例。
* 也就是说，对于奇异值，它跟我们特征分解中的特征值类似，我们也可以用
    最大的 $k$ 个的奇异值和对应的左右奇异向量来近似描述矩阵。


### PCA（主成分分析）

不存在完全无损的降维。
{% include image.html url="/assets/images/221013-artificial-intelligence/v2-589dc1e07c47ce52a82bac13da8d1c85_1440w.png" %}
[from {% include relref_csdn.html %}](https://blog.csdn.net/Dark_Scope/article/details/53150883)
{% include image.html url="/assets/images/221013-artificial-intelligence/20160207114645575.gif" %}

PCA 的算法两种实现方法
* 基于 SVD 分解协方差矩阵实现 PCA 算法
* 基于特征值分解协方差矩阵实现 PCA 算法

**PCA 算法优点**
1. 仅仅需要以方差衡量信息量，不受数据集以外的因素影响
2. 各主成分之间正交，可消除原始数据成分间的相互影响的因素
3. 计算方法简单，主要运算时特征值分解，易于实现
4. 它是无监督学习，完全无参数限制的

**PCA 算法缺点**
1. 主成分各个特征维度的含义具有一定的模糊性，不如原始样本特征的解释性强
2. 方差小的非主成分也可能含有对样本差异的重要信息，因降维丢弃可能对后续数据处理有影响


## 关联规则


### Apriori 算法

**Apriori 算法缺点**
Apriori 在计算的过程中有以下几个缺点：
1. 可能产生大量的候选集。因为采用排列组合的方式，把可能的项集都组合出来了；
2. 每次计算都需要重新扫描数据集，来计算每个项集的支持度。


### FP-Growth 算法

**FP-growth 算法思想**
该算法和 Apriori 算法最大的不同有两点：
1. 不产生候选集
2. 只需要两次遍历数据库，大大提高了效率。

**FP-Growth 算法的优点**
1. 与 Apriori 算法相比，该算法只需对数据库进行两次扫描
2. 该算法不需要对项目进行配对，因此速度更快。
3. 数据库存储在内存中的压缩版本中。
4. 对长、短频繁模式的挖掘具有高效性和可扩展性。

**FP-Growth 算法的缺点**
1. FP-Tree 比 Apriori 更麻烦，更难构建。
2. 可能很耗资源。
3. 当数据库较大时，算法可能不适合共享内存


### Eclat 算法的优缺点

**优点：**
Eclat 的优势是只需扫描一遍完整的数据库， 这种方法与 Apriori 相比有一
个优势，在产生候选 (k+1) 项集时利用先验性质，而且不需要扫描数据库
来确定 (k+1) 项集的支持度，这是因为每个 k 项集的交易集携带了计算支持
度的完整信息。

**缺点：**
当有许多事务需要大量内存和计算时间来相交集合时，就会出现瓶颈。因为在
Eclat 算法中，它由 2 个集合的并集产生新的候选集，通过计算这 2 个项集的交易集
的交集快速得到候选集的支持度，所以，当交易集的规模庞大时将出现以下问题：
* 求交易集的交集的操作将消耗大量时间，影响了算法的效率；
* 交易集的规模相当庞大，消耗系统大量的内存。


## 人工神经网络（ANN）

人工神经网络（Artificial Neural Networks，ANN）可以处理大型复杂的机器学习任务。神经网络本质上是一组带有权值的边和节点组成的相互连接的层，称为神经元。在输入层和输出层之间，我们可以插入多个隐藏层。人工神经网络使用了两个隐藏层。除此之外，还需要处理深度学习。

人工神经网络的工作原理与大脑的结构类似。一组神经元被赋予一个随机权重，以确定神经元如何处理输入数据。通过对输入数据训练神经网络来学习输入和输出之间的关系。在训练阶段，系统可以访问正确的答案。

如果网络不能准确识别输入，系统就会调整权重。经过充分的训练后，它将始终如一地识别出正确的模式。
{% include image.html url="/assets/images/221013-artificial-intelligence/640x.jpg" %}
每个圆形节点表示一个人工神经元，箭头表示从一个人工神经元的输出到另一个人工神经元的输入的连接。

图像识别，就是神经网络中的一个著名应用。


### 最常用 Sigmoid 函数的优缺点

CNN
常见激活函数选择：
Sigmoid 函数
Tanh 函数
ReLU 函数
Leaky ReLU 函数

**Sigmoid 和 softmax**
* Sigmoid 只做值非线性变化映射到 (0,1)，用于二分类。
* softmax 变化过程计算所有结果的权重，使得多值输出的概率和为 1。用于多分类。 指数运算速度慢。梯度饱和消失。

**Tanh 函数**
* 双曲正切函数。以 0 为中心，有归一化的作用。

**ReLu 和 Leaky ReLu**
* 大于 0 为 1，小于 0 为 0，计算速度快。
* leaky 输入为负时，梯度仍有值，避免死掉。

{% include image.html url="/assets/images/221013-artificial-intelligence/20221102012144.png" caption="激活函数" %}

**Sigmoid 函数 优点：**
1. 函数处处连续，便于求导
2. 可将函数值的范围压缩至 [0,1]，可用于压缩数据，且幅度不变
3. 便于前向传输

**Sigmoid 函数 缺点：**
1. 在趋向无穷的地方，函数值变化很小，容易出现梯度消失，不利于深层神经的反馈传输
2. 幂函数的梯度计算复杂
3. 收敛速度比较慢


### BP 算法

优点：

1. 能够自适应、自主学习。BP 可以根据预设参数更新规则，通过不断调整神经网络中的参数，已达到最符合期望的输出。
2. 拥有很强的非线性映射能力。
3. 误差的反向传播采用的是成熟的链式法则，推导过程严谨且科学。
4. 算法泛化能力很强。

缺点：

1. BP 神经网络参数众多，每次迭代需要更新较多数量的阈值和权值，故收敛速度比较慢。
2. 网络中隐层含有的节点数目没有明确的准则，需要不断设置节点数字试凑，根据网络误差结果最终确定隐层节点个数。
3. BP 算法是一种速度较快的梯度下降算法，容易陷入局部极小值的问题。

{% include image.html url="/assets/images/221013-artificial-intelligence/v2-22ee181fbe6046ccec1dc443228ae176_720w.webp" caption="L1 & L2 正则化" %}

评价指标
[ref {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/82105066)
* [线性代数在数据科学中的十个强大应用（一） {% include relref_jianshu.html %}](https://www.jianshu.com/p/56985bcfac66)
* [线性代数在数据科学中的十大强大应用（二）](http://events.jianshu.io/p/c0ced4833192)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-10-13-artificial-intelligence.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1s3411y7WN/]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/www.bilibili.com/9371f15d.html" %})
- [https://blog.csdn.net/qq_39783601/article/details/123365469]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/blog.csdn.net/a44029f7.html" %})
- [https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/www.bzarg.com/c8bef21a.html" %})
- [http://scott.fortmann-roe.com/docs/BiasVariance.html]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/scott.fortmann-roe.com/03c2a188.html" %})
- [https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/scikit-learn.org/3be777ad.html" %})
- [https://www.bilibili.com/read/cv12252018/]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/www.bilibili.com/197befec.html" %})
- [https://blog.csdn.net/weixin_51111267/article/details/122628057]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/blog.csdn.net/cda36618.html" %})
- [https://imgaug.readthedocs.io/en/latest/]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/imgaug.readthedocs.io/aeade3ec.html" %})
- [https://www.lianxh.cn/news/ac0f7a163237d.html]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/www.lianxh.cn/b9cac1b0.html" %})
- [https://zhuanlan.zhihu.com/p/488290289]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/zhuanlan.zhihu.com/b8d23c85.html" %})
- [https://zhuanlan.zhihu.com/p/32877396]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/zhuanlan.zhihu.com/3d4e3ec1.html" %})
- [https://zhuanlan.zhihu.com/p/77750026]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/zhuanlan.zhihu.com/685aa42d.html" %})
- [https://mp.weixin.qq.com/s/kbY8Y3BDmXTm2-wA3eLpMw]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/mp.weixin.qq.com/4c1e2cb5.html" %})
- [http://c.biancheng.net/ml_alg/ensemble-learning.html]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/c.biancheng.net/c8d9d204.html" %})
- [https://blog.csdn.net/a321123b/article/details/119451920]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/blog.csdn.net/66172b00.html" %})
- [https://blog.csdn.net/Dark_Scope/article/details/53150883]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/blog.csdn.net/1144a827.html" %})
- [https://zhuanlan.zhihu.com/p/82105066]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/zhuanlan.zhihu.com/46a745ec.html" %})
- [https://www.jianshu.com/p/56985bcfac66]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/www.jianshu.com/2cac5546.html" %})
- [http://events.jianshu.io/p/c0ced4833192]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence.md/events.jianshu.io/6236c9dc.html" %})
