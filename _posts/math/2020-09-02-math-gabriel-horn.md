---
layout: post
title: "MATHEMATICS -- Gabriel 喇叭，有限的体积无穷的表面积"
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
---

[维基百科 · 加百列的号角 {% include relref_wiki.html %}](https://en.wikipedia.org/wiki/Gabriel%27s_Horn)


## Gabriel 喇叭

{% include image.html url="/assets/images/200902-math-gabriel-horn/200809101.gif" %}

Gabriel 喇叭是 $y=1/x$ 在 $[1, +∞)$ 上的图象沿 $x$ 轴旋转一周所形成的旋转体。这个简单的三维图形有一个奇特的性质：它的表面积无穷大，却只有有限的体积。为了证实这一点，只需注意到：

{% include image.html url="/assets/images/200902-math-gabriel-horn/200809102.gif" %}

Gabriel 喇叭会导出一个非常诡异的悖论：如果你想用涂料把 Gabriel 喇叭的表面刷一遍，你需要无穷多的涂料；然而把涂料倒进 Gabriel 喇叭填满整个内部空间，所需要的涂料反而是有限的。


## 数学过程

双曲线 $1/x$

{% include image.html url="/assets/images/200902-math-gabriel-horn/29381f30e924b899ce7e11f968124f930b7bf64f.jpeg" %}

我们选择右侧部分（以避免 $x=0$ 处的不连续性）并绘制从 $x=1$ 开始的图。我们考虑虚线右侧，曲线下方和 $x$ 上方的（无限）阴影区域。

{% include image.html url="/assets/images/200902-math-gabriel-horn/eac4b74543a982263a6bae068296eb074a90eb00.jpeg" %}

我们围绕 $x$ 轴在 $3$ 维上旋转该区域，最后得到一个（无限长的）类似角的对象。

{% include image.html url="/assets/images/200902-math-gabriel-horn/10dfa9ec8a136327a7d3fa1c969bf2ea08fac7f9.jpeg" %}

我们使用旋转体的体积公式（最基本的体积计算公式，一定要理解）

{% include image.html url="/assets/images/200902-math-gabriel-horn/b64543a98226cffc19e32b5fbf151896f703ea28.jpeg" %}

由此得到如下结果

{% include image.html url="/assets/images/200902-math-gabriel-horn/21a4462309f79052121029db0ae785cc7acbd5e6.jpeg" %}

随着 $b$ 越来越大，答案中的最终分数也越来越小，因此体积为有限量 $π$，用数学符号表示为：

{% include image.html url="/assets/images/200902-math-gabriel-horn/0823dd54564e9258b11b5e7b9996835eccbf4e16.jpeg" %}

接下来，让我们考虑喇叭的表面积，旋转体的表面积计算公式为：

{% include image.html url="/assets/images/200902-math-gabriel-horn/79f0f736afc37931369ed64dedd0e54342a911fd.jpeg" %}

在这种情况下，我们有：

{% include image.html url="/assets/images/200902-math-gabriel-horn/2934349b033b5bb565a144c731c7873fb600bcab.jpeg" %}

如果我们考虑分数的值，当 $x$ 变得非常大时，我们可以看到它会非常接近 $1/x$（但会比它大一点）

{% include image.html url="/assets/images/200902-math-gabriel-horn/faf2b2119313b07e4e65ecdd0bc3c32596dd8c21.jpeg" %}

因此我们可以得出以下结论：

{% include image.html url="/assets/images/200902-math-gabriel-horn/0bd162d9f2d3572c0090177b8c07312163d0c3c5.jpeg" %}

现在，随着 $b$ 越来越大，这个数量也越来越大。即，它是无限大的数量。

这是我们的两个解决方案的图，粉红色是体积 $V=π(1-1/b)$，绿色是表面积 $SA=2πln(b)$。我们可以看到体积趋向于极限 $π$，而表面积却不断增大。

{% include image.html url="/assets/images/200902-math-gabriel-horn/a8773912b31bb051f4ef21fe336e88b24bede033.jpeg" %}


## todo

好多物理定律其实完全是由思维实验推导出来的，难以置信仅仅是思考竟然就能得出物理世界遵从的各种法则。经典的物理思维实验有 Newton 大炮、Galileo 斜塔实验、Schrödinger 的猫猫、Maxwell 的妖怪等等。还有，Turing 机也是一个伟大的思维实验。


## 参考

- [1] <http://www.matrix67.com/blog/archives/773>
- [2] [维基百科 · 加百列的号角 {% include relref_wiki.html %}](https://en.wikipedia.org/wiki/Gabriel%27s_Horn)
- [3] <https://baijiahao.baidu.com/s?id=1660502466103090640>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-09-02-math-gabriel-horn.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://en.wikipedia.org/wiki/Gabriel%27s_Horn]({% include relrefx.html url="/backup/2020-09-02-math-gabriel-horn.md/en.wikipedia.org/c3179941.html" %})
- [http://www.matrix67.com/blog/archives/773]({% include relrefx.html url="/backup/2020-09-02-math-gabriel-horn.md/www.matrix67.com/3e0aa503.html" %})
- [https://baijiahao.baidu.com/s?id=1660502466103090640]({% include relrefx.html url="/backup/2020-09-02-math-gabriel-horn.md/baijiahao.baidu.com/f90f4671.html" %})
