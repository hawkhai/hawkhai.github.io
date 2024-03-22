---
layout: post
title: "机器学习笔记 -- 数学×向量范数和矩阵范数"
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


## 简述

两个标量我们可以比较大小，比如 1，2，我们知道 2 比 1 大。但是现在如果是两个向量 $(1,2,1)$，$(2,2,0)$，我们如何比较大小呢？此时我们把一个向量通过不同的方法，映射到一个标量，从而可以比较大小，这个标量学名就叫做“范数”。

范数分为向量范数和矩阵范数。


## 向量范数

向量 $$x=[x_1,x_2,...,x_N]$$。

{% highlight python %}
import numpy as np
X = np.array([-2, 5, 0, -3, 4])
# X 为 [-2 5 0 -3 4]
{% endhighlight %}


### **p 范数**

为 x 向量各个元素绝对值 $p$ 次方和的 $1/p$ 次方。

$$\|x\|_p=(\sum_{i=1}^N|x_i|^p)^{1/p}$$

{% include image.html url="/assets/images/200831-deep-learning-math-norm/w.jpg" %}

上图表示了 p 从无穷到 0 变化时，三维空间中到原点的距离（范数）为 1 的点构成的图形的变化情况。

{% highlight python %}
# 向量 p-范数
def norm_p(X, p):
    return (sum([abs(x)**p for x in X])) ** (1.0/p)
norm_p(X, 1) # p 取 1，结果为 14.0
norm_p(X, 2) # p 取 2，结果为 7.348
norm_p(X, 3) # p 取 3，结果为 6.073
{% endhighlight %}

特殊地，当 $p$ 取 0，1，2，$$\infty$$，$$-\infty$$，时，对应范数意义如下。

* **向量 0-范数** ：向量中非零元素的个数。

{% highlight python %}
# 向量零范数
def norm_0(X):
    return sum([1 for x in X if x])
norm_0(X)
# X 的零范数为 4
{% endhighlight %}

* **向量 1-范数** : 向量中各个元素绝对值之和。

    $$\|x\|_1=\sum\limits_{i=1}^N|x_i|$$

{% highlight python %}
# 向量 1-范数
def norm_1(X):
    return sum([abs(x) for x in X])
norm_1(X)
# X 的 1-范数为 14
{% endhighlight %}

* **向量 2-范数** : 向量中各个元素平方和的 $1/2$ 次方，L2 范数又称 Euclidean 范数（欧几里得范数），也就是通常说的向量长度。

    $$\|x\|_2=\left(\sum\limits_{i=1}^N|x_i|^2\right)^{1/2}$$

{% highlight python %}
# 向量 2-范数
def norm_2(X):
    return (sum([x*x for x in X])) ** (1.0/2)
norm_2(X)
# X 的 2-范数为 7.348
{% endhighlight %}

* **向量 $$\infty$$-范数** ：向量的正无穷范数即向量元素绝对值中的最大值。到原点的最远距离。

    $$\|x\|_\infty=\max\limits_{i}|x_i|$$

{% highlight python %}
# 向量无穷-范数
def norm_inf(X):
    return max([abs(x) for x in X])
norm_inf(X)
# X 的无穷-范数为 5
{% endhighlight %}

* **向量 $$-\infty$$-范数** ：向量的负无穷范数即向量元素绝对值中的最小值。到原点的最近距离。

    $$\|x\|_{-\infty}=\max\limits_i|x_i|$$

{% highlight python %}
# 向量负无穷-范数
def norm_finf(X):
    return min([abs(x) for x in X])
norm_finf(X)
# X 的负无穷-范数为 0
{% endhighlight %}


### **向量范数的性质**

1. 正定性：$$\|x\|\geq0$$，当 $$x=0$$ 时，$$\|x\|=0$$。

2. 齐次性：$$\|c\cdot x\| = c \|x\|$$。

3. 三角不等式：$$\|x+y\|\leq \|x\|+\|y\|$$。


## 矩阵范数

矩阵 $$A=(a_{ij})_{m\ast n}$$。

* **矩阵 0-范数** ：标识矩阵中非零元素的个数。可以表示矩阵的稀疏程度。

