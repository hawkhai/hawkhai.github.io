---
layout: post
title: "“数字图像处理”笔记 -- 编程马拉松解答"
location: "珠海"
categories: ["图像处理"]
tags: [图像处理]
mathjax: true
toc: true
---

完整的代码下载：<a href="{% include relref.html url="/source/hackathon2020_team24.zip" %}" target="_blank">hackathon2020_team24.zip</a> \- 14\.5 MB

为了不那么占内存，以更好的演示效果，代码重新整理了一遍。

[^_^]: {z% include image.html url="/images/image-marathon/20201025151929.png" %}

输入图片有：

{% include image.html url="/source/marathon/input_images/phase1/phase1_input.jpg" %}

{% include image.html url="/source/marathon/input_images/phase1/phase1_input_optional.jpg" %}

{% include image.html url="/source/marathon/input_images/phase2/phase2_broken.jpg" %}

{% include image.html url="/source/marathon/input_images/phase3/phase3_sky.jpg" %}

[^_^]: {z% include image.html url="/source/marathon/input_images/phase3/phase3_watermark.jpg" %}


## 色彩变换

cv2 读入的图片是 BGR 顺序。


### 图片内存结构

图片读入后是一个三维矩阵。


### 负片转正片

将彩色负片转为彩色正片，矩阵运算，255 减一下，就是答案。

```python
# 将彩色负片转为彩色正片
def phase1(inputImgPath: str, outImgPath: str):
    img = kalgorithm.imgRead(inputImgPath)
    img = 255 - img
    kalgorithm.imgSave(outImgPath, img)
```


## 仿射变换

输入底片不正，需要先寻边调整。
图片矫正。图片输入不正的情况，方法很多，这里是：先剪裁，然后旋转矫正，最后再剪裁。

{% include image.html url="/source/marathon/output_images/phase1/phase1_output_optional.jpg.1.jpg"
url2="/source/marathon/output_images/phase1/phase1_output_optional.jpg.2.jpg" %}


## 图片降噪

每种滤波算法都有自己的特点。

```
## prewitt vertical kernel 提取竖直边缘
[[-1., -1., -1.],
 [ 0.,  0.,  0.],
 [ 1.,  1.,  1.]]
## prewitt horizontal kernel 提取左右边缘
[[-1., 0., 1.],
 [-1., 0., 1.],
 [-1., 0., 1.]]

## Sobel vertical 提取竖直边缘
[[ 1.,  2.,  1.],
 [ 0.,  0.,  0.],
 [-1., -2., -1.]]
## Sobel horizontal 提取左右边缘
[[1., 0., -1.],
 [2., 0., -2.],
 [1., 0., -1.]]
```


### 均值滤波

均值滤波器使用网格内像素的平均值。图片更模糊了。

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken_mean_filter.jpg" %}


### 中值滤波

中值滤波器是一种可以使图像平滑的滤波器。有的噪点没了。

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken_median_filter.jpg" %}


### 高斯滤波

高斯滤波器是一种可以使图像平滑的滤波器，用于去除噪声。图片更模糊了。

GaussianFilter Kernel=5，这些数字的和刚好是 1.0。

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

三维图更明显，可以看到每种插值算法的特点。

{% include image.html url="/images/image-marathon/20201022103740.png" %}


### 最邻近插值


### 双线性二次插值


### 双线性三次插值


### 高级插值算法

phase2_interpolate_Lanczos 实现了 Lanczos 算法。

编译好的 lanczos.exe 已入库，需要 opencv_world3411d.dll 才能跑起来。


## 对比度增强


### 直方图均衡

彩色图像做直方图均衡化似乎不能对三个分量分别均衡化，这么搞可能会导致颜色畸变。
最好将彩色图像转化为 HLS 颜色模型，然后单独对 L 分量做均衡化，最后再转换回 BGR 颜色模型。

