---
layout: post
title: "图像处理 -- 一些奇奇怪怪的图像算法"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["OpenCV", "图像处理"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---


## 直方图均衡化

<https://github.com/Accustomer/TheThingsWithImage/blob/main/Docs/3_%E7%9B%B4%E6%96%B9%E5%9B%BE%E5%9D%87%E8%A1%A1%E5%8C%96.md>

1. 直方图均衡化（HE）
2. 自适应直方图均衡化（AHE）
3. 限制对比度自适应直方图均衡化（CLAHE）
4. 自适应局部区域伸展（Local Region Stretch）直方图均衡化

彩色图像处理
1. 分别对 R G B 进行 均衡，然后在合并，但这样做 可能导致 图像色彩失真
2. 把 BGR 转换成 HSV 色彩空间，然后对 V 通道进行 均衡，这样可 保证图像色彩不失真 【HSV 分别是 色调、饱和度、亮度】


## Optimized contrast enhancement for real-time image and video dehazing

[from {% include relref_csdn.html %}](https://blog.csdn.net/Julialove102123/article/details/90638418)
[翻译 {% include relref_csdn.html %}](https://blog.csdn.net/xx116213/article/details/51848429)
在视频去雾中首先会将视频序列转换到 YUV 颜色空间，然后仅对 luminance(Y) 分量进行计算，以减少算法复杂度。


### 优化对比度增强的实时图像和视频去雾

解释的很清楚：
[知乎 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/413747554)
包含代码：
[知乎 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/413747554)

由于工业发展中的环境污染问题，很多地方雾霾特别严重，不仅对人们的身体健康产生了巨大威胁，而且严重影响户外图像、视频的拍摄质量，使得检测和识别等计算机任务很难完成。因此，图像去雾长期以来都是研究人员所关注的热点。

在图像去雾领域有很多传统图像算法取得了不错的成果，很值得我们学习，如何凯明大神提出的 [暗通道先验](//kaiminghe.com/publications/cvpr09.pdf)，[色彩衰减先验](https://ieeexplore.ieee.org/document/7128396/citations#citations) 等。其中一篇 2013 年的老文章 [Optimized contrast enhancement for real-time image and video dehazing](//mcl.korea.ac.kr/~dotol1216/Publications/2013_JVCIR_JHKIM.pdf) 效果也很不错，实时性很强，因此本文想要对其进行简要解读和复现。


### 大气光散射模型

大气光散射模型指出了雾霾造成观测图像质量下降的主要原因：1）来自目标的反射光被雾霾吸收并发生散射，造成目标发射光能量衰减，成像结果的亮度和对比度自然下降；2）来自太阳、灯等光源产生的环境光受雾霾的散射作用形成背景光，通常这部分背景光强度大于来自目标的反射光，因为目标成像后模糊不清。该模型可表示为：
$$
I(p)=t(p)J(p)+(1-t(p))A
$$
其中，$J(p)$ 表示在像素点 $p$ 的目标反射光的色彩，$I(p)$ 表示在像素点 $p$ 观察到的色彩，而 $A$ 则是环境中的大气光，$t(p)$ 则是反射光在传输过程中的衰减因子（其实俺也不知该咋翻译合适，以下称为 **传输系数** 吧），其值由目标上的场景点到相机的距离和大气条件决定：
$$
t(p) = e^{-\rho d(p)}
$$
其中景深 $d(p)$ 越深，传输被衰减得越厉害。而 $\rho$ 是由大气条件决定得衰减系数。

因此，得到观测图像 $I(p)$ 后，只要估算出环境中的传输系数 $t(p)$ 和大气光 $A$，就可以根据大气光散射模型得到清晰的原图 $J(p)$。


### 大气光估计

通常认为观测图像中最亮的颜色就是大气光 $A$，但是有些场景中会存在比大气光更亮的光源，造成估计错误。为了避免这样的错误估计，文中采用四分查找，将图像等分为长宽为原图一半的四等份，从四等份中选择像素均值与标准差 $\overline{g}-g_{std}$ 最大的区域，然后再对所选区域进行四分查找，直到所分区域尺寸小于预设阈值。在最终选择的区域内，选择与纯白色最接近的颜色向量作为大气光的估计值。


### 传输系数估计

根据大气光散射模型可以得到复原图像的表达式为：
$$
J(p)=\frac{1}{t(p)}(I(p)-A)+A
$$
由于雾霾区域往往表现出很低的对比度，因此图像去雾的一个途径就是增强其对比度。而估算出大气光 $A$ 后，图像去雾的关键就在于优化传输系数 $t(p)$ 使雾霾区域的对比度最大化。此外，通常局部区域的传输系数几乎相同，因此很多文章都将图像分块处理，每块估计一次传输系数，减少运算量。

那么对比度该如何衡量呢？为此，文中统计了三种计算对比度的定量计算方式：

**MSE 对比度**

其计算公式为：
$$
C_{MSE}=\sum_{p=1}^N \frac{(J_c(p)-\overline{J}_c)^2}{N}
$$
其中 $c \in {r,g,b}$ 是色彩通道的索引，$N$ 是局部块内的像素数量，$\overline{J}$ 是 $J_c$ 在点 $p$ 的三通道像素均值。由于图像 $J$ 是未知的待求取的图像，因此需要将其转化为已知量和参数进行表达，即：
$$
C_{MSE}=\sum_{p=1}^N \frac{(I_c(p)-\overline{I}_c)^2}{t^2N}
$$
**Michelson 对比度**

其计算公式为：
$$
C_{Michelson}=\frac{J_{c,max}-J_{c,min}}{J_{c,max}+J_{c,min}}
$$
转化为观测图像 $I$ 表示：
$$
C_{Michelson}=\frac{I_{c,max}-I_{c,min}}{I_{c,max}+I_{c,min}-2A_c+2A_ct}
$$
**Weber 对比度**

Weber 对比度被定义为目标颜色与背景颜色的差值比例：
$$
C_{Weber}=\frac{J_{c,object}-J_{c,background}}{J_{c,background}}
$$
文中通过像素均值去估计背景颜色，那么其计算公式可定义为：
$$
C_{Weber}=\sum_{p=1}^N \frac{|J_c(p)-\overline{J}_c|}{N\overline{J}_c}
$$
转化为观测图像 $I$ 表示：
$$
C_{Weber}=\sum_{p=1}^N \frac{|I_c(p)-\overline{I}_c|}{N\overline{I}_c+N(t-1)A}
$$
原文比较了三种对比度计算方式的得到的去雾图像和传输系数图，发现结果非常相似，三种对比度都可以达到类似的效果。于是，作者就以 MSE 对比度为例展开细讲，其余两种方式按下不表。（*但是俺觉得 Weber 对比度的计算量应该是最少的，后续还是以 Weber 对比度为基础进行复现。*）

根据上面三种对比度计算方式，我们会发现传输系数 $t$ 越小时，对比度就会越高，那还优化什么？直接将 $t$ 置 $0$ 就好啦！可是，通过大气散射模型，我们发现复原图像和观测图是线性关系，且线性权重就是 $\frac{1}{t}$。那么，已知在观测图像中像素值范围是 $[0,255]$，复原图像中的像素值范围是多少？$t$ 越小，那么越界的像素就会越多，图像就会产生更多的损失！（*读到这里，我其实有了个深深的疑问，把越界的像素再通过极差缩放回来不就完了？？？但是我只是个后学末进，暂时还是先继续读完文章复现完了再说，后面试试到底缩放回来效果就知道行不行了*。）因此，原文认为，需要在图像对比度和损失细节之间寻找一个平衡，这就提出了总体损失函数：
$$
E=E_{contrast}+\lambda_L E_{loss}
$$
其中，
$$
E_{contrast} = -\sum_{c\in{r,g,b}} \sum_{p\in B} \frac{|J_c(p)-\overline{J}_c|}{N_B\overline{J}_c}
= -\sum_{c\in{r,g,b}} \sum_{p\in B} \frac{|I_c(p)-\overline{I}_c|}{N_B\overline{I}_c + N_B(t-1)A}
$$
是对比度损失函数，而

$$
\begin{align}

E_{loss}
&= \sum_{c\in{r,g,b}} \sum_{p\in B} \{ |min\{0,J_c(p)\}| + |max\{0,J_c(p)-255 \}| \} \\
&= \sum_{c\in{r,g,b}} \{ \sum_{i=0}^{\alpha_c} |\frac{i-A_c}{t}+A_c| h_c(i) + \sum_{i=\beta_c}^{255} |\frac{i-A_c}{t}+A_c-255)| h_c(i) \}

\end{align}
$$

是信息损失函数，$\lambda_L$ 是用来控制对比度和信息损失的权重系数。$E_{loss}$ 其实就是越界值绝对值值之和，$h_c$ 是通道 $c$ 像素值 $i$ 的统计直方图，$\alpha_c$ 和 $\beta_c$ 是观测图像中的截断上下限。

如果增大权重系数 $\lambda_L$，要使总体损失最小，则需要信息损失很小，从而起到了减小信息损失的作用。在极端情况下 $\lambda_L=\infty$，理论上信息损失为 $0$，即：
$$
min_{c\in{r,g,b}}min_{p\in B} \geq 0, \ max_{c\in{r,g,b}}max_{p\in B} \leq 255
$$
转换为对 $t$ 的限制则是：
$$
t \geq min_{c\in{r,g,b}}min_{p\in B} \{\frac{I_c(p)-A_c}{-A_c}\}, \
t \geq max_{c\in{r,g,b}}max_{p\in B} \{\frac{I_c(p)-A_c}{255-A_c}\}
$$
在信息无损失的情况下，传输系数 $t$ 越小则对比度增强得越多，总体损失也越小，所以无信息损失前提下的最优传输系数为：
$$
t^*=max \{
    min_{c\in{r,g,b}}min_{p\in B} \{\frac{I_c(p)-A_c}{-A_c}\}, \
    max_{c\in{r,g,b}}max_{p\in B} \{\frac{I_c(p)-A_c}{255-A_c}\}
    \}
$$
当然，可能可以调节 $t$ 获得使总体损失更小的最优解，但那也同时伴随着一定的信息损失。


### 传输系数细化

由于前文中将图像分块处理，同一块中所有像素具有相同传输系数，这就造成块与块之间可能因为传输系数相差过大，出现块效应。因此，原文中采用边缘保留滤波器对其进行滤波以消除块效应，具体地，选用的是导向滤波。这里，作者假设滤波后的传输系数是观测图的仿射变换：
$$
\hat{t}(q)=s^TI(q)+\psi
$$
其中，$s=(s_r,s_g,s_b)^T$ 是缩放向量，而 $\psi$ 是偏移量。这熟悉的线性函数，可以使用最小二乘法进行求解，即最小化其均方差：
$$
argmin_t(s, \psi) \sum_{q\in W} (t(q)-\hat{t}(q))^2
$$
解得（求解过程可以参考 [导向滤波 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/386520985)）：

$$
\begin{align}

&s = \frac{\frac{1}{|W|} \sum_{q\in W} t(q)I(q) - \overline{t}\overline{I} }{\overline{I^2} - \overline{I}^2}, \\
&\psi = \overline{t} - s^T\overline{I}

\end{align}
$$

到这里，常规的导向滤波做法就是每次移动一个像素，就根据以该像素为中心的窗口求解仿射变换系数，然后计算窗口内的每个像素处的传输系数，最后对每个像素处的所有重叠窗口的传输系数进行平均。但是原文认为这样的平均策略会对最终的传输系数进行平滑，从而导致去雾图中产生伪影。

为了解决这个问题，文中提出了一种基于移动窗口的导向滤波，与常规的导向滤波之间的差异在于窗口的选取：每次移动一个像素，在所有包含该像素的窗口中选择像素值方差最小的窗口计算传输系数，而并非直接选取以该像素为中心的窗口。需要注意的是，最后每个像素处的重叠窗口数量并不一样（*看到这里，我产生了深深的怀疑，这个移动窗口听上去就很耗时，真的能达到标题所宣称的实时去雾吗？*）。

最后，文章还提及一些 tips，比如传输系数最好是大于 0.1，最后的去雾图还进行了伽马校正以达到最佳效果。


### 视频去雾

视频去雾大概就是在图像去雾的基础之上，添加了帧与帧之间的时间相关性损失。
Resythesizer（正确的应该是 Resynthesizer）



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-08-07-dip-fastimage-notes.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/Accustomer/TheThingsWithImage/blob/main/Docs/3_%E7%9B%B4%E6%96%B9%E5%9B%BE%E5%9D%87%E8%A1%A1%E5%8C%96.md]({% include relrefx.html url="/backup/2022-08-07-dip-fastimage-notes.md/github.com/861cc907.html" %})
- [https://blog.csdn.net/Julialove102123/article/details/90638418]({% include relrefx.html url="/backup/2022-08-07-dip-fastimage-notes.md/blog.csdn.net/e5976eb9.html" %})
- [https://blog.csdn.net/xx116213/article/details/51848429]({% include relrefx.html url="/backup/2022-08-07-dip-fastimage-notes.md/blog.csdn.net/ee553221.html" %})
- [https://zhuanlan.zhihu.com/p/413747554]({% include relrefx.html url="/backup/2022-08-07-dip-fastimage-notes.md/zhuanlan.zhihu.com/675e0221.html" %})
- [https://ieeexplore.ieee.org/document/7128396/citations#citations]({% include relrefx.html url="/backup/2022-08-07-dip-fastimage-notes.md/ieeexplore.ieee.org/a42e8d77.html" %})
- [https://zhuanlan.zhihu.com/p/386520985]({% include relrefx.html url="/backup/2022-08-07-dip-fastimage-notes.md/zhuanlan.zhihu.com/1ce7d5a5.html" %})
