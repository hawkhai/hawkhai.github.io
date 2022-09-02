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


## 在双显示器接双显卡的场景下，Qt 的 QScreen()::geometry() 方法

[note {% include relref_csdn.html %}](https://blog.csdn.net/swift19221/article/details/125552771)
```cpp
// 如果不包括任务栏，则使用 availableGeometry()
rcPrimary = theScreen->geometry();

if (monitorinfo.dwFlags == MONITORINFOF_PRIMARY) {
    // 如果不包括任务栏，则使用 monitorinfo.rcWork
    g_rcPrimary = monitorinfo.rcMonitor;
}
else {
    g_rcSecond = monitorinfo.rcMonitor;
}
```

比较上面 1、2 两个方法的结果，发现方法 1 获取的矩形区域是不正确的，因此用方法 2 来代替。
如果是单显卡接两个显示器，则没有问题。


## Qt 中 QMainWindow、QWidget、QDialog 的区别

[from {% include relref_csdn.html %}](https://blog.csdn.net/qq_41684134/article/details/87973825)
区别总结
* QMainWindow 类提供一个有菜单条、锚接窗口（例如工具条）和一个状态条的主应用程序窗口。
    主窗口通常用在提供一个大的中央窗口部件（例如文本编辑或者绘制画布）以及周围菜单、工具条和一个状态条。
    QMainWindow 常常被继承，因为这使得封装中央部件、菜单和工具条以及窗口状态条变得更容易，当用户点击菜单项或者工具条按钮时，槽会被调用。
* QWidget 类是所有用户界面对象的基类。 窗口部件是用户界面的一个基本单元：它从窗口系统接收鼠标、键盘和其它事件，并且在屏幕上绘制自己。
    每一个窗口部件都是矩形的，并且它们按 Z 轴顺序排列。一个窗口部件可以被它的父窗口部件或者它前面的窗口部件盖住一部分。
* QDialog 是最普通的顶级窗口。 一个不会被嵌入到父窗口部件的窗口部件叫做顶级窗口部件。
    通常情况下，顶级窗口部件是有框架和标题栏的窗口（尽管使用了一定的窗口部件标记，创建顶级窗口部件时也可能没有这些装饰）。
    在 Qt 中，QMainWindow 和不同的 QDialog 的子类是最普通的顶级窗口

选用原则
* 如果是主窗体，则基于 QMainWindow 创建。
* 如果是顶级对话框，则基于 QDialog 创建。
* 如果需要嵌入到其他窗体中，则基于 QWidget 创建
* 如果不确定，或者 1 2 两种情况都有，那么，就选择 QWidget。

* dialog 有 exec 函数，如果是 dialog 窗口，后边的窗口是不可选的；
* widget 和 dialog 都有 show 函数，如果通过这个函数显示这两种类型的窗口，则两个窗口都是可选的；
* widget 主要是在上面放置布局和控件；
* mainwindow 可以显示菜单，工具栏，状态栏、托盘等功能。

QWidget & QFrame
* QWidget：就是一个容器，是 QFrame 基类。
* QFrame：也是一个容器，不过是一个有边框的容器，是 QWidget 子类。
* 两者的主要区别就是容器有无边框，比如组合成下面组件时，最好使用 QFrame：
    QWidget 的子类窗口如要正常显示背景色，需要 `setAttribute(Qt::WA_StyledBackground);`
    目的是脱离父窗口的样式。

如果你从 QWidget 子类化一个自定义小部件，那么为了使用样式表，你需要为自定义小部件提供一个 paintEvent：
```cpp
void myWidget::paintEvent(QPaintEvent *event) {
    QStyleOption opt;
    opt.init(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget, &opt, &p, this);
}
```
再 paintEvent 中加入那几句就 OK 了，可以使用 setStyleSheet 改变背景。


## QGraphicsScene QGraphicsView QGraphicsItem

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
    * QImage 是与硬件无关的绘图设备，提供了像素级操作支持。
* QPixmap 是为在屏幕上显示图像而设计和优化的。
    * QPixmap 为图片在屏幕显示做了优化，QPixmap 与绘图设备底层相关，不提供像素级支持，不同设备上图像有所不同。
    * 可以直接使用 QPainter 在 QPixmap 上绘制也可以接受一个图片文件在屏幕上显示。
* QPicture 类是一个记录和回放 QPainter 命令的绘制设备。
    * QPicture 用于记录 QPainter 的操作，并保存到一个序列化的平台独立的二进制文件中。
* QBitmap 是 QPixmap 的派生类，只能绘制黑白图像（色深为 1）。

[from {% include relref_cnblogs.html %}](https://www.cnblogs.com/finley/p/5268237.html)
QGraphicsScene 类作为容器（MV 中的模型 Model），用于存储所有的图形元素；
QGraphicsView 则是观察窗口，可以显示场景的一部分或者全局；所有的图形元素均继承自 QGraphicsItem。

我们再来看看 QImage 类的几个构造函数：
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

- [https://blog.csdn.net/swift19221/article/details/125552771]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/blog.csdn.net/17a77344.html" %})
- [https://blog.csdn.net/qq_41684134/article/details/87973825]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/blog.csdn.net/0695cb12.html" %})
- [https://github.com/SouthEastUniversityLinuxClub/MiniDraw]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/github.com/2163be2f.html" %})
- [https://blog.csdn.net/kenfan1647/article/details/117289104]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/blog.csdn.net/51006d14.html" %})
- [https://zhuanlan.zhihu.com/p/368192789]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/zhuanlan.zhihu.com/84b77b7b.html" %})
- [https://www.cnblogs.com/ybqjymy/p/13517060.html]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/www.cnblogs.com/1d742575.html" %})
- [https://www.cnblogs.com/finley/p/5268237.html]({% include relrefx.html url="/backup/2022-08-18-qt-QGraphicsScene.md/www.cnblogs.com/b5647bb4.html" %})
