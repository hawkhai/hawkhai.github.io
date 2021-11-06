---
layout: post
title: "图像处理 -- FFmpeg & OpenCV 滤镜"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["FFmpeg", "OpenCV", "图像处理", "音视频"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

一些简单的 OpenCV 滤镜。

* [FFmpeg Filters Documentation](http://www.ffmpeg.org/ffmpeg-filters.html)
* [FFmpeg-Shader 滤镜特效 {% include relref_zhihu.html %}](https://www.zhihu.com/column/c_1319950968562774016)


## 滤镜


### 亮度调节

函数已定义，现在 beta 值将给出适当的结果。正值表示图像较亮，负值表示图像较暗。

$$
\text { dst }(\mathrm{I}) =
\text { saturate_cast<uchar> }
(\mid
    \text { src }(\mathrm{I}) *
    \text { alpha } +
    \text { beta }
\mid)
$$

```python
cv2.convertScaleAbs(img, beta=beta_value)
```


### 锐利效果

我们将使用 OpenCV 中的 filter2D 方法进行适当的编辑。
锐化效果的内核将是：[[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]]

```python
# sharp effect
def sharpen(img):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    imgSharpen = cv2.filter2D(img, -1, kernel)
    return imgSharpen
```


### 棕褐色滤镜

棕褐色为照片增添了温暖的棕色效果。复古、平静和怀旧的效果被添加到图像中。

```python
# sepia effect
def sepia(img):
    # converting to float to prevent loss
    imgSepia = np.array(img, dtype=np.float64)
    # multipying image with special sepia matrix
    imgSepia = cv2.transform(imgSepia, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]]))
    # normalizing values greater than 255 to 255
    imgSepia[np.where(imgSepia > 255)] = 255
    imgSepia = np.array(imgSepia, dtype=np.uint8)
    return imgSepia
```


### 铅笔素描效果

灰度版本：

```python
# grey pencil sketch effect
def pencil_sketch_grey(img):
    #inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
    return sk_gray
```

彩色版本：

```python
# colour pencil sketch effect
def pencil_sketch_col(img):
    # inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
    return sk_color
```


### HDR 效果

```python
# HDR effect
def HDR(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return  hdr
```


### 反转滤镜

```python
# invert filter
def invert(img):
    inv = cv2.bitwise_not(img)
    return inv
```


### 夏季和冬季效果滤镜

单变量插值 UnivariateSpline
```
UnivariateSpline(x,y,w=None,bbox=[None,None],k=3,s=None)
```

* x,y 是 X-Y 坐标数组
* w 是每个数据点的权重值
* k 为样条曲线的阶数
* s 为平滑参数。
    * s=0，样条曲线强制通过所有数据点
    * s>0，满足 $\sum(w(y-spline(x)))^2 \leq s$

创建查找表：

```python
# defining a function
from scipy.interpolate import UnivariateSpline
def LookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))
```

**夏季效果滤镜**
让我们实现一个夏季效果滤镜，它基本上增加了图像的温暖度。
为了实现这一点，我们将增加红色通道中的值并减少蓝色通道中的值。

```python
# summer effect
def Summer(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel, red_channel  = cv2.split(img)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    sum = cv2.merge((blue_channel, green_channel, red_channel ))
    return sum
```

**冬季效果滤镜**
在冬季效果滤镜中，将进行相反的操作。图像的温暖度会降低。红色通道中的值将减少，蓝色通道中的值将增加。

```python
# winter effect
def Winter(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel, red_channel = cv2.split(img)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    win = cv2.merge((blue_channel, green_channel, red_channel))
    return win
```


## 保边滤波器

edgePreservingFilter


## 风格化滤波器

风格化过滤器产生的输出看起来像使用水彩绘制的图像。

```
stylization(Mat src, Mat dst, float sigma_s=60, float sigma_r=0.45f)
```


## 油画

```
cv2.xphoto.oilPainting(img, neighbouring, steps)
```

* neighbouring = 邻近 Pixel 的参数
* steps = 进行 neighbouring 的次数


## FFmpeg 中的滤镜（十六）：视频滤镜 -- colorbalance

取正值时，调整平衡向主色靠近；取负值时调整平衡想补色靠近。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-07-04-ffmpeg-filters.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://www.ffmpeg.org/ffmpeg-filters.html]({% include relrefx.html url="/backup/2021-07-04-ffmpeg-filters.md/www.ffmpeg.org/ad454730.html" %})
- [https://www.zhihu.com/column/c_1319950968562774016]({% include relrefx.html url="/backup/2021-07-04-ffmpeg-filters.md/www.zhihu.com/a082b75b.html" %})
