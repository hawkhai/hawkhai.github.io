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
// offset 为屏幕坐标系。
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

    checkResetScaleOffset();
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

    float mAnimationCenterTarget = mCurlView->getAnimationCenterTarget();
    auto mViewRect = mCurlView->getRenderer()->getViewRect();
    mAnimationCenterTarget = mAnimationCenterTarget / mViewRect.width() * 2;
    glpoint.setX(glpoint.x() - mAnimationCenterTarget);

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

    checkResetScaleOffset();
    this->update();
    return true;
}
```

矩阵作用，是左运算，这个很关键。

```cpp
float mAnimationCenterSource = 0;
ULONGLONG mAnimationCenterStartTime = 0;
float mAnimationCenterTarget = 0; // 这里是自己坐标系的偏移

bool CurlViewAngle::clickPaperTest(QPointF point, QMatrix4x4 projection, QPointF scale, QPointF offset) {
    // We need page rects quite extensively so get them for later use.
    QRectF rightRect = mRenderer.getPageRect(PAGE_RIGHT);
    QRectF leftRect = mRenderer.getPageRect(PAGE_LEFT);

    // 相当于拼接在 projection 的左边。先起作用。
    float offsetz = this->mAnimationCenterTarget; // / mRenderer.getViewRect().width() * 2;

    // 自动居中 的逻辑。
    QMatrix4x4 matrix = projection;
    matrix.translate(offsetz, 0);

    matrix.scale(scale.x(), scale.y());
    matrix.translate(offset.x(), offset.y());

    mRenderer.translate(point); // 自定义空间坐标。
    point = projection.map(point); // OpenGL 坐标。

    leftRect = matrix.mapRect(leftRect);
    rightRect = matrix.mapRect(rightRect);

    if (mViewMode == SHOW_TWO_PAGES) {
        if (mCurrentIndex > 0) {
            if (leftRect.contains(point)) {
                return true;
            }
        }
        if (mCurrentIndex < mPageProvider->getPaperCount()) {
            if (rightRect.contains(point)) {
                return true;
            }
        }
        return false;
    }
    // 单页模式
    if (mCurrentIndex < mPageProvider->getPaperCount() && rightRect.contains(point)) {
        return true;
    }
    return false;
}

void FlipWidgetAngle::paintGL() {
    ULONGLONG currentTime = GetTickCount64();
    FastGLWidget::paintGL();

    QMatrix4x4 projectionk = projection;

    long mAnimationDurationTime = 300 * PAGE_FLIPPING_SPEED;
    ULONGLONG mAnimationStartTime = mCurlView->getAnimationCenterStartTime();
    float mAnimationCenterSource = mCurlView->getAnimationCenterSource();
    float mAnimationCenterTarget = mCurlView->getAnimationCenterTarget();

    bool mAnimate = false;
    if (currentTime >= mAnimationStartTime + mAnimationDurationTime) {
        projectionk.translate(mAnimationCenterTarget, 0);
    } else {
        float t = 1.f - ((float)(currentTime - mAnimationStartTime) / mAnimationDurationTime);
        t = 1.f - (t * t * t * (3 - 2 * t));
        float offsetx = mAnimationCenterSource + (mAnimationCenterTarget - mAnimationCenterSource) * t;
        projectionk.translate(offsetx, 0);
        mAnimate = true;
    }

    //m_offset = QPointF(0.5, 0.5);
    //m_scale = QPointF(2.0, 2.0);
    projectionk.scale(m_scale.x(), m_scale.y());
    projectionk.translate(m_offset.x(), m_offset.y());

    m_framebuffer->bind();
    mCurlView->getRenderer()->onDrawFrame(*this, projectionk, program, false);
    m_framebuffer->release();

    m_framebufferMask->bind();
    mCurlView->getRenderer()->onDrawFrame(*this, projectionk, program, true);
    m_framebufferMask->release();

    mCurlView->getRenderer()->onDrawFrame(*this, projectionk, program, false);

    //m_framebuffer->toImage().save("m_framebuffer.png");
    //m_framebufferMask->toImage().save("m_framebufferMask.png");

    // 使用 32 位 ARGB 格式（0xAARRGGBB）存储帧。这相当于 QImage :: Format_ARGB32_Premultiplied。
    //QImage frame = this->grabFramebuffer();
    mCurlView->getRenderer()->onPostProcessing(*this, program,        //
                                               *m_framebuffer, *m_framebufferMask);

    static int paintConter = 0;
    printf("FlipWidgetAngle::paintGL[%d] %d \n", ++paintConter, GetTickCount64() - currentTime);

    if (m_callback) {
        m_callback->onFlipWidgetPaintGL(*this);
    }
    if (mAnimate) { // 下一轮动画。
        this->update();
    }
}

bool FlipWidgetAngle::checkScaleOffset(bool xaxis) {
    // We need page rects quite extensively so get them for later use.
    QRectF rightRect = mCurlView->getRenderer()->getPageRect(PAGE_RIGHT);
    QRectF leftRect = mCurlView->getRenderer()->getPageRect(PAGE_LEFT);
    QMatrix4x4 projectionk = projection;

    float mAnimationCenterTarget = mCurlView->getAnimationCenterTarget();
    auto mViewRect = mCurlView->getRenderer()->getViewRect();
    // 相当于拼接在 projection 的左边。先起作用。
    //mAnimationCenterTarget = mAnimationCenterTarget / mViewRect.width() * 2;
    projectionk.translate(mAnimationCenterTarget, 0);

    projectionk.scale(m_scale.x(), m_scale.y());
    projectionk.translate(m_offset.x(), m_offset.y());

    QPointF lt, rb;
    if (mCurlView->getViewMode() == SHOW_ONE_PAGE) {
        lt = projectionk * rightRect.topLeft();
        rb = projectionk * rightRect.bottomRight();
    } else {
        // 双页模式。
        lt = projectionk * leftRect.topLeft();
        rb = projectionk * rightRect.bottomRight();

        int curidx = this->getCurrentIndex();
        auto total = mCurlView->getPaperCount();
        if (curidx == 0) {
            lt = projectionk * rightRect.topLeft();
            rb = projectionk * rightRect.bottomRight();
        } else if (curidx == total) {
            lt = projectionk * leftRect.topLeft();
            rb = projectionk * leftRect.bottomRight();
        }
    }
    auto x1 = lt + (rb - lt) * 0.75;
    auto x2 = rb - (rb - lt) * 0.75;
    if (xaxis) {
        return (x1.x() >= -1.0 && x1.x() <= 1.0) || (x2.x() >= -1.0 && x2.x() <= 1.0);
    }
    return (x1.y() >= -1.0 && x1.y() <= 1.0) || (x2.y() >= -1.0 && x2.y() <= 1.0);
}
bool FlipWidgetAngle::checkResetScaleOffset() {
    for (int i = 0; i < 100; i++) {
        bool changed = false;
        if (!checkScaleOffset(true)) {
            m_offset.setX(m_offset.x() * 99 / 100);
            changed = true;
        }
        if (!checkScaleOffset(false)) {
            m_offset.setY(m_offset.y() * 99 / 100);
            changed = true;
        }
        if (!changed) {
            break;
        }
    }
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
