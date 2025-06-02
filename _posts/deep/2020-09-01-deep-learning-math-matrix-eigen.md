---
layout: post
title: "机器学习笔记 -- 线性代数 & 微积分 & 概率论与统计学（进行中）"
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
cluster: "机器学习的数学基础"
---

数学×矩阵的特征值和特征向量


## 定义

设 $A$ 为 $n \times n$ 阶方阵，若存在常数 $\lambda$ 与 $n$ 维非零列向量 $X$ 使 $AX=\lambda X$ 成立，则称 $\lambda$ 为方阵 $A$ 的特征值，非零向量 $X$ 为 $A$ 的对应于 $\lambda$ 的特征向量。

由 $AX=\lambda X$ → $(A-\lambda E)X=0$。

此方程有非零解的充要条件是：$\|A-\lambda E\|=0$，即 **特征多项式方程** ：

$$
\begin{vmatrix}
    a_{11}-\lambda & a_{12} & \dots  & a_{1n} \\
    a_{21} & a_{22}-\lambda & \dots  & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \dots  & a_{nn}-\lambda
\end{vmatrix} = 0
$$

$P_{A}(\lambda)$ 是高次的多项式，它的求根是很困难的。没有数值方法是通过求它的根来求矩阵的特征值。通常对某个特征值，可以用些针对性的方法来求其近似值。若要求所有的特征值，则可以对 $A$ 做一系列的相似变换，“收敛”到对角阵或上（下）三角阵，从而求得所有特征值的近似。


## 举例

求矩阵 $$A=\left(\begin{array}{rr} 3 & -1 \\ -1 & 3 \end{array}\right)$$ 的特征值与特征向量。

解得 $A$ 的两个特征值：$\lambda_1=4$，$\lambda_2=2$。

对应于 $\lambda_1=4$ 的基础解向量：$$\vec{P}_{1}=\left(\begin{array}{r}1 \\-1\end{array}\right)$$。

对应于 $\lambda_2=2$ 的基础解向量：$$\vec{P}_{2}=\left(\begin{array}{r}1 \\1\end{array}\right)$$。


### 乘幂法

幂法是一种迭代法。基本思想：把矩阵的特征值和特征向量作为一个无限序列的极限来求得。求按模最大特征值，即：

$$|\lambda|=\max _{1 \leq i \leq n}\left|\lambda_{i}\right|$$


### 反幂法

求按模最小特征值，即：

$$|\lambda|=\min _{1 \leq i \leq n}\left|\lambda_{i}\right|$$


### 雅可比法（Jacobi）

求实对称矩阵所有特征值和特征向量。


## 参考

