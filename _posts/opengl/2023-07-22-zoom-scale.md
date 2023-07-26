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
virtual bool resetTranslate() = 0;
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
    this->update(); // moveTranslate
    return true;
}
bool FlipWidgetAngle::resetTranslate() {
    m_offset = QPointF(0.0, 0.0);
    this->update(); // resetTranslate
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
    this->update(); // zoomScale
    return true;
}
```

矩阵作用，是左运算，这个很关键。
* auto projectionk = projection;
* projectionk.scale(m_scale.x(), m_scale.y()); -- 先弄上去，其实是后起作用。
* projectionk.translate(m_offset.x(), m_offset.y()); -- 后弄上去，先起作用。

本来有一个坐标系 projection，后来在上面加入了位移动画。
最后又加上了 scale & offset，代码就变的很复杂。

```cpp
float mAnimationCenterSource = 0;
ULONGLONG mAnimationCenterStartTime = 0;
float mAnimationCenterTarget = 0; // 这里是自己坐标系的偏移。

bool CurlViewAngle::clickPaperTest(QPointF point, QMatrix4x4 projection, QPointF scale, QPointF offset) {

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
    ULONGLONG mAnimationCenterStartTime = mCurlView->getAnimationCenterStartTime();
    float mAnimationCenterSource = mCurlView->getAnimationCenterSource();
    float mAnimationCenterTarget = mCurlView->getAnimationCenterTarget();

    bool mAnimate = false;
    if (currentTime >= mAnimationCenterStartTime + mAnimationDurationTime) {
        projectionk.translate(mAnimationCenterTarget, 0);
    } else {
        float t = 1.f - ((float)(currentTime - mAnimationCenterStartTime) / mAnimationDurationTime);
        t = 1.f - (t * t * t * (3 - 2 * t));
        float offsetx = mAnimationCenterSource + (mAnimationCenterTarget - mAnimationCenterSource) * t;
        projectionk.translate(offsetx, 0);
        mAnimate = true;
    }

    projectionk.scale(m_scale.x(), m_scale.y());
    projectionk.translate(m_offset.x(), m_offset.y());

    bool brotate = false;

    m_framebuffer->bind();
    brotate = mCurlView->getRenderer()->onDrawFrame(*this, projectionk, program, false) || brotate;
    m_framebuffer->release();

    m_framebufferMask->bind();
    brotate = mCurlView->getRenderer()->onDrawFrame(*this, projectionk, program, true) || brotate;
    m_framebufferMask->release();

    brotate = mCurlView->getRenderer()->onDrawFrame(*this, projectionk, program, false) || brotate;

    //m_framebuffer->toImage().save("m_framebuffer.png");
    //m_framebufferMask->toImage().save("m_framebufferMask.png");

    // 使用 32 位 ARGB 格式（0xAARRGGBB）存储帧。这相当于 QImage :: Format_ARGB32_Premultiplied。
    //QImage frame = this->grabFramebuffer();
    mCurlView->getRenderer()->onPostProcessing(*this, program, //
                                               *m_framebuffer, *m_framebufferMask);

    static int paintConter = 0;
    printf("FlipWidgetAngle::paintGL[%d] %d \n", ++paintConter, GetTickCount64() - currentTime);

    if (m_callback) {
        m_callback->onFlipWidgetPaintGL(*this);
    }
    if (mAnimate) { // 下一轮动画。
        QTimer::singleShot(MY_ANIMATE_TIMER, this, [&]() {
            this->update(); // 居中动画。
        });
    } else if (brotate) {
        QTimer::singleShot(MY_ANIMATE_TIMER, this, [&]() {
            this->update(); // 旋转动画。
        });
    }
}

bool FlipWidgetAngle::checkScaleOffset(bool xaxis, float& recommend) {
    recommend = 0;
    QRectF rightRect = mCurlView->getRenderer()->getPageRect(PAGE_RIGHT);
    QRectF leftRect = mCurlView->getRenderer()->getPageRect(PAGE_LEFT);
    QMatrix4x4 projectionk = projection;

    float mAnimationCenterTarget = mCurlView->getAnimationCenterTarget();
    auto mViewRect = mCurlView->getRenderer()->getViewRect();
    // 相当于拼接在 projection 的左边。先起作用。
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
    auto x1x = lt + (rb - lt) * 0.25;
    auto x2x = rb - (rb - lt) * 0.25;

    if (m_scale.x() >= 1.0) {
        x1 = lt + (rb - lt) * 0.85;
        x2 = rb - (rb - lt) * 0.85;
        x1x = lt + (rb - lt) * 0.15;
        x2x = rb - (rb - lt) * 0.15;
    }

    if (xaxis) {
        bool retv = (x1.x() >= -1.0 && x1.x() <= 1.0) || (x2.x() >= -1.0 && x2.x() <= 1.0);
        // 两头都看不到了，其实中间的还能看到。
        for (int i = 0; i <= 100 && !retv; i++) {
            float tmpx = x1.x() + (x2.x() - x1.x()) * i / 100;
            retv = retv || (tmpx >= -1.0 && tmpx <= 1.0);
        }
        if (!retv) {
            if (x1x.x() >= 1.0) {
                recommend = -abs(m_offset.x()) / 100;
            } else if (x2x.x() <= -1.0) {
                recommend = abs(m_offset.x()) / 100;
            } else {
                assert(false);
            }
        }
        return retv;
    }
    bool retv = (x1.y() >= -1.0 && x1.y() <= 1.0) || (x2.y() >= -1.0 && x2.y() <= 1.0);
    // 两头都看不到了，其实中间的还能看到。
    for (int i = 0; i <= 100 && !retv; i++) {
        float tmpx = x1.y() + (x2.y() - x1.y()) * i / 100;
        retv = retv || (tmpx >= -1.0 && tmpx <= 1.0);
    }
    if (!retv) {
        if (x1x.y() <= -1.0) {
            recommend = abs(m_offset.y()) / 100;
        } else if (x2x.y() >= 1.0) {
            recommend = -abs(m_offset.y()) / 100;
        } else {
            assert(false);
        }
    }
    return retv;
}
bool FlipWidgetAngle::checkResetScaleOffset() {
    for (int i = 0; i < 100; i++) {
        bool changed = false;
        float recommend = 0;
        if (!checkScaleOffset(true, recommend)) {
            m_offset.setX(m_offset.x() + recommend);
            changed = true;
        }
        recommend = 0;
        if (!checkScaleOffset(false, recommend)) {
            m_offset.setY(m_offset.y() + recommend);
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

纹理旋转：
```cpp
auto rect = getPageRect(PAGE_RIGHT);
QMatrix4x4 matrix;
matrix.setToIdentity();
matrix.translate(0.5, 0.5);
matrix.scale(rect.height(), rect.width());
matrix.rotate(GetTickCount(), 0, 0, 1);
matrix.scale(1.0 / rect.height(), 1.0 / rect.width());
matrix.translate(-0.5, -0.5);
program.setUniformValue("texture_matrix", matrix);
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-07-22-zoom-scale.md.js" %}'></script></p>
