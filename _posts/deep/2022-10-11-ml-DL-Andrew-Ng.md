---
layout: post
title: "机器学习 -- 吴恩达深度学习（进行中）"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
date: 2022-08-31 19:57:58 +0800
cluster: "机器学习课程"
---

* 吴恩达机器学习 19:37:16 142 <https://www.bilibili.com/video/BV1Bq421A74G/>
* 吴恩达深度学习 27:44:07 183 <https://www.bilibili.com/video/BV1FT4y1E74V/>
    * <https://www.bilibili.com/video/BV1D1QqYtExP>
* [html2text](http://www.atoolbox.net/Tool.php?Id=715)

机器学习早期版本（岁月觞）：[吴恩达机器学习系列课程 {% include relref_bili.html %}](https://www.bilibili.com/video/BV164411b7dx/)


# 吴恩达深度学习


## 1 1.1.1 欢迎 05:33


## 2 2.1.2 什么是神经网络 07:17


## 3 3.1.3 用神经网络进行监督学习 08:30


## 4 4.1.4 为什么深度学习会兴起？ 10:22


## 5 5.1.5 关于这门课 02:29


## 6 6.1.6 课程资源 01:56


## 7 7.2.1 二分分类 08:25


## 8 8.2.2 logistic 回归 06:00


## 9 9.2.3 logistic 回归损失函数 08:12


## 10 10.2.4 梯度下降法 11:24


## 11 11.2.5 导数 07:11


## 12 12.2.6 更多导数的例子 10:28


## 13 13.2.7 计算图 03:34


## 14 14.2.8 使用计算图求导 14:35


## 15 15.2.9 logistic 回归中的梯度下降法 06:43


## 16 16.2.10 m 个样本的梯度下降 08:01


## 17 17.2.11 向量化 08:05


## 18 18.2.12 向量化的更多例子 06:22


## 19 19.2.13 向量化 logistic 回归 07:33


## 20 20.2.14 向量化 logistic 回归的梯度输出 09:39

[Synthetic-data-with-text-and-image {% include relref_cnblogs.html %}](https://www.cnblogs.com/shouhuxianjian/p/9962016.html)

本文是之前为了解决如何将文字贴到图片上而编写的代码，默认是如发票一类的，所以并未考虑透视变换等。
且采用的是 pygame 粘贴方式，之前也尝试过 opencv 的 seamlessClone 粘贴。

值得注意的是，通过修改参数，增加各种干扰操作（羽化，噪音等等），生成的数据集看似丰富，其实因为内在的数据分布还是十分单一，也就是用该数据集去作为 ocr 的模型训练集，得到的模型仍然无法在现实生活场景上使用。
因为在现实世界中，你光照角度，拍摄角度，打印机用墨等等都是一种变量，而这些变量都会让现实世界的票据呈现的文字内在数据分布是十分丰富的。
而通过简单的代码生成的数据分布却并不能覆盖，或者说重叠其中一部分。故而，通过代码生成数据集的方式是无法解决 ocr 现实数据集不够的问题的。


## 21 21.2.15 Python 中的广播 11:07


## 22 22.2.16 关于 python \_ numpy 向量的说明 06:50

{% include image.html url="/assets/images/221011-ml-dl-andrew-ng/20250825232801.png" %}


## 23 23.2.17 Jupyter \_ ipython 笔记本的快速指南 03:44

<https://huggingface.co/spaces/mteb/leaderboard>
<https://huggingface.co/spaces/mteb/leaderboard_legacy>


## 24 24.2.18 （选修）logistic 损失函数的解释 07:16


## 25 25.3.1 神经网络概览 04:27


## 26 26.3.2 神经网络表示 05:15


## 27 27.3.3 计算神经网络的输出 09:59


## 28 28.3.4 多个样本的向量化 09:06


## 29 29.3.5 向量化实现的解释 07:38


## 30 30.3.6 激活函数 10:57


## 31 31.3.7 为什么需要非线性激活函数？ 05:37


## 32 32.3.8 激活函数的导数 07:58


## 33 33.3.9 神经网络的梯度下降法 09:58


## 34 34.3.10 （选修）直观理解反向传播 15:49

潜在空间可视化：PCA、t-SNE、UMAP
<https://www.bilibili.com/video/BV1oH4y1c7ZR/>

群论的本质
<https://www.bilibili.com/video/BV1UKuwzbEqt/>
群论：一个超前于时代的强大理论
<https://www.bilibili.com/video/BV1XMhgz1EXm/>

大型语言模型中的注意力机制图解（中文配音）
<https://www.bilibili.com/video/BV1ki4y1871e/>
【中文配音】3Blue1Brown 线性代数的本质全 16 章｜动画拆解矩阵 / 向量 / 特征值，数学直觉大升级！
<https://www.bilibili.com/video/BV19TNLzhEeW/>
【中文配音】MIT18.06 线性代数 最新翻译
<https://www.bilibili.com/video/BV163sqetEyJ/>


## 35 35.3.11 随机初始化 07:58


## 36 36.4.1 深层神经网络 05:52


## 37 37.4.2 前向和反向传播 10:30


## 38 38.4.3 深层网络中的前向传播 07:16


## 39 39.4.4 核对矩阵的维数 11:11


## 40 40.4.5 为什么使用深层表示 10:34


## 41 41.4.6 搭建深层神经网络块 08:34


## 42 42.4.7 参数 VS 超参数 07:18


## 43 43.4.8 这和大脑有什么关系？ 03:18


## 44 44.1. 吴恩达采访 Geoffrey Hinton 40:23


## 45 45.2. 吴恩达采访 Pieter Abbeel 16:04


## 46 46.3. 吴恩达采访 Ian Goodfellow 14:56


## 47 47.1.1 训练 \_ 开发 \_ 测试集 12:05


## 48 48.1.2 偏差 \_ 方差 08:47


## 49 49.1.3 机器学习基础 06:22


## 50 50.1.4 正则化 09:43


## 51 51.1.5 为什么正则化可以减少过拟合？ 07:10


## 52 52.1.6 Dropout 正则化 09:26


## 53 53.1.7 理解 Dropout 07:05


## 54 54.1.8 其他正则化方法 08:25


## 55 55.1.9 归一化输入 05:31


## 56 56.1.10 梯度消失与梯度爆炸 06:08


## 57 57.1.11 神经网络的权重初始化 06:13


## 58 58.1.12 梯度的数值逼近 06:36


## 59 59.1.13 梯度检验 06:35


## 60 60.1.14 关于梯度检验实现的注记 05:19


## 61 61.2.1 Mini-batch 梯度下降法 11:30


## 62 62.2.2 理解 mini-batch 梯度下降法 08:15


## 63 63.2.3 指数加权平均 05:59


## 64 64.2.4 理解指数加权平均 09:43


## 65 65.2.5 指数加权平均的偏差修正 04:12


## 66 66.2.6 动量梯度下降法 09:21


## 67 67.2.7 RMSprop 07:42


## 68 68.2.8 Adam 优化算法 07:09


## 69 69.2.9 学习率衰减 06:45


## 70 70.2.10 局部最优的问题 05:24


## 71 71.3.1 调试处理 07:11


## 72 72.3.2 为超参数选择合适的范围 08:51


## 73 73.3.3 超参数训练的实践：Pandas VS Caviar 06:52


## 74 74.3.4 正则化网络的激活函数 08:56


## 75 75.3.5 将 Batch Norm 拟合进神经网络 12:56


## 76 76.3.6 Batch Norm 为什么奏效？ 11:40


## 77 77.3.7 测试时的 Batch Norm 05:47


## 78 78.3.8 Softmax 回归 11:48


## 79 79.3.9 训练一个 Softmax 分类器 10:08


## 80 80.3.10 深度学习框架 04:16


## 81 81.3.11 TensorFlow 16:08


## 82 82.1. 吴恩达采访 Yoshua Bengio 25:49


## 83 83.2. 吴恩达采访 林元庆 13:38


## 84 84.1.1 为什么是 ML 策略 02:44


## 85 85.1.2 正交化 10:39


## 86 86.1.3 单一数字评估指标 07:17


## 87 87.1.4 满足和优化指标 05:59


## 88 88.1.5 训练 \_ 开发 \_ 测试集划分 06:36 88.1.5 训练 _ 开发 _ 测试集划分


## 89 89.1.6 开发集合测试集的大小 05:40


## 90 90.1.7 什么时候该改变开发 \_ 测试集和指标 11:08 90.1.7 什么时候该改变开发 _ 测试集和指标


## 91 91.1.8 为什么是人的表现 05:47


## 92 92.1.9 可避免偏差 07:00


## 93 93.1.10 理解人的表现 11:13


## 94 94.1.11 超过人的表现 06:22


## 95 95.1.12 改善你的模型的表现 04:35


## 96 96.2.1 进行误差分析 10:33


## 97 97.2.2 清除标注错误的数据 13:06


## 98 98.2.3 快速搭建你的第一个系统，并进行迭代 06:02


## 99 99.2.4 在不同的划分上进行训练并测试 10:56


## 100 100.2.5 不匹配数据划分的偏差和方差 18:17


## 101 101.2.6 解决数据不匹配 10:09


## 102 102.2.7 迁移学习 11:18


## 103 103.2.8 多任务学习 13:00


## 104 104.2.9 什么是端到端的深度学习 11:48


## 105 105.2.10 是否要使用端到端的深度学习 10:20


## 106 106.1. 采访 Andrej Karpathy 15:11


## 107 107.2. 采访 Ruslan Salakhutdinov 17:09


## 108 108.1.1 计算机视觉 05:45


## 109 109.1.2 边缘检测示例 11:32


## 110 110.1.3 更多边缘检测内容 07:58


## 111 111.1.4 Padding 09:50


## 112 112.1.5 卷积步长 09:03


## 113 113.1.6 三维卷积 10:45


## 114 114.1.7 单层卷积网络 16:11


## 115 115.1.8 简单卷积网络示例 08:33


## 116 116.1.9 池化层 10:26


## 117 117.1.10 卷积神经网络示例 12:38


## 118 118.1.11 为什么使用卷积？ 09:41


## 119 119.2.1 为什么要进行实例探究？ 03:09


## 120 120.2.2 经典网络 18:20


## 121 121.2.3 残差网络 07:09


## 122 122.2.4 残差网络为什么有用？ 09:13


## 123 123.2.5 网络中的网络以及 1×1 卷积 06:41


## 124 124.2.6 谷歌 Inception 网络简介 10:15


## 125 125.2.7 Inception 网络 08:47


## 126 126.2.8 使用开源的实现方案 04:57


## 127 127.2.9 迁移学习 08:49


## 128 128.2.10 数据扩充 09:32


## 129 129.2.11 计算机视觉现状 12:39


## 130 130.3.1 目标定位 11:55


## 131 131.3.2 特征点检测 05:57


## 132 132.3.3 目标检测 05:50


## 133 133.3.4 卷积的滑动窗口实现 11:09


## 134 134.3.5 Bounding Box 预测 14:32


## 135 135.3.6 交并比 04:20


## 136 136.3.7 非极大值抑制 08:03


## 137 137.3.8 Anchor Boxes 09:44


## 138 138.3.9 YOLO 算法 07:02


## 139 139.3.10 候选区域 06:28


## 140 140.4.1 什么是人脸识别？ 04:38


## 141 141.4.2 One-Shot 学习 04:46 141.4.2  One-Shot 学习


## 142 142.4.3 Siamese 网络 04:36 142.4.3  Siamese 网络


## 143 143.4.4 Triplet 损失 15:31 143.4.4  Triplet 损失


## 144 144.4.5 面部验证与二分类 06:06 144.4.5  面部验证与二分类


## 145 145.4.6 什么是神经风格转换？ 02:03 145.4.6  什么是神经风格转换？


## 146 146.4.7 什么是深度卷积网络？ 07:58 146.4.7  什么是深度卷积网络？


## 147 147.4.8 代价函数 \_bilibili 03:51 147.4.8 代价函数 \_bilibili


## 148 148.4.9 内容代价函数 03:38 148.4.9  内容代价函数


## 149 149.4.10 风格代价函数 17:02 149.4.10  风格代价函数


## 150 150.4.11 一维到三维推广 09:09


## 151 151.1.1 为什么选择序列模型 03:01


## 152 152.1.2 数学符号 09:16


## 153 153.1.3 循环神经网络 16:32


## 154 154.1.4 通过时间的反向传播 06:12


## 155 155.1.5 不同类型的循环神经网络 09:35


## 156 156.1.6 语言模型和序列生成 12:02


## 157 157.1.7 新序列采样 08:39


## 158 158.1.8 带有神经网络的梯度消失 06:29


## 159 159.1.9 GRU 单元 17:07


## 160 160.1.10 长短期记忆（LSTM） 09:54


## 161 161.1.11 双向神经网络 08:20


## 162 162.1.12 深层循环神经网络 05:17


## 163 163.2.1 词汇表征 10:08


## 164 164.2.2 使用词嵌入 09:23


## 165 165.2.3 词嵌入的特性 11:55


## 166 166.2.4 嵌入矩阵 05:58


## 167 167.2.5 学习词嵌入 10:10


## 168 168.2.6 Word2Vec 12:48


## 169 169.2.7 负采样 11:54


## 170 170.2.8 GloVe 词向量 11:09


## 171 171.2.9 情绪分类 07:38


## 172 172.2.10 词嵌入除偏 11:09


## 173 173.3.1 基础模型 06:19


## 174 174.3.2 选择最可能的句子 08:57


## 175 175.3.3 定向搜索 11:55


## 176 176.3.4 改进定向搜索 11:01


## 177 177.3.5 定向搜索的误差分析 09:44


## 178 178.3.6 Bleu 得分（选修） 16:27


## 179 179.3.7 注意力模型直观理解 09:42


## 180 180.3.8 注意力模型 12:24


## 181 181.3.9 语音辨识 08:54


## 182 182.3.10 触发字检测 05:04


## 183 183.3.11 结论和致谢 02:45



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-10-11-ml-DL-Andrew-Ng.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1Bq421A74G/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/738a77eb.html" %})
- [https://www.bilibili.com/video/BV1FT4y1E74V/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/821695be.html" %})
- [https://www.bilibili.com/video/BV1D1QqYtExP]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/7fb10648.html" %})
- [http://www.atoolbox.net/Tool.php?Id=715]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.atoolbox.net/ecf02067.php" %})
- [https://www.bilibili.com/video/BV164411b7dx/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/816eb90a.html" %})
- [https://www.cnblogs.com/shouhuxianjian/p/9962016.html]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.cnblogs.com/4a79bd4d.html" %})
- [https://huggingface.co/spaces/mteb/leaderboard]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/huggingface.co/8cd97355.html" %})
- [https://huggingface.co/spaces/mteb/leaderboard_legacy]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/huggingface.co/9e731ed2.html" %})
- [https://www.bilibili.com/video/BV1oH4y1c7ZR/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/9c9b3856.html" %})
- [https://www.bilibili.com/video/BV1UKuwzbEqt/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/23fbb52c.html" %})
- [https://www.bilibili.com/video/BV1XMhgz1EXm/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/23a8fb16.html" %})
- [https://www.bilibili.com/video/BV1ki4y1871e/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/7704a269.html" %})
- [https://www.bilibili.com/video/BV19TNLzhEeW/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/1d4fe86e.html" %})
- [https://www.bilibili.com/video/BV163sqetEyJ/]({% include relrefx.html url="/backup/2022-10-11-ml-DL-Andrew-Ng.md/www.bilibili.com/ba6412a4.html" %})