* **矩阵 1-范数** ：也称列和范数，即所有矩阵列向量的绝对值之和的最大值。

    $$\|A\|_1=\max\limits_j\sum\limits_{i=1}^m|a_{ij}|$$

* **矩阵 2-范数** ：也称谱范数，即 $$A^TA$$ 的最大特征值开平方。

    $$\|A\|_2 = \sqrt{max(\lambda_i)}$$ 其中，$\lambda_i$ 是 $A^TA$ 矩阵的特征值，只有方阵才有 2-范数。

* **矩阵 $$\infty$$-范数** ：矩阵的 $$\infty$$-范数，也称行和范数，即所有矩阵行向量的绝对值之和的最大值。

    $$\|A\|_\infty=\max\limits_i\sum\limits_{j=1}^m|a_{ij}|$$

* **矩阵 F-范数** ：即 Frobenius 范数，矩阵元素的平方和再开平方。

    $$\|A\|_F=\left(\sum\limits_{i=1}^m\sum\limits_{j=1}^na_{ij}^2\right)^{1/2}$$


### 谱范数代码实现

这玩意最难看懂，网上好多公式还是错的，写了代码实现。计算方法为 $A^TA$ 矩阵的最大特征值的开平方。

{% highlight python %}
import numpy as np
x = np.array([[-1, 1, 0], [-4, 3, 0], [1, 0, 2]])
print x
xtx = np.matmul(x.T, x)
print 'lambda  ', np.linalg.eigvals(xtx)
n2 = np.linalg.norm(x, ord = 2)
print 'norm_2  ', n2, np.sqrt(27.71086452)
{% endhighlight %}

程序执行结果：
{% highlight plaintext %}
[[-1  1  0]
 [-4  3  0]
 [ 1  0  2]]
lambda   [ 27.71086452   0.03392256   4.25521292]
norm_2   5.26411099011  5.2641109904712309
{% endhighlight %}

矩阵 X 的 2-范数计算是先计算 $X^TX$ 的特征值 $\lambda_i$，然后找 $\lambda_i$ 中的最大值，再开方。代码里 xtx 即为 $X^TX$，eigvals 函数的返回值就是各个 $\lambda_i$。


### 矩阵乘法

矩阵第 m 行与第 n 列交叉位置的那个值，等于第一个矩阵第 m 行与第二个矩阵第 n 列，对应位置的每个值的乘积之和。

{% include image.html url="/assets/images/200831-deep-learning-math-norm/bg2015090105.gif" %}

**矩阵的本质就是线性方程式，两者是一一对应关系。**

