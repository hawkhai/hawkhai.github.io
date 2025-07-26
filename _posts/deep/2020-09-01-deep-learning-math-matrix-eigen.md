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
* <https://www.bilibili.com/video/BV1gQ4y1E7iy/?129> 5.7w ---
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

* 8-1-正太分布 19:23
* 8-2-二项式分布 11:03
* 8-3-泊松分布 15:56
* 8-4-均匀分布 03:23
* 8-5-卡方分布 05:36
* 8-6-beta 分布 14:55


## 9-5-高斯核函数 08:51

{% include image.html url="/assets/images/200901-deep-learning-math-matr~e0/20250705191535.png" %}


## 11-5-回归方程求解小例子 06:33

<https://scikit-learn.org.cn/lists/2.html>
<https://scikit-learn.cn/stable/>

**分类**
标识对象所属的类别。
应用范围：垃圾邮件检测，图像识别。
算法：SVM 最近邻 随机森林 更多 ...

**回归**
预测与对象关联的连续值属性。
应用范围：药物反应，股票价格。
算法：SVR 最近邻 随机森林 更多 ...

**聚类**
自动将相似对象归为一组。
应用：客户细分，分组实验成果。
算法：K-均值 谱聚类 MeanShift 更多 ...

**降维**
减少要考虑的随机变量的数量。
应用：可视化，提高效率。
算法：K-均值 特征选择 非负矩阵分解 更多 ...

**模型选择**
比较，验证和选择参数和模型。
应用：通过参数调整改进精度。
算法：网格搜索 交叉验证 指标 更多 ...

**预处理**
特征提取和归一化。
应用程序：转换输入数据，例如文本，以供机器学习算法使用。
算法：预处理 特征提取 更多 ...

1. 有监督学习
    1.1 线性模型
    1.2 线性和二次判别分析
    1.3 内核岭回归
    1.4 支持向量机
    1.5 随机梯度下降
    1.6 最近邻
    1.7 高斯过程
    1.8 交叉分解
    1.9 朴素贝叶斯
    1.10 决策树
    1.11 集成算法
    1.12 多类和多标签算法
    1.13 特征选择
    1.14 半监督学习
    1.15 Isotonic 回归
    1.16 概率校准
    1.17 神经网络模型（有监督）
2. 无监督学习
    2.1. 高斯混合模型
    2.2. 流形学习
    2.3. 聚类
    2.4. 双聚类
    2.5. 分解成分中的信号（矩阵分解问题）
    2.6. 协方差估计
    2.7. 奇异值和异常值检测
    2.8. 密度估计
    2.9. 神经网络模型（无监督）
3. 模型选择与评估
    3.1 交叉验证：评估模型表现
    3.2 调整估计器的超参数
    3.3 指标和评分：量化预测的质量
    3.4 模型持久性
    3.5 验证曲线：绘制分数以评估模型
4. 检验
    4.1 部分依赖图
    4.2 基于排列的特征重要性
5. 可视化
    5.1 提供的绘图工具
6. 数据集转换
    6.1 管道和复合估算器
    6.2 特征提取
    6.3 数据预处理
    6.4 缺失值插补
    6.5 无监督降维
    6.6 随机投影
    6.7 内核近似
    6.8 成对度量，近似关系和内核
    6.9 转换预测目标（y）
7. 数据集加载实用程序
    7 数据集加载工具
8. 使用 scikit-learn 计算
    8.1. 大数据的计算策略
    8.2. 计算性能
    8.3. 并行，资源管理和配置

Missing data visualization module for Python.
<https://github.com/ResidentMario/missingno>


## 12-3-Z 检验基本原理 07:04

{% include image.html url="/assets/images/200901-deep-learning-math-matr~e0/20250726003237.png" %}


## 12-9-假设检验中的两类错误 10:02


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

机器学习面试复习资源
<https://github.com/wangyuGithub01/Machine_Learning_Resources>

:point_right: 此 repo 主要是为了整理机器学习面试相关知识点的有用链接
（注：目前不打算将一些基础算法的内容加入这个 repo 里，比如 LR、SVM 算法在《统计学习方法》里已经得到了很好的解释，面试时可能考到的手推公式在书里已经写的很好了，所以推荐直接看书即可。）


