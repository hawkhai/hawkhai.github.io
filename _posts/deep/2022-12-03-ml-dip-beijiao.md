---
layout: post
title: "人工智能 -- 北交 / 图像处理与机器学习（已完成）"
author:
location: "珠海"
categories: ["人工智能"]
tags: ["图像处理", "人工智能"]
toc: true
toclistyle: none
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "人工智能课程"
---

学习是一件非常困难的事情。首先是工作本身已经很累了，然后是一些客观的家里的事情会消耗你的时间，再然后是新知识本身的难度，面对一堆看不懂的公式，再掂量一下自己有限的智商，不学习貌似日子还是可以继续过下去，那我为什么还要学习呢？夜深人静的时候，媳妇已经睡下，想到自己人生将半，学习计划还是得坚持下去：夜来欹枕细思量，独卧残灯漏夜长； **名不显时心不朽，再挑灯火夜读书。**

路虽远行则将至。
北交 · [图像处理与机器学习 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1Kh411X7Qv/)
“数字图像处理”主要包括图像增强、形态学处理、图像分割等。
“机器学习”部分主要包括贝叶斯决策、人工神经网络以及深度学习导论。


### P1 0 绪论授课视频 09:45


### P2 1-1 基本概念授课视频 06:28


### P3 1-2 基本概念（续）授课视频 08:56


### P4 1-3 图像直方图授课视频 08:10


### P5 课程实验平台介绍视频 03:46


### P6 实验环境安装配置，请务必观看！ 07:51


### P7 实验一图像显示~1 08:21


### P8 实验二图像直方图视频 04:23


### P9 2.1 引言 07:32


### P10 2.2 灰度变换授课视频 08:46


### P11 直方图均衡授课视频 14:07

已完成。


### P12 2-4 代数运算授课视频 04:27


### P13 2-5 空间域滤波授课视频 11:15


### P14 2-6 空间域滤波中值滤波 04:52


### P15 2-7 空间域滤波高通 10:08


### P16 2.8 二维傅里叶变换定义授课视频 05:24


### P17 2.9 二维傅里叶变换性质授课视频 07:17


### P18 2.10 频域滤波低通授课视频 14:52

