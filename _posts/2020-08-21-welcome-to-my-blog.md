---
layout: post
title: "Welcome to my blog"
location: "Japan"
categories: ["生活"]
comments: true
mathjax: true
toc: true
---

Hey, there! Welcome to my blog. I hope you enjoy reading the stuff in here. Nothing fancy, really. Just bits and bobs about tech and random topics.<br/><br/>
Enjoy!


## Test MathJax

[MathJax basic tutorial and quick reference](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

[基本数学公式语法 (of MathJax)](https://blog.csdn.net/ethmery/article/details/50670297)

[MathJax 总结](https://www.zybuluo.com/yangfch3/note/267947)


### 1. Inline MathJax

Inline MathJax: $E = mc^2$.


### 2. Display MathJax

[维基百科·麦克斯韦方程组](https://zh.wikipedia.org/wiki/%E9%A6%AC%E5%85%8B%E5%A3%AB%E5%A8%81%E6%96%B9%E7%A8%8B%E7%B5%84)。初等数学不是这个世界的真相，高等数学才是。麦克斯韦方程组有三种形式，表达的居然是同一个东西：积分形式、微分形式、复数形式。将电现象、磁现象与光的本质有机地统一在完整的电磁场理论中。

#### [麦克斯韦方程](https://blog.csdn.net/weixin_43318626/article/details/102329794)

##### 积分形式

$$
\begin{cases}
\oiint_{\partial V} \mathbf{E} \cdot d\mathbf{a} = \frac{Q_V}{\epsilon_0} \\
\oint_{\partial S} \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_{S} \mathbf{B} \cdot d\mathbf{a} \\
\oiint_{\partial V} \mathbf{B} \cdot d\mathbf{a} = 0 \\
\oint_{\partial S} \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_S + \mu_0 \epsilon_0 \frac{d}{dt} \int_{S} \mathbf{E} \cdot d\mathbf{a} \\
\end{cases}
$$

##### 微分形式

$$
\begin{cases}
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} \\
\nabla \times \mathbf{E} = -\frac{\partial}{\partial t} \mathbf{B} \\
\nabla \cdot \mathbf{B} = 0 \\
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial}{\partial t} \mathbf{E} \\
\end{cases}
$$

这里 $\mathbf{E}$ 表示电场，$\mathbf{B}$ 表示磁场，$\epsilon_0$ 和 $\mu_0$ 只是两个常数暂时可以忽略。积分形式中 $Q$ 是电荷，$I$ 是电流，$V$ 表示一块体积，$\partial V$ 表示它的表面，而 $S$ 表示一块曲面，$\partial S$ 表示它的边缘。微分形式中 $\rho$ 是电荷密度（$$电荷/体积$$），$\mathbf{J}$ 是电流密度（$$电流/面积$$），$\nabla\cdot$ 和 $\nabla\times$ 是两个不同的算符，基本可以理解为对向量的某种微分。

四个方程中，两个是关于电场 $\mathbf{E}$ 的，两个是关于磁场 $\mathbf{B}$ 的；两个是曲面积分 $\int \cdots d\mathbf{a}$ 或者散度 $\nabla\cdot$，两个是曲线积分 $\int \cdots d\mathbf{l}$ 或者旋度 $\nabla\times$。等式左边四个式子分别描述电场和磁场的两个东西，非常对称。

##### 复数形式

$$
\left\{\begin{array}{l}
{\nabla \times \boldsymbol{E}             = -\mathbf{i} \omega \mu \boldsymbol{H}} \\
{\nabla \times \boldsymbol{H}             = \boldsymbol{j}_{f}+\mathrm{i} \omega \varepsilon \boldsymbol{E}} \\
{\nabla \cdot \varepsilon \boldsymbol{E}  = \dot{\rho}_{f}} \\
{\nabla \cdot \mu \boldsymbol{H}          = 0} \\
{\nabla \cdot \boldsymbol{j}_{f}          = -\mathrm{i} \omega \dot{\rho}_{f}}
\end{array}\right.
$$


## 参考式 / 行内式

<https://www.imydl.tech/ty/70.html>


## Tools

* 公式在线编辑 <https://kerzol.github.io/markdown-mathjax/editor.html>
* **公式在线编辑** <https://latex.codecogs.com/eqneditor/editor.php>
* 文档在线编辑 <http://www.mdeditor.com/>
* 文档在线编辑 <https://www.zybuluo.com/mdeditor>
* **图片转公式** <https://gongshi.wang/>
* <https://mathpix.com/><sup>图片转公式貌似要收钱</sup>
* **HTML 转 MarkDown** <http://domchristie.github.io/turndown/>
* [Html 转 MarkDown](http://www.fly63.com/tool/htmarkdown/)
