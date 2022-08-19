---
layout: post
title: "编程与调试 C++ -- Qt QGraphicsScene QGraphicsView QGraphicsItem"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "QT", "C/C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
---

* <https://github.com/SouthEastUniversityLinuxClub/MiniDraw>
* <https://blog.csdn.net/kenfan1647/article/details/117289104>

QGraphicsScene 是管理 QGraphicsItem 的容器，它继承自 QObject，而不是 QWidget，因此它本身不可见，需要和 QGraphicsView 配合使用才能看到管理的项目。

[from {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/368192789)
{% include image.html url="/assets/images/220818-qt-qgraphicsscene/v2-c842d05d0eefa511d0cc6b3857f2cd3c_1440w.jpg" %}
{% include image.html url="/assets/images/220818-qt-qgraphicsscene/v2-41d12298a0a73e6e5f6252c2ddfe28c1_1440w.jpg" %}

QGraphicsScene 通过查找算法来管理 item 的位置，默认算法是 BSP tree。
{% include image.html url="/assets/images/220818-qt-qgraphicsscene/v2-429668ba479b5c89c91df4499eded67b_720w.jpg" %}

[Qt 绘图之 QGraphicsScene QGraphicsView QGraphicsItem 详解 {% include relref_cnblogs.html %}](https://www.cnblogs.com/ybqjymy/p/13517060.html)

Graphics View 提供的是一种类似于 Qt model-view 的编程。多个 views 可以监视同一个场景，而场景包含多个具有多种几何外形的 items。

* E:\kpdf\paint\MiniDraw

Qt 提供了处理图像数据的类：QImage, QPixmap 和 QPicture。
* QImage 是为 I/O 和直接像素访问和操作而设计和优化的。
* QPixmap 是为在屏幕上显示图像而设计和优化的。
* QPicture 类是一个记录和回放 QPainter 命令的绘制设备。

我们再来看看QImage类的几个构造函数：
```cpp
// 浅拷贝
QImage(uchar * data, int width, int height, Format format)
// 浅拷贝
QImage(const uchar * data, int width, int height, Format format)
// 浅拷贝
QImage(uchar * data, int width, int height, int bytesPerLine, Format format)
// 浅拷贝
QImage(const uchar * data, int width, int height, int bytesPerLine, Format format)
// 深拷贝
QImage QImage::copy(const QRect & rectangle = QRect()) const
// 浅拷贝
QImage QImage::rgbSwapped() const
```


<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-08-18-qt-QGraphicsScene.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/SouthEastUniversityLinuxClub/MiniDraw]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/github.com/2163be2f.html" %})
- [https://blog.csdn.net/kenfan1647/article/details/117289104]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/blog.csdn.net/51006d14.html" %})
- [https://zhuanlan.zhihu.com/p/368192789]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/zhuanlan.zhihu.com/84b77b7b.html" %})
- [https://www.cnblogs.com/ybqjymy/p/13517060.html]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/www.cnblogs.com/1d742575.html" %})
