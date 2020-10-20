---
layout: post
title: "“数字图像处理”笔记 -- 图像缩放插值算法直观感受"
location: "珠海"
categories: ["图像处理"]
tags: [图像处理]
mathjax: true
toc: true
---

写了一个 Python 直观感受各种图像缩放插值算法。

* INTER_NEAREST  -- 最近邻插值法
* INTER_LINEAR   -- 双线性插值法（默认）
* INTER_AREA     -- 基于局部像素的重采样（resampling using pixel area relation）
* INTER_CUBIC    -- 基于 4x4 像素邻域的 3 次插值法
* INTER_LANCZOS4 -- 基于 8x8 像素邻域的 Lanczos 插值


## 先上图

{% include image.html url="/images/image-interpolation/result.png" %}


## Python 代码

```python
#encoding=utf8
import re, os, sys
import matplotlib.pyplot as plt
import numpy as np
import cv2

def strcolor(str):
    return [int(str[0:2], 16),
            int(str[2:4], 16),
            int(str[4:6], 16)]

def imgshow(img, title="result"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imgshow4(imga, titlea, imgb, titleb, imgc, titlec, imgd, titled):
    plt.figure(num='result', figsize=(8,8))

    plt.subplot(2, 2, 1)
    plt.title(titlea)
    plt.imshow(imga)
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title(titleb)
    plt.imshow(imgb)
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title(titlec)
    plt.imshow(imgc)
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title(titled)
    plt.imshow(imgd)
    plt.axis('off')
    plt.show()

def imgtest(myimg, interpolation):
    img = cv2.resize(myimg, (0, 0), fx=100, fy=100,
                     interpolation=interpolation).astype(np.uint8)
    return img

# INTER_NEAREST  - 最近邻插值法
# INTER_LINEAR   - 双线性插值法（默认）
# INTER_AREA     - 基于局部像素的重采样（resampling using pixel area relation）
# INTER_CUBIC    - 基于 4x4 像素邻域的 3 次插值法
# INTER_LANCZOS4 - 基于 8x8 像素邻域的 Lanczos 插值
# https://github.com/pytorch/pytorch/issues/25039
def main():
    imagestr = """
000000 0047ff e7ff00 000000
820000 00ffe7 ff4b00 0047ff
e7ff00 0047ff 000000 ff4b00
ff4b00 e7ff00 0047ff 00ffe7
"""
    myimage = [strcolor(color) for color in imagestr.split()]
    myimage = np.asarray(myimage).reshape(4, 4, 3).astype(np.uint8)

    nearest  = imgtest(myimage, cv2.INTER_NEAREST)
    linear   = imgtest(myimage, cv2.INTER_LINEAR)
    cubic    = imgtest(myimage, cv2.INTER_CUBIC)
    lanczos4 = imgtest(myimage, cv2.INTER_LANCZOS4)

    imgshow4(nearest, "INTER_NEAREST",
        linear, "INTER_LINEAR",
        cubic, "INTER_CUBIC",
        lanczos4, "INTER_LANCZOS4",
    )

if __name__ == "__main__":
    main()

```


## 后来发现网上很多

* [Show all different interpolation methods for imshow](https://matplotlib.org/1.4.1/examples/images_contours_and_fields/interpolation_methods.html)

{% include image.html url="/images/image-interpolation/interpolation_methods.png" %}

* [Interpolation](http://haifengl.github.io/interpolation.html)

{% include image.html url="/images/image-interpolation/grid-interpolation2d.png" %}
{% include image.html url="/images/image-interpolation/63556641-eeb89400-c545-11e9-8f90-58e1c0eb0840.png" %}

* [OpenCV 图像缩放 resize 各种插值方式的比较](https://blog.csdn.net/guyuealian/article/details/85097633)
