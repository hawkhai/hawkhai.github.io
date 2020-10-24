---
layout: post
title: "“数字图像处理”笔记 -- 编程马拉松解答"
location: "珠海"
categories: ["图像处理"]
tags: [图像处理]
mathjax: true
toc: true
---

完整的代码下载：下载。为了不那么占内存，输入图片缩小了 50%，以更好的演示效果。代码重新整理了一遍，思路更清晰了。


## 色彩变换


### 图片内存结构

图片读入后是一个三维矩阵。

```python
def imgRead(fpath, float=False):
    img = cv2.imread(fpath)
    if float:
        return img.astype(np.float32)
    return img

def imgSave(fpath, img):
    print("Image Save\r\n", fpath)
    cv2.imwrite(fpath, img)
    return fpath

def imgShow(img, title="result"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```


### 负片转正片

将彩色负片转为彩色正片。

```python
# 将彩色负片转为彩色正片
def phase1(inputImgPath: str, outImgPath: str):
    img = kalgorithm.imgRead(inputImgPath)
    img = 255 - img
    kalgorithm.imgSave(outImgPath, img)
```

{% include image.html url="/source/marathon/input_images/phase1/phase1_input.jpg"
url2="/source/marathon/output_images/phase1/phase1_output.jpg" %}


## 仿射变换

输入底片不正，需要先寻边调整。

{% include image.html url="/source/marathon/input_images/phase1/phase1_input_optional.jpg"
url2="/source/marathon/output_images/phase1/phase1_output_optional.jpg" %}


### 图片矫正

图片输入不正的情况，方法很多，这里是：先剪裁，然后旋转矫正，最后再剪裁。

{% include image.html url="/source/marathon/output_images/phase1/phase1_output_optional.jpg.1.jpg"
url2="/source/marathon/output_images/phase1/phase1_output_optional.jpg.2.jpg" %}


## 图片降噪

每种滤波算法都有自己的特点。


### 均值滤波

均值滤波器使用网格内像素的平均值。

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken_mean_filter.jpg" %}


### 中值滤波

中值滤波器是一种可以使图像平滑的滤波器。

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken_median_filter.jpg" %}


### 高斯滤波

高斯滤波器是一种可以使图像平滑的滤波器，用于去除噪声。

GaussianFilter Kernel，这些数字的和刚好是 1.0。

```json
 [[0.0097565  0.02370077 0.03186045 0.02370077 0.0097565 ]
 [0.02370077 0.0575746  0.07739634 0.0575746  0.02370077]
 [0.03186045 0.07739634 0.10404229 0.07739634 0.03186045]
 [0.02370077 0.0575746  0.07739634 0.0575746  0.02370077]
 [0.0097565  0.02370077 0.03186045 0.02370077 0.0097565 ]]
```

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken_gaussian_filter.jpg" %}


## 图片插值

不同的插值算法。越高级的算法越圆润，越基础的算法马赛克效果越明显。

{% include image.html url="/images/image-marathon/63556641-eeb89400-c545-11e9-8f90-58e1c0eb0840.png" %}


### 最邻近插值


### 双线性二次插值


### 双线性三次插值


### 高级插值算法

phase2_interpolate_Lanczos 实现了 Lanczos 算法。

编译好的 lanczos.exe 已入库，需要 opencv_world3411d.dll 才能跑起来。


## 对比度增强


### 直方图均衡

彩色图像做直方图均衡化似乎不能对三个分量分别均衡化，这么搞可能会导致颜色畸变。最好将彩色图像转化为 HLS 颜色模型，然后单独对 L 分量做均衡化，最后再转换回 BGR 颜色模型。

这里直接把三个颜色作为一个整体均衡化，可以直接看到直方图的变化。

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken.src.png" %}

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken.histEqualization.png" %}

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken.histManipulation.png" %}


## 图片锐化


### 空域算法


### 频域算法


## 图片修复

图片噪点去除。这个噪点的特点，中值滤波可以很好的修复图片了。


## 天空识别


### 色彩追踪

完成天空替换。


## 空域盲提水印


## 频域盲提水印
