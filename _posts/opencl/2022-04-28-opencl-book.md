---
layout: post
title: "编程与调试 C++ -- OpenCL 2.0 异构计算 笔记"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++", "OpenCL"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "OpenCL"
---


## OpenCL 同步函数

barrier(CLK_LOCAL_MEM_FENCE);
barrier(CLK_GLOBAL_MEM_FENCE);
<http://cjld.github.io/2013/07/31/openclasync/>


## Arm Mali Bifrost OpenCL Developer Guide Version 1.0

<https://developer.arm.com/documentation/101574/0100/>


## NVIDIA OpenCL SDK Code Samples

<https://developer.nvidia.com/opencl>

* OpenCL Bandwidth Test
    * developer.download.nvidia.com/compute/DevZone/OpenCL/Projects/oclBandwidthTest.zip

* Test the bandwidth for DEVICE_TO_HOST
* host to device HOST_TO_DEVICE
* device to device transfers DEVICE_TO_DEVICE
    * clEnqueueCopyBuffer

* pinned memory（Create a host buffer）PINNED
    * clCreateBuffer(cxGPUContext, CL_MEM_READ_WRITE \| CL_MEM_ALLOC_HOST_PTR, memSize, NULL, &ciErrNum);
* standard host alloc PAGEABLE
    * h_data = (unsigned char \*)malloc(memSize);
* allocate device memory
    * clCreateBuffer(cxGPUContext, CL_MEM_READ_WRITE, memSize, NULL, &ciErrNum);

* 直接访问：DIRECT
    * clEnqueueWriteBuffer(cqCommandQueue, cmDevData, CL_FALSE, 0, memSize, h_data, 0, NULL, NULL);
* map 访问：（Get a mapped pointer）MAPPED
    * void\* dm_idata = clEnqueueMapBuffer(cqCommandQueue, cmDevData, CL_TRUE, CL_MAP_WRITE, 0, memSize, 0, NULL, NULL, &ciErrNum);


## OpenCL Programming Guide

<https://rocmdocs.amd.com/en/latest/Programming_Guides/Opencl-programming-guide.html>


## OpenCL Programming Guide

<https://rocmdocs.amd.com/en/latest/Programming_Guides/Opencl-programming-guide.html>
<https://www.nersc.gov/assets/pubs_presos/MattsonTutorialSC14.pdf>

<https://www.khronos.org/registry/OpenCL/specs/opencl-1.2.pdf>
<https://www.khronos.org/files/opencl-1-2-quick-reference-card.pdf>

{% include image.html url="/assets/images/220428-opencl-book/20220511114644.png" %}

Use the Memory Hierarchy effectively
• Organize your computation so it puts the most frequently used data
in faster memory … optimized of course around the available size.

----

**OpenCL 是一个小而美的东西，比 OpenGL 要简单很多，妙不可言。(￣▽￣)"**
OpenGL 需要图形学的知识储备，OpenCL 不太需要。