这里直接把三个颜色作为一个整体均衡化，可以直接看到图片直方图的变化。

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken.Original.png" %}

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken.histEqualization.png" %}


## 图片锐化


### 空域算法

空域算法比较简单，直接用算子套上去算一下就可以了。平滑的算子加起来是 0，这个锐化的算子加起来，值是 1，所以感觉锐化了。
一般在灰度图上进行，彩色图像变成 HSV 空间，针对亮度 V 变换，也可以达到灰度类似的效果。

```
[ 0, -1,  0],
[-1,  5, -1],
[ 0, -1,  0]
```


### 频域算法

用到傅里叶变换。低频是轮廓，高频是细节。用到高频提升滤波器，一般在灰度图上进行，彩色图在亮度上做变换。
将高频加强和直方图均衡相结合是得到边缘锐化和对比度增强的有效方法。[频域图像增强-锐化]

[频域图像增强-锐化]: https://blog.csdn.net/qq_30815237/article/details/98655630

这玩意的原理和过程，可以参考写的另外一篇文章。[傅里叶变换]

[傅里叶变换]: https://sunocean.life/blog/blog/2020/09/26/dip-fourier-transform

{% include image.html url="/images/image-marathon/fft/v2-bad520e27c839917cf27d76e1206bb70_1440w.jpg" %}

{% include image.html url="/images/image-marathon/fft/v2-73ad89919f066942a612107925152c8c_720w.jpg" %}

{% include image.html url="/images/image-marathon/fft/v2-39eb0e4cd7fa4f0cd927bc97fc1c1674_720w.jpg" %}

{% include image.html url="/images/image-marathon/fft/v2-5b1db77b17cc490cae1e9670bb34eeeb_720w.jpg" %}

{% include image.html url="/images/image-marathon/fft/v2-2c6301e214b1766e2b4173c2a0593bb2_720w.jpg" %}

可以编程，显示这个 Gaussian 高哦他那个滤波函数。

{% include image.html url="/images/image-marathon/gaussian_1.png" %}

{% include image.html url="/images/image-marathon/gaussian_2.png" %}

和原图对比，效果还不错。

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken_sharpen_spatial.jpg" %}

{% include image.html url="/source/marathon/output_images/phase2/phase2_sharpen_frequency_gaussian.jpg" %}


## 图片修复

图片噪点去除。这个噪点的特点，中值滤波可以很好的修复图片了。

OpenCV 实现了 INPAINT_TELEA : Fast Marching Method based 算法，INPAINT_NS : Navier-Stokes based Inpainting 算法。[OpenCV Inpainting] / [OpenCV 图像修复]

[OpenCV Inpainting]: https://blog.csdn.net/LuohenYJ/article/details/90640654
[OpenCV 图像修复]: https://blog.csdn.net/dcrmg/article/details/53792061

我们简单的实现了简易修复算法：先二值化，找到水印位置，然后根据位置，用最近邻算法填充。
下载了一个 TELEA 算法的 Python 实现，效果更好，但是没用它。这次的图片难度很小，没必要。

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken_repair.jpg.mask.png" %}

{% include image.html url="/source/marathon/output_images/phase2/phase2_broken_repair.jpg" %}


## 二值化


### 大津二值化算法

Otsu Binarization，大津二值化算法（Otsu's Method）。
假定一个阈值，方差越大，说明差别越大。


## 天空识别


### 图像形态学

以 B 结构中心点为准心，在 A 中找能满足 B 结构的点即为腐蚀。
把 A 结构的每个点放到 B 中心点，以 B 结构外扩即为膨胀。
开操作表示先腐蚀后膨胀；闭操作表示先膨胀后腐蚀。
闭运算，弥合，毛刺保留；开运算，分裂，毛刺去掉。

#### 膨胀（dilation）

一般用来扩充边缘或填充小的孔洞。

#### 腐蚀（erosion）

可用来提取骨干信息，去掉毛刺，去掉孤立的像素。

