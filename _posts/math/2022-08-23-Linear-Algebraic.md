---
layout: post
title: "数学之美 --《线性代数》宋浩老师（进行中……）"
author:
location: "珠海"
categories: ["数学"]
tags: ["数学"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
cluster: "数学基础"
---

1. [《线性代数》 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1aW411Q7x1)
1. 《微积分》
1. 《概率论与数理统计》
1. [《高等数学》 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1Eb411u7Fw)

**从新学习，并用 mathjax 做笔记。**
[mathjax {% include relref_cnblogs.html %}](https://www.cnblogs.com/linxd/p/4955530.html)
[html2text](http://www.atoolbox.net/Tool.php?Id=715)
[公式及时编辑](https://spaces.ac.cn/latex.html/comment-page-1)
[在线函数图像](https://zuotu.91maths.com/)

[image](https://weibo.com/6122278407/K9Ggaa2Vl)
[note](https://www.xiaohongshu.com/explore/6062a48a000000000102411f)
{% include image.html url="/assets/images/220823-linear-algebraic/006GkshVgy1gpa9ogu9hlj34mo334000.jpg" caption="光线追踪 / 中山影视城" %}


## 1.1 二阶三阶行列式 38:52

完成。


## 1.1 n 阶行列式 43:55

完成。
[note {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/416717502)

比如三阶：
$$
D = \begin{vmatrix} a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23} \\ a_{31}&a_{32}&a_{33} \end{vmatrix}
$$

$$
D = (-1)^{1+1}a_{11}\begin{vmatrix} a_{22}&a_{23} \\ a_{32}&a_{33} \end{vmatrix} +   (-1)^{1+2}a_{12}\begin{vmatrix} a_{21}&a_{23} \\ a_{31}&a_{33} \end{vmatrix} +   (-1)^{1+3}a_{13}\begin{vmatrix} a_{21}&a_{22} \\ a_{31}&a_{32} \end{vmatrix} \\ =a_{11}\begin{vmatrix} a_{22}&a_{23} \\ a_{32}&a_{33} \end{vmatrix}  -a_{12}\begin{vmatrix} a_{21}&a_{23} \\ a_{31}&a_{33} \end{vmatrix} +  a_{13}\begin{vmatrix} a_{21}&a_{22} \\ a_{31}&a_{32} \end{vmatrix} \\ =  a_{11}a_{22}a_{33} -a_{11}a_{23}a_{32}    - a_{12}a_{21}a_{33}+ a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31}
$$


## 1.2 行列式的性质 1:16:58

转置。

* 性质 1：$D^{\top}=D$ 对行成立的性质，对列也成立。
* 性质 2：两行互换，值变号。推论：两行（列）相等，$D=0$。
* 性质 4：某一行都乘以 $k$，等于用 $k$ 乘以 $D$。

$$
\left|\begin{array}{ccc}
1 & 2 & 3 \\
4 k & 5 k & 6 k \\
7 & 8 & 9
\end{array}\right|=k\left|\begin{array}{lll}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{array}\right|
$$

* 性质 5：两行对应成比例 $D=0$。
    * 两行相等。
    * 某一行全为 $0$。


## 1.3 行列式按行展开 49:21


## 1.4 行列式的计算（一） 33:30


## 1.4 行列式的计算（二） 51:06


## 1.5 克莱姆法则 17:36


## 2.1 矩阵概念 36:44


## 2.2 矩阵运算（一） 58:47


## 2.2 矩阵运算（二） 32:23


## 2.3 特殊矩阵 30:47


## 2.4 逆矩阵（一） 45:30


## 2.4 逆矩阵（二） 1:20:03


## 2.5 分块矩阵 40:47


## 2.6 初等变换（一） 41:48


## 2.6 初等变换（二） 1:00:56


## 2.6 初等变换（三） 32:28


## 2.7 矩阵的秩（一） 13:10


## 2.7 矩阵的秩（二） 1:01:18


## 3.1 n 维向量及其运算 25:21


## 3.2 向量间的线性关系（一） 28:03


## 3.2 向量间的线性关系（二） 52:02


## 3.2 线性相关线性无关 23:09


## 3.3 向量组的秩（一） 20:48


## 3.3 向量组的秩（二） 35:39


## 4.1 线性方程组 10:37


## 4.2 线性方程组有解判定 1:09:17


## 4.3 齐次方程组的解 28:16


## 4.4 方程组解的结构（一） 54:26


## 4.4 方程组解的结构（二） 45:32


## 上个视频 32 分钟的错误更正 01:24


## 5.1 矩阵的特征值与特征向量（一） 23:43


## 5.1 矩阵的特征值与特征向量（二） 45:49


## 5,1 特征值和特征向量的性质 1:18:25


## A 星星的行列式的更正 01:35


## 5.2 相似矩阵和矩阵可对角化的条件 1:06:14


## 5.3 实对称矩阵的对角化（一） 26:46


## 5.3 实对称矩阵的对角化（二） 35:44


## 5.3 实对称矩阵的对角化（三） 1:03:41


## 6.1 二次型定义 57:46


## 6.2 二次型化标准型（配方法） 18:52


## 6.2 二次型化标准型（初等变换法和正交替换法） 36:48


## 6.3 有定性 16:20


## 6.3 有定性的判别 29:28


## 7.1 线性空间 17:14


## 7.2 基维数坐标 22:51



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-08-23-Linear-Algebraic.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1aW411Q7x1]({% include relrefx.html url="/backup/2022-08-23-Linear-Algebraic.md/www.bilibili.com/43361190.html" %})
- [https://www.bilibili.com/video/BV1Eb411u7Fw]({% include relrefx.html url="/backup/2022-08-23-Linear-Algebraic.md/www.bilibili.com/f90a16e2.html" %})
- [https://www.cnblogs.com/linxd/p/4955530.html]({% include relrefx.html url="/backup/2022-08-23-Linear-Algebraic.md/www.cnblogs.com/f5a952ec.html" %})
- [http://www.atoolbox.net/Tool.php?Id=715]({% include relrefx.html url="/backup/2022-08-23-Linear-Algebraic.md/www.atoolbox.net/ecf02067.php" %})
- [https://spaces.ac.cn/latex.html/comment-page-1]({% include relrefx.html url="/backup/2022-08-23-Linear-Algebraic.md/spaces.ac.cn/363c9e5d.html" %})
- [https://zuotu.91maths.com/]({% include relrefx.html url="/backup/2022-08-23-Linear-Algebraic.md/zuotu.91maths.com/7f1a51d4.html" %})
- [https://weibo.com/6122278407/K9Ggaa2Vl]({% include relrefx.html url="/backup/2022-08-23-Linear-Algebraic.md/weibo.com/037bbcae.html" %})
- [https://www.xiaohongshu.com/explore/6062a48a000000000102411f]({% include relrefx.html url="/backup/2022-08-23-Linear-Algebraic.md/www.xiaohongshu.com/ade04cfe.html" %})
- [https://zhuanlan.zhihu.com/p/416717502]({% include relrefx.html url="/backup/2022-08-23-Linear-Algebraic.md/zhuanlan.zhihu.com/9094b2cf.html" %})
