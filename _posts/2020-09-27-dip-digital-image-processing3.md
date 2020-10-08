---
layout: post
title: "“数字图像处理”笔记 -- 几个实验 (DIP)"
location: "珠海"
categories: ["图像处理"]
tags: [图像处理]
mathjax: true
toc: true
mermaid: truez
visibility: hidden
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

* [2005.3 毕业设计](https://wenku.baidu.com/view/c26f1ea5492fb4daa58da0116c175f0e7cd119ea.html)
* [2005.3 毕业设计](https://max.book118.com/html/2018/1108/8013115051001132.shtm)

* [OpenCV：裁剪 6 位数的手写邮政编码](https://stackoom.com/question/3xNO6/Opencv-%E8%A3%81%E5%89%AA-%E4%BD%8D%E6%95%B0%E7%9A%84%E6%89%8B%E5%86%99%E9%82%AE%E6%94%BF%E7%BC%96%E7%A0%81)


## 汽车牌照识别

二值化阈值集中常用的选取方法：双峰（2-Mode）法，P 参数法，Otsu 法，迭代法。


### 大津法（OTSU 法或最大类间方差法）

假定一个阈值，方差越大，说明差别越大。


### 迭代法（最佳阈值法）


### 一些代码

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


### toP56 总变差（TV）模型·图像恢复

图象恢复是一个客观过程，需要利用**某些先验知识从退化和干扰的图像中去除模糊因素和噪声、尽可能恢复图像的本来面貌**。复原技术一般是先把**退化和干扰模型化**，然后采用相反的过程进行处理，复原图像。


## 参考

- [1] [bilibili <img src="{% include relref.html url="/assets/bilibili.svg" %}" class="bilibili" />](https://www.bilibili.com/video/BV1tx41147Tx)
- [2] [标题自动编号](https://www.cnblogs.com/36bian/p/7609304.html)
- [3] [课程目录](https://www.cnblogs.com/-wenli/p/11744405.html)
