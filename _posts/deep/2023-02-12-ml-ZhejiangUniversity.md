---
layout: post
title: "机器学习 -- 浙江大学 · 机器学习（进行中……）"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习"]
toc: true
toclistyle: none
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
cluster: "机器学习课程"
---

路虽远行则将至。
浙江大学 · [机器学习 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1qf4y1x7kB/)

> 惊叹深度网络的每次改进都如此精妙，也不知道为啥，反正收敛靠运气，试验效果更好，太神奇了。
> 每次看到 ReLU，都想起这玩意，简单的函数可以折叠出任意复杂的高维，感觉自编码器最大的作用是保证信息不丢失。
{% include image.html url="/assets/images/230212-ml-zhejianguniversity/730sfaf.jpg" caption="F-117A" %}

**深度学习与炼丹。**
经典网络 AlexNet 第一层的卷积内核是 11x11 像素。
为什么是 11 不是 10，不是 12？不知道，作者写论文的时候也没讲。
AlexNet 为什么有 9 层，为什么第二层就变成 5x5，后面又变成 3x3 了？
作者也没说。甚至，为什么这个内核的大小越来越小也没有交代。
深度学习像一剂成分复杂、原理不明的药。

{% include image.html url="/assets/images/230212-ml-zhejianguniversity/gdgc-46-7-1-190082-1-3.jpg" %}

严伯钧
神经网络处理架构 Transformer，适合处理自然语言 NLP。
卷积架构 适合图像处理，RNN 架构适合语言处理。