<div id="refer-anchor-1"></div>
- [1] [《动手学深度学习》 {% include relref_gluon.html %}](http://zh.gluon.ai/)
- [2] [求二范数 C++ 代码 {% include relref_csdn.html %}](https://blog.csdn.net/tianya_team/article/details/53310617)
- [3] **[计算方法之计算矩阵的特征值和特征量](https://wenku.baidu.com/view/095bebde2a4ac850ad02de80d4d8d15abf23004d.html)**

[机器学习基础 \| 人工智能数学 \| 线性代数 \| 微积分 \| 概率论与统计学 {% include relref_bili.html %}](https://space.bilibili.com/3546736784050628)
[note {% include relref_bili.html %}](https://www.bilibili.com/video/BV12Sc4e7Eat/)
by [atoolbox](http://www.atoolbox.net/Tool.php?Id=715)

唐宇迪
人工智能-数学基础
129 讲全！微积分、概率论、线性代数、机器学习数学基础
* <https://www.bilibili.com/video/BV1FP411L7t1/?129> 5.4w
* <https://www.bilibili.com/video/BV1gQ4y1E7iy/?129> 5.7w
* <https://www.bilibili.com/video/BV1iS4y1W7FP/?129> 2.4w
* <https://www.bilibili.com/video/BV1ah411x76z/?129> 5978


## 3.3-阶数的作用 08:08

泰勒公式（Taylor's formula）是数学分析中的一个重要公式，用于在某一点附近用多项式逼近函数。它以英国数学家 **布鲁克 · 泰勒（Brook Taylor）** 命名，是 **泰勒展开** （Taylor series expansion）的基础。


### **泰勒公式的表达式**

设 $ f(x) $ 在某点 $ x = a $ 处具有足够阶的导数，则可以用泰勒展开式表示它在 $ x $ 附近的近似值：
$$
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots + \frac{f^{(n)}(a)}{n!}(x-a)^n + R_n
$$
其中：
- $ f^{(k)}(a) $ 表示 $ f(x) $ 在 $ x=a $ 处的 **第 $ k $ 阶导数** 。
- $ R_n $ 是 **余项（误差项）** ，表示截断后剩余的误差。


### **泰勒余项**

常见的泰勒余项形式是 **拉格朗日型余项** ：
$$
R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!} (x-a)^{n+1}, \quad \text{ 其中 } \quad \xi \text{ 介于 } a \text{ 和 } x \text{ 之间 }
$$
当 $ n \to \infty $ 且 $ R_n \to 0 $ 时，泰勒级数可以无穷展开，并 **完全等于** 原函数。


### **常见特殊情况**

1. **麦克劳林公式（Maclaurin's formula）**
   当 $ a=0 $ 时，泰勒公式化为：
   $$
   f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \dots + \frac{f^{(n)}(0)}{n!}x^n + R_n
   $$
   这被称为 **麦克劳林展开** （Maclaurin series）。

2. **常见函数的泰勒展开**
   - $ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots $
   - $ \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots $
   - $ \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots $
   - $ \ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots \quad (-1 < x \leq 1) $


### **应用**

- **函数近似** ：在计算机计算中，泰勒展开用于近似复杂函数，提高计算效率。
- **极限计算** ：在微积分中，泰勒展开可以用于求解某些极限问题。
- **微分方程** ：在解微分方程时，泰勒级数提供了一种级数解法。
- **物理学** ：在物理学中，许多公式（如相对论速度加成公式）可以用泰勒展开进行近似。


## 3.5-拉格朗日乘子法 09:54

**拉格朗日乘子法（Lagrange Multiplier Method）** 是一种用于求解 **带约束的最优化问题** （即在一定约束条件下找到目标函数的极值）的数学方法。它通过引入一个或多个 **拉格朗日乘子（Lagrange Multipliers）** 将约束合并到目标函数中，转换为无约束优化问题，从而求解。


### **问题形式**

假设有一个优化问题：
$$
\text{Maximize or Minimize } f(x, y)
$$
在约束条件：
$$
g(x, y) = 0
$$
下求解。

其中：
- $ f(x, y) $ 是 **目标函数** （要极大化或极小化的函数）。
- $ g(x, y) = 0 $ 是 **约束条件** 。


### **拉格朗日函数**

为了将约束条件合并到目标函数中，我们引入一个新的变量 **$ \lambda $（拉格朗日乘子）** ，定义 **拉格朗日函数（Lagrange function）** ：
$$
\mathcal{L}(x, y, \lambda) = f(x, y) - \lambda g(x, y)
$$
然后，我们通过求解 **KKT 条件** （一阶必要条件）来找到极值点。


### **计算步骤**

要找到极值点，需要解以下方程组：
$$
\begin{cases}
\frac{\partial \mathcal{L}}{\partial x} = f_x - \lambda g_x = 0 \\
\frac{\partial \mathcal{L}}{\partial y} = f_y - \lambda g_y = 0 \\
g(x, y) = 0
\end{cases}
$$
其中：
- $ f_x, f_y $ 是目标函数的偏导数。
- $ g_x, g_y $ 是约束函数的偏导数。
- 这三条方程联立求解 $ x, y, \lambda $ 的值。


### **直观理解**

拉格朗日乘子法的几何直觉是：
- **等高线法** ：在约束条件 $ g(x, y) = 0 $ 下，函数 $ f(x, y) $ 的极值点发生在 **目标函数等值线与约束曲线相切** 的地方。
- 在这些点上， **目标函数的梯度（$ \nabla f $）与约束函数的梯度（$ \nabla g $）方向相同** ，即：
   $$
   \nabla f = \lambda \nabla g
   $$
   这说明目标函数在约束条件下不能再沿着约束方向进一步增加或减少。


### **例子**

**例子：**
求解函数 $ f(x, y) = x^2 + y^2 $ 在约束 $ x + y = 1 $ 下的最小值。

**步骤：**
1. **定义拉格朗日函数** ：
   $$
   \mathcal{L}(x, y, \lambda) = x^2 + y^2 - \lambda (x + y - 1)
   $$
2. **求偏导数** ：
   $$
   \frac{\partial \mathcal{L}}{\partial x} = 2x - \lambda = 0 \quad \Rightarrow \quad \lambda = 2x
   $$
   $$
   \frac{\partial \mathcal{L}}{\partial y} = 2y - \lambda = 0 \quad \Rightarrow \quad \lambda = 2y
   $$
   $$
   \frac{\partial \mathcal{L}}{\partial \lambda} = x + y - 1 = 0
   $$
3. **联立方程求解** ：
   $$
   2x = 2y \quad \Rightarrow \quad x = y
   $$
   $$
   x + y = 1 \quad \Rightarrow \quad 2x = 1 \quad \Rightarrow \quad x = \frac{1}{2}, y = \frac{1}{2}
   $$
4. **计算最小值** ：
   $$
   f\left(\frac{1}{2}, \frac{1}{2}\right) = \left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}
   $$

所以， **在 $ x + y = 1 $ 的约束下，$ f(x, y) $ 的最小值是 $ \frac{1}{2} $ ，发生在 $ (x, y) = (\frac{1}{2}, \frac{1}{2}) $** 。


### **拓展**

- **多个约束条件：** 如果有多个约束 $ g_1(x, y) = 0, g_2(x, y) = 0 $，则引入多个拉格朗日乘子 $ \lambda_1, \lambda_2 $ 并构造：
   $$
   \mathcal{L}(x, y, \lambda_1, \lambda_2) = f(x, y) - \lambda_1 g_1(x, y) - \lambda_2 g_2(x, y)
   $$
- **不等式约束：** 拉格朗日乘子法通常用于 **等式约束** ，但可以扩展到 **不等式约束** ，形成 **KKT（Karush-Kuhn-Tucker）条件** ，用于更一般的最优化问题。


### **结论**

**拉格朗日乘子法的核心思想：**
- 通过引入拉格朗日乘子，将 **带约束的优化问题** 转化为 **无约束优化问题** 。
- 目标函数的梯度与约束函数的梯度方向相同（或成比例），即：
   $$
   \nabla f = \lambda \nabla g
   $$
- 适用于 **等式约束优化** 问题，且可以扩展到更复杂的情况（如多个约束或不等式约束）。

这一方法广泛应用于 **经济学、物理学、工程优化、机器学习** 等领域，例如：
- **机器学习** 中的 **拉格朗日对偶（Lagrange Duality）** ，用于支持向量机（SVM）。
- **经济学** 中用于 **效用最大化问题** 。
- **物理学** 中用于 **最小作用量原理** 。


## 5.5-SVD 矩阵分解 11:53

SVD（Singular Value Decomposition，奇异值分解）是矩阵分解的一种方法，适用于任何 $ m \times n $ 的实数或复数矩阵。其基本形式是：

$$
A = U \Sigma V^T
$$

其中：
- $ A $ 是 $ m \times n $ 的原始矩阵。
- $ U $ 是 $ m \times m $ 的正交矩阵（列向量为左奇异向量）。
- $ \Sigma $ 是 $ m \times n $ 的对角矩阵，对角线上的值称为奇异值。
- $ V $ 是 $ n \times n $ 的正交矩阵（列向量为右奇异向量）。
- $ V^T $ 是 $ V $ 的转置。


### 主要特性：

1. **降维** ：SVD 可以用于数据降维，如 PCA（主成分分析）。
2. **矩阵压缩** ：可以通过保留最大的奇异值进行低秩近似，提高计算效率。
3. **求解最小二乘问题** ：用于求解欠定或过定线性方程组。
4. **信号和图像处理** ：在噪声去除、特征提取等方面有广泛应用。

如果 $ A $ 是方阵且满秩，SVD 还可以用于计算矩阵的伪逆、条件数等重要性质。


## 7.11-马尔科夫不等式 08:36

马尔可夫不等式（Markov's inequality）是概率论中的一个基本不等式，用于估计随机变量取较大值的概率。其数学表达式如下：

设 $X$ 是一个非负的随机变量，且其数学期望 $E[X]$ 存在，则对于任意 $a > 0$，有：
$$
P(X \geq a) \leq \frac{E[X]}{a}
$$

解释：
- 该不等式表明：如果一个随机变量的期望较小，那么它取大值的概率也不会太高。
- 适用于非负随机变量。
- 这是切比雪夫不等式和其他概率界限推导的基础。


## 7.12-切比雪夫不等式 11:15

**切比雪夫不等式（Chebyshev's Inequality）** 描述了随机变量偏离其数学期望的概率上界。具体来说，对于任意随机变量 $ X $ （不一定服从特定分布），如果它的数学期望 $ \mathbb{E}[X] $ 存在，且方差 $ \text{Var}(X) $ 有限，则对于任意 $ k > 0 $，有：

$$
P(|X - \mathbb{E}[X]| \geq k\sigma) \leq \frac{1}{k^2}
$$

其中，$ \sigma $ 是随机变量的标准差，即 $ \sigma = \sqrt{\text{Var}(X)} $。

**直观理解** ：
切比雪夫不等式给出了随机变量偏离其均值一定倍数的标准差的概率上限。它适用于任何具有有限方差的分布，即使该分布不是正态分布。例如，当 $ k = 2 $ 时，不等式表明随机变量至少偏离均值 2 倍标准差的概率不会超过 $ 1/4 $，即最多 25%。

**应用** ：
- 证明大数定律
- 估计概率分布的尾部行为
- 处理不服从正态分布的数据分析

{% include image.html url="/assets/images/200901-deep-learning-math-matr~e0/20250404154824.jpg" %}

马尔科夫不等式

$$
\begin{aligned}
& P(X \geqslant a) \\
& =\int_a^{+\infty} f(x) d x \leqslant \int_a^{+\infty} \frac{X}{a} f(x) d x \\
& \text { 由于 } \mathcal{\text { E }}\left(\frac{x}{a}\right)=\int_{-\infty}^{a} \frac{X}{a} f(x) d x+\int_a^{+\infty} \frac{X}{a} f(x) d x \\
& \text { 所以 } P(x \geqslant a) \leqslant \int_a^{+\infty}-\frac{x}{a} f(x) d x \leqslant E\left(\frac{x}{a}\right) \\
& \text { 即 } P(X \geqslant a) \leqslant E\left(\frac{X}{a}\right)=\frac{E(X)}{a}
\end{aligned}
$$

切比雪夫不等式

$$
\begin{aligned}
& P\{|X-E(x)| \geqslant \varepsilon\} \leqslant \frac{\delta^2}{\varepsilon^2} \\
& P\{|X-E(x)|<\varepsilon\} \geqslant 1-\frac{\delta^2}{\varepsilon^2} \\
& \text { 将 } \mid x-\mu \mid \text { 带入 } \text { 马尔科夫不等式 } \\
& P(|x-\mu|>\alpha) \leqslant \frac{E(|x-\mu|)}{\alpha} \\
& \text { 即 } P\left((x-\mu)^2 \geqslant a^2\right) \leqslant \frac{E\left((x-\mu)^2\right)}{a^2}=\frac{\sigma^2}{a^2}
\end{aligned}
$$

<https://onlinestatbook.com/stat_sim/sampling_dist/index.html>
**应用**
在 n 重贝努里试验中，若已知每次试验事件 A 出现的概率为 0.75，试利用契比雪夫不等式估计 n，
使 A 出现的频率在 0.74 至 0.76 之间的概率不小于 0.90。

$$
\begin{aligned}
&\text { 设在 } n \text { 重贝努里试验中，事件 } A \text { 出现的次数为 } X \text { ，}\\
&\begin{aligned}
& \text { 则 } \mathrm{X} \sim b(n, 0.75), \\
& E(X)=n p=0.75 n, D(X)=n p q=0.1875 n, \\
& \begin{aligned}
\text { 又 } f_n(A)=\frac{X}{n} \quad \text { 而 } P\left\{0.74<\frac{X}{n}<0.76\right\}=P\{|X-0.75 n|<0.01 n\} \geq 1-\frac{0.1875 n}{(0.01 n)^2} & =1-\frac{1875}{n} \geq 0.90 \\
& \Rightarrow n \geq 18750
\end{aligned}
\end{aligned}
\end{aligned}
$$


## 7.13-后验概率估计 10:05


## 7.14-贝叶斯拼写纠错实例 11:47


## 7.15-垃圾邮件过滤实例 14:10

掷一个硬币，观察到的是“正”，根据最大似然估计的精神，我们应该猜测这枚硬币掷出“正”的概率是 1，
因为这个才是能最大化 $P(D\|h)$ 的那个猜测。

如果平面上有 N 个点，近似构成一条直线，但绝不精确地位于一条直线上。
这时我们既可以用直线来拟合（模型 1）也可以用二阶多项式（模型 2）拟合，也可以用三阶多项式（模型 3），
特别地，用 N-1 阶多项式便能够保证肯定能完美通过 N 个数据点。
那么，这些可能的模型之中到底哪个是最靠谱的呢？
**奥卡姆剃刀：越是高阶的多项式越是不常见。**


## 8-1-正太分布 19:23


## 8-2-二项式分布 11:03


## 8-3-泊松分布 15:56


## 8-4-均匀分布 03:23


## 8-5-卡方分布 05:36


## 8-6-beta 分布 14:55


## 9-1-核函数的目的


## 06:38


## 9-2-线性核函数


## 05:44


## 9-3-多项式核函数


## 04:35


## 9-4-核函数实例


## 06:54


## 9-5-高斯核函数


## 08:51


## 9-6-参数的影响


## 08:37


## 10-1-熵的概念


## 04:51


## 10-2-熵的大小意味着什么


## 12:10


## 10-3-激活函数


## 06:31


## 10-4-激活函数的问题


## 10:00


## 11-1-回归分析概述


## 07:12


## 11-2-回归方程定义


## 04:43


## 11-3-误差项的定义


## 07:48


## 11-4-最小二乘法推导与求解


## 12:42


## 11-5-回归方程求解小例子


## 06:33


## 11-6-回归直线拟合优度


## 11:09


## 11-7-多元与曲线回归问题


## 08:26


## 11-8-Python 工具包介绍


## 05:02


## 11-9-statsmodels 回归分析


## 09:38


## 11-10-高阶与分类变量实例


## 12:07


## 11-11-案例：汽车价格预测任务概述


## 09:20


## 11-12-案例：缺失值填充


## 13:37


## 11-13-案例：特征相关性


## 13:48


## 11-14-案例：预处理问题


## 07:06


## 11-15-案例：回归求解


## 13:24


## 12-1-假设检验基本思想


## 12:29


## 12-2-左右侧检验与双侧检验


## 14:21


## 12-3-Z 检验基本原理


## 07:04


## 12-4-Z 检验实例


## 14:07


## 12-5-T 检验基本原理


## 13:03


## 12-6-T 检验实例


## 06:18


## 12-7-T 检验应用条件


## 07:44


## 12-8-卡方检验


## 11:29


## 12-9-假设检验中的两类错误


## 10:02


## 12-10-Python 假设检验实例


## 12:35


## 12-11-Python 卡方检验实例


## 08:00


## 13-1-相关分析概述


## 09:04


## 13-2-皮尔森相关系数


## 08:17


## 13-3-计算与检验


## 13:06


## 13-4-斯皮尔曼等级相关


## 14:07


## 13-5-肯德尔系数


## 06:49


## 13-6-质量相关分析


## 13:34


## 13-7-偏相关与复相关


## 07:35


## 14-1-方差分析概述


## 06:49


## 14-2-方差的比较


## 11:51


## 14-3-方差分析计算方法


## 14:01


## 14-4-方差分析中的多重比较


## 08:16


## 14-5-多因素方差分析


## 09:26


## 14-6-Python 方差分析实例


## 08:35


## 15-1-1-层次聚类概述


## 04:42


## 15-1-2-层次聚类流程


## 12:11


## 15-1-3-层次聚类实例


## 11:34


## 15-2-1-KMEANS 算法概述


## 11:34


## 15-2-2-KMEANS 工作流程


## 09:43


## 15-2-3-KMEANS 迭代可视化展示


## 08:20


## 15-3-1-DBSCAN 聚类算法


## 11:04


## 15-3-2-DBSCAN 工作流程


## 15:04


## 15-3-3-DBSCAN 可视化展示


## 08:53


## 15-4-1-多种聚类算法概述


## 04:35


## 15-4-2-聚类案例实战


## 17:20


## 16-1-贝叶斯分析概述


## 07:22


## 16-2-概率的解释


## 06:07


## 16-3-贝叶斯学派与经典统计学派的争论


## 05:50


## 16-4-贝叶斯算法概述


## 06:59


## 16-5-贝叶斯推导实例


## 07:38


## 16-6-贝叶斯拼写纠错实例


## 11:47


## 16-7-垃圾邮件过滤实例


## 14:10


## 16-8-贝叶斯解释


## 10:50


## 16-9-经典求解思路


## 08:17


## 16-10-MCMC 概述


## 11:03


## 16-11-PYMC3 概述


## 05:41


## 16-12-模型诊断


## 09:54


## 16-13-模型决策


## 10:49


## 0-0. 课程简介


## 06:05


## 1-1-回归问题概述


## 07:12


## 1-2-误差项定义


## 09:42


## 1-3-独立同分布的意义


## 07:33


## 1-4-似然函数的作用


## 10:51


## 1-5-参数求解


## 11:12


## 1-6-梯度下降通俗解释


## 08:35


## 1-7 参数更新方 1-法


## 08:18


## 1-8-优化参数设置


## 08:52


## 2-1-线性回归整体模块概述


## 05:17


## 2-2-初始化步骤


## 07:12


## 2-3-实现梯度下降优化模块


## 10:11


## 2-4-损失与预测模块


## 11:41


## 2-5-数据与标签定义


## 10:01


## 2-6-训练线性回归模型


## 10:44


## 2-7-得到线性回归方程


## 06:59


## 2-8-整体流程 debug 解读


## 08:17


## 2-9-多特征回归模型


## 09:47


## 2-10-非线性回归


## 11:23


## 3-1-Sklearn 工具包简介


## 04:57


## 3-2-数据集切分


## 07:16


## 3-3-交叉验证的作用


## 11:04


## 3-4-交叉验证实验分析


## 14:52


## 3-5-混淆矩阵


## 07:53


## 3-6-评估指标对比分析


## 12:14


## 3-7-阈值对结果的影响


## 08:27


## 3-8-ROC 曲线


## 08:59


## 4-1-实验目标分析


## 08:10


## 4-2-参数直接求解方法


## 08:48


## 4-3-预处理对结果的影响


## 12:40


## 4-4-梯度下降模块


## 06:37


## 4-5-学习率对结果的影响


## 10:36


## 4-6-随机梯度下降得到的效果


## 13:16


## 4-7-MiniBatch 方法


## 08:43


## 4-8-不同策略效果对比


## 08:37


## 4-9-多项式回归


## 11:17


## 4-10-模型复杂度


## 16:03


## 4-11-样本数量对结果的影响


## 15:56



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-09-01-deep-learning-math-matrix-eigen.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://zh.gluon.ai/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zh.gluon.ai/b73bb84d.html" %})
- [https://blog.csdn.net/tianya_team/article/details/53310617]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/ab76a7bc.html" %})
- [https://wenku.baidu.com/view/095bebde2a4ac850ad02de80d4d8d15abf23004d.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/wenku.baidu.com/aca20332.html" %})
- [https://space.bilibili.com/3546736784050628]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/space.bilibili.com/a7afe6a0.html" %})
- [https://www.bilibili.com/video/BV12Sc4e7Eat/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.bilibili.com/7840516e.html" %})
- [http://www.atoolbox.net/Tool.php?Id=715]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.atoolbox.net/ecf02067.php" %})
- [https://www.bilibili.com/video/BV1FP411L7t1/?129]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.bilibili.com/eabd2b2e.html" %})
- [https://www.bilibili.com/video/BV1gQ4y1E7iy/?129]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.bilibili.com/6aba709f.html" %})
- [https://www.bilibili.com/video/BV1iS4y1W7FP/?129]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.bilibili.com/b42fb279.html" %})
- [https://www.bilibili.com/video/BV1ah411x76z/?129]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.bilibili.com/336d5e09.html" %})
- [https://onlinestatbook.com/stat_sim/sampling_dist/index.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/onlinestatbook.com/31773f1c.html" %})
