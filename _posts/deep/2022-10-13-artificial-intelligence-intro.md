---
layout: post
title: "机器学习笔记 -- 神经网络内部发生了什么？深度学习可视化"
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

机器学习。这个视频太惊艳了，大概讲的是，我们训练出来的网络模型究竟是个什么东西，其内部是怎么运作的。
关键帧翻译并截图注解。原创文章。感觉歪果人都不用上班的，完全没有生活的压力。

* GitHub 代码 : <https://github.com/vivek3141/dl-visualization>
* youtube [Visualizing Deep Learning](//www.youtube.com/playlist?list=PLyPKqVSnetmEOp_g_hfabuRAs9ET-shl_)
    * youtube [The Neural Network, A Visual Introduction](//www.youtube.com/watch?v=UOvPeC8WOt8)
        * bilibili 机翻版本 [深度学习可视化入门 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1mD4y127sg/)
    * youtube [What does a neural network *actually* do?](//www.youtube.com/watch?v=-at7SLoVK_I)
        * bilibili 机翻版本 [神经网络“内部”发生了什么？ {% include relref_bili.html %}](https://www.bilibili.com/video/BV1s3411y7WN/)

在图形图像学里面，图像变换是通过仿射变换实现的，一个仿射矩阵乘上去，搞定。
这个是以前写的笔记：[图像几何变换]({% include relref.html url="/blog/2020/09/19/dip-digital-image-processing#%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2" %})，这玩意二维三维都是可以的：旋转（rotation）、缩放（scale）、平移（shift）以及错切（shear）。

{% include image.html url="/assets/images/221013-artificial-intelligence~43/20180628113033537.png" %}

看了这个视频才恍然大悟，两块知识居然是相通的，从而实现了神经网络的可视化。


## 激活函数

有了这些激活函数，才能拟合那些非常复杂，非线性的数据集。因为仿射变换毕竟是线性变换，有了激活函数，才能更复杂灵活，拟合更复杂模型。


### sigmoid

{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221014234725.png" %}


### ReLU

{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221014235007.png" %}


## 神经网络 2-2-2


### 建立网络

为了可视化，我们建立一个简单的神经网络。每层只有两个维度，这样方便二维演示。

{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221014235534.png" %}

输入一个二维数据集：
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221014235701.png" %}


### 第一层变换

第一层的变换，刚好是二维图像的仿射变换：旋转（rotation）、缩放（scale）、平移（shift）以及错切（shear）。
数据集经过第一层后，变成了：
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015000200.png" %}

此时，精彩的地方来了，应用激活函数 ReLU 后，数据集变成了：
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015000342.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015000508.png" %}

相当于把其它三个象限的数据都收集（刨）到了轴上。因为激活函数的存在，整个网络才可以拟合更复杂的数据集了，能拟合出更复杂的决策边界了。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/aafafafa233zbzbz4.gif" %}


### 第二层变换

第二层变换，相当于再来一次矩阵乘法（二维仿射变换），此时我们的数据集变成了这样：

{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015000822.png" %}

最后再通过激活函数 sigmoid 把结果约束到 0-1 的区域。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015000935.png" %}

到这里，从最开始不好分类的数据集，分类成了很容易归类的数据集了。
**一个原来不好分类的数据集，经过两次二维空间仿射变换，变成了很容易分类的数据集了。**


## 三维的情况 2-3-2

再搞一个新网络：2-3-2。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015001320.png" %}

还是一样的数据集。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015001417.png" %}


### 第一层

第一层相当于把一个二维的数据集映射到了三维。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015001541.png" %}

此时再应用 ReLU 激活函数，像折纸飞机一样，相当于把这个面折叠成三维，太酷了。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015001723.png" %}

处理后的数据集，都在 xyz 的正空间里面了，二维活生生变成了三维。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015001830.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/az4567.webp" %}


### 第二层变换

由于这一层相当于又把三维变换到了二维，像拍黄瓜一样，拍扁了。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015001944.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015002025.png" %}

同前面一个网络一样，最终同样得到了很好分类的数据集。
正是有了这些激活函数，整个网络处理过程才能拟合非线性决策，通过多次空间变换，数据变的更容易区分了。
可以把整个网络理解为一个逐层的空间变换函数。


## 高级网络 2-100-5

尝试对这个数据集分类，螺旋参数方程。一共 5 个颜色的点。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015004230.png" %}

构建一个网络，尝试对这些点分类，第一层为每个点的 x & y 坐标（二维），第二层 100 个隐藏节点（隐藏层），第三层是输出层，代表 5 个分类。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015004432.png" %}


### 激活函数 argmax

激活函数的可微性非常重要。我们这里引入一个新的激活函数 **argmax**。
这个函数返回最大值的索引。

比如一个 25 个数字组成的随机变量，应用这个激活函数，返回 3（第三个点最大）。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015005212.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015005249.png" %}

相当于把所有的信号都屏蔽了，仅仅保留最强的那个信号，这里对应的值就是 3。


### 激活函数 softmax

**softmax** 它保证平滑，它的输出是每个元素的概率，这些概率的和是 1。激活函数的可微性非常重要，最终的决策边界也可以很平滑。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015005955.png" %}


### 简单网络

{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015010131.png" %}

通过训练后，这个网络的分类决策边界是：
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015010330.png" %}

为了方便可视化，在最后一层的前面插入一层，只有两个节点，方便二维可视化。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015010549.png" %}

奇妙的事情发生了，这些螺旋数据集在新加的这一层，自动分布变成了这样：
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015010902.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015010754.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/az4.webp" %}

因为我们倒数第二层只有两个节点，所以最后一次变换只能是线性变换分割，而上面这个分布，刚好可以完美线性分割。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015011100.png" %}

几条直线实现了数据分割，太奇妙了。


### 决策边界

泛化能力不一样。
不同的激活函数最终生成的决策边界不一样。
ReLU 激活函数，线性扩展特性。把视角放大。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015011431.png" %}

但是，也许我们真正的决策边界是这样子的。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015011538.png" %}

我们采用正弦作为激活函数，可以训练出某些周期性特征。把视角放大看，哇塞。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015011721.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015011808.png" %}


## 最终决策边界


### argmax 激活的情况

倒数第二层绘制成二维。
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015012342.png" %}

经过前面的变换，最后一层的运算，决策边界 $y=f(x_1, x_2)$ 刚好可以绘制成三维。相当于是用不同的平面去切割出这些数据集，刚好 5 个平面。

{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015012512.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015012555.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015012638.png" %}

从顶部看：
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015012714.png" %}


### softmax 激活的情况

采用 softmax 激活函数后，这些分割平面变成了，高潮又来了：
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015012902.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015012949.png" %}

全部绘制在一起：
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015013029.png" %}

从顶部看，5 个平面决策边界：
{% include image.html url="/assets/images/221013-artificial-intelligence~43/20221015013058.png" %}
{% include image.html url="/assets/images/221013-artificial-intelligence~43/az456.webp" %}


## 结语

作者最终有一个分离 0-9 字符的例子，也很精彩；也只有歪果仁，非常有时间，才能做出这么惊艳的视频。
第三个视频没有出，期待。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-10-13-artificial-intelligence-intro.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/vivek3141/dl-visualization]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence-intro.md/github.com/8db464ce.html" %})
- [https://www.bilibili.com/video/BV1mD4y127sg/]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence-intro.md/www.bilibili.com/1ad0e5b9.html" %})
- [https://www.bilibili.com/video/BV1s3411y7WN/]({% include relrefx.html url="/backup/2022-10-13-artificial-intelligence-intro.md/www.bilibili.com/9371f15d.html" %})
