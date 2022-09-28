---
layout: post
title: "深度学习 -- 吴恩达机器学习（进行中……）"
author:
location: "珠海"
categories: ["深度学习"]
tags: ["机器学习", "深度学习"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
date: 2022-08-31 19:57:58 +0800
---

[机器学习应补充哪些数学基础？ {% include relref_weixin.html %}](https://mp.weixin.qq.com/s?__biz=MzU2NTUwNjQ1Mw==&mid=2247485091&idx=1&sn=8844a2dfafcd35ea45d1bf0146ba8a5a&chksm=fcbbfe59cbcc774f68a18bd11d529422e0048896ffa3a253c52a749fc6e45d7292e1791052da&scene=27#wechat_redirect)

入门的话，本科的数学分析，线性代数，概率论与数理统计足够了。
微积分：MIT 18.01, MIT 18.02
线性代数：MIT 18.06
概率论与数理统计：MIT 6.041
凸优化：CVX101

> 人工智能依然不会思考，但依靠亿万次运算也足够在很多工作上处理地比大多数人更好。人们讨论的新问题是，人工智能会不会强化偏见。


## 吴恩达

* [吴恩达机器学习系列课程 {% include relref_bili.html %}](https://www.bilibili.com/video/BV164411b7dx)
* [视频的讲义 {% include relref_github.html %}](https://github.com/TheisTrue/MLofAndrew-Ng)

* <https://www.coursera.org/specializations/deep-learning>
* <https://www.coursera.org/learn/machine-learning-course/home/week/1>
* <https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes>
* <http://www.ai-start.com/ml2014/>


### 有监督学习和无监督学习

监督（supervised）= 标签（label），是否有监督，就是输入数据（input）是否有标签，有标签则为有监督学习，没标签则为无监督学习。
至于半监督学习，就是一半（一点点）数据有标签，一半（极其巨大）数据没标签。

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/20190717172554930.png" %}

#### 监督学习

[from {% include relref_jianshu.html %}](https://www.jianshu.com/p/682c88cee5a8)

定义：根据已有的数据集，知道输入和输出结果之间的关系。根据这种已知的关系，训练得到一个最优的模型。
也就是说，在监督学习中训练数据既有特征（feature）又有标签（label），通过训练，让机器可以自己找到特征和标签之间的联系，
在面对只有特征没有标签的数据时，可以判断出标签。

监督学习的分类：回归（Regression）、分类（Classification）。

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/20211108161254.png" %}

#### 无监督学习

定义：我们不知道数据集中数据、特征之间的关系，而是要根据聚类或一定的模型得到数据之间的关系。

Cocktail party problem algorithm:
$$
[W, s, v]=\operatorname{svd}\left((\operatorname{repmat}(\operatorname{sum}(x . * x, 1), \operatorname{size}(x, 1), 1) . * x) * x^{\prime}\right)
$$

[note](https://cs.nyu.edu/~roweis/kica.html)
** xx are the mixed microphone measurements (one per column)
** W is the unmixing matrix.
```
% W = kica(xx);
yy = sqrtm(inv(cov(xx')))*(xx-repmat(mean(xx,2),1,size(xx,2)));
[W,ss,vv] = svd((repmat(sum(yy.*yy,1),size(yy,1),1).*yy)*yy');
```


## **Octave** P6 start...


### 1-1. 欢迎参加《机器学习》课程 06:56

完成了。


### 1-2. 什么是机器学习？ 07:15

完成了。


### 1-3. 监督学习 12:30

定义：根据已有的数据集，知道输入和输出结果之间的关系。


### 1-4. 无监督学习 14:14

定义：我们不知道数据集中数据、特征之间的关系，而是要根据聚类或一定的模型得到数据之间的关系。


### 2-1. 模型描述 08:11

yes.


### 2-2. 代价函数 08:13

代价函数：
$$
J \left( \theta_0, \theta_1 \right) = \frac{1}{2m}\sum\limits_{i=1}^m \left( h_{\theta}(x^{(i)})-y^{(i)} \right)^{2}
$$

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/v2-c94c2b2ffd3d45539f5c80ab2addffcd_720w.jpg" %}

为什么要除以 2，感觉是要让数字小一点，更直观，便于计算。


### 2-3. 代价函数（一） 11:10

完成。


### 2-4. 代价函数（二） 08:49

等高线图。


### 2-5. 梯度下降 11:31

**Gradient descent algorithm**

repeat until convergence \{
$\theta_j:=\theta_j-\alpha \frac{\partial}{\partial \theta_i} J\left(\theta_0, \theta_1\right)$
$($ for $j=0$ and $j=1$ $)$
\}
* $\alpha$ **learning rate** ，梯度下降时，我们迈出多大的步子。
* $\frac{\partial}{\partial \theta_i} J\left(\theta_0, \theta_1\right)$ 偏导。

Correct: Simultaneous update
$$
\begin{aligned}
&\text { temp } 0:=\theta_0-\alpha \frac{\partial}{\partial \theta_0} J\left(\theta_0, \theta_1\right) \\
&\text { temp } 1:=\theta_1-\alpha \frac{\partial}{\partial \theta_1} J\left(\theta_0, \theta_1\right) \\
&\theta_0:=\text { temp0 } \\
&\theta_1:=\text { temp1 }
\end{aligned}
$$


### 2-6. 梯度下降知识点总结 11:52

完成。鞍点？


### 2-7. 线性回归的梯度下降 10:21

$$
\begin{aligned}
\theta_0 &:=\theta_0-\alpha \frac{1}{m} \sum_{i=1}^m\left(h_\theta\left(x^{(i)}\right)-y^{(i)}\right) \\
\theta_1 &:=\theta_1-\alpha \frac{1}{m} \sum_{i=1}^m\left(h_\theta\left(x^{(i)}\right)-y^{(i)}\right) \cdot x^{(i)}
\end{aligned}
$$


### 3-1. 矩阵和向量 08:46

矩阵维度：$rows \times cols$

Vector: An nx1 matrix.


### 3-2. 加法和标量乘法 06:55


### 3-3. 矩阵向量乘法 13:40


### 3-4. 矩阵乘法 11:10

ok. 03"13


### 3-5. 矩阵乘法特征 09:03

- Associative and distributive
- $(AB)C=A(BC)$
- $A(B+C) = AB + AC$
- $(A+B)C = AC + BC$
- 有交换律，没有交换律。
- $(A B)^{T}=B^{T} A^{T}$


### 3-6. 逆和转置 11:14

并不是每个矩阵都存在逆矩阵。


### 4-1. 多功能 08:23


### 4-2. 多元梯度下降法 05:05

Hypothesis: $\quad h_\theta(x)=\theta^T x=\theta_0 x_0+\theta_1 x_1+\theta_2 x_2+\cdots+\theta_n x_n$

Parameters: $\theta_0, \theta_1, \ldots, \theta_n$

Cost function:
$$
J\left(\theta_0, \theta_1, \ldots, \theta_n\right)=\frac{1}{2 m} \sum_{i=1}^m\left(h_\theta\left(x^{(i)}\right)-y^{(i)}\right)^2
$$


### 4-3. 多元梯度下降法演练 .I.–. 特征缩放 08:53

先把每个输入的特征归一化到特定的范围。
可以加快迭代收敛速度。


### 4-4. 多元梯度下降法 II.–. 学习率 08:59


### 4-5. 特征和多项式回归 07:40

尝试二次函数拟合。


### 4-6. 正规方程（区别于迭代方法的直接解法） 16:19

通过解偏导函数等于 0 的情况，直接求出最小值的 $\theta$。

$$
\theta=(X^TX)^{-1}X^Ty
$$

矩阵求逆只能采用高斯消元法，时间复杂度 $O(n^3)$。


### 4-7. 正规方程在矩阵不可逆情况下的解决方法 06:00

$X^T\*X$ 出现不可逆的情况原因可能是：
1. 方阵中的两个维度之间存在线性变换关系，导致方阵不满秩（奇异或退化矩阵）
2. n（特征数量）相较于 m（样本数量）过大，导致其产生的齐次方程组 $Ax=0$ 不只有零解


### 4-8. 导师的编程小技巧 03:34

完成了。[Octave](https://www.octave.org/)

[安装文档](https://cloud.tencent.com/developer/article/1650390)
[Symbolic](https://octave.sourceforge.io/symbolic/index.html)


### 5-1. 基本操作 14:00


### 5-2. 移动数据 16:08


### 5-3. 计算数据 13:16

伪逆矩阵 $pinv(A)$


### 5-4. 数据绘制 09:39

```python
plot(t,y);
hold on;
plot(t,y2,'r');

A = magic(5)
imagesc(A)
imagesc(A), colorbar, colormap gray;
```


### 5-5. 控制语句：for，while，if. 语句 12:57

定义函数：
```python
function [y1,y2] = squareAndCubeThisNumber(x)
y1 = x ^ 2;
y2 = x ^ 3;
```

```python
function J = costFunctionJ(x, y, theta)

m = size(X, 1);
predictions = X * theta;
sqrErrors = (predictions - y) .^ 2;

J = 1/(2*m) * sum(sqrErrors);
```


### 5-6. 矢量 13:49

$h_\theta (x)=\theta^Tx$

$$
\theta=\left[\begin{array}{l}
\theta_0 \\
\theta_1 \\
\theta_2
\end{array}\right] \quad x=\left[\begin{array}{l}
x_0 \\
x_1 \\
x_2
\end{array}\right]
$$


### 6-1. 分类 08:09

logistic


### 6-2. 假设陈述 07:25

Sigmoid function & Logistic function

1. $h_{\theta}(x)=g(\theta^Tx)$
2. $g(z)=1/(1+e^{-z})$

$h_{\theta}(x) =P(y=1\|x;\theta)$

$$
\begin{array}{l}P(y=0 \mid x ; \theta)+P(y=1 \mid x ; \theta)=1 \\h_{\theta}(x)=P(y=1 \mid x ; \theta)=1-P(y=0 \mid x ; \theta)\end{array}
$$

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/v2-e5d8e804c0af6a097700cec2be5e7834_720w.jpg" caption="logistic function (S-shape)" %}
{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/20191130021642167.png" %}


### 6-3. 决策界限 14:50

**决策边界**


### 6-4. 代价函数 10:25


### 6-5. 简化代价函数与梯度下降 10:16

统计学中极大似然法得来的，快速寻找参数的方法。
{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/v2-37a0e94bf99b619c6b57518671602e19_1440w.jpg" %}
[快速理解极大似然法 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/89074979)
{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/v2-5f4f12bc7ef874f68ea28c4c350ad73f_1440w.jpg" caption="不同参数下高斯分布的形状" %}


### 6-6. 高级优化 14:07

* Gradient descent
* Conjugate gradient
* BFGS 共轭梯度法
* L-BFGS

Example:
$$
\begin{aligned}
&\theta=\left[\begin{array}{l}
\theta_1 \\
\theta_2
\end{array}\right] \\
&J(\theta)=\left(\theta_1-5\right)^2+\left(\theta_2-5\right)^2 \\
&\frac{\partial}{\partial \theta_1} J(\theta)=2\left(\theta_1-5\right) \\
&\frac{\partial}{\partial \theta_2} J(\theta)=2\left(\theta_2-5\right)
\end{aligned}
$$


### 6-7. 多元分类：一对多 06:16

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/1800369-20190923214320485-513783816.png" %}

[Docs / Azure / 机器学习](https://docs.microsoft.com/zh-cn/azure/machine-learning/component-reference/one-vs-all-multiclass)


### 7-1. 过拟合问题 09:43

* undefit, high bias. 高偏差。
* just right.
* overfit, high variance.

过拟合问题（overfitting）
* Underfitting（欠拟合）–> high bias（高偏差）
* Overfitting（过拟合）–> high variance（高方差）

Overfitting: If we have too many features, the learned hypothesis（假设）
may fit the training set very well, but fail to generalize to new examples (predict prices on new examples).
模型泛化能力差

addressing overfitting 解决过拟合的方法：
options:
1. reduce number of features（减少特征数量）
    1. Manually select which features to keep 人为的保留一些重要的特征值
    2. Model selection algorithm（模型选择算法）用特征选择算法进行特征的选择（PCA、层次分析法）
2. regularization（正则化）
    1. keep all the features but reduce magnitude/values（但减少参数的大小 / 值）of parameters $\theta_j$.
        * 通过对目标函数添加一个参数范数惩罚，限制模型的学习能力。（保留所有的特征，但是减少参数 $\theta$ 的大小）
    2. Works well when we have a lot of features, each of which contributes a bit to predicting $y$.
        * 最终要找到一个平衡点，使得模型能够更好地拟合训练集并且同时具有良好的泛化能力。


### 7-2. 代价函数 10:12

$$
J(\theta)=\frac{1}{2 m}\left[\sum_{i=1}^m\left(h_\theta\left(x^{(i)}\right)-y^{(i)}\right)^2+\lambda \sum_{j=1}^n \theta_j^2\right]
$$


### 7-3. 线性回归的正则化 10:41

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/v2-86856ef352e507ca0f853343e802cbd8_720w.jpg" %}
{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/v2-b3f8923467e9314b1d03f0e756189bbd_720w.jpg" %}

[note {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/410358244)

$$
\theta=\left(X^{T} X\right)^{-1} X^{T} y
$$

$$
\text { If } \lambda>0 \text {, }
$$

$$
\theta=\left(X^{T} X+\lambda\left[\begin{array}{lllll}0 & & & & \\& 1 & & & \\& & 1 & & \\& & & \ddots & \\& & & & 1\end{array}\right]\right)^{-1} X^{T} y
$$

#### L1 和 L2 正则项

* 当正则化项为 $\lambda\sum_{j=1}^{n}{\theta_{j}^{2}}$ 时，称为 L2 正则化，也称为岭回归（Ridge 回归）。
* 当正则化项为 $\lambda\sum_{j=1}^{n}\|{\theta_{j}}\|$ 时，称为 L1 正则化，也称为 Lasso 回归。

相比 L2 正则化，L 正则化会产生更稀疏的解，此处稀疏性指的是最优值中的一些参数为 0，和 L2 正则化相比，L1 正则化的稀疏性具有本质的不同。

由 L1 正则化导出的稀疏性质已被广泛地用于特征选择机制，特征选择从可用的特征子集选择出有意义的特征，化简问题。
如 Lasso 回归中，L1 惩罚使得部分参数为 0，表明相应的特征可以被安全得忽略。


### 7-4. Logistic. 回归的正则化 08:35

yes。


### 8-1. 非线性假设 09:37


### 8-2. 神经元与大脑 07:48


### 8-3. 模型展示 Ⅰ 12:02


### 8-4. 模型展示 Ⅱ 11:47

前向传播。


### 8-5. 例子与直觉理解 Ⅰ 07:16

AND / OR


### 8-6. 例子与直觉理解 Ⅱ 10:21

手写数字识别。


### 8-7. 多元分类 03:52


### 9-1. 代价函数 06:44

Cost function, Logistic regression:
$$
J(\theta)=-\frac{1}{m}\left[\sum_{i=1}^{m} y^{(i)} \log h_{\theta}\left(x^{(i)}\right)+\left(1-y^{(i)}\right) \log \left(1-h_{\theta}\left(x^{(i)}\right)\right)\right]+\frac{\lambda}{2 m} \sum_{j=1}^{n} \theta_{j}^{2}
$$

Neural network:
$$
\begin{array}{l}
h_{\Theta}(x) \in \mathbb{R}^{K} \quad\left(h_{\Theta}(x)\right)_{i}=i^{t h} \text { output }\\
J(\Theta)=-\frac{1}{m}\left[\sum_{i=1}^{m} \sum_{k=1}^{K} y_{k}^{(i)} \log \left(h_{\Theta}\left(x^{(i)}\right)\right)_{k}+\left(1-y_{k}^{(i)}\right) \log \left(1-\left(h_{\Theta}\left(x^{(i)}\right)\right)_{k}\right)\right]\\+\frac{\lambda}{2 m} \sum_{l=1}^{L-1} \sum_{i=1}^{s_{l}} \sum_{j=1}^{s_{l+1}}\left(\Theta_{j i}^{(l)}\right)^{2}\end{array}
$$


### 9-2. 反向传播算法 12:00

**为了计算代价函数的偏导数 $\frac{\partial}{\partial\Theta^{(l)}_{ij}}J\left(\Theta\right)$，**
**我们需要采用一种反向传播算法**，也就是首先计算最后一层的误差，然后再一层一层反向求出各层的误差，
直到倒数第二层。


### 9-3. 理解反向传播 12:45

？？？


### 9-4. 使用注意：展开参数 07:48


### 9-5. 梯度检测 11:38

梯度近似值：
$$
gradApprox = (J(\theta + \epsilon) – J(\theta - \epsilon)) / (2*\epsilon)
$$

Implementation Note:
* Implement backprop to compute DVec (unrolled $D^{(1)}$, $D^{(2)}$, $D^{(3)}$).
* Implement numerical gradient check to compute gradApprox.
* Make sure they give similar values.
* Turn off gradient checking. Using backprop code for learning.

Important:
* Be sure to disable your gradient checking code before training your classifier.
    If you run numerical gradient computation on every iteration of gradient descent
    (or in the inner loop of costFunction(…))your code will be very slow.


### 9-6. 随机初始化 06:52


### 9-7. 组合到一起 13:24

网络结构：第一件要做的事是选择网络结构，即决定选择多少层以及决定每层分别有多少个单元。

第一层的单元数即我们训练集的特征数量。
最后一层的单元数是我们训练集的结果的类的数量。

如果隐藏层数大于 1，确保每个隐藏层的单元个数相同，通常情况下隐藏层单元的个数越多越好。
我们真正要决定的是隐藏层的层数和每个中间层的单元数。

训练神经网络：
1. 参数的随机初始化
2. 利用正向传播方法计算所有的 $h_{\theta}(x)$
3. 编写计算代价函数 $J$ 的代码
4. 利用反向传播方法计算所有偏导数
5. 利用数值检验方法检验这些偏导数
6. 使用优化算法来最小化代价函数


### 9-8. 无人驾驶 06:31

**ALVINN**（**Autonomous Land Vehicle In a Neural Network**）是一个基于神经网络的智能系统，通过观察人类的驾驶来学习驾驶，
**ALVINN** 能够控制 **NavLab**，装在一辆改装版军用悍马，这辆悍马装载了传感器、计算机和驱动器用来进行自动驾驶的导航试验。
实现 **ALVINN** 功能的第一步，是对它进行训练，也就是训练一个人驾驶汽车。


### 10-1. 决定下一步做什么 05:51


### 10-2. 评估假设 07:36

**评估是否过度拟合**
为了检验算法是否过拟合，我们将数据分成训练集和测试集，
通常用 70% 的数据作为训练集，用剩下 30% 的数据作为测试集。
很重要的一点是训练集和测试集均要含有各种类型的数据，
通常我们要对数据进行“洗牌”，然后再分成训练集和测试集。


### 10-3. 模型选择和训练、验证、测试集 12:04

**多个模型，怎么选择？**
泛化能力。模型选择的方法为：
1. 使用训练集训练出 10 个模型
2. 用 10 个模型分别对交叉验证集计算得出交叉验证误差（代价函数的值）
3. 选取代价函数值最小的模型
4. 用步骤 3 中选出的模型对测试集计算得出推广误差（代价函数的值）

***Train/validation/test error***

**Training error:**
$$J_{train}(\theta) = \frac{1}{2m}\sum_\limits{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})^2$$

**Cross Validation error:**
$$J_{cv}(\theta) = \frac{1}{2m_{cv}}\sum_\limits{i=1}^{m}(h_{\theta}(x^{(i)}_{cv})-y^{(i)}_{cv})^2$$

**Test error:**
$$J_{test}(\theta)=\frac{1}{2m_{test}}\sum_\limits{i=1}^{m_{test}}(h_{\theta}(x^{(i)}_{cv})-y^{(i)}_{cv})^2$$


### 10-4. 诊断偏差与方差 07:43

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/bca6906add60245bbc24d71e22f8b836.png" %}

* 训练集误差和交叉验证集误差近似时：偏差 / 欠拟合
* 交叉验证集误差远大于训练集误差时：方差 / 过拟合
{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/25597f0f88208a7e74a3ca028e971852.png" %}


### 10-5. 正则化和偏差、方差 11:21

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/38eed7de718f44f6bb23727c5a88bf5d.png" %}
* 训练集误差和交叉验证集误差近似时：偏差 / 欠拟合
* 交叉验证集误差远大于训练集误差时：方差 / 过拟合


### 10-6. 学习曲线 11:54


### 10-7. 决定接下来做什么 06:51

1. 获得更多的训练样本 —— 解决高方差
2. 尝试减少特征的数量 —— 解决高方差
3. 尝试获得更多的特征 —— 解决高偏差
4. 尝试增加多项式特征 —— 解决高偏差
5. 尝试减少正则化程度 λ —— 解决高偏差
6. 尝试增加正则化程度 λ —— 解决高方差


### 11-1. 确定执行的优先级 09:30

垃圾邮件分类。


### 11-2. 误差分析 13:13

构建一个学习算法的推荐方法为：
1. 从一个简单的能快速实现的算法开始，实现该算法并用交叉验证集数据测试这个算法
2. 绘制学习曲线，决定是增加更多数据，或者添加更多特征，还是其他选择
3. 进行误差分析：人工检查交叉验证集中我们算法中产生预测误差的样本，看看这些样本是否有某种系统化的趋势


### 11-3. 不对称性分类的误差评估 11:36

偏斜类。

查准率。
召回率。

**查准率**（**Precision**）和**查全率**（**Recall**） 我们将算法预测的结果分成四种情况：

1. **正确肯定**（**True Positive, TP**）：预测为真，实际为真
2. **正确否定**（**True Negative, TN**）：预测为假，实际为假
3. **错误肯定**（**False Positive, FP**）：预测为真，实际为假（假阳性）
4. **错误否定**（**False Negative, FN**）：预测为假，实际为真（假阴性）

则：查准率 =**TP/(TP+FP)**。例，在所有我们预测有恶性肿瘤的病人中，实际上有恶性肿瘤的病人的百分比，越高越好。

查全率 =**TP/(TP+FN)**。例，在所有实际上有恶性肿瘤的病人中，成功预测有恶性肿瘤的病人的百分比，越高越好。

这样，对于我们刚才那个总是预测病人肿瘤为良性的算法，其查全率是 0。

|            |              | **预测值**   |             |
| ---------- | ------------ | ------------ | ----------- |
|            |              | **Positive** | **Negtive** |
| **实际值** | **Positive** | **TP**       | **FN**      |
|            | **Negtive**  | **FP**       | **TN**      |

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/20220926001838.png" %}


### 11-4. 精确度和召回率的权衡 14:06

$F_1$ Score (F score)

$$
2\frac{PR}{P+R}
$$


### 11-5. 机器学习数据 11:10

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/05a3c884505e08028d37a04472d0964a.png" %}
* 参数多，特征多，保证低偏差。
* 数据样本多，就不太可能过拟合，保证低方差。

这是一个关键的假设：特征值有足够的信息量，且我们有一类很好的函数，这是为什么能保证低误差的关键所在。它有大量的训练数据集，这能保证得到更多的方差值，因此这给我们提出了一些可能的条件，如果你有大量的数据，而且你训练了一种带有很多参数的学习算法，那么这将会是一个很好的方式，来提供一个高性能的学习算法。


### 12-1. 优化目标 14:48


### 12-2. 直观上对大间隔的理解 10:37


### 12-3. 大间隔分类器的数学原理 19:42


### 12-4. 核函数 1 15:45


### 12-5. 核函数 2 15:44


### 12-6. 使用 SVM 21:03


### 13-1. 无监督学习 03:18


### 13-2. K-Means 算法 12:33


### 13-3. 优化目标 07:05


### 13-4. 随机初始化 07:50


### 13-5. 选取聚类数量 08:23


### 14-1. 目标 .I：数据压缩 10:10


### 14-2. 目标 .II：可视化 05:28


### 14-3. 主成分分析问题规划 1 09:06


### 14-4. 主成分分析问题规划 2 15:15


### 14-5. 主成分数量选择 10:31


### 14-6. 压缩重现 03:55


### 14-7. 应用 .PCA. 的建议 12:49


### 15-1. 问题动机 07:39


### 15-2. 高斯分布 10:28


### 15-3. 算法 12:03


### 15-4. 开发和评估异常检测系统 13:08


### 15-5. 异常检测 .VS. 监督学习 07:37


### 15-6. 选择要使用的功能 12:18


### 15-7. 多变量高斯分布 13:47


### 15-8. 使用多变量高斯分布的异常检测 14:04


### 16-1. 问题规划 07:55


### 16-2. 基于内容的推荐算法 14:32


### 16-3. 协同过滤 10:15


### 16-4. 协同过滤算法 08:28


### 16-5. 矢量化：低轶矩阵分解 08:29


### 16-6. 实施细节：均值规范化 08:32


### 17-1. 学习大数据集 05:46


### 17-2. 随机梯度下降 13:20


### 17-3. Mini-Batch. 梯度下降 06:19


### 17-4. 随机梯度下降收敛 11:32


### 17-5. 在线学习 12:51


### 17-6. 减少映射与数据并行 14:09


### 18-1. 问题描述与 .OCR.pipeline 07:03


### 18-2. 滑动窗口 14:41


### 18-3. 获取大量数据和人工数据 16:21


### 18-4. 天花板分析：下一步工作的 .pipeline 13:51


### 19-1. 总结与感谢 04:43


## 李宏毅

* [李宏毅 2020 机器学习 & 深度学习 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1JE411g7XF)
* 课件：<http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html>

P3 08:42

英语



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-10-11-ml-MLofAndrew-Ng.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://mp.weixin.qq.com/s?__biz=MzU2NTUwNjQ1Mw==&mid=2247485091&idx=1&sn=8844a2dfafcd35ea45d1bf0146ba8a5a&chksm=fcbbfe59cbcc774f68a18bd11d529422e0048896ffa3a253c52a749fc6e45d7292e1791052da&scene=27#wechat_redirect]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/mp.weixin.qq.com/68945947.html" %})
- [https://www.bilibili.com/video/BV164411b7dx]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.bilibili.com/72ebaee9.html" %})
- [https://github.com/TheisTrue/MLofAndrew-Ng]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/github.com/f1eeb779.html" %})
- [https://www.coursera.org/specializations/deep-learning]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.coursera.org/f044c5d5.html" %})
- [https://www.coursera.org/learn/machine-learning-course/home/week/1]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.coursera.org/53a67f91.html" %})
- [https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/github.com/9e99497d.html" %})
- [http://www.ai-start.com/ml2014/]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.ai-start.com/21b3ffdf.html" %})
- [https://www.jianshu.com/p/682c88cee5a8]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.jianshu.com/fdc8f898.html" %})
- [https://cs.nyu.edu/~roweis/kica.html]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/cs.nyu.edu/89374dba.html" %})
- [https://www.octave.org/]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.octave.org/461e7f5e.html" %})
- [https://cloud.tencent.com/developer/article/1650390]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/cloud.tencent.com/0075b71d.html" %})
- [https://octave.sourceforge.io/symbolic/index.html]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/octave.sourceforge.io/044f4336.html" %})
- [https://zhuanlan.zhihu.com/p/89074979]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/zhuanlan.zhihu.com/89dee774.html" %})
- [https://docs.microsoft.com/zh-cn/azure/machine-learning/component-reference/one-vs-all-multiclass]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/docs.microsoft.com/c6aa7749.html" %})
- [https://zhuanlan.zhihu.com/p/410358244]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/zhuanlan.zhihu.com/0da53915.html" %})
- [https://www.bilibili.com/video/BV1JE411g7XF]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.bilibili.com/68e17dc9.html" %})
- [http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/speech.ee.ntu.edu.tw/f319f059.html" %})