### 一、特征工程

#### （一）特征预处理

- [标准化、归一化、异常特征清洗、不平衡数据 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/9093890.html)
- [不平衡数据的处理方法 {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/84635540)

#### （二）特征表达

- [缺失值、特殊特征 (eg. 时间 )、离散特征、连续特征 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/9061549.html)
- [连续特征离散化的好处](http://note.youdao.com/noteshare?id=024fa3dbabf4b5a07eb72c8021e60f62)
- [什么样的模型对缺失值更敏感？ {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/88717220)

#### （三）特征选择

- [过滤法、包装法、嵌入法 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/9032759.html)
- [Kaggle 中的代码实战](https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection)


### 二、算法基础

#### （一）评价指标

- [PR 曲线和 F1 & ROC 曲线和 AUC](http://note.youdao.com/noteshare?id=13d31b4a7dc317b3d4abd18bf42a74df)
- [AUC & GAUC {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/84350940)

#### （二）正则项

- [正则化与数据先验分布的关系](http://note.youdao.com/noteshare?id=2851b97199bcdc174001d72b1bec0372)
- [L1 在 0 点处不可导怎么办？ {% include relref_cnblogs.html %}](http://www.cnblogs.com/pinard/p/6018889.html) 可采用坐标轴下降、最小角回归法
- [L1 为什么比 L2 的解更稀疏 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/74874291)

#### （三）损失函数

- [常见损失函数 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/58883095)
- [常见损失函数 2 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/77686118)

#### （四）模型训练

- [经验误差与泛化误差、偏差与方差、欠拟合与过拟合、交叉验证](http://note.youdao.com/noteshare?id=b629383adb3b09eb31b754c337f690b5)
- [参数初始化为什么不能全零](https://cloud.tencent.com/developer/article/1535198)
- [深度学习参数初始化 Lecunn、Xavier、He 初始化](https://cloud.tencent.com/developer/article/1542736)
- [dropout]()
- [Batch Normalization](https://cloud.tencent.com/developer/article/1551518)
- [dropout 和 BN 在训练 & 预测时有什么不同 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/61725100)
- [Layer Normalization {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/113233908)
- [Transformer 为什么用 LN 不用 BN（LN 和 BN 两者分别关注什么） {% include relref_zhihu.html %}](https://www.zhihu.com/question/395811291/answer/2141681320)
- [ResNet](https://cloud.tencent.com/developer/article/1591484)

#### （五）优化算法

- [梯度下降法、牛顿法和拟牛顿法 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/37524275)
- [深度学习优化算法 SGD、Momentum、Adagrad 等 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/22252270)
- [最大似然估计 和 最大后验估计 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/61905474)
- [最小二乘法 和 最大似然估计的对比联系 {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/88716699)
- [最大似然估计 和 EM {% include relref_csdn.html %}](https://blog.csdn.net/zouxy09/article/details/8537620)
- [浅谈最优化问题的 KKT 条件 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/26514613)

#### （六）其他知识点

- [先验概率 & 后验概率 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/38567891)
- [MLE 最大似然估计 & MAP 最大后验估计 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/32480810)
- [判别模型 vs 生成模型 {% include relref_zhihu.html %}](https://www.zhihu.com/question/20446337)
- [参数模型 vs 非参数模型 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/26012348)
- [参数估计 最大似然估计与贝叶斯估计 {% include relref_csdn.html %}](https://blog.csdn.net/bitcarmanlee/article/details/52201858)
- [交叉熵 {% include relref_github.html %}](https://colah.github.io/posts/2015-09-Visual-Information/)
- [交叉熵 等价 KL 散度 等价 MLE 最大似然估计 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/346518942)
- [向量间距离度量方式](http://note.youdao.com/noteshare?id=ffba716f9f94f1cf3fac48fca300c198)
- [余弦距离和欧氏距离的转换 {% include relref_zhihu.html %}](https://www.zhihu.com/question/19640394/answer/207795500)


### 三、机器学习算法

1. 线性回归、逻辑回归、SVM
  - [LR 优缺点 {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/lr_pros_and_cons.md)
  - [SVM、logistic regression、linear regression 对比 {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/compare_svm_lr.md)
  - [KNN vs K-Means {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/31580379)
  - [LR 和最大熵模型的关系, LR 的并行化 {% include relref_csdn.html %}](https://blog.csdn.net/dp_BUPT/article/details/50568392)
  - [为什么 LR 要用对数似然，而不是平方损失？ {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/88717326)
  - [似然函数 {% include relref_wiki.html %}](https://zh.wikipedia.org/wiki/%E4%BC%BC%E7%84%B6%E5%87%BD%E6%95%B0)
2. 树模型
- [逻辑回归与决策树在分类上的区别 {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/84841988)
- [回归树、提升树、GBDT {% include relref_jianshu.html %}](https://www.jianshu.com/p/005a4e6ac775)
- [GBDT、XGBOOST、LightGBM 讲解（强烈推荐看一下） {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/gbdt_wepon.pdf)
- [XGBOOST 具体例子一步步推导，包括缺失值怎么处理（很细值得看） {% include relref_jianshu.html %}](https://www.jianshu.com/p/ac1c12f3fba1)
    [(-> 这个链接包含前面文章内容，更全的总结 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/92837676)
- [随机森林 GBDT  XGBOOST  LightGBM 比较](http://note.youdao.com/noteshare?id=65790e27fd5737155c31af2c05df8985)
- [树分裂：信息增益、信息增益率、基尼系数 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/245617910)

3. 其他
- [各种机器学习算法的应用场景 {% include relref_zhihu.html %}](https://www.zhihu.com/question/26726794)


### 四、NLP 相关

- word2vec [文章 1 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/7160330.html)
    [文章 2 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/7243513.html)
    [文章 3 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/7249903.html)
- [LSTM {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/34203833)
- [LSTM 为什么用 tanh {% include relref_zhihu.html %}](https://www.zhihu.com/question/46197687/answer/895834510)
- [fasttext {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/32965521)
- [Transformer、self-attention {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/54356280)
- [Transformer 图解 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/338817680)
- [encode-decode attention 和 transformer self-attention 对比 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/53682800)
- [Transformer 中的 positional encoding {% include relref_zhihu.html %}](https://www.zhihu.com/question/347678607/answer/864217252)
- [Bert {% include relref_github.html %}](https://fancyerii.github.io/2019/03/05/bert-prerequisites/) 零基础入门，prerequisites 很全
- [XLNet {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/70257427)
- [nlp 中的词向量对比：word2vec/glove/fastText/elmo/GPT/bert {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/56382372)
- [NLP/AI 面试全记录 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/57153934)


### 五、推荐系统 & 计算广告 相关

- [LR & FTRL {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/55135954)
- [FM 算法 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/37963267): 讲的蛮细的
- [FM 算法结合推荐系统的讲解 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/58160982)
- [DSSM 模型 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/335112207)
- [DSSM 模型的损失函数（顺带讲了 point-wise, list-wise, pair-wise 损失函数） {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/322065156)
- [在线最优化求解 Online Optimization {% include relref_github.html %}](https://github.com/wzhe06/Ad-papers/blob/master/Optimization%20Method/%E5%9C%A8%E7%BA%BF%E6%9C%80%E4%BC%98%E5%8C%96%E6%B1%82%E8%A7%A3%28Online%20Optimization%29-%E5%86%AF%E6%89%AC.pdf)


### 六、推荐书籍 / 笔记 / 代码实现

- [统计学习方法 {% include relref_github.html %}](https://github.com/wangyuGithub01/E-book/blob/master/)
    （注意这个 pdf 是第一版，其中的勘误可在 [这里 / {% include relref_github.html %}](https://github.com/wangyuGithub01/E-book/blob/master/%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95%EF%BC%88%E5%8B%98%E8%AF%AF%EF%BC%89.pdf)
        查看）
    （[代码实现及 ppt {% include relref_github.html %}](https://github.com/fengdu78/lihang-code)）
- [西瓜书的公式推导细节解析 {% include relref_github.html %}](https://datawhalechina.github.io/pumpkin-book/#/)
- [deeplearning.ai 深度学习课程的中文笔记 {% include relref_github.html %}](https://github.com/fengdu78/deeplearning_ai_books)
- [机器学习训练秘籍 (Andrew NG) {% include relref_github.html %}](https://github.com/AcceptedDoge/machine-learning-yearning-cn)
- [推荐系统实战 {% include relref_github.html %}](https://github.com/wangyuGithub01/E-book)


### 七、推荐专栏

- [刘建平 Pinard {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/)：很多高质量文章讲解基础的知识和算法
- [华校专](http://huaxiaozhuan.com/)：基础算法讲解，多而全（其实还没怎么看
- [王喆的机器学习专栏 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/wangzhenotes)：结合论文 + 工业界的推荐系统应用，讲的很清晰
- [荐道馆 {% include relref_zhihu.html %}](https://www.zhihu.com/column/learningdeep)：讲推荐相关，文章写的比较透
- [美团技术团队](https://tech.meituan.com/tags/%E7%AE%97%E6%B3%95.html)：美团的技术博客，新技术与实际应用相结合
- [深度学习前沿笔记 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/c_188941548)：NLP 相关较多，预训练技术讲解的多
- [计算广告小觑 {% include relref_csdn.html %}](https://blog.csdn.net/breada/article/details/50572914)
- [计算广告论文、学习资料、业界分享 {% include relref_github.html %}](https://github.com/wzhe06/Ad-papers)


### 八、面试问题汇总

- [牛客网面经总结](https://www.nowcoder.com/discuss/165930)


### 九、其他面试常考

- [海量数据判重](https://www.nowcoder.com/discuss/153978)
- [常考智力题 / 逻辑题 {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Resources/blob/master/pdf/IQ.md)
- [常考概率题 {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Resources/blob/master/pdf/statistic.md)


### 十、C++ 相关

- [STL 详解及常见面试题 {% include relref_csdn.html %}](https://blog.csdn.net/daaikuaichuan/article/details/80717222)


### 工作之后工程实践相关

- [基于 PQ 量化的近似近邻搜索 (ANN) ](http://xtf615.com/2020/08/01/EBR/)
- [ANN 召回算法之 IVFPQ( 跟上面的差不多，这篇图第一张画的 PQ 图更清晰 ) {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/378725270)



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
- [https://scikit-learn.org.cn/lists/2.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/scikit-learn.org.cn/10f956af.html" %})
- [https://scikit-learn.cn/stable/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/scikit-learn.cn/10f57596.html" %})
- [https://github.com/ResidentMario/missingno]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/0d887675.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Resources]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/946e7a98.html" %})
- [https://www.cnblogs.com/pinard/p/9093890.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.cnblogs.com/5af2c785.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/84635540]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/007d73f8.html" %})
- [https://www.cnblogs.com/pinard/p/9061549.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.cnblogs.com/ad16de54.html" %})
- [http://note.youdao.com/noteshare?id=024fa3dbabf4b5a07eb72c8021e60f62]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/note.youdao.com/9c8dc335.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/88717220]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/282c1223.html" %})
- [https://www.cnblogs.com/pinard/p/9032759.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.cnblogs.com/494c44f4.html" %})
- [https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.kaggle.com/326d6084.html" %})
- [http://note.youdao.com/noteshare?id=13d31b4a7dc317b3d4abd18bf42a74df]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/note.youdao.com/e2ab7ebe.html" %})
- [https://zhuanlan.zhihu.com/p/84350940]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/e14f5e21.html" %})
- [http://note.youdao.com/noteshare?id=2851b97199bcdc174001d72b1bec0372]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/note.youdao.com/9bcf97e9.html" %})
- [http://www.cnblogs.com/pinard/p/6018889.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.cnblogs.com/d1dfca42.html" %})
- [https://zhuanlan.zhihu.com/p/74874291]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/96a91346.html" %})
- [https://zhuanlan.zhihu.com/p/58883095]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/c2778f3d.html" %})
- [https://zhuanlan.zhihu.com/p/77686118]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/855ab777.html" %})
- [http://note.youdao.com/noteshare?id=b629383adb3b09eb31b754c337f690b5]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/note.youdao.com/64871d22.html" %})
- [https://cloud.tencent.com/developer/article/1535198]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/cloud.tencent.com/807912d0.html" %})
- [https://cloud.tencent.com/developer/article/1542736]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/cloud.tencent.com/97064906.html" %})
- [https://cloud.tencent.com/developer/article/1551518]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/cloud.tencent.com/9a898506.html" %})
- [https://zhuanlan.zhihu.com/p/61725100]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/ccd57b39.html" %})
- [https://zhuanlan.zhihu.com/p/113233908]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/aab0c19d.html" %})
- [https://www.zhihu.com/question/395811291/answer/2141681320]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.zhihu.com/0d3fc98b.html" %})
- [https://cloud.tencent.com/developer/article/1591484]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/cloud.tencent.com/75d75389.html" %})
- [https://zhuanlan.zhihu.com/p/37524275]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/c5eac9d9.html" %})
- [https://zhuanlan.zhihu.com/p/22252270]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/81219569.html" %})
- [https://zhuanlan.zhihu.com/p/61905474]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/06c543ac.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/88716699]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/e5f17d32.html" %})
- [https://blog.csdn.net/zouxy09/article/details/8537620]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/22d1d7a9.html" %})
- [https://zhuanlan.zhihu.com/p/26514613]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/032cec84.html" %})
- [https://zhuanlan.zhihu.com/p/38567891]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/aff113a6.html" %})
- [https://zhuanlan.zhihu.com/p/32480810]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/9dc3ded7.html" %})
- [https://www.zhihu.com/question/20446337]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.zhihu.com/b1392a63.html" %})
- [https://zhuanlan.zhihu.com/p/26012348]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/00b8d0c8.html" %})
- [https://blog.csdn.net/bitcarmanlee/article/details/52201858]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/ebdda854.html" %})
- [https://colah.github.io/posts/2015-09-Visual-Information/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/colah.github.io/b8f6b360.html" %})
- [https://zhuanlan.zhihu.com/p/346518942]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/7b93b9ec.html" %})
- [http://note.youdao.com/noteshare?id=ffba716f9f94f1cf3fac48fca300c198]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/note.youdao.com/a96fa0c9.html" %})
- [https://www.zhihu.com/question/19640394/answer/207795500]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.zhihu.com/3c4fc27d.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/lr_pros_and_cons.md]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/8eff022e.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/compare_svm_lr.md]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/1921ab50.html" %})
- [https://zhuanlan.zhihu.com/p/31580379]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/5d6b3b4f.html" %})
- [https://blog.csdn.net/dp_BUPT/article/details/50568392]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/69bce3b7.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/88717326]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/7a3609ec.html" %})
- [https://zh.wikipedia.org/wiki/%E4%BC%BC%E7%84%B6%E5%87%BD%E6%95%B0]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zh.wikipedia.org/09feaa14.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/84841988]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/879134d7.html" %})
- [https://www.jianshu.com/p/005a4e6ac775]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.jianshu.com/512d30d9.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/gbdt_wepon.pdf]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/ea1131e0.pdf" %})
- [https://www.jianshu.com/p/ac1c12f3fba1]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.jianshu.com/56a085fe.html" %})
- [https://zhuanlan.zhihu.com/p/92837676]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/6a16de5f.html" %})
- [http://note.youdao.com/noteshare?id=65790e27fd5737155c31af2c05df8985]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/note.youdao.com/50cd6d63.html" %})
- [https://zhuanlan.zhihu.com/p/245617910]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/13501447.html" %})
- [https://www.zhihu.com/question/26726794]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.zhihu.com/b130a46f.html" %})
- [https://www.cnblogs.com/pinard/p/7160330.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.cnblogs.com/56fc1b1b.html" %})
- [https://www.cnblogs.com/pinard/p/7243513.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.cnblogs.com/510d37e2.html" %})
- [https://www.cnblogs.com/pinard/p/7249903.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.cnblogs.com/e450eca8.html" %})
- [https://zhuanlan.zhihu.com/p/34203833]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/1d0fc2ca.html" %})
- [https://www.zhihu.com/question/46197687/answer/895834510]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.zhihu.com/f8094be6.html" %})
- [https://zhuanlan.zhihu.com/p/32965521]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/866c5373.html" %})
- [https://zhuanlan.zhihu.com/p/54356280]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/589b2bc2.html" %})
- [https://zhuanlan.zhihu.com/p/338817680]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/f98cb261.html" %})
- [https://zhuanlan.zhihu.com/p/53682800]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/82187b51.html" %})
- [https://www.zhihu.com/question/347678607/answer/864217252]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.zhihu.com/4dfaa53b.html" %})
- [https://fancyerii.github.io/2019/03/05/bert-prerequisites/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/fancyerii.github.io/a835e11e.html" %})
- [https://zhuanlan.zhihu.com/p/70257427]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/ab4f5cb3.html" %})
- [https://zhuanlan.zhihu.com/p/56382372]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/4d1b48d3.html" %})
- [https://zhuanlan.zhihu.com/p/57153934]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/aa39b9f0.html" %})
- [https://zhuanlan.zhihu.com/p/55135954]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/f400c7c0.html" %})
- [https://zhuanlan.zhihu.com/p/37963267]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/37be221a.html" %})
- [https://zhuanlan.zhihu.com/p/58160982]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/58a5bc4f.html" %})
- [https://zhuanlan.zhihu.com/p/335112207]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/4e8e2579.html" %})
- [https://zhuanlan.zhihu.com/p/322065156]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/96d35007.html" %})
- [https://github.com/wzhe06/Ad-papers/blob/master/Optimization%20Method/%E5%9C%A8%E7%BA%BF%E6%9C%80%E4%BC%98%E5%8C%96%E6%B1%82%E8%A7%A3%28Online%20Optimization%29-%E5%86%AF%E6%89%AC.pdf]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/617ca1c8.pdf" %})
- [https://github.com/wangyuGithub01/E-book/blob/master/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/7f944c04.html" %})
- [https://github.com/wangyuGithub01/E-book/blob/master/%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95%EF%BC%88%E5%8B%98%E8%AF%AF%EF%BC%89.pdf]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/6f9531d5.pdf" %})
- [https://github.com/fengdu78/lihang-code]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/505a3b79.html" %})
- [https://datawhalechina.github.io/pumpkin-book/#/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/datawhalechina.github.io/dc925f5a.html" %})
- [https://github.com/fengdu78/deeplearning_ai_books]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/d720115f.html" %})
- [https://github.com/AcceptedDoge/machine-learning-yearning-cn]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/247b2f97.html" %})
- [https://github.com/wangyuGithub01/E-book]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/81f1b0ea.html" %})
- [https://www.cnblogs.com/pinard/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.cnblogs.com/bd9e25d1.html" %})
- [http://huaxiaozhuan.com/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/huaxiaozhuan.com/ae777d42.html" %})
- [https://zhuanlan.zhihu.com/wangzhenotes]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/7fdacec4.html" %})
- [https://www.zhihu.com/column/learningdeep]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.zhihu.com/a6901a31.html" %})
- [https://tech.meituan.com/tags/%E7%AE%97%E6%B3%95.html]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/tech.meituan.com/600f7b5e.html" %})
- [https://zhuanlan.zhihu.com/c_188941548]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/1c7b8420.html" %})
- [https://blog.csdn.net/breada/article/details/50572914]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/20807905.html" %})
- [https://github.com/wzhe06/Ad-papers]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/88963e8c.html" %})
- [https://www.nowcoder.com/discuss/165930]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.nowcoder.com/ce36cdeb.html" %})
- [https://www.nowcoder.com/discuss/153978]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/www.nowcoder.com/aab2fcc1.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Resources/blob/master/pdf/IQ.md]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/771a9208.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Resources/blob/master/pdf/statistic.md]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/github.com/58330a7d.html" %})
- [https://blog.csdn.net/daaikuaichuan/article/details/80717222]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/28aa3806.html" %})
- [http://xtf615.com/2020/08/01/EBR/]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/xtf615.com/bfce888c.html" %})
- [https://zhuanlan.zhihu.com/p/378725270]({% include relrefx.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zhuanlan.zhihu.com/2a4deb13.html" %})
