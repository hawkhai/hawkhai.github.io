---
layout: post
title: "机器学习 -- 盘点卷积神经网络中十大令人拍案叫绝的操作"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习"]
toc: true
toclistyle: none
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

CNN 从 2012 年的 AlexNet 发展至今，科学家们发明出各种各样的 CNN 模型，一个比一个深，一个比一个准确，一个比一个轻量。我下面会对近几年一些具有变革性的工作进行简单盘点，从这些充满革新性的工作中探讨日后的 CNN 变革方向。


## 卷积只能在同一组进行吗？-- Group convolution

Group convolution 分组卷积，最早在 AlexNet 中出现，由于当时的硬件资源有限，训练 AlexNet 时卷积操作不能全部放在同一个 GPU 处理，因此作者把 feature maps 分给多个 GPU 分别进行处理，最后把多个 GPU 的结果进行融合。

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-328bd42aae09c585.webp" caption="alexnet" %}

分组卷积的思想影响比较深远，当前一些轻量级的 SOTA（State Of The Art）网络，都用到了分组卷积的操作，以节省计算量。但题主有个疑问是，如果分组卷积是分在不同 GPU 上的话，每个 GPU 的计算量就降低到 1/groups，但如果依然在同一个 GPU 上计算，最终整体的计算量是否不变？找了 pytorch 上有关组卷积操作的介绍，望读者解答我的疑问。

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-9f70771773fb134b.webp" caption="pytroch github" %}


## 二、卷积核一定越大越好？-- 3×3 卷积核

AlexNet 中用到了一些非常大的卷积核，比如 11×11、5×5 卷积核，之前人们的观念是，卷积核越大，receptive field（感受野）越大，看到的图片信息越多，因此获得的特征越好。虽说如此，但是大的卷积核会导致计算量的暴增，不利于模型深度的增加，计算性能也会降低。于是在 Inception 网络中，作者提出利用 2 个 3×3 卷积核的组合比 1 个 5×5 卷积核的效果更佳，同时参数量（3×3×2+1 VS 5×5×1+1）被降低，因此后来 3×3 卷积核被广泛应用在各种模型中。

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-8b808506ce0d9962.webp" caption="" %}


## 三、每层卷积只能用一种尺寸的卷积核？-- Inception 结构

传统的层叠式网络，基本上都是一个个卷积层的堆叠，每层只用一个尺寸的卷积核，例如 VGG 结构中使用了大量的 3×3 卷积层。事实上，同一层 feature map 可以分别使用多个不同尺寸的卷积核，以获得不同尺度的特征，再把这些特征结合起来，得到的特征往往比使用单一卷积核的要好，因此谷歌发明的 GoogleNet，或者说 Inception 系列的网络，就使用了多个卷积核的结构：

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-ef44e4546aa1cba1.webp" caption="最初版本的 Inception 结构" %}

如上图所示，一个输入的 feature map 分别同时经过 1×1、3×3、5×5 的卷积核的处理，得出的特征再组合起来，获得更佳的特征。但这个结构会存在一个严重的问题：参数量比单个卷积核要多很多，如此庞大的计算量会使得模型效率低下。这就引出了一个新的结构：


## 四、怎样才能减少卷积层参数量？-- Bottleneck

发明 GoogleNet 的团队发现，如果仅仅引入多个尺寸的卷积核，会带来大量的额外的参数，为了解决这个问题，他们往 Inception 结构中加入了一些 1×1 的卷积核，如图所示：

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-0c8e0d418a72dcac.webp" %}

加入 1×1 卷积核的 Inception 结构：
{% include image.html url="/assets/images/240521-cnn-evolution/v2-45d489b52bff50139774e80dce3e2d72_1440w.webp" %}

根据上图，我们看着 1×1 --> 3×3 这段通路，来做个计算，假设输入 feature map 的维度为 256 维，要求输出维度也是 256 维。有以下两种操作：

1. 256 维的输入直接经过一个 3×3×256 的卷积层，输出一个 256 维的 feature map，那么参数量为：256×3×3×256 = 589,824
2. 256 维的输入先经过一个 1×1×64 的卷积层，再经过一个 3×3×64 的卷积层，最后经过一个 3×3×256 的卷积层，输出 256 维，参数量为：256×1×1×64 + 64×3×3×63 + 64×1×1×256 = 69,632。足足把第一种操作的参数量降低到九分之一！

1×1 卷积核也被认为是影响深远的操作，往后大型的网络为了降低参数量都会应用上 1×1 卷积核。


## 五、越深的网络就越难训练吗？-- Resnet 残差网络

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-43b9223903c85e36.webp" caption="ResNet skip connection" %}