[OpenCL 2.0 异构计算 \[第三版 \] （Heterogeneous Computing with OpenCL 2.0）](https://www.bookstack.cn/read/Heterogeneous-Computing-with-OpenCL-2.0/README.md)

OpenCL 是一个异构编程架构，其管理者是非盈利技术组织 **Khronos Group** 。OpenCL 是一个应用开发框架，在其框架下开发的应用，能够在不同的硬件供应商的设备上运行。
* 第一版的 OpenCL (1.0) 标准在 2008 年正式发布，并出现在苹果 Mac OSX 雪豹系统当中。
* 2009 年，AMD 宣布其旗下的显卡支持 OpenCL 。IBM 也在该年宣布，其 XL 编译器在 Power 架构的处理器下支持 OpenCL 。
* 2010 年， **Khronos Group** 发布了 OpenCL 1.1 标准。
* 2011 年，发布了 OpenCL 1.2 标准。本书的第一版介绍了很多 OpenCL 1.2 的特性。
* 2013 年， **Khronos Group** 发布了 OpenCL 2.0 标准。
* OpenCL 3.0 处于最终模式（2020-09-30）。 OpenCL 1.2 是强制性的。所有 OpenCL 2.x 模块和新的 3.0 模块都是可选的。新的首选语言是具有许多 C++ 17 功能的 OpenCL 的 C++。

OpenCL 2.0 较大的改变有如下内容：

* 共享虚拟内存 —— 主机和设备端可以共享复杂数据结构指针，比如：树和链表；以减少花在数据结构转换上的精力。
* 动态并行 —— 可以在不用主机代码参与的情况下，进行内核的加载，为的就是减小加载内核所产生的瓶颈。
* 统一地址空间 —— 这样同样的函数就可以处理 GPU 和 CPU 上的数据，以减少编程的难度。
* C++ 原子操作 —— 工作项可以跨越工作组共享数据和设备，可以让更多的算法使用 OpenCL 实现。

**<font color="red">OpenCL 1.2 是支持的最广泛的版本，我采用了这个版本。</font>**


## OpenCL 主机端内存模型

讨论 OpenCL 主机端的内存模型，包括资源和内存管理。

图像对象就有些不同，其数据的布局或存放方式在硬件上进行过一些优化，这样指针就很难直接一个一个的访问对应的数据，并且硬件上的数据布局方式对于开发者来说是不可见的。这样，内核端只能使用内置函数对图像对象进行访问。因为 GPU 设计之初就是为了处理图形任务，所以 GPU 对图像数据访问效率已有较高优化。图像有三个优势：
1. GPU 上的层级缓存和数据流结构就是为了优化访问图像类型数组所准备
2. GPU 驱动会在硬件层面上优化图像数据的排布，从而提升访问图像数据的效率，尤其是二维图像模式
3. 硬件支持图像是一个很复杂的数据访问过程，在这个过程中硬件会将一些存储的数据进行压缩

图像对象和数组对象最大的区别，就是图像对象支持的格式。图像格式包括通道序和通道类型。
通道顺序定义了有多少通道需要使用 —— 例如，CL_RGB，CL_R 或 CL_ARGB。通道类型就是要选择通道内数据存储的格式，从 CL_FLOAT 到充分利用内存的 CL_UNORM_SHORT_565（其将一个 16 比特字打包后放入内存）。当内核代码要访问这些数据时，读取到的数据结果都上转换成标准的 OpenCL C 类型数据。图像格式支持的列表可以通过 clGetSupportedImageFormats() 获取。


## 异构系统下解析 OpenCL

讨论 OpenCL 在三种完全不同的异构平台上的表现，这三个异构平台包括：
1. AMD FX-8350 CPU
2. AMD Radeon R9 290X GPU
3. AMD A10-7850K APU。

OpenCL C 内核语言也实现了 C 语言中著名的 printf() 函数。printf() 函数也可以用来进行调试，这种调试方式对于 C/C++ 开发者来说并不陌生。


## API 实践


### clCreateBuffer

<https://blog.csdn.net/breakawayroad/article/details/9003632>

GPU 内存可以虚拟化，驱动程序将在 / 不需要时从 GPU 交换内存。

CL_DEVICE_GLOBAL_MEM_SIZE
CL_DEVICE_MAX_MEM_ALLOC_SIZE


### OpenCL 中三种内存创建 image 的效率对比

<https://www.cnblogs.com/willhua/p/10123398.html>

同时，clEnqueueUnmapMemObject 和 memcpy 都很快，耗时分别为 0.015ms 和 0.0004ms 左右。
从测量结果来看，使用 ION 的方式，在各项速度上都是占优的。使用 OpenCL API 也比较接近。而使用 CL_MEM_USE_HOST_PTR 则会获得比较差的效果。


### GPU 优化技术 - OpenCL 运行时 API 介绍

<https://aijishu.com/a/1060000000293412>

这里的文档都不错：
<https://deepinout.com/opencl/opencl-memory-object/opencl-image-descriptor.html>

[cl_image_format {% include relref_khronos.html %}](https://www.khronos.org/registry/OpenCL/sdk/2.0/docs/man/xhtml/cl_image_format.html)
The image format descriptor structure is defined as...


### OpenCL：图像处理基础 note

<https://www.programminghunter.com/article/1125142473/>

虽然对于图像也可以把它的像素数据当做一般的缓存数据来处理，但是如果把它当做图像来处理有如下好处：
1. 在 GPU 中，图像数据是保存在特殊的全局内存中，即纹理内存，它和一般的全局内存不相同，它是被缓存的，用于高速访问处理。GPU 中有专门支持图像读写的硬件，使用内置读写函数可以充分发挥这个优势。
2. 只要 OpenCL 支持该图像格式，那么就可以不用考虑图像格式的前提下使用读写图像数据的函数
3. 可以使用采样器来配置读取图像中数据的的方式
4. OpenCL 提供函数来获取图像相关信息，比如宽度等


### 图像插值算法总结

<https://www.cnblogs.com/laozhanghahaha/p/12580822.html>

{% include image.html url="/assets/images/220428-opencl-book/721540-20200325125319873-461037239.png" %}

<table class="tablestyle" ntablew="1:3"></table>

interpolation 选项 | 所用的插值方法
---- | ----
INTER_NEAREST | 最近邻插值
INTER_LINEAR | 双线性插值（默认设置）
INTER_AREA | 使用像素区域关系进行重采样。 它可能是图像抽取的首选方法，因为它会产生无云纹理的结果。 但是当图像缩放时，它类似于 INTER_NEAREST 方法。
INTER_CUBIC | 4x4 像素邻域的双三次插值
INTER_LANCZOS4 | 8x8 像素邻域的 Lanczos 插值


### OpenCL: C++ 实现双线性插值图像缩放

<https://blog.csdn.net/10km/article/details/50755584>

用 OpenCL 实现图像缩放代码是比较简单的，因为 OpenCL 本身就支持双线性插值
下面是 kernel 代码
从 Mali OpenCL SDK 抄来的：/samples/image_scaling/assets/image_scaling.cl


## Intel 显卡

if (!checkSuccess(clGetSupportedImageFormats(context, 0, CL_MEM_OBJECT_IMAGE2D, 0, NULL, &numberOfImageFormats)))

{% include image.html url="/assets/images/220428-opencl-book/20220428215101.png" caption="clGetSupportedImageFormats" %}



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-04-28-opencl-book.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://cjld.github.io/2013/07/31/openclasync/]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/cjld.github.io/c9fc1f9b.html" %})
- [https://developer.arm.com/documentation/101574/0100/]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/developer.arm.com/4b4706c0.html" %})
- [https://developer.nvidia.com/opencl]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/developer.nvidia.com/927d3188.html" %})
- [https://www.bookstack.cn/read/Heterogeneous-Computing-with-OpenCL-2.0/README.md]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/www.bookstack.cn/1229ec09.html" %})
- [https://blog.csdn.net/breakawayroad/article/details/9003632]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/blog.csdn.net/eac3a1b2.html" %})
- [https://www.cnblogs.com/willhua/p/10123398.html]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/www.cnblogs.com/d261be41.html" %})
- [https://aijishu.com/a/1060000000293412]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/aijishu.com/92e880be.html" %})
- [https://deepinout.com/opencl/opencl-memory-object/opencl-image-descriptor.html]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/deepinout.com/21c7c698.html" %})
- [https://www.khronos.org/registry/OpenCL/sdk/2.0/docs/man/xhtml/cl_image_format.html]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/www.khronos.org/93ba8e59.html" %})
- [https://www.programminghunter.com/article/1125142473/]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/www.programminghunter.com/2b552fde.html" %})
- [https://www.cnblogs.com/laozhanghahaha/p/12580822.html]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/www.cnblogs.com/29fd4c83.html" %})
- [https://blog.csdn.net/10km/article/details/50755584]({% include relrefx.html url="/backup/2022-04-28-opencl-book.md/blog.csdn.net/23f8c35b.html" %})
