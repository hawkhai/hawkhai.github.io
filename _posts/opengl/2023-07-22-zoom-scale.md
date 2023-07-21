---
layout: post
title: "图形学笔记 -- OpenGL 图形学 / 二维缩放和移动"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

* 移动的时候，参考屏幕坐标，便于用户手动操作。
* 缩放的时候，鼠标指示的位置不变。

```cpp
// point 为屏幕坐标，拉伸后保证，这个点在屏幕的位置不变化。
virtual bool zoomScale(QPointF scale, QPointF point) = 0;
// 屏幕坐标系，便于用户手动操作。
virtual bool moveTranslate(QPointF offset) = 0;
```

关于移动：
```cpp
bool FlipWidgetAngle::moveTranslate(QPointF offset) {

    auto mViewRect = mCurlView->getRenderer()->getViewRect();

    // OpenGL 坐标系
    float fdx = 1.0 * offset.x() / width() * mViewRect.width() / m_scale.x();
    float fdy = 1.0 * offset.y() / height() * mViewRect.height() / m_scale.y();

    m_offset.setX(m_offset.x() + fdx);
    m_offset.setY(m_offset.y() + fdy);

    this->update();
    return true;
}
```

关于缩放：
```cpp
bool FlipWidgetAngle::zoomScale(QPointF scale, QPointF point) {

    QPointF glpoint; // 在 OpenGL 中的坐标。
    glpoint.setX(1.0 * (point.x() - width() / 2) / (1.0 * width() / 2));
    glpoint.setY(1.0 * (height() / 2 - point.y()) / (1.0 * height() / 2));

    auto projectionk = projection;
    projectionk.scale(m_scale.x(), m_scale.y());
    projectionk.translate(m_offset.x(), m_offset.y());

    // orig --> glpoint
    auto orig = projectionk.inverted() * glpoint;
    auto target1 = projectionk * orig;

    m_scale = scale;
    projectionk = projection;
    projectionk.scale(m_scale.x(), m_scale.y());

    auto target2 = projectionk * orig;
    m_offset = projectionk.inverted() * (target1 - target2);

    projectionk.translate(m_offset.x(), m_offset.y());
    target2 = projectionk * orig;

    assert(abs(target1.x() - target2.x()) <= 0.0001);
    assert(abs(target1.y() - target2.y()) <= 0.0001);
    this->update();
    return true;
}
```

1. 通过逆矩阵，找到对应 OpenGL 点对应的 orig 点。
2. 根据 orig 点，进行新的 变换，得到新的 target2。
3. 计算新的 `m_offset = projectionk.inverted() * (target1 - target2);`

最终实现的效果：

{% include image.html url="/assets/images/230722-zoom-scale/flipx1.webp" caption="单页的情况" %}

{% include image.html url="/assets/images/230722-zoom-scale/flipx2.webp" caption="双页的情况" %}



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-07-22-zoom-scale.md.js" %}'></script></p>