#### 开运算（opening）

先腐蚀再膨胀，可以消除小物体或小斑块。
先腐蚀后膨胀的过程。开运算可以用来消除小黑点，在纤细点处分离物体、平滑较大物体的边界的同时并不明显改变其面积。

#### 闭运算（closing）

先膨胀再腐蚀，可用来填充孔洞。
先膨胀后腐蚀的过程。闭运算可以用来排除小黑洞。

#### 自定义算子

```
1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1
```

这个算子很长条，神奇过滤，可以过滤出海平线。


### 色彩追踪

完成天空替换。有倒影，有剪影。

我们把色彩变换到 HSV，然后做一个直方图，可以准确看到颜色分布情况，最高尖尖就是蓝色天空还海水部分，也是整张图的大部分颜色集中的地方。

{% include image.html url="/images/image-marathon/color_tracking.png" %}


## 空域盲提水印

8 比特位图像的最低阶比特对人眼感知几乎没有影响，因此，可以将水印图像的高阶比特位“插入”在衬底的低阶比特位中。$$f_w = 4(\frac{f}{4}) + \frac{w}{64}$$

LSB 水印非常脆弱，诸如裁剪，旋转，缩放，图像压缩等操作可以轻易破坏该水印。[水印]

[水印]: http://accu.cc/content/pil/watermark/


## 频域盲提水印


### 离散余弦变换


### TODO...


## 渔女处理


### 第一步，修复矫正图片

为了计算速度，一上来把 3 倍大图缩小回去，等处理完了，最后在变大三倍。

首先修复图片，不再累述，然后用上面的 prewitt sobel 算子计算整个图的边缘。

{% include image.html url="/source/marathon/output_images/phase3/phase3_repair_original.png.mask.png" %}

通过自定义的算子，分理出海平线，可以发现是倾斜的。

{% include image.html url="/source/marathon/output_images/phase3/phase3_repair_original.png.mask.line.png" %}

根据倾斜角度，矫正胶片，同时修复边缘。再计算出图片边缘，同时用水平投影法计算出海平线位置。

{% include image.html url="/source/marathon/output_images/phase3/phase3_repair.png" %}

{% include image.html url="/source/marathon/output_images/phase3/phase3_repair_mask.png.mask.line.png" %}


### 第二步，分离天空海水渔女

使用色彩追踪和形态学运算得到图像中感兴趣区域，可以很准确的分离出渔女部分，贴回原图，二值化，把黑乎乎的小岛也准确识别出来。
用闭运算处理一下毛刺，再用腐蚀把渔女变圆润一点。对分离出来的 mask 做一次均值滤波，让接头不那么生硬。

#### 分离渔女：形态学追踪

{% include image.html url="/source/marathon/output_images/phase3/phase3_sky.jpg_fisher_girl_mask.png" %}

{% include image.html url="/source/marathon/output_images/phase3/phase3_sky.jpg_fisher_girl.png" %}

#### 分离天空：海平线以上减去渔女

{% include image.html url="/source/marathon/output_images/phase3/phase3_sky.jpg_sky_mask.png" %}

#### 分离海水：海平线以下减去渔女

{% include image.html url="/source/marathon/output_images/phase3/phase3_sky.jpg_ocean_wave_mask.png" %}


### 第三步，合成天空。

finalimage = newsky * masksky + imgsrc * (1 - masksky)

{% include image.html url="/source/marathon/output_images/phase3/phase3_sky.jpg_sky_cloud.png" %}


## 渔女高级处理


### 倒影处理

{% include image.html url="/source/marathon/output_images/phase3/phase3_sky_final.png_mask_sea.png" %}


### 给背景加一个高斯函数

{% include image.html url="/source/marathon/output_images/phase3/phase3_sky_final.png" %}


### 尝试换一个色调

{% include image.html url="/source/marathon/output_images/phase3/phase3_sky_final.png_glod.png" %}

（完）
