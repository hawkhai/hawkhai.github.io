---
layout: post
title: "“数字图像处理”笔记 -- 几个实验 (DIP)"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid: truez
glslcanvas:
---


## 基本几何变换


## 手写数字识别

* <https://www.jb51.net/article/133880.htm>

* <https://github.com/HanpuLiang/Simple-Handwritten-Numerel-Recogntion>


## scikit-image 进行图像分割

* <https://blog.csdn.net/weixin_42142987/article/details/87717861>


## 邮政编码识别

* [图像识别与处理笔记——字符识别、邮政编码识别（10 月 8 日暂存）](https://blog.csdn.net/mao_hui_fei/article/details/78177471)

* [2010 毕业设计](http://www.doc88.com/p-693272517244.html)

* [2005.3 毕业设计](https://wenku.baidu.com/view/c26f1ea5492fb4daa58da0116c175f0e7cd119ea.html) / [2005.3 毕业设计](https://max.book118.com/html/2018/1108/8013115051001132.shtm)

* [OpenCV：裁剪 6 位数的手写邮政编码](https://stackoom.com/question/3xNO6/Opencv-%E8%A3%81%E5%89%AA-%E4%BD%8D%E6%95%B0%E7%9A%84%E6%89%8B%E5%86%99%E9%82%AE%E6%94%BF%E7%BC%96%E7%A0%81)


## 汽车牌照识别

二值化阈值集中常用的选取方法：双峰（2-Mode）法，P 参数法，Otsu 法，迭代法。


### 大津法（OTSU 法或最大类间方差法）

假定一个阈值，方差越大，说明差别越大。


### 迭代法（最佳阈值法）


### 一些代码

* **from <https://github.com/wzh191920/License-Plate-Recognition>**

* 代码还可以 [车牌检测与定位](https://www.freesion.com/article/5566190803/)

* 代码还可以 [PYTHON 实现车牌识别](https://www.freesion.com/article/9575144324/)

* [使用 opencv 和 python 实现车牌区域提取](https://www.jianshu.com/p/08ddeb0d8878)

* [opencv + python 车牌识别](https://www.cnblogs.com/kekexxr/p/11574589.html)

* <https://github.com/DataXujing/vehicle-license-plate-recognition>


## 案例分析


### toP61-1 手写数字识别


### toP58-2 邮政编码识别


### toP60-3 汽车牌照识别


### toP62-4 条形码识别


### toP63-5 印刷体汉字识别


### toP54-6 人脸识别


### toP57-7 细胞识别与统计

{% include image.html url="/images/digital-image-processing3/xibao.png" %}


### toP55 SAR 图像分割 / 遥感图像配准

谱聚类（求解规范化 Laplace 矩阵的特征值和特征向量）


### toP56/59 总变差（TV）模型·图像恢复

图象恢复是一个客观过程，需要利用**某些先验知识从退化和干扰的图像中去除模糊因素和噪声、尽可能恢复图像的本来面貌**。复原技术一般是先把**退化和干扰模型化**，然后采用相反的过程进行处理，复原图像。


### 数字图像处理 源码

* **<http://accu.cc/content/pil/agwn/>**

* 学习笔记 <https://github.com/LiuFG/digital_image_process>

* **孔洞填充、骨架算法、边界提取。**冈萨雷斯《数字图像处理》Python（第三版） <https://github.com/qcymkxyc/Image-Process>

* <https://github.com/iwuqing/Digital-Image-Processing>

* 冈萨雷斯《数字图像处理》读书笔记 <https://github.com/MAhaitao999/digital_image_processing>

* 数字图像处理（第三版） <https://github.com/ljy9826/Digital-Image-Processing_code>


### CPP 源码

冈萨雷斯《数字图像处理》RafaelC.Gonzalez


### 一堆复习笔记

* [数字图像处理学习笔记](http://zuzhiang.cn/2019/09/24/DIP/)

* [数字图像处理笔记](https://a-suozhang.xyz/2019/09/06/Diigital-Image-Procss/)

* **这个不错 [数字图像处理——知识点](https://www.jianshu.com/p/926d6c15dbf9)**

* 数字图像处理 总结 <https://blog.csdn.net/u011178262/article/details/79067643>

* 数字图像处理复习总结 <https://blog.csdn.net/sunshine_lyn/article/details/85400015>

* **冈萨雷斯《数字图像处理》读书笔记 <https://blog.csdn.net/weixin_37625243/article/details/102556940>**


### 一堆 Python 代码

* 实现了离散傅里叶变换：<https://github.com/tesfagabir/Digital-Image-Processing/blob/master/01-Implementing-Discrete-Fourier-Transform-Using-Python.ipynb>

* 实现了快速傅里叶变换：<https://github.com/tesfagabir/Digital-Image-Processing/blob/master/02-Implementing-Fast-Fourier-Transform-Using-Python.ipynb>

* 几个简单的处理：<https://github.com/mohammaduzair9/Basic-Image-Processing>

* 一个偏门的库 Library for Digital Pathology Image Processing <https://github.com/histolab/histolab>

* 毛发去除算法，有点意思：<https://github.com/sunnyshah2894/DigitalHairRemoval>

* 4-simple-steps-in-Builiding-OCR <https://github.com/Nagakiran1/4-simple-steps-in-Builiding-OCR>


### 一堆滤镜

* 一批复古风：A set of image filters crafted and curated by This Is My Jam <https://github.com/thisismyjam/jam-image-filter>

* 一个库，风格丰富：Image processors and filters for use with ImageKit <https://github.com/fish2000/instakit>

* Simple python demos of Guided Image Filtering (Python). <https://github.com/tody411/GuidedFilter>

* 专门为除去照片中腿毛等体毛而设计。Specially designed for image leg/arm hair removal. <https://github.com/FerryYoungFan/FanselineImageToolbox>

* BeautyCamera <https://github.com/PerpetualSmile/BeautyCamera>

    饱和度调整，明度调节，皮肤识别，皮肤磨皮（value1 精细度，value2 程度），美白算法（皮肤识别），美白算法（人脸识别），Gamma 矫正，怀旧滤镜，木刻滤镜，细节增强，风格化，铅笔画（彩色）。

    <https://github.com/Ssssix40/Cameo1.1/blob/master/filters.py>

* An Wiener Filter Implementation for Image Processing Task <https://github.com/tranleanh/wiener-filter-image-restoration>

* image filtering techniques in python with examples <https://github.com/vikasgola/image-filtering>

* Commonly used image filters. 🌎 包罗常见的图像滤波器。<https://github.com/JNingWei/Image_Filter>

#### Python ImageFilter, ImageEnhance

* 纯 Python 综合图像处理小工具（2）图像增强 <https://www.cnblogs.com/sopic/p/4537718.html>

* 纯 Python 综合图像处理小工具（3）10 种滤镜算法 <https://www.cnblogs.com/sopic/p/4538052.html>

    BLUR、CONTOUR、DETAIL、EDGE_ENHANCE、EDGE_ENHANCE_MORE、EMBOSS、FIND_EDGES、SMOOTH、SMOOTH_MORE、SHARPEN（GaussianBlur、UnsharpMask、Kernel、RankFilter、MedianFilter、MinFilter、MaxFilter、ModeFilter）

    各种效果：<https://zhuanlan.zhihu.com/p/62737338>

    | ImageFilter.BLUR                | 模糊滤镜 |
    | ImageFilter.CONTOUR             | 轮廓 |
    | ImageFilter.DETAIL              | 细节滤镜 |
    | ImageFilter.EDGE_ENHANCE        | 边界加强 |
    | ImageFilter.EDGE_ENHANCE_MORE   | 边界加强（阀值更大） |
    | ImageFilter.EMBOSS              | 浮雕滤镜 |
    | ImageFilter.FIND_EDGES          | 边界滤镜 |
    | ImageFilter.SMOOTH              | 平滑滤镜 |
    | ImageFilter.SMOOTH_MORE         | 平滑滤镜（阀值更大） |
    | ImageFilter.SHARPEN             | 锐化滤镜 |
    | GaussianBlur（radius）          | 高斯模糊 |
    | UnsharpMask                     | USM 锐化 |
    | MedianFilter                    | 中值滤波 |

* 纯 Python 综合图像处理小工具（4）自定义像素级处理（剪纸滤镜）<https://www.cnblogs.com/sopic/p/4665946.html>


## 参考

- [1] [bilibili {% include relref_svgbili.html %}](https://www.bilibili.com/video/BV1tx41147Tx)
- [2] [标题自动编号](https://www.cnblogs.com/36bian/p/7609304.html)
- [3] [课程目录](https://www.cnblogs.com/-wenli/p/11744405.html)
- [4] GITHUB 数学公式展开：<https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima>