实践中，根据经验多试几个网络，哪个效果更好就用那个。
Stefano Bachis·F-117A
{% include image.html url="/assets/images/230212-ml-zhejianguniversity/d6ca7bcb0a46f21ff08913a7267ac5640d33ae6c.webp" %}
{% include image.html url="/assets/images/230212-ml-zhejianguniversity/aec379310a55b319bb06819c84f72c22cefc173a.webp" %}
{% include image.html url="/assets/images/230212-ml-zhejianguniversity/79f0f736afc379319386587b2c9a194142a9115d.webp" %}
[深入理解 ReLU 函数（ReLU 函数的可解释性） {% include relref_csdn.html %}](https://blog.csdn.net/weixin_41929524/article/details/112253138)


### P1 [1.1.1] -- 机器学习定义 09:38


### P2 [1.2.1] -- 机器学习的分类 10:52

非监督学习算法：
* 聚类 Clustering
* EM 算法（Expectation-Maximization algorithm）
* 主成分分析（Principle Component Analysis）

监督学习：
* 分类：标签是离散的值
* 回归：标签是连续的值


### P3 [1.3.1] -- 机器学习算法的过程 12:39

完成。


### P4 [1.4.1] -- 没有免费午餐定理 09:37


### P5 [1.5.1] -- 总结 05:36


### P6 [2.1.1] -- 支持向量机（线性可分定义） 09:49


### P7 [2.2.1] -- 支持向量机（问题描述） 08:07


### P8 [2.3.1] -- 支持向量机（优化问题） 13:33


### P9 [2.4.1] -- 支持向量机（线性不可分情况） 09:32


### P10 [2.5.1] -- 支持向量机（低维到高维的映射） 07:25

完成。


### P11 [2.6.1] -- 支持向量机（核函数的定义） 09:46


### P12 [2.7.1] -- 支持向量机（原问题和对偶问题） 08:12

KKT 条件。


### P13 [2.8.1] -- 支持向量机（转化为对偶问题） 08:38

跳过。


### P14 [2.9.1] -- 支持向量机（算法流程） 08:26


### P15 [2.10.1] -- 支持向量机（兵王问题描述） 08:00


### P16 [2.11.1] -- 支持向量机（兵王问题程序设计） 08:39

$$
\begin{aligned}
& \text { - Linear ( 线性内核 ) : } K(x, y)=x^T y \\
& \text { - Ploy ( 多项式核 ) : } \quad K(x, y)=\left(x^T y+1\right)^d \\
& \text { - Rbf ( 高斯径向基函数核 ) : } \quad K(x, y)=e^{-\frac{\|x-y\|^2}{\sigma^2}} \\
& \text { - Tanh ( sigmoid 核 ) : } \\
& \qquad K(x, y)=\tanh \left(\beta x^T y+b\right) \quad \tanh (x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
\end{aligned}
$$


### P17 [2.12.1] -- 支持向量机（兵王问题 MATLAB 程序） 16:26

交叉验证。
五折交叉验证 挑选出最好的 超参数。C & Gamma。
最后再用所有数据训练一次。


### P18 [2.13.1] -- 支持向量机（识别系统的性能度量） 15:30

混淆矩阵。
ROC 曲线。

{% include image.html url="/assets/images/230212-ml-zhejianguniversity/20230218114452.png"
caption="通过 ROC 曲线获得系统性能度量。（AUC & EER）" %}


### P19 [2.14.1] -- 支持向量机（多类情况） 09:37

政治选举的经济学分析当中，非常重要的中位数投票原理，就是说，你要获得最大多数的支持，你就要去迎合那些中位数者的偏好。

**阿罗不可能定律**
在人们有多种不同选择的情况下，选举不一定能够反映出大多数人的意愿。选举会出现议而不决、循环不已的情况，而要阻止这种情况，要么是由议程决定人决定会议的程序，要么把选票改成钞票。
{% include image.html url="/assets/images/230212-ml-zhejianguniversity/1975008-d845694d9fa2a1fd.webp" %}


### P20 [3.1.1] -- 人工神经网络（神经元的数学模型） 10:13

**单个神经元是一阶泰勒近似。**


### P21 [3.2.1] -- 人工神经网络（感知器算法） 18:50


### P22 [3.3.1] -- 人工神经网络（感知器算法的意义） 10:44


### P23 [3.4.1] -- 人工神经网络（第一次寒冬） 09:54


### P24 [3.5.1] -- 人工神经网络（多层神经网络） 14:35

三层神经网络可以模拟任意的非线性函数。


### P25 [3.6.1] -- 人工神经网络（梯度下降算法） 15:27

完成。


### P26 [3.7.1] -- 人工神经网络（后向传播算法上） 14:02


### P27 [3.8.1] -- 人工神经网络（后向传播算法下） 11:02


### P28 [3.9.1] -- 人工神经网络（后向传播算法的应用） 18:22

模拟任意决策面的
证明是基于阶跃函数的。

1. sigmoid 和 tanh 非线性函数；
2. 分类问题中基于 softmax 和交叉熵的目标函数；
3. 随机梯度下降法。


### P29 [3.10.1] -- 人工神经网络（兵王问题 MATLAB 程序） 10:00

完成。


### P30 [3.11.1] -- 人工神经网络（参数设置） 11:44

[note {% include relref_csdn.html %}](https://blog.csdn.net/DIPDWC/article/details/117110173)

#### 训练神经网络的建议

首先是三个训练神经网络的建议，这几个建议应该是学术界一致公认的。

1. 一般情况下，在训练集上的**目标函数的平均值（cost）**会随着训练的深入而不断减小，如果这个指标有增大的情况，请停下来。
    有两种情况：
    1. 采用的模型不够复杂，以至于不能在训练集上完全拟合；
    2. 已经训练很好了。因此停下来检查一下是否训练好，采取相应的措施。

2. **分出一些验证集（Validation Set）**，训练的本质目标是在验证集上获取最大的识别率。
因此训练一段时间后，必须在验证集上测试识别率，同时需要保存使验证集上识别率最大的模型参数，作为最后的结果。

3. **注意调整学习率（Learning Rate）**，如果刚训练几步损失函数 cost 就增加，一般来说是学习率太高了；如果每次 cost 变化很小，说明学习率太低了。根据实际情况适度的调整学习率是使神经网络快速正确收敛的基础。

#### 训练神经网络的经验

1. 目标函数可以加入正则项（regularization term）
2. 训练数据归一化
3. 参数 w 和 b 的初始化
4. Batch Normalization
5. 参数的更新策略


### P31 [4.1.1] -- 深度学习（历史发展） 12:20

生成对抗网络（Generative Adversarial Networks）、循环神经网络（Recurrent Neural Networks）、图卷积神经网络（Graph Convolutional Neural Networks）。

#### 人工神经网络的劣势

[note {% include relref_csdn.html %}](https://blog.csdn.net/DIPDWC/article/details/117215115)
和支持向量机相比，多层神经网络的劣势：
1. 多层神经网络在数学上不够优美，它的优化算法只能获得局部极值，算法的性能与初始值有关。
2. 多层神经网络不可解释训练神经网络获得的参数与实际任务的关联性非常模糊。
3. 模型可调整的参数很多，它包括网络层数、每层神经元个数、非线性函数、学习率、优化方法、终止条件等，使得训练神经网络变成了一门艺术，而以支持向量机为代表的方法所需要调整的参数却非常少。
4. 如果要训练相对复杂的网络，那么需要大量的训练样本。这与支持向量机基于小规模训练样本而产生的方法是背道而驰的。


### P32 [4.2.1] -- 深度学习（自编码器） 07:19


### P33 [4.3.1] -- 深度学习（卷积神经网络 LENET） 16:22

卷积神经网络（Convolutional Neural Network, CNN）。
{% include image.html url="/assets/images/230212-ml-zhejianguniversity/20210525101916740.png" caption="经典的 LeNet 结构" %}


### P34 [4.4.1] -- 深度学习（卷积神经网络 ALEXNET） 12:04

AlexNet 的结构以及 AlexNet 对于卷积神经网络的一系列改进，它们分别是：
1. **Relu 函数** 第一个改进以 ReLu 函数代替 LeNet 中的 Sigmoid 或 tanh 函数。
2. **最大池化（Maxpooling）** 第二个改进是降采样层 Maxpooling 代替 LeNet 的平均降采样。
3. **随机丢弃（Dropout）** 第三个改进是随机丢弃（Dropout）。
4. **数据扩增（Data Augumentation）** 第四个改进是数据扩增（Data Augumentation）。
5. **用 GPU 加速训练深度神经网络** 第五个改进是用 GPU 加速训练过程。


### P35 [4.5.1] -- 深度学习的编程工具 PYTORCH 06:20

TensorFlow、Caffe 和 Pytorch 三种深度学习编程工具。

torch.nn 模块之常用激活函数详解 [note {% include relref_csdn.html %}](https://blog.csdn.net/DIPDWC/article/details/112686489)

名称 	| 层对应的类 	| 功能
---- | ---- | ----
S 型激活函数 	| torch.nn.Sigmoid	| Sigmoid 激活函数
双曲正切函数 	| torch.nn.Tanh	| Tanh 激活函数
线性修正单元函数 	| torch.nn.ReLu	| ReLu 激活函数
ReLu 函数变体 	| torch.nn.LeakyReLu	| LeakyReLu 激活函数
平滑近似 ReLu 函数 	| torch.nn.Softplus	| ReLu 激活函数的平滑近似


### P36 [4.6.1] -- 深度学习的编程工具 Tensorflow 09:37

{% include image.html url="/assets/images/230212-ml-zhejianguniversity/20210531094412483.png" %}


### P37 [4.7.1] -- 深度学习的编程工具 CAFFE 13:10


### P38 [4.8.1] -- 深度学习（近年来流行的卷积神经网络） 11:24

在卷积神经网络中，感受野（Receptive Field）的定义是卷积神经网络每一层输出的特征图（Feature Map）上的像素点在输入图片上映射的区域大小。
[note {% include relref_csdn.html %}](https://blog.csdn.net/DIPDWC/article/details/117436454)

用更小的卷积核叠加代替大的卷积核可以起到降低待估计参数的作用。但是多层卷积需要更大的计算量，中间过程过程特征图也需要更多的储存空间，因此 VGGNet 是一个计算和存储开销都较大的网络。

#### VGGNet

* 增加了网络的深度
* 用多个 3×3 卷积核叠加代替更大的卷积核，用以增加感受野（Receptive Field）

#### GooleNet

GooleNet 提出了 Inception 结构，Inception 结构是用一些 1×1，3×3 和 5×5 的小卷积核用固定方式组合到一起来代替大的卷积核，达到增加感受野和减少参数个数的目的。

2014 年研究人员分析了深度神经网络，并从理论和实践上证明更深的卷积神经网络能够达到更高的识别准确率（L.J. Ba and R.Caruana，Do deep nets really need to be deep? NIPS 2014.）。因此，如何构建让更深的卷积神经网络收敛成了研究领域共同关注的问题。

#### ResNet

在 2015 年，Kaiming He 等人发明了 ResNet，使得训练深层的神经网络成为了可能（K. He，X. Zhang S. Ren and J.sun， Deep residual learning forimage recognition，cVPR2016.）。

{% include image.html url="/assets/images/230212-ml-zhejianguniversity/20210601170950881.png" %}

将浅层的输出直接加到深层当中去，当然在实际的添加中，由于浅层和深层的特征图在维度上有可能不一致导致无法直接相加，我们可以用一个线性变换直接把浅层特征图的维度变为深层特征图的维度。

* Batch Normalization 在每个卷积层后加上了 Batch Normalization
* Xavier initialization 使用 Xavier/2 来初始化参数
* SGD + Momentum (0.9) 使用 SGD+Momentum（momentum=0.9）
* Learning Rate:0.1 初始学习率设为 0.1，每到验证误差高原期（validation error plateaus）的时候就下降 10 倍
* Batch size 256 / Mini-batch size 256
* Weight decay 1e-5 / 权重衰减 weight decay 设为 1e-5
* No dropout 没有使用 dropout，因为 BN 已经减少了过拟合，而且效果很好

寻找更好的神经网络结构的努力一直在持续，严格的说这是一个需要在识别精度、计算量、存储量三个方面平衡取舍的问题。近年来，流行的趋势是利用紧凑的、小而深的网络代替以往稀疏的、大而浅的网络，同时在具体的实践过程中加入一些创意和技巧。近年来流行的例如 ShuffleNet、MobileNet 等都是其中的典型代表，另一方面，网络结搜索（Network Architecture Search），即如何从一大堆网络结构中搜索适合具体的网络结构成为领域内另一个热点问题。

不同网络计算量和识别率的联合比较。横坐标是网络的计算量，纵坐标是网络的 Top1 识别率。
{% include image.html url="/assets/images/230212-ml-zhejianguniversity/20210601174642259.png" %}

* VGG：效率最低，使用最多内存，但表现得确实好
* GoogleNet：最高效
* AlexNet：精确度最低，计算量很小，但占用内存很大。
* ResNet：在内存使用和操作复杂度之间平衡，但精确度最高
* GoogleNet 和 ResNet 没有使用大型的全连接层，而是在神经网络末端使用全局平均池化 global average pooling，大幅降低参数数量。


### P39 [4.9.1] -- 人脸识别介绍 13:57


### P40 [4.10.1] -- 目标检测与分割上 12:52


### P41 [4.11.1] -- 目标检测与分割下 12:00


### P42 [4.12.1] -- 时间序列的深度学习模型（RNN 和 LSTM） 14:50


### P43 [4.13.1] -- 生成对抗网络 11:48


### P44 [5.1.1] -- 强化学习（Q - Learning 和 epsilon - greedy 算法） 16:51


### P45 [5.2.1] -- 强化学习（深度强化学习） 09:38


### P46 [5.3.1] -- 强化学习（policygradient 和 actor - critic） 10:48


### P47 [5.4.1] -- 强化学习（AlphaGo 上） 13:54


### P48 [5.5.1] -- 强化学习（AlphaGo 下） 10:28


### P49 [6.1.1] -- ADABOOST 15:33


### P50 [6.2.1] -- 人工智能中的哲学 12:39


### P51 [6.3.1] -- 主成分分析 17:23


### P52 [6.4.1] -- K - 均值聚类 12:20


### P53 [6.5.1] -- 高斯混合模型 13:01


### P54 往年现场版 - 教科书介绍 06:31


### P55 成绩安排 17:44


### P56 概念介绍 10:20


### P57 这门课程的内容概述 17:36


### P58 没有免费午餐定理 20:41


### P59 支持向量机（线性模型）问题 20:05


### P60 支持向量机（线性模型）数学描述 38:28


### P61 支持向量机（线性模型）的图像展示 01:33


### P62 支持向量机（非线性模型）优化目标函数和限制条件 11:29


### P63 支持向量机（非线性模型） 低维到高维映射 28:28


### P64 支持向量机（非线性模型）原问题和对偶问题 30:51


### P65 支持向量机 - 将支持向量机原问题转化为对偶问 57:33


### P66 支持向量机 – 核函数介绍 07:36


### P67 支持向量机的应用 -- 兵王问题（规则介绍） 10:44


### P68 支持向量机的应用 – 兵王问题 （参数设置） 31:51


### P69 支持向量机的应用 – 兵王问题 （测试结果） 04:23


### P70 ROC 曲线 18:19


### P71 支持向量机 – 处理多类问题 11:58


### P72 人工神经网络 – 神经元的数学模型 17:27


### P73 人工神经网络 – 感知器算法 38:58


### P74 人工神经网络 – 人工智能的第一次寒冬 15:07


### P75 人工神经网络 – 多层神经网络 11:44


### P76 人工神经网络 — 三层神经网络可以模拟任意决策面 15:54


### P77 人工神经网络 — 后向传播算法 1:29:55


### P78 人工神经网络 – 参数设置 1:22:15


### P79 深度学习数据库准备 18:00


### P80 深度学习自编码器 23:42


### P81 深度学习 卷积神经网络 LeNet 1:18:45


### P82 深度学习 – 卷积神经网络（AlexNet） 39:22


### P83 深度学习 – 编程工具（Caffe 和 Tensorflow） 29:32


### P84 深度学习 – 近年来流行的网络结构 19:05


### P85 深度学习 – 卷积神经网络的应用 18:40


### P86 AlphaGo（围棋有必胜策略的证明） 08:58


### P87 强化学习 Q - learning 1:18:08


### P88 强化学习（policy gradience） 19:23


### P89 增强学习 \_(AlphaGo) 23:25


### P90 特征提取 – 主成分分析（PCA） 1:13:04


### P91 特征选择 – 自适应提升（AdaBoost） 1:11:15


### P92 目标检测 （RCNN 和 FCN） 57:25


### P93 概率分类法概述 19:54


### P94 概率密度估计 – 朴素贝叶斯分类器 16:41


### P95 概率密度估计 – 高斯密度函数 31:06


### P96 概率密度估计 – 高斯混合模型 03:47


### P97 EM 算法（高斯混合模型和 K - 均值算法） 48:44


### P98 K - 均值算法在图像压缩方面的应用 05:16


### P99 高斯混合模型在说话人识别方面的应用 23:49


### P100 EM 算法（收敛性证明） 39:24


### P101 语音识别概述 07:27


### P102 隐含马尔科夫过程 1:29:00


### P103 大词汇量连续语音识别介绍 35:15


### P104 循环神经网络（RNN）和 LSTM 39:42


### P105 人工智能中的哲学 缸中之脑 09:05


### P106 人工智能中的哲学 意识问题 13:04


### P107 人工智能中的哲学 图灵测试 04:17


### P108 人工智能中的哲学 世界是否有规律 05:38


### P109 人工智能中的哲学 中文屋子假想试验 07:03


### P110 人工智能中的哲学 创造力和洞穴理论 14:00


### P111 人工智能中的哲学 - 生成对抗网络 15:41


### P112 人工智能中的哲学 - 道德难题 09:37


### P113 人工智能中的哲学未来展望 04:58

[toolbox](http://www.atoolbox.net/Tool.php?Id=715)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-02-12-ml-ZhejiangUniversity.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1qf4y1x7kB/]({% include relrefx.html url="/backup/2023-02-12-ml-ZhejiangUniversity.md/www.bilibili.com/93706280.html" %})
- [https://blog.csdn.net/weixin_41929524/article/details/112253138]({% include relrefx.html url="/backup/2023-02-12-ml-ZhejiangUniversity.md/blog.csdn.net/bfbc4011.html" %})
- [https://blog.csdn.net/DIPDWC/article/details/117110173]({% include relrefx.html url="/backup/2023-02-12-ml-ZhejiangUniversity.md/blog.csdn.net/27c2fbca.html" %})
- [https://blog.csdn.net/DIPDWC/article/details/117215115]({% include relrefx.html url="/backup/2023-02-12-ml-ZhejiangUniversity.md/blog.csdn.net/ffbce7aa.html" %})
- [https://blog.csdn.net/DIPDWC/article/details/112686489]({% include relrefx.html url="/backup/2023-02-12-ml-ZhejiangUniversity.md/blog.csdn.net/4daa8911.html" %})
- [https://blog.csdn.net/DIPDWC/article/details/117436454]({% include relrefx.html url="/backup/2023-02-12-ml-ZhejiangUniversity.md/blog.csdn.net/688a7b1e.html" %})
- [http://www.atoolbox.net/Tool.php?Id=715]({% include relrefx.html url="/backup/2023-02-12-ml-ZhejiangUniversity.md/www.atoolbox.net/ecf02067.php" %})
