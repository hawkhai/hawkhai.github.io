---
layout: post
title: "图像处理笔记 -- 图像处理"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid: true
glslcanvas:
codeprint:
---


## 自适应阈值

与二元阈值法不同，该方法根据像素值的小周围区域来确定其阈值。这种方法也有两种类型：
* 自适应阈值均值：阈值是平均值附近区域减去固定的 $C$。
* 自适应高斯阈值：阈值是邻域值减去常数 $C$ 的高斯加权总和。

```python
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2)
```


## 降噪

大多数计算机视觉任务失败的最重要因素是噪声。噪声可以是高斯噪声（由于不同的光照条件而产生）和椒盐噪声（稀疏的明暗干扰）。

```python
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
```


## 背景颜色检测


### 算法一

先对原图进行缩放处理，处理成固定的像素面积。
将 RGB 矩阵分离为单独的颜色通道，然后使用 Counter() 函数分别对 3 个 RGB 矩阵中的每个像素值进行频率计数。

然后，选择 10 个出现频率最高的值并取它们的平均值来获得结果像素值。

最后，只需使用 np.zeros() 生成一个空白图像，并用获得的背景色填充它即可显示最终结果。
这种技术只需 40 行代码就可以产生结果！


### 算法二

对 RGB 值使用 K-Means 聚类算法，并找出图像中存在的一组不同颜色的聚类。
之后，再次利用频率计数，最后找到背景色。
这种方法涉及到无监督机器学习的使用，其应用范围远远超出了背景颜色检测。

图像分割任务大量使用这种方法对图像进行 K 均值聚类。

[code {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/5CNRCL2XGFZOZBNJTGgI-w)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-11-02-dip-fastimage.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://mp.weixin.qq.com/s/5CNRCL2XGFZOZBNJTGgI-w]({% include relrefx.html url="/backup/2021-11-02-dip-fastimage.md/mp.weixin.qq.com/8e751598.html" %})
