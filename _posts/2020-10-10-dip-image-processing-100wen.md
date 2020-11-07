---
layout: post
title: "“数字图像处理”笔记 -- 画像処理 100 本ノック（为图像处理初学者设计的 100 个问题）"
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
visibility: hidden
toc: true
toclistyle: none
comments:
mathjax: true
mermaid: truez
glslcanvas:
---

「画像処理 100 本ノック」中文版本！为图像处理初学者设计的 100 个问题。
<https://github.com/gzr2017/ImageProcessing100Wen>

画像処理 100 本ノックして画像処理を画像処理して画像処理するためのもの Jap, Eng, Chi
<https://github.com/yoyoyo-yo/Gasyori100knock>


## 环境搭建

[windows 安装并使用 Anaconda](https://www.cnblogs.com/xiongmozhou/p/9391323.html)

* Anaconda 下载地址 <https://www.anaconda.com/download/>

* 加入国内清华的镜像

  ```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```


## 颜色处理


### 一：通道交换


### 二：灰度化（Grayscale）


### 三：二值化（Thresholding）


### 四：大津二值化算法（Otsu's Method）


### 五：$\text{HSV}$ 变换


### 六：减色处理


## 图像池化


### 七：平均池化（Average Pooling）


### 八：最大池化（Max Pooling）


## 各种滤波器

* 图像平滑

    * 九：高斯滤波（Gaussian Filter）-- 去除噪声
    * 十：中值滤波（Median Filter）-- 去除噪声
    * 十一：均值滤波器 -- 去除噪声
    * 十九：LoG 滤波器 -- ??

* 边缘检测

    * 十三：MAX-MIN 滤波器 -- 边缘检测 / 特征提取
    * 十四：差分滤波器（Differential Filter） -- 边缘检测
    * 十五：Sobel 滤波器 -- 提取特定方向（纵向或横向）的边缘
    * 十六：Prewitt 滤波器 -- 边缘检测
    * 十七：Laplacian 滤波器 -- 亮度进行二次微分从而检测边缘
    * 十九：LoG 滤波器 -- ??

* 边缘加强

    * 十八：Emboss 滤波器 -- 使物体轮廓更加清晰
    * 十九：LoG 滤波器 -- ??

* 没啥用处

    * 十二：Motion Filter -- 感觉倾斜模糊了


### 九：高斯滤波（Gaussian Filter）

高斯滤波器是一种可以使图像平滑的滤波器，用于去除噪声。可用于去除噪声的滤波器还有中值滤波器（参见问题十），平滑滤波器（参见问题十一）、LoG 滤波器（参见问题十九）。

高斯滤波器将中心像素周围的像素按照高斯分布加权平均进行平滑化。


### 十：中值滤波（Median Filter）

中值滤波器是一种可以使图像平滑的滤波器。


### 十一：均值滤波器

均值滤波器使用网格内像素的平均值。


### 十二：Motion Filter

Motion Filter 取对角线方向的像素的平均值。


### 十三：MAX-MIN 滤波器

MAX-MIN 滤波器使用网格内像素的最大值和最小值的差值对网格内像素重新赋值。通常用于边缘检测。

边缘检测用于检测图像中的线。像这样提取图像中的信息的操作被称为特征提取。
边缘检测通常在灰度图像上进行。


### 十四：差分滤波器（Differential Filter）

差分滤波器对图像亮度急剧变化的边缘有提取效果，可以获得邻接像素的差值。


### 十五：Sobel 滤波器

Sobel 滤波器可以提取特定方向（纵向或横向）的边缘。


### 十六：Prewitt 滤波器

Prewitt 滤波器是用于边缘检测的一种滤波器。


### 十七：Laplacian 滤波器

Laplacian 滤波器是对图像亮度进行二次微分从而检测边缘的滤波器。


### 十八：Emboss 滤波器

Emboss 滤波器可以使物体轮廓更加清晰。


### 十九：LoG 滤波器

LoG 即高斯-拉普拉斯（Laplacian of Gaussian）的缩写，使用高斯滤波器使图像平滑化之后再使用拉普拉斯滤波器使图像的轮廓更加清晰。

为了防止拉普拉斯滤波器计算二次微分会使得图像噪声更加明显，所以我们首先使用高斯滤波器来抑制噪声。


## 直方图


### 二十：直方图

直方图显示了不同数值的像素出现的次数。


### 二十一：直方图归一化（Histogram Normalization）

将直方图所有分量限制在一定范围。


### 二十二：直方图操作

这里并不是变更直方图的动态范围，而是让直方图变得平坦。

可以使用下式将平均值为 m 标准差为 s 的直方图变成平均值为 m0 标准差为 s0 的直方图。


### 二十三：直方图均衡化（Histogram Equalization）

拉开灰度差别，增强对比度。

直方图均衡化是使直方图变得平坦的操作，是不需要计算上面的问题中的平均值、标准差等数据使直方图的值变得均衡的操作。


### 二十四：伽玛校正（Gamma Correction）

伽马校正用来对照相机等电子设备传感器的非线性光电转换特性进行校正。如果图像原样显示在显示器等上，画面就会显得很暗。伽马校正通过预先增大 RGB 的值来排除显示器的影响，达到对图像修正的目的。


## 图像插值


### 二十五：最邻近插值（Nearest-neighbor Interpolation）

最近邻插值在图像放大时补充的像素取最临近的像素的值。由于方法简单，所以处理速度很快，但是放大图像画质劣化明显。


### 二十六：双线性插值（Bilinear Interpolation）

双线性插值考察 4 邻域的像素点，并根据距离设置权值。虽然计算量增大使得处理时间变长，但是可以有效抑制画质劣化。


### 二十七：双三次插值（Bicubic Interpolation）

双三次插值是双线性插值的扩展，使用邻域 16 像素进行插值。


## 仿射变换


### 二十八：仿射变换（Afine Transformations）——平行移动


### 二十九：仿射变换（Afine Transformations）——放大缩小


### 三十：仿射变换（Afine Transformations）——旋转


### 三十一：仿射变换（Afine Transformations）——倾斜


## 傅立叶变换


### 三十二：傅立叶变换（Fourier Transform）

离散傅里叶变换太慢，快速傅里叶变换才有实用价值。


### 三十三：傅立叶变换——低通滤波

保留轮廓，移除细节。

在图像中，高频成分指的是颜色改变的地方（噪声或者轮廓等），低频成分指的是颜色不怎么改变的部分（比如落日的渐变）。在这里，使用去除高频成分，保留低频成分的低通滤波器吧！


### 三十四：傅立叶变换——高通滤波

保留细节，移除轮廓。

在这里，我们使用可以去除低频部分，只保留高频部分的高通滤波器。


### 三十五：傅立叶变换——带通滤波

不知道有啥用处。

在这里，我们使用可以保留介于低频成分和高频成分之间的分量的带通滤波器。


## JPEG 压缩


### 三十六：JPEG 压缩——第一步：离散余弦变换（Discrete Cosine Transformation）


### 三十七：PSNR


### 三十八：JPEG 压缩——第二步：离散余弦变换 + 量化


### 三十九：JPEG 压缩——第三步：YCbCr 色彩空间


### 四十：JPEG 压缩——第四步：YCbCr + 离散余弦变换 + 量化


## Canny 边缘检测


### 四十一：Canny 边缘检测：第一步——边缘强度


### 四十二：Canny 边缘检测：第二步——边缘细化


### 四十三：Canny 边缘检测：第三步——滞后阈值


## 霍夫直线检测


### 四十四：霍夫变换（Hough Transform）／直线检测——第一步：霍夫变换


### 四十五：霍夫变换（Hough Transform）／直线检测——第二步：NMS


### 四十六：霍夫变换（Hough Transform）／直线检测——第三步：霍夫逆变换


## 形态学


### 四十七：膨胀（Dilate）


### 四十八：腐蚀（Erode）


### 四十九：开运算（Opening Operation）

开运算可以用来去除仅存的小块像素。


### 五十：闭运算（Closing Operation）

闭运算能够将中断的像素连接起来。


### 五十一：形态学梯度（Morphology Gradient）

形态学梯度为经过膨胀操作（dilate）的图像与经过腐蚀操作（erode）的图像的差，可以用于抽出物体的边缘。


### 五十二：顶帽（Top Hat）

顶帽运算是原图像与开运算的结果图的差。可以提取出细线状的部分或者噪声。


### 五十三：黑帽（Black Hat）

黑帽运算是原图像与闭运算的结果图的差。可以提取出细线状的部分或者噪声。


## 模式匹配


### 五十四：使用误差平方和算法（Sum of Squared Difference）进行模式匹配（Template Matching）


### 五十五：使用绝对值差和（Sum of Absolute Differences）进行模式匹配


### 五十六：使用归一化交叉相关（Normalization Cross Correlation）进行模式匹配


### 五十七：使用零均值归一化交叉相关（Zero-mean Normalization Cross Correlation）进行模式匹配


## 连通域标记


### 五十八：4−邻域连通域标记


### 五十九：8−邻域连通域标记


## 图层混合


### 六十： 透明混合（Alpha Blending）


## 连接数


### 六十一：4−连接数


### 六十二：8−连接数


## 细化处理


### 六十三：细化处理


### 六十四：Hilditch 细化算法


### 六十五：Zhang-Suen 细化算法


## 方向梯度直方图

HOG（Histogram of Oriented Gradients）是一种表示图像特征量的方法。特征量是表示图像的状态等的向量集合。


### 六十六：方向梯度直方图（HOG）第一步：梯度幅值·梯度方向


### 六十七：方向梯度直方图（HOG）第二步：梯度直方图


### 六十八：方向梯度直方图（HOG）第三步：直方图归一化


### 六十九：方向梯度直方图（HOG）第四步：可视化特征量


## 掩膜


### 七十：色彩追踪（Color Tracking）


### 七十一：掩膜（Masking）


### 七十二：掩膜（色彩追踪（Color Tracking）+ 形态学处理）


## 显著图


### 七十三：缩小和放大


### 七十四：使用差分金字塔提取高频成分

在这里求得的就是图像的边缘。即，图像的高频成分。


### 七十五：高斯金字塔（Gaussian Pyramid）


### 七十六：显著图（Saliency Map）


## Gabor 滤波器

Gabor 滤波器是一种结合了高斯分布和频率变换的滤波器，用于在图像的特定方向提取边缘。


### 七十七：Gabor 滤波器（Gabor Filter）


### 七十八：旋转 Gabor 滤波器


### 七十九：使用 Gabor 滤波器进行边缘检测


### 八十：使用 Gabor 滤波器进行特征提取

通过将问题七十九中得到的 4 张图像加在一起，提取图像的特征。


## 角点检测


### 八十一：Hessian 角点检测


### 八十二：Harris 角点检测第一步：Sobel + Gausian


### 八十三：Harris 角点检测第二步：角点检测


## 简单图像识别


### 八十四：简单图像识别第一步：减色化 + 柱状图


### 八十五：简单图像识别第二步：判别类别


### 八十六：简单图像识别第三步：评估


### 八十七：简单图像识别第四步：k-NN


## 图像分类


### 八十八：k-平均聚类算法（k -means Clustering）第一步：生成质心


### 八十九：k-平均聚类算法（k -means Clustering）第二步：聚类（Clustering）


### 九十：k-平均聚类算法（k -means Clustering）第三步：调整初期类别


### 九十一：$k-$ 平均聚类算法进行减色处理第一步----按颜色距离分类


### 九十二：利用 $k-$ 平均聚类算法进行减色处理第二步----减色处理


## 机器学习


### 九十三：准备机器学习的训练数据第一步——计算 $\text{IoU}$


### 九十四：准备机器学习的训练数据第二步——随机裁剪（Random Cropping）


### 九十五：神经网络（Neural Network）第一步——深度学习（Deep Learning）


### 九十六：神经网络（Neural Network）第二步——训练


## 简单物体检测


### 九十七：简单物体检测第一步----滑动窗口（Sliding Window）+ HOG


### 九十八：简单物体检测第二步——滑动窗口（Sliding Window）+ NN


### 九十九：简单物体检测第三步——非极大值抑制（Non-Maximum Suppression）


### 一百：简单物体检测第四步——评估（Evaluation）：Precision、Recall、F-Score、mAP
