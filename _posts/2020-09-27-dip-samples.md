---
layout: post
title: "图像处理笔记 -- 几个实验 (DIP)"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid: truez
glslcanvas:
codeprint:
---


## 基本几何变换


## 手写数字识别

* <https://www.jb51.net/article/133880.htm>

* <https://github.com/HanpuLiang/Simple-Handwritten-Numerel-Recogntion>


## scikit-image 进行图像分割

* <https://blog.csdn.net/weixin_42142987/article/details/87717861>


## 邮政编码识别

* [图像识别与处理笔记 —— 字符识别、邮政编码识别（10 月 8 日暂存） {% include relref_csdn.html %}](https://blog.csdn.net/mao_hui_fei/article/details/78177471)

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

* [使用 opencv 和 python 实现车牌区域提取 {% include relref_jianshu.html %}](https://www.jianshu.com/p/08ddeb0d8878)

* [opencv + python 车牌识别 {% include relref_cnblogs.html %}](https://www.cnblogs.com/kekexxr/p/11574589.html)

* <https://github.com/DataXujing/vehicle-license-plate-recognition>


## 案例分析


### toP61-1 手写数字识别


### toP58-2 邮政编码识别


### toP60-3 汽车牌照识别


### toP62-4 条形码识别


### toP63-5 印刷体汉字识别


### toP54-6 人脸识别


### toP57-7 细胞识别与统计

{% include image.html url="/assets/images/200927-dip-samples/xibao.png" %}


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


### Python 徒手实现识别手写数字

这个 demo 还勉强不错的。

* https://zhuanlan.zhihu.com/p/30120447
* https://zhuanlan.zhihu.com/p/32996841
* https://zhuanlan.zhihu.com/p/30590235
* https://zhuanlan.zhihu.com/p/30212013


### 一堆复习笔记

* [数字图像处理学习笔记](http://zuzhiang.cn/2019/09/24/DIP/)

* [图像处理笔记](https://a-suozhang.xyz/2019/09/06/Diigital-Image-Procss/)

* **这个不错 [数字图像处理 —— 知识点 {% include relref_jianshu.html %}](https://www.jianshu.com/p/926d6c15dbf9)**

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

- [1] [bilibili {% include relref_bili.html %}](https://www.bilibili.com/video/BV1tx41147Tx)
- [2] [标题自动编号 {% include relref_cnblogs.html %}](https://www.cnblogs.com/36bian/p/7609304.html)
- [3] [课程目录 {% include relref_cnblogs.html %}](https://www.cnblogs.com/-wenli/p/11744405.html)
- [4] GITHUB 数学公式展开：<https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima>

<hr class='reviewline'/>
<p class='reviewtip'>2021-01-23: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.jb51.net/article/133880.htm]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.jb51.net/e089c4c3.htm" %})
- [https://github.com/HanpuLiang/Simple-Handwritten-Numerel-Recogntion]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/de4a224d.html" %})
- [https://blog.csdn.net/weixin_42142987/article/details/87717861]({% include relref.html url="/backup/2020-09-27-dip-samples.md/blog.csdn.net/2d070392.html" %})
- [https://blog.csdn.net/mao_hui_fei/article/details/78177471]({% include relref.html url="/backup/2020-09-27-dip-samples.md/blog.csdn.net/1b0074e8.html" %})
- [http://www.doc88.com/p-693272517244.html]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.doc88.com/0d44cdd2.html" %})
- [https://wenku.baidu.com/view/c26f1ea5492fb4daa58da0116c175f0e7cd119ea.html]({% include relref.html url="/backup/2020-09-27-dip-samples.md/wenku.baidu.com/19342336.html" %})
- [https://max.book118.com/html/2018/1108/8013115051001132.shtm]({% include relref.html url="/backup/2020-09-27-dip-samples.md/max.book118.com/885b0c74.shtm" %})
- [https://stackoom.com/question/3xNO6/Opencv-%E8%A3%81%E5%89%AA-%E4%BD%8D%E6%95%B0%E7%9A%84%E6%89%8B%E5%86%99%E9%82%AE%E6%94%BF%E7%BC%96%E7%A0%81]({% include relref.html url="/backup/2020-09-27-dip-samples.md/stackoom.com/c9ec5dcb.html" %})
- [https://github.com/wzh191920/License-Plate-Recognition]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/d61e7747.html" %})
- [https://www.freesion.com/article/5566190803/]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.freesion.com/01081375.html" %})
- [https://www.freesion.com/article/9575144324/]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.freesion.com/8e773cc1.html" %})
- [https://www.jianshu.com/p/08ddeb0d8878]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.jianshu.com/fe0d15de.html" %})
- [https://www.cnblogs.com/kekexxr/p/11574589.html]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.cnblogs.com/68f7f01f.html" %})
- [https://github.com/DataXujing/vehicle-license-plate-recognition]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/76d16c1b.html" %})
- [http://accu.cc/content/pil/agwn/]({% include relref.html url="/backup/2020-09-27-dip-samples.md/accu.cc/32e6fa9f.html" %})
- [https://github.com/LiuFG/digital_image_process]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/c9ea02a2.html" %})
- [https://github.com/qcymkxyc/Image-Process]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/9ecd0aa6.html" %})
- [https://github.com/iwuqing/Digital-Image-Processing]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/15f2c7ed.html" %})
- [https://github.com/MAhaitao999/digital_image_processing]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/7ec74c4a.html" %})
- [https://github.com/ljy9826/Digital-Image-Processing_code]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/0f2ed824.html" %})
- [https://zhuanlan.zhihu.com/p/30120447]({% include relref.html url="/backup/2020-09-27-dip-samples.md/zhuanlan.zhihu.com/ab62cffa.html" %})
- [https://zhuanlan.zhihu.com/p/32996841]({% include relref.html url="/backup/2020-09-27-dip-samples.md/zhuanlan.zhihu.com/3d3fbae2.html" %})
- [https://zhuanlan.zhihu.com/p/30590235]({% include relref.html url="/backup/2020-09-27-dip-samples.md/zhuanlan.zhihu.com/dfa67855.html" %})
- [https://zhuanlan.zhihu.com/p/30212013]({% include relref.html url="/backup/2020-09-27-dip-samples.md/zhuanlan.zhihu.com/abf47696.html" %})
- [http://zuzhiang.cn/2019/09/24/DIP/]({% include relref.html url="/backup/2020-09-27-dip-samples.md/zuzhiang.cn/9f0716fa.html" %})
- [https://a-suozhang.xyz/2019/09/06/Diigital-Image-Procss/]({% include relref.html url="/backup/2020-09-27-dip-samples.md/a-suozhang.xyz/d17c66dc.html" %})
- [https://www.jianshu.com/p/926d6c15dbf9]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.jianshu.com/cabe0955.html" %})
- [https://blog.csdn.net/u011178262/article/details/79067643]({% include relref.html url="/backup/2020-09-27-dip-samples.md/blog.csdn.net/d7aad285.html" %})
- [https://blog.csdn.net/sunshine_lyn/article/details/85400015]({% include relref.html url="/backup/2020-09-27-dip-samples.md/blog.csdn.net/214b1181.html" %})
- [https://blog.csdn.net/weixin_37625243/article/details/102556940]({% include relref.html url="/backup/2020-09-27-dip-samples.md/blog.csdn.net/67ada943.html" %})
- [https://github.com/tesfagabir/Digital-Image-Processing/blob/master/01-Implementing-Discrete-Fourier-Transform-Using-Python.ipynb]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/fbe3fa6d.ipynb" %})
- [https://github.com/tesfagabir/Digital-Image-Processing/blob/master/02-Implementing-Fast-Fourier-Transform-Using-Python.ipynb]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/f116888c.ipynb" %})
- [https://github.com/mohammaduzair9/Basic-Image-Processing]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/110f6b2d.html" %})
- [https://github.com/histolab/histolab]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/8c9935a8.html" %})
- [https://github.com/sunnyshah2894/DigitalHairRemoval]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/90be912e.html" %})
- [https://github.com/Nagakiran1/4-simple-steps-in-Builiding-OCR]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/96f537de.html" %})
- [https://github.com/thisismyjam/jam-image-filter]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/69e9af72.html" %})
- [https://github.com/fish2000/instakit]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/4560b447.html" %})
- [https://github.com/tody411/GuidedFilter]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/640e9b83.html" %})
- [https://github.com/FerryYoungFan/FanselineImageToolbox]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/8fc91886.html" %})
- [https://github.com/PerpetualSmile/BeautyCamera]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/fa004f53.html" %})
- [https://github.com/Ssssix40/Cameo1.1/blob/master/filters.py]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/5c0de854.py" %})
- [https://github.com/tranleanh/wiener-filter-image-restoration]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/e075a6d5.html" %})
- [https://github.com/vikasgola/image-filtering]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/c76332a5.html" %})
- [https://github.com/JNingWei/Image_Filter]({% include relref.html url="/backup/2020-09-27-dip-samples.md/github.com/e22166be.html" %})
- [https://www.cnblogs.com/sopic/p/4537718.html]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.cnblogs.com/1121165d.html" %})
- [https://www.cnblogs.com/sopic/p/4538052.html]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.cnblogs.com/2f2e4ebe.html" %})
- [https://zhuanlan.zhihu.com/p/62737338]({% include relref.html url="/backup/2020-09-27-dip-samples.md/zhuanlan.zhihu.com/a05596ef.html" %})
- [https://www.cnblogs.com/sopic/p/4665946.html]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.cnblogs.com/a5e9a3be.html" %})
- [https://www.bilibili.com/video/BV1tx41147Tx]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.bilibili.com/57d122ce.html" %})
- [https://www.cnblogs.com/36bian/p/7609304.html]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.cnblogs.com/9c1872d6.html" %})
- [https://www.cnblogs.com/-wenli/p/11744405.html]({% include relref.html url="/backup/2020-09-27-dip-samples.md/www.cnblogs.com/98804d9b.html" %})
- [https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima]({% include relref.html url="/backup/2020-09-27-dip-samples.md/chrome.google.com/b204bb6b.html" %})
