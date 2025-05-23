---
layout: post
title: "机器学习 -- 吴恩达深度学习（进行中）"
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
date: 2022-08-31 19:57:58 +0800
cluster: "机器学习课程"
---

* 吴恩达机器学习 19:37:16 142 <https://www.bilibili.com/video/BV1Bq421A74G/>
* 吴恩达深度学习 27:44:07 183 <https://www.bilibili.com/video/BV1FT4y1E74V/>
* [html2text](http://www.atoolbox.net/Tool.php?Id=715)

机器学习早期版本（岁月觞）：[吴恩达机器学习系列课程 {% include relref_bili.html %}](https://www.bilibili.com/video/BV164411b7dx/)


# 吴恩达机器学习


## 1 1.1 欢迎来到机器学习 ! 02:45


## 2 1.2 机器学习的应用 04:29


## 3 2.1 什么是机器学习 05:36


## 4 2.2 监督学习 part 1 06:57


## 5 2.3 监督学习 part 2 07:17


## 6 2.4 非监督学习 part 1 08:54


## 7 2.5 非监督学习 part 2 03:40


## 8 2.6 Jupyter Notebooks 04:30


## 9 3.1 线性回归模型 part 1 10:27


## 10 3.2 线性回归模型 part 2 06:45


## 11 3.3 代价函数 09:05

$$
J(w, b)=\frac{1}{2 m} \sum_{i=1}^m\binom{\hat{y}^{(i)}-y^{(i)}}{\text { error }}^2
$$


## 12 3.4 代价函数的直观理解 15:47


## 13 3.5 可视化代价函数 08:34


## 14 3.6 可视化的例子 06:01


## 15 4.1 梯度下降 08:04


## 16 4.2 实现梯度下降 10:00


## 17 4.3 梯度下降的直观理解 07:02


## 18 4.4 学习率 09:04


## 19 4.5 线性回归中的梯度下降 06:37


## 20 4.6 运行梯度下降 05:49


## 21 5.1 多类特征 09:52


## 22 5.2 向量化 part 1 06:55


## 23 5.3 向量化 part 2 06:53


## 24 5.4 多元线性回归的梯度下降法 07:47


## 25 6.1 特征缩放 part 1 06:36


## 26 6.2 特征缩放 part 2 07:35


## 27 6.3 检查梯度下降是否收敛 05:40


## 28 6.4 学习率的选择 06:07


## 29 6.5 特征工程 03:05


## 30 6.6 多项式回归 05:53


## 31 7.1 Motivations 09:48


## 32 7.2 逻辑 (logistic) 回归 09:49


## 33 7.3 决策边界 10:43


## 34 8.1 逻辑回归的代价函数 12:00

$$
\begin{aligned}
& J(\overrightarrow{\mathrm{w}}, b)=\frac{1}{m} \sum_{i=1}^m \underbrace{L\left(f_{\overrightarrow{\mathrm{w}}, b}\left(\overrightarrow{\mathrm{x}}^{(i)}\right), y^{(i)}\right)}_{\operatorname{loss}} \\
& \rightarrow=\left\{\begin{aligned}
-\log \left(f_{\overrightarrow{\mathrm{w}}, b}\left(\overrightarrow{\mathrm{x}}^{(i)}\right)\right) & \text { if } y^{(i)}=1 \\
-\log \left(1-f_{\overrightarrow{\mathrm{w}}, b}\left(\overrightarrow{\mathrm{x}}^{(i)}\right)\right) & \text { if } y^{(i)}=0
\end{aligned}\right.
\end{aligned}
$$

变化一下，转成 凸函数（convex function）。


## 35 8.2 逻辑回归的简化版代价函数 05:46

$$
L\left(f_{\bar{w}, b}\left(\mathrm{x}^{(i)}\right), y^{(i)}\right)=-y^{(i)} \log \left(f_{\bar{w}, b}\left(\vec{x}^{(i)}\right)\right)-\left(1-y^{(i)}\right) \log \left(1-f_{\bar{w}, b}\left(\vec{x}^{(i)}\right)\right)
$$


## 36 9.1 梯度下降实现 06:32


## 37 10.1 过拟合的问题 11:53


## 38 10.2 解决过拟合 08:16


## 39 10.3 正则化代价函数 09:04

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240603231306.png" %}
{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240603232039.png" %}

越高阶的，参数越大，平衡后，更趋向于低阶，从而达到正则化的目的。


## 40 10.4 正则化线性回归 08:53


## 41 10.5 正则化 logistic 回归 05:33


## 42 1.1 欢迎来到第二部分 \_ 高级学习算法 02:54


## 43 1.2 神经元和大脑 10:53


## 44 1.3 需求预测 16:24


## 45 1.4 例子：图像识别 06:36


## 46 2.1 神经网络中的层 09:50


## 47 2.2 更复杂的神经网络 07:19


## 48 2.3 推理：做出预测（前向传播） 05:24


## 49 3.1 代码中的推理 07:13


## 50 3.2 TensorFlow 中的数据 11:20


## 51 3.3 构建一个神经网络 08:21


## 52 4.1 在一个单层中的前向传播 05:07


## 53 4.2 前向传播的一般实现 07:53


## 54 5.1 是否有路通向 AGI（通用人工智能） 10:35

看了吴恩达和李飞飞的采访，目前的人工智能距离 AGI 还存在无法逾越的鸿沟。人类目前对大脑的工作原理不得而知，大脑的每个神经元是一个活体细胞，而大模型的每个神经元还是很简陋的函数。宇宙为什么会诞生生命？意识来源是啥？不得而知。

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/2d6b0ae7300461af0098ef82113271.jpg" %}


## 55 6.1 神经网络如何高效实现 04:23


## 56 6.2 矩阵乘法 09:28


## 57 6.3 矩阵乘法的规则 09:33


## 58 6.4 矩阵乘法代码 06:42


## 59 7.1 TensorFlow 实现 03:38


## 60 7.2 训练细节 13:41

It's still useful to understand how they work under the hood.
So that if something unexpected happends,
You have a better chance of knowing how to fix it.


## 61 8.1 sigmoid 的替代品 05:30

ReLU: rectified linear unit.


## 62 8.2 选择激活函数 08:25

The relu function kind of goes flat only in one part of the graph,
Whereas the sigmoid activation function,
It kind of goes flat in two places.

And if you're using gradient descent to train a neural network,
Then when you have a function that is flat in a lot of places,
Gradient descent will be really slow.

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240611004147.png" %}


## 63 8.3 为什么我们需要激活函数 05:32


## 64 9.1 多类 03:29


## 65 9.2 Softmax 11:33


## 66 9.3 神经网络的 Softmax 输出 07:25


## 67 9.4 softmax 的改进实现 09:13

相当于是为了计算更精确，所以把 softmax 函数运算放到了损失函数里面，而此时模型预测出来的值不再是概率，
必须再经过 softmax 函数还原成预测概率。


## 68 9.5 多个输出的分类 (Optional) 04:20


## 69 10.1 高级优化方法 06:26

每个维度一个学习率，自动调整。
Adam Algorithm Intuition

Adam: Adaptive Moment estimation


## 70 10.2 Additional Layer Types 08:56


## 71 11.1 决定下一步做什么 03:42

搞机器学习最重要的就是分配你的时间。
应该搞数据还是搞算法。

Diagnostic: A test that you run to gain insight into whatis/isn't working with a learning algorithm,
to gain guidanceinto improving its performance.

Diagnostics can take time to implement but doing so can bea very good use of your time.


## 72 11.2 模型评估 10:26

* 70% / 80%
* 30% / 20%


## 73 11.3 模型选择和训练交叉验证测试集 14:53

* 60% 训练集 training set
* 20% 交叉验证集 cross validation
* 20% 测试集 test set


## 74 12.1 诊断偏差和方差 11:13

* Jtrain high, Jcv high
* Jtrain low, Jcv low
* Jtrain low, Jcv high

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240703010732.png" %}

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240703012546.png" %}


## 75 12.2 正则化和偏差或方差 10:37


## 76 12.3 建立表现基准 09:26

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240703234901.png" %}


## 77 12.4 学习曲线 12:14

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240703235720.png" %}

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240704000207.png" caption="High bias" %}
if a learning algorithm suffersfrom high bias, getting moretraining data will not (byitself) help much.

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240704000734.png" caption="High variance" %}
if a learning algorithm suffersfrom high variance, gettingmore training data is likely tohelp.

建立基线作为参考，
这里应该存在三种情况：
1. 数据过少。
    * 往往高方差。加强正则化。
2. 模型过于简单。
    * 往往高偏差。减弱正则化。
3. 模型过于复杂。等价于数据过少。

sometimes, luck is essential


## 78 12.5 再次决定下一步做什么 08:47

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240704003706.png" %}

一时学习，一生去理解。
大体是说，有一个博士生，偏差和方差一生去理解。
07:00
Andrew Ng:
One of my phd students form stanford,
Many years after he had already graduated from stanford,
Once said to be that while he was studying at stanford,
He learned about bias and variance,
But he understood it,
But that susequently,
After many years of work experience and a few different companies,
He realized that,
Bias and variance is one of those concepts that takes a short time to learn,
Beut it takes a lifetime to master.

Andrew Ng:
“One of my PhD students from Stanford,
many years after he had already graduated from Stanford,
once said to me that while he was studying at Stanford,
he learned about bias and variance.
He understood it at the time,
but subsequently,
after many years of work experience at a few different companies,
he realized that
bias and variance are concepts that take a short time to learn,
but a lifetime to master.”


## 79 12.6 偏差或方差与神经网络 10:45

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240704004904.png" %}


## 80 13.1 机器学习的迭代发展 07:43

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240704005744.png" %}


## 81 13.2 误差分析 08:21

看到 13.2 误差分析 00:24


## 82 13.3 添加数据 14:24

数据增强，随机噪声意义不大，因为这些情况在测试集里面不会出现。

用于照片 OCR 的人工数据合成
Artificial data synthesis for photo OCR


## 83 13.4 迁移学习：使用其他任务中的数据 12:11


## 84 13.5 机器学习项目的完整周期 08:45

traditional procedure of statistical study, machine learning <-> statistics


## 85 13.6 公平、偏见与伦理 09:57


## 86 14.1 倾斜数据集的误差指标 11:36

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240708010350.png" %}


## 87 14.2 精确率与召回率的权衡 11:50

F1 score
{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240708010432.png" %}


## 88 15.1 决策树模型 07:06


## 89 15.2 学习过程 11:21


## 90 16.1 测量纯度 07:50

Entropy as a measure of impurity
熵作为杂质的度量
{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240709005338.png" %}


## 91 16.2 选择拆分信息增益 11:52


## 92 16.3 整合 09:29

水。


## 93 16.4 使用分类特征的一种独热编码 (One-Hot) 05:26

热编码 (One-Hot)


## 94 16.5 连续的有价值特征 06:55


## 95 16.6 回归树 (optional) 09:52

有点像贪心算法，不断的按照方差减少最多的选择持续分裂。


## 96 17.1 使用多个决策树 03:57

ensemble of trees
学习是一件很困难的事情，特别是那种纯英文的，稍不留意一走神，就不知道在讲啥了。
需要集中精力 ++。


## 97 17.2 放回抽样 04:00


## 98 17.3 随机森林算法 06:23

随机森林使用一种名为 Bagging 的技术，通过数据集的随机自助抽样样本并行构建完整的决策树。最终得到的预测结果是所有决策树预测结果的平均值。

整个过程有点像正则化的过程。
和 dropout 思想有相似性。


## 99 17.4 XGBoost 07:26

和残差网络有点像，把那些分类不好的重点关注重新分类。

eXtreme Gradient Boosting
<https://www.nvidia.cn/glossary/data-science/xgboost/>

[如何向 10 岁小孩解释 XGBoost 回归算法 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/BJozV5rPJLrynuT1mvbFGQ)
[极端梯度提升（XGBoost）的理论基础 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/Rf2uczXi2JG43Y-utH7YZg)
{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/6402946827.webp" %}

XGBoost 是一种提升树模型，即将许多树模型集成在一起形成一个很强的分类器。

算法思想是不断地添加树，不断地进行特征分裂生成一棵树，每次添加一棵树，就是学习一个新函数，去拟合上次预测的残差，当训练完成就得到了 k 棵树。

根据样本特征在每棵树中会落到对应的一个叶子节点，每个叶子节点对应的一个分数就是该样本的预测分数，将每棵树对应的分数加起来就是该样本的预测值。

XGBoost 工作原理：

1. 初始模型：从一个简单的模型开始（比如一个只输出平均值的模型）。
2. 计算残差：计算该简单模型的“残差”（即模型预测值与实际值之间的差异）。
3. 训练新决策树模型：训练一个新的决策树模型来预测该残差，目标是尽量减小残差。
4. 更新模型：把新决策树模型加入现有模型，使得新的模型可以更好地预测目标值。
5. 重复步骤：重复上述过程，不断加入新的树，每次都使模型的预测更准确，直到达到预定的树的数量或者误差降到可以接受的范围。

XGBoost 跟 ResNet 还有点像，不断计算模型的“残差”，相对模型的黑盒，这个更偏向于可解释的白盒。
每次都以当前预测为基准，下一个弱分类器去拟合误差函数对预测值的残差（预测值与真实值之间的误差）。
损失函数的泰勒展开：XGBoost 利用损失函数的二阶泰勒展开进行优化，提升计算效率。
{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/6403323.webp" %}


## 100 17.5 什么时候使用决策树 06:55

Decision Trees and Tree ensumbles
* Works well on tabular (structured) data
* Not recommended for unstructured data (images, audio, text)
* Fast
* Small decision trees may be human interpretable

Neural Networks
* Works well on all types of data, including tabular (structed) and unstructured data
* May be slower than a decision tree
* Works with transfer learning
* When building a system of multiple models working together, is might be easier to string together multiple neural networks

在表格数据上，基于树的模型仍然优于深度学习方法。
表格数据具有特征不均匀、样本量小、极值较大等特点，因此很难找到相应的不变量。
基于树的模型不可微，不能与深度学习模块联合训练。
在表格数据上，使用基于树的方法比深度学习（甚至是现代架构）更容易实现良好的预测。

越来越感觉随机森林算法是一种变相的正则化，而 XGBoost 算一种残差算法。


## 101 1.1 欢迎来到第三部分 无监督学习、推荐系统和强化学习 03:23


## 102 2.1 什么是聚类 04:13


## 103 2.2 K-means 的直观理解 06:50


## 104 2.3 K-means 算法 09:51


## 105 2.4 优化目标 11:14


## 106 2.5 初始化 K-means 08:54


## 107 2.6 选择聚类的个数 07:58

手肘法 缺陷：大部分情况，可能并不存在明确的肘部。


## 108 3.1 发现异常事件 11:55


## 109 3.2 高斯（正态）分布 10:51

m-1 是样本方差，m 是二阶中心矩。


## 110 3.3 异常检测算法 12:09

多元正态分布。


## 111 3.4 开发和评估异常检测系统 11:39


## 112 3.5 异常检测 vs. 监督学习 08:09

<table class="tablestyle" ntablew="2:2"></table>

Anomaly detection | Supervised learning
---- | ----
Very small number of positive examples (y=1). (0-20 is common). Large number of negative (y=0) examples. 数据量非常小的时候 | Large number of positive and negative examples. **20 positive examples**
Many different "types" of anomalies. Hard for any algorithm to learn from positive examples what the anomalies look like; future anomalies may look nothing like any of the anomalous examples we've seen so far. 可以处理没见过的错误 **Fraud** | Enough positive examples for algorithm to get a sense of what positive examples are like, future positive examples likely to be similar to ones in training set. **Spam**
Fraud detection | Email spam classification
Manufacturing - Finding new previously **unseen** defects in manufacturing. (e.g. aircraft engines) | Manufacturing - Finding known, previously **seen** defects
Monitoring machines in a data center | Weather prediction (sunny / rainy / etc.)
... | Diseases classification


## 113 3.6 选择要使用的特征 14:58

这里有点 SVM 的思想。


## 114 4.1 提出建议 05:33


## 115 4.2 使用每项特征 11:23


## 116 4.3 协同过滤算法 13:56

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240826000520.png" %}


## 117 4.4 Binary labels- favs, likes and c 08:28

二分类问题。


## 118 5.1 均值归一化 08:46


## 119 5.2 协同过滤的 TensorFlow 实现 11:39


## 120 5.3 查找相关项目 06:34


## 121 6.1 协同过滤 vs. 基于内容的过滤 09:46

Collaborative filtering:
* Recommend items to you based on rating of users whogave similar ratings as you.

Content-based filtering:
* Recommend items to you based on features of user and itemto find good match.

有点 CLIP 的思想。


## 122 6.2 Deep learning for content-based 09:43

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20240829013450.png" %}


## 123 6.3 从大目录中推荐 07:53

CLIP & FAISS!!


## 124 6.4 推荐系统的道德使用 10:49


## 125 6.5 基于内容过滤的 TensorFlow 实现 04:49


## 126 7.1 什么是强化学习 08:49


## 127 7.2 火星探测器示例 06:42


## 128 7.3 The Return in reinforcement lear 10:19


## 129 7.4 强化学习中的决策与策略制定 02:38


## 130 7.5 回顾关键概念 05:35


## 131 8.1 状态动作值函数定义 10:37


## 132 8.2 状态动作值函数示例 05:23

经典，。


## 133 8.3 Bellman 方程 12:53

$$
Q(s, a)=R(s)+\gamma \max _{a^{\prime}} Q\left(s^{\prime}, a^{\prime}\right)
$$


## 134 8.4 随机环境（可选） 08:25


## 135 9.1 连续状态空间应用示例 06:25


## 136 9.2 月球着陆器 05:55


## 137 9.3 学习状态值函数 16:51


## 138 9.4 算法优化-改进的神经网络结构 03:02


## 139 9.5 算法优化ϵ-贪婪策略 09:00


## 140 9.6 算法优化-小批量和软更新（可选） 11:44


## 141 9.7 强化学习的状态 02:55


## 142 10.1 总结与感谢 03:12

* Supervised Machine Learning:
    * Regression and Classification
    * Linear regression, logistic regression, gradient descent

* Advanced Learning Algorithms
    * Neural networks, decision trees, advice for ML

* Unsupervised Learning, Recommenders, Reinforcement Learning
    * Clustering, anomaly detection, collaborative filtering,
    * content-based filtering, reinforcement learning


# 吴恩达深度学习


## 1 1.1.1 欢迎 05:33


## 2 2.1.2 什么是神经网络 07:17


## 3 3.1.3 用神经网络进行监督学习 08:30


## 4 4.1.4 为什么深度学习会兴起？ 10:22


## 5 5.1.5 关于这门课 02:29


## 6 6.1.6 课程资源 01:56


## 7 7.2.1 二分分类 08:25


## 8 8.2.2 logistic 回归 06:00


## 9 9.2.3 logistic 回归损失函数 08:12


## 10 10.2.4 梯度下降法 11:24


## 11 11.2.5 导数 07:11


## 12 12.2.6 更多导数的例子 10:28


## 13 13.2.7 计算图 03:34


## 14 14.2.8 使用计算图求导 14:35


## 15 15.2.9 logistic 回归中的梯度下降法 06:43


## 16 16.2.10 m 个样本的梯度下降 08:01


## 17 17.2.11 向量化 08:05


## 18 18.2.12 向量化的更多例子 06:22


## 19 19.2.13 向量化 logistic 回归 07:33


## 20 20.2.14 向量化 logistic 回归的梯度输出 09:39


## 21 21.2.15 Python 中的广播 11:07


## 22 22.2.16 关于 python \_ numpy 向量的说明 06:50 22.2.16 关于 python _ numpy 向量的说明


## 23 23.2.17 Jupyter \_ ipython 笔记本的快速指南 03:44 23.2.17 Jupyter _ ipython 笔记本的快速指南


## 24 24.2.18 （选修）logistic 损失函数的解释 07:16


## 25 25.3.1 神经网络概览 04:27


## 26 26.3.2 神经网络表示 05:15


## 27 27.3.3 计算神经网络的输出 09:59


## 28 28.3.4 多个样本的向量化 09:06


## 29 29.3.5 向量化实现的解释 07:38


## 30 30.3.6 激活函数 10:57


## 31 31.3.7 为什么需要非线性激活函数？ 05:37


## 32 32.3.8 激活函数的导数 07:58


## 33 33.3.9 神经网络的梯度下降法 09:58


## 34 34.3.10 （选修）直观理解反向传播 15:49


## 35 35.3.11 随机初始化 07:58


## 36 36.4.1 深层神经网络 05:52


## 37 37.4.2 前向和反向传播 10:30


## 38 38.4.3 深层网络中的前向传播 07:16


## 39 39.4.4 核对矩阵的维数 11:11


## 40 40.4.5 为什么使用深层表示 10:34


## 41 41.4.6 搭建深层神经网络块 08:34


## 42 42.4.7 参数 VS 超参数 07:18


## 43 43.4.8 这和大脑有什么关系？ 03:18


## 44 44.1. 吴恩达采访 Geoffrey Hinton 40:23


## 45 45.2. 吴恩达采访 Pieter Abbeel 16:04


## 46 46.3. 吴恩达采访 Ian Goodfellow 14:56


## 47 47.1.1 训练 \_ 开发 \_ 测试集 12:05 47.1.1 训练 _ 开发 _ 测试集


## 48 48.1.2 偏差 \_ 方差 08:47 48.1.2 偏差 _ 方差


## 49 49.1.3 机器学习基础 06:22


## 50 50.1.4 正则化 09:43


## 51 51.1.5 为什么正则化可以减少过拟合？ 07:10


## 52 52.1.6 Dropout 正则化 09:26


## 53 53.1.7 理解 Dropout 07:05


## 54 54.1.8 其他正则化方法 08:25


## 55 55.1.9 归一化输入 05:31


## 56 56.1.10 梯度消失与梯度爆炸 06:08


## 57 57.1.11 神经网络的权重初始化 06:13


## 58 58.1.12 梯度的数值逼近 06:36


## 59 59.1.13 梯度检验 06:35


## 60 60.1.14 关于梯度检验实现的注记 05:19


## 61 61.2.1 Mini-batch 梯度下降法 11:30


## 62 62.2.2 理解 mini-batch 梯度下降法 08:15


## 63 63.2.3 指数加权平均 05:59


## 64 64.2.4 理解指数加权平均 09:43


## 65 65.2.5 指数加权平均的偏差修正 04:12


## 66 66.2.6 动量梯度下降法 09:21


## 67 67.2.7 RMSprop 07:42


## 68 68.2.8 Adam 优化算法 07:09


## 69 69.2.9 学习率衰减 06:45


## 70 70.2.10 局部最优的问题 05:24


## 71 71.3.1 调试处理 07:11


## 72 72.3.2 为超参数选择合适的范围 08:51


## 73 73.3.3 超参数训练的实践：Pandas VS Caviar 06:52


## 74 74.3.4 正则化网络的激活函数 08:56


## 75 75.3.5 将 Batch Norm 拟合进神经网络 12:56


## 76 76.3.6 Batch Norm 为什么奏效？ 11:40


## 77 77.3.7 测试时的 Batch Norm 05:47


## 78 78.3.8 Softmax 回归 11:48


## 79 79.3.9 训练一个 Softmax 分类器 10:08


## 80 80.3.10 深度学习框架 04:16


## 81 81.3.11 TensorFlow 16:08


## 82 82.1. 吴恩达采访 Yoshua Bengio 25:49


## 83 83.2. 吴恩达采访 林元庆 13:38


## 84 84.1.1 为什么是 ML 策略 02:44


## 85 85.1.2 正交化 10:39


## 86 86.1.3 单一数字评估指标 07:17


## 87 87.1.4 满足和优化指标 05:59


## 88 88.1.5 训练 \_ 开发 \_ 测试集划分 06:36 88.1.5 训练 _ 开发 _ 测试集划分


## 89 89.1.6 开发集合测试集的大小 05:40


## 90 90.1.7 什么时候该改变开发 \_ 测试集和指标 11:08 90.1.7 什么时候该改变开发 _ 测试集和指标


## 91 91.1.8 为什么是人的表现 05:47


## 92 92.1.9 可避免偏差 07:00


## 93 93.1.10 理解人的表现 11:13


## 94 94.1.11 超过人的表现 06:22


## 95 95.1.12 改善你的模型的表现 04:35


## 96 96.2.1 进行误差分析 10:33


## 97 97.2.2 清除标注错误的数据 13:06


## 98 98.2.3 快速搭建你的第一个系统，并进行迭代 06:02


## 99 99.2.4 在不同的划分上进行训练并测试 10:56


## 100 100.2.5 不匹配数据划分的偏差和方差 18:17


## 101 101.2.6 解决数据不匹配 10:09


## 102 102.2.7 迁移学习 11:18


## 103 103.2.8 多任务学习 13:00


## 104 104.2.9 什么是端到端的深度学习 11:48


## 105 105.2.10 是否要使用端到端的深度学习 10:20


## 106 106.1. 采访 Andrej Karpathy 15:11


## 107 107.2. 采访 Ruslan Salakhutdinov 17:09


## 108 108.1.1 计算机视觉 05:45


## 109 109.1.2 边缘检测示例 11:32


## 110 110.1.3 更多边缘检测内容 07:58


## 111 111.1.4 Padding 09:50


## 112 112.1.5 卷积步长 09:03


## 113 113.1.6 三维卷积 10:45


## 114 114.1.7 单层卷积网络 16:11


## 115 115.1.8 简单卷积网络示例 08:33


## 116 116.1.9 池化层 10:26


## 117 117.1.10 卷积神经网络示例 12:38


## 118 118.1.11 为什么使用卷积？ 09:41


## 119 119.2.1 为什么要进行实例探究？ 03:09


## 120 120.2.2 经典网络 18:20


## 121 121.2.3 残差网络 07:09


## 122 122.2.4 残差网络为什么有用？ 09:13


## 123 123.2.5 网络中的网络以及 1×1 卷积 06:41


## 124 124.2.6 谷歌 Inception 网络简介 10:15


## 125 125.2.7 Inception 网络 08:47


## 126 126.2.8 使用开源的实现方案 04:57


## 127 127.2.9 迁移学习 08:49


## 128 128.2.10 数据扩充 09:32


## 129 129.2.11 计算机视觉现状 12:39


## 130 130.3.1 目标定位 11:55


## 131 131.3.2 特征点检测 05:57


## 132 132.3.3 目标检测 05:50


## 133 133.3.4 卷积的滑动窗口实现 11:09


## 134 134.3.5 Bounding Box 预测 14:32


## 135 135.3.6 交并比 04:20


## 136 136.3.7 非极大值抑制 08:03


## 137 137.3.8 Anchor Boxes 09:44


## 138 138.3.9 YOLO 算法 07:02


## 139 139.3.10 候选区域 06:28


## 140 140.4.1 什么是人脸识别？ 04:38


## 141 141.4.2 One-Shot 学习 04:46 141.4.2  One-Shot 学习


## 142 142.4.3 Siamese 网络 04:36 142.4.3  Siamese 网络


## 143 143.4.4 Triplet 损失 15:31 143.4.4  Triplet 损失


## 144 144.4.5 面部验证与二分类 06:06 144.4.5  面部验证与二分类


## 145 145.4.6 什么是神经风格转换？ 02:03 145.4.6  什么是神经风格转换？


## 146 146.4.7 什么是深度卷积网络？ 07:58 146.4.7  什么是深度卷积网络？


## 147 147.4.8 代价函数 \_bilibili 03:51 147.4.8 代价函数 \_bilibili


## 148 148.4.9 内容代价函数 03:38 148.4.9  内容代价函数


## 149 149.4.10 风格代价函数 17:02 149.4.10  风格代价函数


## 150 150.4.11 一维到三维推广 09:09


## 151 151.1.1 为什么选择序列模型 03:01


## 152 152.1.2 数学符号 09:16


## 153 153.1.3 循环神经网络 16:32


## 154 154.1.4 通过时间的反向传播 06:12


## 155 155.1.5 不同类型的循环神经网络 09:35


## 156 156.1.6 语言模型和序列生成 12:02


## 157 157.1.7 新序列采样 08:39


## 158 158.1.8 带有神经网络的梯度消失 06:29


## 159 159.1.9 GRU 单元 17:07


## 160 160.1.10 长短期记忆（LSTM） 09:54


## 161 161.1.11 双向神经网络 08:20


## 162 162.1.12 深层循环神经网络 05:17


## 163 163.2.1 词汇表征 10:08


## 164 164.2.2 使用词嵌入 09:23


## 165 165.2.3 词嵌入的特性 11:55


## 166 166.2.4 嵌入矩阵 05:58


## 167 167.2.5 学习词嵌入 10:10


## 168 168.2.6 Word2Vec 12:48


## 169 169.2.7 负采样 11:54


## 170 170.2.8 GloVe 词向量 11:09


## 171 171.2.9 情绪分类 07:38


## 172 172.2.10 词嵌入除偏 11:09


## 173 173.3.1 基础模型 06:19


## 174 174.3.2 选择最可能的句子 08:57


## 175 175.3.3 定向搜索 11:55


## 176 176.3.4 改进定向搜索 11:01


## 177 177.3.5 定向搜索的误差分析 09:44


## 178 178.3.6 Bleu 得分（选修） 16:27


## 179 179.3.7 注意力模型直观理解 09:42


## 180 180.3.8 注意力模型 12:24


## 181 181.3.9 语音辨识 08:54


## 182 182.3.10 触发字检测 05:04


## 183 183.3.11 结论和致谢 02:45



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-10-11-ml-DL-Andrew-Ng.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1Bq421A74G/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/738a77eb.html" %})
- [https://www.bilibili.com/video/BV1FT4y1E74V/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/821695be.html" %})
- [http://www.atoolbox.net/Tool.php?Id=715]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.atoolbox.net/ecf02067.php" %})
- [https://www.bilibili.com/video/BV164411b7dx/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/816eb90a.html" %})
- [https://www.nvidia.cn/glossary/data-science/xgboost/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.nvidia.cn/a13b000a.html" %})
- [https://mp.weixin.qq.com/s/BJozV5rPJLrynuT1mvbFGQ]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/mp.weixin.qq.com/911df19b.html" %})
- [https://mp.weixin.qq.com/s/Rf2uczXi2JG43Y-utH7YZg]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/mp.weixin.qq.com/0a09e136.html" %})
