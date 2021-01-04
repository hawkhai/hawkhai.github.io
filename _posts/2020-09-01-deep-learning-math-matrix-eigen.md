---
layout: post
title: "深度学习笔记 -- 数学×矩阵的特征值和特征向量"
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


## 定义

设 $A$ 为 $n \times n$ 阶方阵，若存在常数 $\lambda$ 与 $n$ 维非零列向量 $X$ 使 $AX=\lambda X$ 成立，则称 $\lambda$ 为方阵 $A$ 的特征值，非零向量 $X$ 为 $A$ 的对应于 $\lambda$ 的特征向量。

由 $AX=\lambda X$ → $(A-\lambda E)X=0$。

此方程有非零解的充要条件是：$\|A-\lambda E\|=0$，即**特征多项式方程**：

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

-----

<font class='ref_snapshot'>参考资料快照</font>

- [http://zh.gluon.ai/]({% include relref.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/zh.gluon.ai/b73bb84d.html" %})
- [https://blog.csdn.net/tianya_team/article/details/53310617]({% include relref.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/blog.csdn.net/ab76a7bc.html" %})
- [https://wenku.baidu.com/view/095bebde2a4ac850ad02de80d4d8d15abf23004d.html]({% include relref.html url="/backup/2020-09-01-deep-learning-math-matrix-eigen.md/wenku.baidu.com/aca20332.html" %})