传统的卷积层层叠网络会遇到一个问题，当层数加深时，网络的表现越来越差，很大程度上的原因是因为当层数加深时，梯度消散得越来越严重，以至于反向传播很难训练到浅层的网络。
为了解决这个问题，何凯明大神想出了一个“残差网络”，使得梯度更容易地流动到浅层的网络当中去，而且这种“skip connection”能带来更多的好处，这里可以参考一个 PPT：
[极深网络（ResNet/DenseNet）: Skip Connection 为何有效及其它 {% include relref_csdn.html %}](https://blog.csdn.net/malefactor/article/details/67637785)，
以及我的一篇文章：
[为什么 ResNet 和 DenseNet 可以这么深？一文详解残差块为何能解决梯度弥散问题。 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/28124810?group_id=883267168542789632)，大家可以结合下面的评论进行思考。


## 六、卷积操作时所有通道都只能用同一个过滤器吗？-- DepthWise 操作

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-bdea8a9b7784a324.webp" %}

标准的卷积过程可以看上图，一个 2×2 的卷积核在卷积时， **对应图像区域中的所有通道均用同一个过滤器** ，问题在于，为什么一定要同时考虑图像区域和通道？我们为什么不能每个通道分开考虑？

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-cd2480acc62515a0.webp" %}

Xception 网络就是基于以上的问题发明而来。我们首先对每一个通道进行各自的卷积操作，有多少个通道就有多少个过滤器。得到新的通道 feature maps 之后，这时再对这批新的通道 feature maps 进行标准的 1×1 跨通道卷积操作。这种操作被称为 “ **DepthWise convolution** ” ，缩写“DW”。

这种操作是相当有效的，在 imagenet 1000 类分类任务中已经超过了 InceptionV3 的表现，而且也同时减少了大量的参数，我们来算一算，假设输入通道数为 3，要求输出通道数为 256，两种做法：

1. 直接接一个 3×3×256 的卷积核，参数量为：3×3×3×256 = 6,912
2. DW 操作，分两步完成，参数量为：3×3×3 + 3×1×1×256 = 795，又把参数量降低到九分之一！

因此，一个 depthwise 操作比标准的卷积操作降低不少的参数量，同时得到更好的效果，
**因为它对每一个通道都进行了学习（每个通道对应一个不同的过滤器），而不是所有通道对应同一个过滤器，得到的特征质量更佳！**


## 七、分组卷积能否对通道进行随机分组？-- ShuffleNet

在 AlexNet 的 Group Convolution 当中，特征的通道被平均分到不同组里面，最后再通过两个全连接层来融合特征，这样一来，就只能在最后时刻才融合不同组之间的特征，对模型的泛化性是相当不利的。为了解决这个问题，ShuffleNet 在每一次层叠这种 Group conv 层前，都进行一次 channel shuffle，shuffle 过的通道被分配到不同组当中。进行完一次 group conv 之后，再一次 channel shuffle，然后分到下一层组卷积当中，以此循环。

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-59f0c95736fa2d9f.webp" caption="来自 ShuffleNet 论文" %}

经过 channel shuffle 之后，Group conv 输出的特征能考虑到更多通道，输出的特征自然代表性就更高。另外，AlexNet 的分组卷积，实际上是标准卷积操作，而在 ShuffleNet 里面的分组卷积操作是 depthwise 卷积，因此结合了通道洗牌和分组 depthwise 卷积的 ShuffleNet，能得到超少量的参数以及超越 mobilenet、媲美 AlexNet 的准确率！

另外值得一提的是，微软亚洲研究院 MSRA 最近也有类似的工作，他们提出了一个 IGC 单元（Interleaved Group Convolution），即通用卷积神经网络交错组卷积，
形式上类似进行了两次组卷积，Xception 模块可以看作交错组卷积的一个特例，特别推荐看看这篇文章：
王井东详解 ICCV 2017 入选论文：通用卷积神经网络交错组卷积

**要注意的是，Group conv 是一种 channel 分组的方式，Depthwise +Pointwise 是卷积的方式，只是 ShuffleNet 里面把两者应用起来了。因此 Group conv 和 Depthwise +Pointwise 并不能划等号。**


## 八、通道间的特征都是平等的吗？ -- SEnet

无论是在 Inception、DenseNet 或者 ShuffleNet 里面，我们对所有通道产生的特征都是不分权重直接结合的， **那为什么要认为所有通道的特征对模型的作用就是相等的呢？** 这是一个好问题，于是，ImageNet2017 冠军 SEnet 就出来了。

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-55d347361b790a70.webp" caption="SEnet 结构" %}

一组特征在上一层被输出，这时候分两条路线，第一条直接通过，第二条首先进行 Squeeze 操作（Global Average Pooling），把每个通道 2 维的特征压缩成一个 1 维，
从而得到一个特征通道向量（每个数字代表对应通道的特征）。然后进行 Excitation 操作，把这一列特征通道向量输入两个全连接层和 sigmoid，建模出特征通道间的相关性，
**得到的输出其实就是每个通道对应的权重** ，把这些权重通过 Scale 乘法通道加权到原来的特征上（第一条路），这样就完成了特征通道的权重分配。
作者详细解释可以看这篇文章：专栏 \| Momenta 详解 ImageNet 2017 夺冠架构 SENet


## 九、能否让固定大小的卷积核看到更大范围的区域？-- Dilated convolution

标准的 3×3 卷积核只能看到对应区域 3×3 的大小，但是为了能让卷积核看到更大的范围，dilated conv 使其成为了可能。dilated conv 原论文中的结构如图所示：

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-c2548b6093abb75e.webp" %}

上图 b 可以理解为卷积核大小依然是 3×3，但是每个卷积点之间有 1 个空洞，也就是在绿色 7×7 区域里面，只有 9 个红色点位置作了卷积处理，其余点权重为 0。
这样即使卷积核大小不变，但它看到的区域变得更大了。详细解释可以看这个回答：
[如何理解空洞卷积（dilated convolution）？ {% include relref_zhihu.html %}](https://www.zhihu.com/question/54149221)


## 十、卷积核形状一定是矩形吗？-- Deformable convolution 可变形卷积核

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-eed9b79bbeb37022.webp" caption="图来自微软亚洲研究院公众号" %}

传统的卷积核一般都是长方形或正方形，但 MSRA 提出了一个相当反直觉的见解， **认为卷积核的形状可以是变化的，变形的卷积核能让它只看感兴趣的图像区域** ，这样识别出来的特征更佳。

{% include image.html url="/assets/images/240521-cnn-evolution/6014825-c4ecb9cfca695b79.webp" caption="图来自微软亚洲研究院公众号" %}

要做到这个操作，可以直接在原来的过滤器前面再加一层过滤器，这层过滤器学习的是下一层卷积核的位置偏移量（offset），
这样只是增加了一层过滤器，或者直接把原网络中的某一层过滤器当成学习 offset 的过滤器，这样实际增加的计算量是相当少的，但能实现可变形卷积核，识别特征的效果更好。
详细 MSRA 的解读可以看这个链接：可变形卷积网络：计算机新“视”界。


## 启发与思考

现在越来越多的 CNN 模型从巨型网络到轻量化网络一步步演变，模型准确率也越来越高。现在工业界追求的重点已经不是准确率的提升（因为都已经很高了），都聚焦于速度与准确率的 trade off，都希望模型又快又准。因此从原来 AlexNet、VGGnet，到体积小一点的 Inception、Resnet 系列，到目前能移植到移动端的 mobilenet、ShuffleNet（体积能降低到 0.5mb！），我们可以看到这样一些趋势：


### 卷积核方面：

1. 大卷积核用多个小卷积核代替；
2. 单一尺寸卷积核用多尺寸卷积核代替；
3. 固定形状卷积核趋于使用可变形卷积核；
4. 使用 1×1 卷积核（bottleneck 结构）。


### 卷积层通道方面：

1. 标准卷积用 depthwise 卷积代替；
2. 使用分组卷积；
3. 分组卷积前使用 channel shuffle；
4. 通道加权计算。


### 卷积层连接方面：

1. 使用 skip connection，让模型更深；
2. densely connection，使每一层都融合上其它层的特征输出（DenseNet）


### 启发

类比到通道加权操作，卷积层跨层连接能否也进行加权处理？bottleneck + Group conv + channel shuffle + depthwise 的结合会不会成为以后降低参数量的标准配置？

如果你有更多的想法或意见，欢迎评论留言，好的 idea 值得交流传播。本人的知乎号是：[Professor ho—知乎 {% include relref_zhihu.html %}](https://www.zhihu.com/people/professor-ho/posts)，简书上会发一些比较技术性的文章，如 GPU 降温等，知乎上会发比较理论性的见解文章，欢迎关注。


## Refs

通道洗牌、变形卷积核、可分离卷积？盘点卷积神经网络中十大令人拍案叫绝的操作。
作者：人工智豪
链接：<https://www.jianshu.com/p/71804c97123d>
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

* <https://zhuanlan.zhihu.com/p/28749411>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-05-21-CNN-Evolution.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/malefactor/article/details/67637785]({% include relrefx.html url="/backup/2024-05-21-CNN-Evolution.md/blog.csdn.net/bd69187c.html" %})
- [https://zhuanlan.zhihu.com/p/28124810?group_id=883267168542789632]({% include relrefx.html url="/backup/2024-05-21-CNN-Evolution.md/zhuanlan.zhihu.com/0d9d62d3.html" %})
- [https://www.zhihu.com/question/54149221]({% include relrefx.html url="/backup/2024-05-21-CNN-Evolution.md/www.zhihu.com/218996ff.html" %})
- [https://www.zhihu.com/people/professor-ho/posts]({% include relrefx.html url="/backup/2024-05-21-CNN-Evolution.md/www.zhihu.com/45ac0d1c.html" %})
- [https://www.jianshu.com/p/71804c97123d]({% include relrefx.html url="/backup/2024-05-21-CNN-Evolution.md/www.jianshu.com/919146b3.html" %})
- [https://zhuanlan.zhihu.com/p/28749411]({% include relrefx.html url="/backup/2024-05-21-CNN-Evolution.md/zhuanlan.zhihu.com/664fde8a.html" %})
