---
layout: post
title: "深度学习 -- 吴恩达机器学习"
author:
location: "珠海"
categories: ["深度学习"]
tags: ["机器学习", "深度学习"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
---


## 吴恩达

* [吴恩达机器学习系列课程 {% include relref_bili.html %}](https://www.bilibili.com/video/BV164411b7dx)
* [视频的讲义 {% include relref_github.html %}](https://github.com/TheisTrue/MLofAndrew-Ng)


### 有监督学习和无监督学习

监督（supervised）= 标签（label），是否有监督，就是输入数据（input）是否有标签，有标签则为有监督学习，没标签则为无监督学习。
至于半监督学习，就是一半（一点点）数据有标签，一半（极其巨大）数据没标签。

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/20190717172554930.png" %}

#### 监督学习

[from {% include relref_jianshu.html %}](https://www.jianshu.com/p/682c88cee5a8)

定义：根据已有的数据集，知道输入和输出结果之间的关系。根据这种已知的关系，训练得到一个最优的模型。
也就是说，在监督学习中训练数据既有特征（feature）又有标签（label），通过训练，让机器可以自己找到特征和标签之间的联系，
在面对只有特征没有标签的数据时，可以判断出标签。

监督学习的分类：回归（Regression）、分类（Classification）。

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/20211108161254.png" %}

#### 无监督学习

定义：我们不知道数据集中数据、特征之间的关系，而是要根据聚类或一定的模型得到数据之间的关系。

Cocktail party problem algorithm:
$$
[W, s, v]=\operatorname{svd}\left((\operatorname{repmat}(\operatorname{sum}(x . * x, 1), \operatorname{size}(x, 1), 1) . * x) * x^{\prime}\right)
$$

**Octave**
P6 start...


## 李宏毅

* [李宏毅 2020 机器学习 & 深度学习 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1JE411g7XF)
* 课件：<http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html>

P3 08:42



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-10-11-ml-MLofAndrew-Ng.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV164411b7dx]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.bilibili.com/72ebaee9.html" %})
- [https://github.com/TheisTrue/MLofAndrew-Ng]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/github.com/f1eeb779.html" %})
- [https://www.jianshu.com/p/682c88cee5a8]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.jianshu.com/fdc8f898.html" %})
- [https://www.bilibili.com/video/BV1JE411g7XF]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.bilibili.com/68e17dc9.html" %})
- [http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/speech.ee.ntu.edu.tw/f319f059.html" %})
