---
layout: post
title: "特效编程笔记 -- OpenGL 图形学 / 高级 OpenGL：Stencil Test（模板测试）"
author:
location: "珠海"
categories: ["特效"]
tags: ["特效", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
cluster: "LearnOpenGL"
---

前面的简单，看到后面，慢慢的有难度了，stencil 模板測試，要看好久才能理解。看了 ARM 的那篇文章，瞬间透彻了。
原来是一个 GPU 硬件版本的预设回调函数。[旺柴][旺柴]

在 OpenGLES 中，有三个可以绘制的 buffer（缓存），color buffer（颜色缓存），depth buffer（深度缓存）和 stencil buffer（模板缓存）。
对于 color buffer 和 depth buffer 来说，buffer 里面存储的一般都是浮点数，然而对于 stencil buffer，buffer 存储的是无符号整数，确切的说，0 或者 1。
在 OpenGLES 中，stencil buffer 一般最大有 8 位，这就意味着 stencil buffer 的最大值就是 0xFF。
首先要建立起来的观念就是 stencil buffer 的操作并不是加减乘除等算术运算，而是位操作运算。

{% include image.html url="/assets/images/201216-shader-opengl-advanced-~98/0825.pfo.png" %}


## 三个 stencil test 相关的函数

```cpp
void glStencilMask(GLuint mask);
void glStencilOp(GLenum sfail, GLenum dpfail, GLenum dppass);
void glStencilFunc(GLenum func, GLint ref, GLuint mask);
```

* glStencilMask 控制着写 stencil buffer 之前要做的一个与操作
* glStencilOp 设置了在完成 stencil test 后对当前 fragment 的 stencil 值的操作
    * stencil test 的结果有三种情况
        * stencil test 失败
        * stencil test 成功，depth test 失败
        * stencil test 成功，depth test 成功
    * 对于 stencil 值有 7 个操作
        * GL_KEEP
        * GL_ZERO
        * GL_REPLACE
        * GL_INCR
        * GL_INCR_WRAP
        * GL_DECR
        * GL_DECR_WRAP
        * GL_INVERT
* glStencilFunc 提供了三个参数
    * 比较函数 func，这个和 depth test 是完全一样的
    * 比较基准值 ref
    * 比较时需要用到的 mask

伪代码：

```cpp
// stencil test 比较的时候需要 mask
status = glStencilFunc.func((stencilbuf[x,y] & glStencilFunc.mask), (glStencilFunc.ref & glStencilFunc.mask));
status |= depth_test_result;
if (status == stencil_test_fail) stencilop = glStencilOp.sfailop;
else if (status == stencil_test_pass & depth_test_fail) stencilop = glStencilOp.dpfailop;
else if (status == stencil_test_pass & depth_test_pass) stencilop = glStencilOp.dppassop;
// stencil test 结束后的操作不需要 mask
stencil_new_value = stencilop(stencilbuf[x,y]);
// 写入 stencil buffer 的时候需要另一个 mask
stencilbuf[x,y] = (stencil_new_value & glStencilMask.mask) | (stencilbuf[x,y] & (~glStencilMask.mask));
```


## 给物体加上轮廓的步骤

1. 在绘制物体前，把模板方程设置为 `GL_ALWAYS`，用 1 更新物体将被渲染的片段。
2. 渲染物体，写入模板缓冲。
3. 关闭模板写入和深度测试。
4. 每个物体放大一点点。
5. 使用一个不同的片段着色器用来输出一个纯颜色。
6. 再次绘制物体，但只是当它们的片段的模板值不为 1 时才进行。
7. 开启模板写入和深度测试。


## 在应用程序端的性能优化

尽量多用 GL_KEEP，避免 GL_REPLACE。
假如应用程序只希望写 stencil buffer，下面两种情况是等价的。

```cpp
glStencilOp(GL_REPLACE, GL_REPLACE, GL_REPLACE);
glStencilFunc(GL_ALWAYS, ref, mask);
```

```cpp
glStencilOp(GL_KEEP, GL_REPLACE, GL_REPLACE);
glStencilFunc(GL_NOTEQUAL, ref, mask);
```


## 参考资料

- [1] 这个资料最好。[Stencil Test（模板测试）不得不说的那些事 ARM](https://community.arm.com/cn/b/blog/posts/stencil-test)
- [3] 这个资料第二好。[OpenGL 模板缓存 {% include relref_csdn.html %}](https://blog.csdn.net/korekara88730/article/details/42213217)
- [2] 这个不知道在讲啥。[使用 OpenGL 实现遮罩效果 {% include relref_csdn.html %}](https://blog.csdn.net/jaryguo/article/details/52627151)
- [4] [高级 OpenGL » 模板测试](https://learnopengl-cn.readthedocs.io/zh/latest/04%20Advanced%20OpenGL/02%20Stencil%20testing/)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [https://community.arm.com/cn/b/blog/posts/stencil-test]({% include relref.html url="/backup/2020-12-16-shader-OpenGL-Advanced-stencil-test.md/community.arm.com/113572ca.html" %})
- [https://blog.csdn.net/korekara88730/article/details/42213217]({% include relref.html url="/backup/2020-12-16-shader-OpenGL-Advanced-stencil-test.md/blog.csdn.net/e53c4341.html" %})
- [https://blog.csdn.net/jaryguo/article/details/52627151]({% include relref.html url="/backup/2020-12-16-shader-OpenGL-Advanced-stencil-test.md/blog.csdn.net/162243d8.html" %})
- [https://learnopengl-cn.readthedocs.io/zh/latest/04%20Advanced%20OpenGL/02%20Stencil%20testing/]({% include relref.html url="/backup/2020-12-16-shader-OpenGL-Advanced-stencil-test.md/learnopengl-cn.readthedocs.io/a758e9ee.html" %})
