---
layout: post
title: "数学之美 -- 欧拉公式，复数域的成人礼"
location: "珠海"
categories: ["数学之美"]
tags: [数学之美]
mathjax: true
toc: true
---

虽然作者署名，不能转载。但是文章实在太优美了，隔了半个月还印象深刻，最终还是转了。所有公式一个字母一个字母重新敲的。

> 原文：[马同学·欧拉公式，复数域的成人礼](https://www.matongxue.com/madocs/2066/)


## 导言

之前在“复数，通往真理的最短路径”中说过，复数域其实就是二维的数域，提供了更高维度的、更抽象的视角。本文来看看，我们是怎么从实数域扩展到复数域的。

大家可能觉得这个扩展并不复杂，也就是 $a$、$b$ 两个任意实数，外加虚数 $i=\sqrt{-1}$，把它们结合在一起，就完成了：

$$a+bi,\quad (a,b\in\mathbb{R})$$

但数域的扩张从来没有这么简单，就好像夫妻生下小孩只是个开始，困难的是之后的抚养、教育：

{% include image.html url="/images/math-complex/1.jpg" %}

复数域的扩张充满崎岖。正如欧拉的老师对他的赞扬：

> 我介绍数学分析的时候，它还是个孩子，而你正在将它带大成人。
> <p style="text-align: right;">---- 约翰·伯努利</p>

这句话虽然是说微积分（数学分析）的，但用在复数域上也不违和。欧拉的欧拉公式正是“复数域”的成人礼：

$$
e^{i\theta}=\cos\theta+i\sin\theta,\quad (\theta\in\mathbb{R})
$$


## 数域扩张的历史

来看看之前的数域是怎么扩张的吧。每次想到数域的扩张，我都有种大爆炸的画面感，宇宙从一个奇点爆炸中产生：

{% include image.html url="/images/math-complex/2.gif" %}


### 自然数到整数

数学刚开始也是一片空白：

{% include image.html url="/images/math-complex/3.png" %}

0 的出现就是数学的奇点：

{% include image.html url="/images/math-complex/4.png" %}

根据皮亚诺定理（可以参考为什么 1+1=2？）“爆炸”出了自然数域（可以参考自然数是否包含 0？）：

{% include image.html url="/images/math-complex/5.png" %}

很显然上面的图像是不对称的，哪怕出于美学考虑，人们都有冲动把左边补齐，增加负数，这样就得到了整数域：

{% include image.html url="/images/math-complex/6.png" %}

添加负数之后，有一个问题就出现了：

$$
4^{-1}=\color{red}{?}
$$

我们知道 $4^3$ 是对 $4\times 4\times 4$ 的缩写，并且容易推出如下计算规则：

$$
4^{2}\times 4^{3}=4^{2+3}=4^5
$$

我们添加负数之后，希望这个规则依然适用，即：

$$
4^{-1}\times 4^{1}=4^0=1\implies 4^{-1}=\frac{1}{4^1}
$$

更一般的有：

$$
4^{-n}=\frac{1}{4^n},\quad (n\in\mathbb{Z}^+)
$$

并且还惊喜地发掘出负数次方的意义，如果说正数次方是对乘法的缩写，那么负数次方（正数的相反数）是对除法（乘法的逆运算）的缩写：

$$
\begin{array}{c|c}
    \hline
    \\
    \quad 4^3\quad&4\times 4\times 4\quad \\
    \quad 4^{-3}\quad&\quad 1\div 4\div 4\div 4\quad\\
    \\
    \hline
\end{array}
$$


### 整数到实数

很显然整数之间还有很多空隙，我们可以用有理数（rational number，翻译为“可比数”更合理）：

$$
\frac{a}{b},\quad(a,b\in\mathbb{Z},b\ne0)
$$

来填满这些空隙（示意图）：

{% include image.html url="/images/math-complex/7.png" %}

还有空隙，最终用无理数（irrational number，“不可比数”）来填满这些缝隙，得到实数轴：

{% include image.html url="/images/math-complex/8.png" %}

自然会有这么一个问题：

$$
4^{\pi}=\color{red}{?}
$$

$\pi$ 是无理数，上面这个问题需要用极限来回答，这里不再赘述，只是可以看出实数域的扩张也是很艰难的。


## 复数基础

往下面讲之前，稍微复习下复数的一些基础知识。


### 复数的运算规则

复数的运算规则并非凭空捏造的。开头提到的文章“复数，通往真理的最短路径”说过，形如：

$$x^3-3px-2q=0$$

的三次方程，卡尔丹诺在《大术》这本书中给出了通解：

$$
x=\sqrt[3]{q+\sqrt{q^2-p^3}}+\sqrt[3]{q-\sqrt{q^2-p^3}}
$$

如果 $p=5$、$q=2$，可以得到方程：

$$
x^3-15x-4=0
$$

从图像上看，$x^3-15x-4$ 与 $y=0$ 有三个交点的：

{% include image.html url="/images/math-complex/9.png" %}

套用通解会得到：

$$
x=\sqrt[3]{2+\sqrt{2^2-5^3}}+\sqrt[3]{2-\sqrt{2^2-5^3}}=\sqrt[3]{2+11i}+\sqrt[3]{2-11i}
$$

这里就出现复数了。拉斐尔·邦贝利（1526－1572），文艺复兴时期欧洲著名的工程师，给出了一个思维飞跃，指出如果复数遵循如下的计算规则：

加法：$$(a+bi)+(c+di)=a+c+(b+d)i$$

乘法：$$(a+bi)(c+di)=ac+(ad+bc)i+bdi^2$$

那么就可以根据之前的通解得到三个实数解。


### 复数加法、减法的几何意义

为了之后的讲解，先引入几个符号，对于一般的向量 $z=a+bi$ 有：

$$
\begin{array}{c|c}
    \hline
    \quad 名称 \quad&\quad 解释 \quad&\quad 符号
    \\
    \hline
    \\
    \quad 模 \quad&\quad 长度 \quad&\quad |z|\quad \\
    \quad 幅角 \quad&\quad 与实轴正方向的角度 \quad&\quad \arg(z)\\
    \\
    \hline
\end{array}
$$

复数的几何表示和二维向量有点类似，只是横坐标是实轴（$$Re$$），纵坐标是虚轴（$$Im$$），下图还把刚才的符号给标了出来：

{% include image.html url="/images/math-complex/10.png" %}

加法的几何意义和向量也一样：

{% include image.html url="/images/math-complex/11.png" %}

但向量没有乘法（点积、叉积和实数乘法不一样），这就是复数和向量的区别。复数是对实数的扩展，所以要尽量兼容实数，必须要有加减乘除、乘方开方、对数等运算。

根据刚才的乘法规则，计算可得：

$$
(a+bi)i=-b+ai
$$

画出来发现，两者是正交的：

{% include image.html url="/images/math-complex/12.png" %}

还可以从另外一个角度来理解这一点，$i$ 在复平面上是这样的：

{% include image.html url="/images/math-complex/13.png" %}

那么，$(a+bi)$ 乘以虚数 $i$，就是：

$$
\begin{array}{c|c}
    \hline
    \quad \quad&\quad 长度 \quad&\quad 幅角 \quad
    \\
    \hline
    \\
    \quad z=a+bi\quad&\quad |z|\quad&\quad\arg(z)\quad \\
    \quad i\quad&\quad |i|=1\quad&\quad\arg(i)=90^\circ\quad \\
    \quad z\times i\quad&\quad |i|\times|z|\quad&\quad\arg(z)+\arg(i)\quad \\
    \\
    \hline
\end{array}
$$

对于一般的向量 $$c+di$$，也符合这个规律：

$$
\begin{array}{c|c}
    \hline
    \quad \quad&\quad 长度 \quad&\quad 幅角 \quad
    \\
    \hline
    \\
    \quad z_1=a+bi\quad&\quad |z_1|\quad&\quad\arg(z_1)\quad \\
    \quad z_2=c+di\quad&\quad |z_2|\quad&\quad\arg(z_2)\quad \\
    \quad z_1\times z_2\quad&\quad |z_1|\times|z_2|\quad&\quad\arg(z_1)+\arg(z_2)\quad \\
    \\
    \hline
\end{array}
$$

好了，知道这些差不多了，开始正题。


## 复数域的扩张

好了，轮到复数域了，复数定义为：

$$
a+bi,\quad (a,b\in\mathbb{R})
$$

那么，来回答数域扩张都会问到的问题吧：

$$
e^{i}=\color{red}{?}
$$

这个问题可以用欧拉公式：

$$
e^{i\theta}=\cos\theta+i\sin\theta,\quad (\theta\in\mathbb{R})
$$

来回答，取 $$\theta=1$$，可得：

$$
e^{i}=\cos 1+i\sin 1
$$

画出来就是复平面上模长为 $1$，幅角也为 $1$ 的点：

{% include image.html url="/images/math-complex/14.png" %}

更一般的，欧拉公式说明，$e^{i\theta}$ 是单位圆上幅角为 $\theta$ 的点：

{% include image.html url="/images/math-complex/3.gif" %}

但是，欧拉公式 $$\color{red}{凭什么}$$ 长这个样子！


### $e^x$ 的定义

欧拉公式肯定不是凭空捏造的，先来看看实数域中有什么可以帮助我们的。

实数域中的 $e^x$ 函数，起码有三种定义方式：

* 极限的方式：$e^x=\lim_{n\to\infty}\left(1+\frac{x}{n}\right)^n$

* 泰勒公式的方式：$e^x=1+x+\frac{1}{2!}x^2+\frac{1}{3!}x^3+\cdots$

* 导数的方式：$e^x=\frac{\mathrm{d}}{\mathrm{d}x}e^x$

从这三种定义出发都可以得到欧拉公式。


### 极限的方式

因为：

$$
e^x=\lim_{n\to\infty}\left(1+\frac{x}{n}\right)^n
$$

我们可以大胆地令 $x=i\theta$：

$$
e^{\color{orange}{i\theta}}=\lim_{n\to\infty}\left(1+\frac{\color{orange}{i\theta}}{n}\right)^n
$$

那么之前的 $e^i$ 就等于：

$$
e^{i}=\lim_{n\to\infty}\left(1+\frac{i}{n}\right)^n
$$

我们来看看这个式子在几何上有什么意义。因为 $e^i$ 对应的是单位圆上幅角为 $1$ 的点，所以先给个参照物，虚线是单位圆，实线对应的幅角为 $1$：

{% include image.html url="/images/math-complex/15.png" %}

然后取 $n=3$，可以得到：

$$
\left(1+\frac{i}{3}\right)^3=\left(1+\frac{i}{3}\right)\times \left(1+\frac{i}{3}\right)\times \left(1+\frac{i}{3}\right)
$$

根据复数的乘法规则，可以看出：

{% include image.html url="/images/math-complex/16.png" %}

取 $n=10$：

{% include image.html url="/images/math-complex/17.png" %}

取 $n=30$，已经很接近单位圆上幅角为 $1$ 的点了：

{% include image.html url="/images/math-complex/18.png" %}

对于更一般的 $e^{i\theta}$ 也是同样的：

{% include image.html url="/images/math-complex/19.png" %}

当 $n=100$ 时，就很接近单位圆上幅角为 $\theta$ 的点了：

{% include image.html url="/images/math-complex/20.png" %}

可以证明当 $n\to\infty$ 时，$e^{i\theta}$ 为单位圆上幅角为 $\theta$ 的点，也就是得到了欧拉公式：

$$
e^{i\theta}=\cos\theta+i\sin\theta,\quad (\theta\in\mathbb{R})
$$

可能你还会问，直接替换 $x$ 为 $i\theta$，合理吗：

$$
e^x=\lim_{n\to\infty}\left(1+\frac{x}{n}\right)^n\implies e^{\color{orange}{i\theta}}=\lim_{n\to\infty}\left(1+\frac{\color{orange}{i\theta}}{n}\right)^n
$$

这里是理解欧拉公式的 $$\color{red}{关键}$$，我们要意识到一点，欧拉公式是一种人为的选择，完全可以不这么去定义 $$e^{i\theta}$$。但是，做了别的选择，会面临一个问题：会不会在现有的庞大复杂的数学体系中产生矛盾？

打个比方吧，在实数中“除以 0”是不合理的，假如你想让它变得合理，那么分分钟会导出矛盾：

$$
\begin{aligned}
    0=0\implies 2\cdot 0=1\cdot 0\implies \frac{2\cdot 0}{0}=\frac{1\cdot 0}{0}\implies 2=1
\end{aligned}
$$

欧拉公式并不会引发冲突，并且随着学习的深入，你会发现数学家已经证明了它是一种足够好的选择，这里就不赘述了。


### 泰勒公式的方式

实数域下，有这些泰勒公式：

$$
e^x=1+x+\frac{1}{2!}x^2+\frac{1}{3!}x^3+\cdots
$$

$$
\sin x=x-\frac{1}{3!}x^3+\frac{1}{5!}x^5+\cdots
$$

$$
\cos x=1-\frac{1}{2!}x^2+\frac{1}{4!}x^4+\cdots
$$

也是直接替换 $e^x$，令 $x=i\theta$ 有：

$$
\begin{aligned}
    e^{i\theta} & = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \frac{(i\theta)^4}{4!} + \frac{(i\theta)^5}{5!} + \frac{(i\theta)^6}{6!} + \frac{(i\theta)^7}{7!} + \frac{(i\theta)^8}{8!} + \cdots \\
    & = 1 + i\theta - \frac{\theta^2}{2!} - \frac{i\theta^3}{3!} + \frac{\theta^4}{4!} + \frac{i\theta^5}{5!} - \frac{\theta^6}{6!} - \frac{i\theta^7}{7!} + \frac{\theta^8}{8!} + \cdots \\
    & = \left( 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \frac{\theta^8}{8!} - \cdots \right) + i\left(\theta-\frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots \right) \\
    &=\cos\theta + i\sin\theta
\end{aligned}
$$

这也有漂亮的几何意义，看看 $e^i$ 的前三项：

$$
e^i\approx 1 + i + \frac{i^2}{2!}
$$

这是三个复数相加，加出来就是：

{% include image.html url="/images/math-complex/21.png" %}

再增加第四项 $\frac{i^3}{3!}$：

{% include image.html url="/images/math-complex/22.png" %}

随着 $n\to\infty$，仿佛一个螺旋不断地接近单位圆上幅角为 $1$ 的点。对于更一般的 $e^{i\theta}$ 也是类似的螺旋：

{% include image.html url="/images/math-complex/23.png" %}


### 导数的方式

实数域有：

$$
\frac{\mathrm{d}}{\mathrm{d}x}e^{rx}=re^{rx},\quad(r\in\mathbb{R})
$$

直接套用：

$$
\frac{\mathrm{d}}{\mathrm{d}t}e^{it}=ie^{it}
$$

假设 $t$ 是时间，那么 $e^{it}$ 是运动在复平面上的点的位移函数，$t=0$ 时位置为 $e^{i0}=1$：

{% include image.html url="/images/math-complex/24.png" %}

$e^{it}$ 的运动速度，也就是导数 $ie^{it}$。这个速度很显然是一个向量，有方向，也有速度。它的方向垂直于 $e^{it}$（根据乘法规则，乘以 $i$ 表示旋转 $90^\circ$）：

{% include image.html url="/images/math-complex/25.png" %}

并且不论 $t$ 等于多少，运动方向都垂直于位移，所以只能在单位圆上运动（圆的切线始终垂直于半径）：

{% include image.html url="/images/math-complex/4.gif" %}

而速度的大小就是速度的模长 $$\vert ie^{it}\vert $$。之前说了，对于两个复数 $z_1\times z_2$，它们的模长为 $$\vert z_1\vert \times \vert z_2\vert $$，那么：

$$
\vert ie^{it}\vert =\vert i\vert \times \vert e^{it}\vert
$$

$$\vert i\vert $$ 肯定等于 $1$ 了，$e^{it}$ 在单位圆上运动，所以模长也为 $1$，所以速度的大小为：

$$
\vert ie^{it}\vert =1
$$

速度大小为 $1$ 意味着 $t$ 时刻走了 $t$ 长度的路程。而 $e^{it}$ 在单位圆上运动，那么 $t$ 时刻运动了 $t$ 弧长，因为是单位圆，所以对应的幅角为 $t$：

{% include image.html url="/images/math-complex/26.png" %}


## 总结

有了欧拉公式之后，任何复数都可以表示为：

$$
z=a+bi=re^{i\theta}
$$

其中：

$$
r=\vert z\vert,\quad\theta=\arg(z)
$$

个人觉得 $a+bi$ 只是复数的初始形态，而 $re^{i\theta}$ 才是复数的完成形态，因为它更具有启发性。比如计算乘法的时候：

$$
z_1=r_1e^{i\theta_1},\quad z_2=r_2e^{i\theta_2}
$$

那么有：

$$
z_1\times z_2=r_1r_2e^{i(\theta_1+\theta_2)}
$$

$$
z_1\div z_2=\frac{r_1}{r_2}e^{i(\theta_1-\theta_2)}
$$

几何意义更加明显。并且扩展了乘方和对数运算：

$$
a^i=e^{i\ln a}
$$

$$
\ln \underbrace{i}_{ 单位圆上幅角为 \frac{\pi}{2} 的点 }=\ln \left(e^{i\frac{\pi}{2}}\right)=i\frac{\pi}{2}
$$

到此为止，基本上所有的初等运算都全了。更多高等的运算比如三角函数、积分、导数，也需要借助欧拉公式在复数上进行推广。

欧拉公式中，如果取 $\theta=\pi$，就得到了欧拉恒等式：

$$
e^{i\pi}+1=0
$$

这个公式也被誉为了上帝公式，包含了数学中最基本的 $e$、$\pi$、$i$、$1$、$0$，仿佛一句诗，道尽了数学的美好。


## 参考

- [1] [马同学·欧拉公式，复数域的成人礼](https://www.matongxue.com/madocs/2066/)