[note {% include relref_csdn.html %}](https://blog.csdn.net/cjsh_123456/article/details/79342300)
巴特沃斯（Butterworth）滤波器
{% include image.html url="/assets/images/221203-ml-dip-beijiao/20180221115450744.png" %}
1 阶巴特沃斯没有“振铃“，随着阶数增大，振铃现象越发明显。下图取 n=2, 可以看出空域函数外围部分出现震荡。
{% include image.html url="/assets/images/221203-ml-dip-beijiao/20141216233653921.png" %}

高斯滤波器的过度特性非常平坦，因此不会产生振铃现象。


### P19 2.11 频域滤波高通授课视频 05:37


### P20 2.12 频域滤波同态滤波授课视频 09:27

同态滤波实现图像去雾。
消除不均匀照度的影响而又不损失图象细节。

同态滤波是把频率过滤和灰度变换结合起来的一种图像处理方法，它依靠图像的照度 / 反射率模型作为频域处理的基础，利用压缩亮度范围和增强对比度来改善图像的质量。使用这种方法可以使图像处理符合人眼对于亮度响应的非线性特性，避免了直接对图像进行傅立叶变换处理的失真。

基于 Retinex 滤波。基于迭代多尺度引导滤波 Retinex 的低照度图像增强。
{% include image.html url="/assets/images/221203-ml-dip-beijiao/20200929100704232.png" %}

#### 颜色

[颜色 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/498289926)

{% include image.html url="/assets/images/221203-ml-dip-beijiao/v2-a2094f80d456f0cbd0adf14ed4f6b90e_720w.webp" caption="RGB（显示器）" %}

因为 RGB 模型中与『负光』混合所带来的种种问题，CIE 从数学上定义了三种标准基色 XYZ（是理论上的颜色，而非实际的颜色），形成了『CIE XYZ 颜色模型』。
{% include image.html url="/assets/images/221203-ml-dip-beijiao/v2-cf15f1ee5c3f390873668ab1c51fdcb2_720w.webp" caption="XYZ 颜色模型" %}

CMYK（印刷）
Lab & YUV（YCbCr 现代彩色电视）
HSI（人的视觉系统）、HSV

颜色建模的发展历程：
1. 基于人眼视觉感知三原色理论，CIE 通过大量实验数据建立了 RGB 颜色模型，标准化了 RGB 表示。
2. 为了解决 RGB 模型中与负光混合所带来的种种问题，CIE 从数学上定义了三种标准基色 XYZ，形成了 CIE XYZ 颜色模型。
3.  在模拟电视时代，RGB 工业显示器要求一幅彩色图像由分开的 R、G、B 信号组成，而电视显示器则需要混合信号输入，为了实现对这两种标准的兼容，NTSC 基于 XYZ 模型制定了 YIQ 颜色模型，实现了彩色电视和黑白电视的信号兼容。
4. 为了解决 NTSC YIQ 的组合模拟视频信号中分配给色度信息的带宽较低，而影响了图像颜色质量的问题，PAL 引入了 YUV 颜色模型，支持用不同的采样格式来调整传输的色度信息量。
5. 进入数字电视时代，ITU-R 为数字视频转换制定了 YCbCr 颜色模型，成为我们现在最常使用的颜色模型。

在早年 CRT 显示器流行的年代，我们遇到了显示伽马问题，从而引入了伽马校正过程并延用至今。


### P21 实验三直方图均衡 05:18


### P22 实验平台介绍 03:47


### P23 实验平台设置 08:20

看完了。


### P24 实验四均值高斯低通滤波视频 05:16


### P25 实验五中值滤波视频 03:53


### P26 3.1 形态学基本概念视频 04:57


### P27 3.2 形态学处理算法 11:09


### P28 3.3 图像形态学处理应用视频 05:43


### P29 实验七图像形态学处理 07:00


### P30 4.1 图像分割引言 06:00


### P31 4.2 基于阈值的分割算法 10:30


### P32 4.3 基于边缘的分割算法 05:01


### P33 4.4 霍夫变换 07:31


### P34 4.5 基于区域的分割算法 08:28

基于区域的分割算法。4 叉树，根据方差递归回溯合并。
[note {% include relref_github.html %}](https://gy23333.github.io/2020/01/19/%E5%9F%BA%E4%BA%8E%E5%8C%BA%E5%9F%9F%E7%9A%84%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2%E2%80%94%E2%80%94%E5%8C%BA%E5%9F%9F%E5%88%86%E8%A3%82%E4%B8%8E%E5%90%88%E5%B9%B6/)
​
分裂与合并是一种区域分割方式，将图像划分成不相交的区域，以某一检测准则从四叉树数据结构的任一层开始，对区域进行分裂或合并。并逐步改善区域划分的性能，直到最后将图像分成数量最小的均匀区域为止。

{% include image.html url="/assets/images/221203-ml-dip-beijiao/PUAhMeZjsBI6v8m.jpg" %}


### P35 5.1 人工智能简介 09:43

Alpha Go，基于深度神经网络、强化学习和蒙特卡洛树搜索。
Alpha Go/Zero 系统是一个伟大的工程作品，由多种方法混合组装而成。其中的核心组件是：
* 蒙特卡洛树搜索（用于树遍历的 PUCT 函数的一个变种）。
* 残差卷积 神经网络 —— 用于博弈评估和行动先验概率估算的策略和估值网络。
* 强化学习 —— 用于通过自我对弈来训练网络。


### P36 5.2 机器学习引言 10:21


### P37 5.3 贝叶斯公式 05:57


### P38 5.4 贝叶斯决策--最小错误率决策 03:25

{% include image.html url="/assets/images/221203-ml-dip-beijiao/20200313150754672.png" %}
{% include image.html url="/assets/images/221203-ml-dip-beijiao/20221218183113.png" %}
这里看完了。


### P39 5.5 贝叶斯决策--最小风险决策 08:26

{% include image.html url="/assets/images/221203-ml-dip-beijiao/20230107122309.png" %}
似然比
likelihood ratio, LR


### P40 5.6 判别函数（上） 11:20

判别函数
特征空间
决策面

贝叶斯理论并用贝叶斯的思想解释了线性回归器和分类器。
线性分类器
Linear Discriminant Function (LDF)


### P41 5.7 判别函数（下） 06:36

非线性分类器
Quadratic Discriminant Function (QDF)


### P42 5.8 概率密度估计--参数法 07:49

概率是已知参数，对结果可能性的预测。似然是已知结果，对参数是某个值的可能性预测。

[区别 {% include relref_cnblogs.html %}](https://www.cnblogs.com/eilearn/p/9433911.html)
* 极大似然估计（MLE，Maximum Likelihood Estimation）
    * 极大似然估计，就是利用已知的样本结果，反推最有可能（最大概率）导致这样结果的参数值（模型已知，参数未知）。
* 贝叶斯估计（BE，Bayesian Estimation）
    * 参数未知且不确定，因此作为随机变量，参数本身也是一个分布，同时，根据已有的信息可以得到参数 θ 的先验概率，根据先验概率来推断 θ 的后验概率。

[note {% include relref_cnblogs.html %}](https://www.cnblogs.com/simon6666/p/11009510.html)
极大似然估计（MLE）、贝叶斯估计、最大后验概率估计（MAP）
极大似然估计（Maximum likelihood estimation, 简称 MLE）和
最大后验概率估计（Maximum aposteriori estimation, 简称 MAP）是很常用的两种参数估计方法。


### P43 5.9 概率密度估计--非参数法 09:33

* Parzen window / Parzen 窗估计
* K-nearest Neighbor / k 最近邻估计


### P44 6.1 人工神经网络引言 09:28


### P45 6.2 单层神经网络 06:02


### P46 6.3 多层神经网络 08:53

{% include image.html url="/assets/images/221203-ml-dip-beijiao/20230108104712.png" %}


### P47 7.1 引言 08:21


### P48 7.2 卷积神经网络 13:36

1998, LeNet


### P49 7.3 深度学习网络 19:22

* Recurrent Neural Network, RNN 循环神经网络
* Long Short-Term Memory Neural Network, LSTM 长短时记忆神经网络

* LeNet, AlexNet, VGG, GoogleNet
* MobileNet, ShuffleNet：压缩存储量和计算量
* 层数极深网络：Deep Residual Network
* DenseNet
* Graph CNN
* Capsule(CapsNet)
* 生成对抗网络（GAN）

Caffe
* 加州伯克利（Yangqing Jia 等人），C++ 编写，主要面向视觉。
* <http://caffe.berkeleyvision.org/>

TensorFlow
* Google 开发，C++ 编写
* <https://www.tensorflow.org/>

Theono
* 2008 年诞生于蒙特利尔工学院（Yoshua Bengio），Python 编写
* www.deeplearning.net/software/theano/

Torch, PyTorch
* Torch: 历史悠久的机器学习综合平台，Lua 编写，torch.ch
* PyTorch: In Python.

MxNet
* 民间项目开发，C++ 编写，内存使用效率高，分布式计算能力强。
* mxnet.apache.org/

{% include image.html url="/assets/images/221203-ml-dip-beijiao/20230108211711.png" %}
[note](https://www.kdnuggets.com/2015/07/deep-learning-adversarial-examples-misconceptions.html)
Deep learning is **more vulnerable** to adversarial examples than other kind of machine leaning due to the **extreme non-linearity** of deep models.
Deep learning is more vulnerable to adversarial examples than other kind of machine learning.

#### 当前深度学习的不足

- 学习能力
    * 需要 **大量标记样本进行监督学习**
    * 人类：无监督、小样本、在线自适应
- 解释能力
    * 主流方法进行统计分类
    * 结构分析、 **可解释性** 不足
- 鲁棒性
    * 对噪声模式的 **拒识能力**
    * 对对抗样本的稳定性
- 综合信息处理能力
    * **多模态** 协同
    * **上下文** 、语义知识


### P50 8.1 聚类算法 19:02


### P51 8.2 主成份分析（上） 08:18


### P52 8.3 主成份分析（下） 05:34


### P53 9.1.1 复杂背景下的人脸检测算法预处理 07:26

三种方法：
* 模板匹配
* 特征提取
* 基于学习

Preprocessing
* Illumination gradient correction -- **这里有点意思。**
    * 光线为斜平面
    * 求出光平面，减去光平面。
* Histogram equalization
* Masking...

{% include image.html url="/assets/images/221203-ml-dip-beijiao/20230209003442.png" %}
{% include image.html url="/assets/images/221203-ml-dip-beijiao/20230209003521.png" %}


### P54 9.1.2 复杂背景下的人脸检测算法特征提取 06:01

* Gray levels 灰度级
* Gradient features 梯度
* Gabor features 边缘特征
* Harr features 小波


### P55 9.1.3 复杂背景下的人脸检测算法分类器设计 07:03

{% include image.html url="/assets/images/221203-ml-dip-beijiao/20230207001433.png" %}


### P56 9.2 基于深度学习的车辆检测算法 09:08

* 两级网络
    * 候选框生成网络（RPN）+ 检测识别网络
    * 网络结构较复杂，检测精度高，检测速度慢
* 单级网络
    * 同时预测物体选框和类别
    * 网络结构较简单，精度稍低，检测速度快。


### P57 大作业（上）车牌检测与字符分割 08:29


### P58 车牌检测与字符分割演示视频 01:07


### P59 大作业（下）车牌字符识别 02:32

分类器
* ANN
* SVM


### P60 实验平台搭建设置 07:51

[toolbox](http://www.atoolbox.net/Tool.php?Id=715)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-12-03-ml-dip-beijiao.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1Kh411X7Qv/]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/www.bilibili.com/8e92be72.html" %})
- [https://blog.csdn.net/cjsh_123456/article/details/79342300]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/blog.csdn.net/6c4bed89.html" %})
- [https://zhuanlan.zhihu.com/p/498289926]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/zhuanlan.zhihu.com/b66f35f1.html" %})
- [https://gy23333.github.io/2020/01/19/%E5%9F%BA%E4%BA%8E%E5%8C%BA%E5%9F%9F%E7%9A%84%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2%E2%80%94%E2%80%94%E5%8C%BA%E5%9F%9F%E5%88%86%E8%A3%82%E4%B8%8E%E5%90%88%E5%B9%B6/]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/gy23333.github.io/314f9593.html" %})
- [https://www.cnblogs.com/eilearn/p/9433911.html]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/www.cnblogs.com/e0fff013.html" %})
- [https://www.cnblogs.com/simon6666/p/11009510.html]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/www.cnblogs.com/f88dd4f1.html" %})
- [http://caffe.berkeleyvision.org/]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/caffe.berkeleyvision.org/199cc1bf.html" %})
- [https://www.tensorflow.org/]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/www.tensorflow.org/c8c2399b.html" %})
- [https://www.kdnuggets.com/2015/07/deep-learning-adversarial-examples-misconceptions.html]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/www.kdnuggets.com/69c72ced.html" %})
- [http://www.atoolbox.net/Tool.php?Id=715]({% include relrefx.html url="/backup/2022-12-03-ml-dip-beijiao.md/www.atoolbox.net/ecf02067.php" %})