$$
\left\{
    \begin{array}{1}
        2x+y=3 \\
        4x+3y=7
    \end{array}
\right.$$

$$
\left(
    \begin{array}{ll}
        2 & 1 \\
        4 & 3
    \end{array}
\right)
\left(
    \begin{array}{l}
        x \\
        y
    \end{array}
\right)
=
\left(
    \begin{array}{l}
        3 \\
        7
    \end{array}
\right)$$


### 矩阵特征值

设 A 是 n 阶方阵，如果存在数 m 和非零 n 维列向量 x，使得 $Ax=mx$ 成立，则称 m 是矩阵 A 的一个特征值（characteristic value）或本征值（eigenvalue）。


## 机器学习与范数

机器学习中常用 L1 范数和 L2 范数来进行正则化，因为机器学习中往往需要最小化损失函数 Loss function，而最小化 Loss function 的过程中，模型参数不加以限制就容易导致过拟合，所以我们使用 L1 范数和 L2 范数把参数向量转化成一个可以度量的标量，同时加上最小化的约束，就达到了控制模型参数的目的从而防止过拟合。

{% include image.html url="/assets/images/200831-deep-learning-math-norm/20140504122353812.png" %}

{% include image.html url="/assets/images/200831-deep-learning-math-norm/20140504122410234.png" %}


## L1 vs L2

L1 在江湖上人称 Lasso，L2 人称 Ridge。
[note {% include relref_cnblogs.html %}](https://www.cnblogs.com/fanhaha/p/7104997.html)

我们将模型空间限制在 w 的一个 L1-ball 中。为了便于可视化，我们考虑两维的情况，在 (w1, w2) 平面上可以画出目标函数的等高线，
而约束条件则成为平面上半径为 C 的一个 norm ball 。等高线与 norm ball 首次相交的地方就是最优解：

{% include image.html url="/assets/images/200831-deep-learning-math-norm/20140504123020546.png" %}

可以看到，L1-ball 与 L2-ball 的不同就在于 L1 在和每个坐标轴相交的地方都有“角”出现，而目标函数的测地线除非位置摆得非常好，
大部分时候都会在角的地方相交。注意到在角的位置就会产生稀疏性，例如图中的相交点就有 w1=0，
而更高维的时候（想象一下三维的 L1-ball 是什么样的？）除了角点以外，还有很多边的轮廓也是既有很大的概率成为第一次相交的地方，
又会产生稀疏性。

相比之下，L2-ball 就没有这样的性质，因为没有角，所以第一次相交的地方出现在具有稀疏性的位置的概率就变得非常小了。
这就从直观上来解释了为什么 L1-regularization 能产生稀疏性，而 L2-regularization 不行的原因了。

因此，一句话总结就是：L1 会趋向于产生少量的特征，而其他的特征都是 0，而 L2 会选择更多的特征，这些特征都会接近于 0。
Lasso 在特征选择时候非常有用，而 Ridge 就只是一种规则化而已。

​​​​​​​q 不同取值时正则项的函数值图像
{% include image.html url="/assets/images/200831-deep-learning-math-norm/5cf8e68c59424ec38624bf8916f01edc~noop.png" %}

不同函数值图像对应的等高线（即俯视图）为
{% include image.html url="/assets/images/200831-deep-learning-math-norm/7c1a431c85774da7b095b47ccb56348d~noop.png" caption="图像等高线" %}

L1 正则先验是 Laplace 分布，L2 正则先验分布是高斯分布。

* L-0 范数：用来统计向量中非零元素的个数。
* L-1 范数：向量中所有元素的绝对值之和。可用于优化中去除没有取值的信息，又称稀疏规则算子。
* L-2 范数：典型应用 —— 欧式距离。可用于优化正则化项，避免过拟合。
* L-∞范数：计算向量中的最大值。

{% include image.html url="/assets/images/200831-deep-learning-math-norm/20240121192729.png" %}


## 参考

<div id="refer-anchor-1"></div>
- [1] [《动手学深度学习》 {% include relref_gluon.html %}](http://zh.gluon.ai/)
- [2] <https://ww2.mathworks.cn/help/matlab/ref/norm.html>
- [3] <https://mathpix.com/><sup>图片转公式貌似要收钱</sup>
- [4] [NumPy 范数计算](http://liao.cpython.org/numpy11/)
- [5] [理解矩阵乘法](http://www.ruanyifeng.com/blog/2015/09/matrix-multiplication.html)<sup>阮一峰</sup>
- [6] <https://blog.csdn.net/zouxy09/article/details/24971995>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-08-31-deep-learning-math-norm.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/fanhaha/p/7104997.html]({% include relrefx.html url="/backup/2020-08-31-deep-learning-math-norm.md/www.cnblogs.com/54655134.html" %})
- [http://zh.gluon.ai/]({% include relrefx.html url="/backup/2020-08-31-deep-learning-math-norm.md/zh.gluon.ai/b73bb84d.html" %})
- [https://ww2.mathworks.cn/help/matlab/ref/norm.html]({% include relrefx.html url="/backup/2020-08-31-deep-learning-math-norm.md/ww2.mathworks.cn/a7e5323f.html" %})
- [https://mathpix.com/]({% include relrefx.html url="/backup/2020-08-31-deep-learning-math-norm.md/mathpix.com/6a3d6789.html" %})
- [http://liao.cpython.org/numpy11/]({% include relrefx.html url="/backup/2020-08-31-deep-learning-math-norm.md/liao.cpython.org/180b77ae.html" %})
- [http://www.ruanyifeng.com/blog/2015/09/matrix-multiplication.html]({% include relrefx.html url="/backup/2020-08-31-deep-learning-math-norm.md/www.ruanyifeng.com/eeea3212.html" %})
- [https://blog.csdn.net/zouxy09/article/details/24971995]({% include relrefx.html url="/backup/2020-08-31-deep-learning-math-norm.md/blog.csdn.net/bb20dd8a.html" %})
