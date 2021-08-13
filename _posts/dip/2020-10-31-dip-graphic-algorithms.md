---
layout: post
title: "图像处理笔记 -- 神奇的图像处理算法"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

深度学习大行其道，传统图像处理算法发展也是很牛逼的。整理翻译了一些。
自己发明算法感觉不太现实，把这些算法用好了就很牛了。


## 像素图片矢量化

Implemented by [Scale2x](http://www.scale2x.it/) (on Sourceforge). [HQX](https://code.google.com/archive/p/hqx/) is a similar super resolution command line tool to enlarge images.

[Depixelizing pixel art](http://johanneskopf.de/publications/pixelart/).

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/example-depixelization.jpg"
url2="/assets/images/201031-dip-graphic-algorithms/pa-teaser.png" %}


## 灰色图片上色

It is explained in an article, [Colorization Using Optimization](http://www.cs.huji.ac.il/~yweiss/Colorization/) giving several examples.

A tool on GitHub allows also to color a sketch, with another image as color sample: [Style2Paint {% include relref_github.html %}](https://github.com/lllyasviel/style2paints).

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/colorization.jpg" %}


## 图片恢复 HDR

Wisely by removing the "noise", ie the image defects such as dots and stripes, and it needs to know to interpret that, the algorithm gives life to a cliche damaged or washed out.

It is implemented in a plugin for Gimp, [G'Mic](http://gmic.eu/). It can also automatically make HDR, ie increase the brightness of light areas and darken the dark parts.

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/house-hdr.jpg" %}


## 图片卡通化

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/convert-photo-to-drawing.jpg" %}


## Seam carving

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/seam-carving.jpg" %}

Intelligent algorithm to resize images maintaining the appearance of objects within it. It is actually implemented in the resizing functions of the main graphical utilities like Gimp with the [Liquid Rescale plugin](http://liquidrescale.wikidot.com/), ImageMagick with the -liquid-rescale option.

[Seam Carving for Content-Aware Image Resizing](http://www.faculty.idc.ac.il/arik/site/seam-carve.asp).


## 杂物移除

This algorithm is available both as a [Gimp {% include relref_scriptol.html %}](https://www.scriptol.com/design/gimp/removing-objects.php) plugin to install or in Photoshop.

<http://www.logarithmic.net/pfh/resynthesizer>

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/remove-object.jpg" %}


## 合成照片

This algorithm is implemented in the software [Sketch To Photo {% include relref_scriptol.html %}](https://www.scriptol.com/design/sketchtophoto.php). From the article, you can download the command line program.

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/composition.jpg" %}


## 美容

More information about this [esthetic trick algorithm {% include relref_scriptol.html %}](https://www.scriptol.com/programming/algorithm-pretty-face.php).

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/pretty-face-algorithm.jpg" %}


## PixelNN 算法

深度学习 PixelNN: Example-based Image Synthesis

[PixedNN](http://www.cs.cmu.edu/~aayushb/pixelNN/). Appearing more recently in 2017, turns a sketch into a photo!

pix2pix 来自卡内基梅隆大学的 Aayush Bansal 、Yaser Sheikh、Deva Ramanan，联合研究了一种基于示例图像合成清晰照片的技术 — PixelNN，把模糊的低分辨率或者是有马赛克的图片，使用表面法线贴图和草图等，合成出高分辨率的逼真图像。

这玩意可以提高驾驶技术：用 GAN 去除（爱情）动作片中的马赛克和衣服。

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/teaser1.png" %}

<https://www.ri.cmu.edu/publications/pixelnn-example-based-image-synthesis/>


## 阴影去除

[The Shadow meets the Mask: Pyramid-based shadow removal](http://www.cs.huji.ac.il/~danix/ShadowRemoval/index.html).

<https://www.cs.huji.ac.il/~danix/>

{% include image.html url="/assets/images/201031-dip-graphic-algorithms/ball_on_wood_no_shadow.jpg" %}


## 更牛逼的

[Animating a photo, a sketch](https://youtu.be/G63goXc5MyU). This algo of artificial intelligence makes the subject walk on a picture! Not available in a toolbox for now.

[List of all algorithms {% include relref_scriptol.html %}](https://www.scriptol.com/programming/list-algorithms.php).

[Creating a logo from a simple sketch {% include relref_scriptol.html %}](https://www.scriptol.com/design/gimp/logo.php).

[Image improvements](http://www.cs.huji.ac.il/~danix/). Demos of various algos for processing pictures to improve or restore them (the sources files are not linked).


## 参考

- [1] [Amazing algorithms to enhance or transform images {% include relref_scriptol.html %}](https://www.scriptol.com/programming/graphic-algorithms.php)
- [2] <http://www.ruanyifeng.com/blog/2011/08/amazing_algorithms_of_image_processing.html>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-10-31-dip-graphic-algorithms.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://www.scale2x.it/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.scale2x.it/11a3eccf.html" %})
- [https://code.google.com/archive/p/hqx/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/code.google.com/147ac2dc.html" %})
- [http://johanneskopf.de/publications/pixelart/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/johanneskopf.de/a8679ee7.html" %})
- [http://www.cs.huji.ac.il/~yweiss/Colorization/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.cs.huji.ac.il/b824e860.html" %})
- [https://github.com/lllyasviel/style2paints]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/github.com/f2f5bca4.html" %})
- [http://gmic.eu/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/gmic.eu/907f2721.html" %})
- [http://liquidrescale.wikidot.com/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/liquidrescale.wikidot.com/367f9dec.html" %})
- [http://www.faculty.idc.ac.il/arik/site/seam-carve.asp]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.faculty.idc.ac.il/2ae25b57.asp" %})
- [https://www.scriptol.com/design/gimp/removing-objects.php]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.scriptol.com/84c25ac0.php" %})
- [http://www.logarithmic.net/pfh/resynthesizer]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.logarithmic.net/ae603632.html" %})
- [https://www.scriptol.com/design/sketchtophoto.php]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.scriptol.com/4632068f.php" %})
- [https://www.scriptol.com/programming/algorithm-pretty-face.php]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.scriptol.com/a8cd8272.php" %})
- [http://www.cs.cmu.edu/~aayushb/pixelNN/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.cs.cmu.edu/e83fb960.html" %})
- [https://www.ri.cmu.edu/publications/pixelnn-example-based-image-synthesis/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.ri.cmu.edu/d8310e8d.html" %})
- [http://www.cs.huji.ac.il/~danix/ShadowRemoval/index.html]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.cs.huji.ac.il/c03658c8.html" %})
- [https://www.cs.huji.ac.il/~danix/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.cs.huji.ac.il/6a2d9330.html" %})
- [https://youtu.be/G63goXc5MyU]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/youtu.be/ea542fbd.html" %})
- [https://www.scriptol.com/programming/list-algorithms.php]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.scriptol.com/e2718941.php" %})
- [https://www.scriptol.com/design/gimp/logo.php]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.scriptol.com/c6e09d20.php" %})
- [http://www.cs.huji.ac.il/~danix/]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.cs.huji.ac.il/0cf626d4.html" %})
- [https://www.scriptol.com/programming/graphic-algorithms.php]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.scriptol.com/608cee18.php" %})
- [http://www.ruanyifeng.com/blog/2011/08/amazing_algorithms_of_image_processing.html]({% include relrefx.html url="/backup/2020-10-31-dip-graphic-algorithms.md/www.ruanyifeng.com/7ebac3ce.html" %})
