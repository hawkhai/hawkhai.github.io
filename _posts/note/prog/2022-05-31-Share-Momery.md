---
layout: post
title: "编程与调试 C++ -- 共享内存，同步机制"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

[^_^]: blog.csdn.net/shuilan0066/article/details/87979315


## 共享内存

Windows 下进程的地址空间在逻辑上是相互隔离的，但在物理上却是重叠的。所谓的重叠是指同一块内存区域可能被多个进程同时使用。
共享内存，各个进程可以共享同一块物理内存，进程可以直接读写内存，不需要数据拷贝。
由于多个进程共享一块内存，所以也需要同步机制。


## 实现步骤


### 本进程创建

1. 创建内存映射文件对象 CreateFileMapping，
    Windows 即在物理内存申请一块指定大小的内存区域，返回文件映射对象的句柄 hMap。
2. 将内存对象映射在进程地址空间 MapViewOfFile。


### 其它进程访问

其它进程访问这个内存对象时，
1. OpenFileMapping 获取对象句柄。
2. 调用 MapViewOfFile 映射在自己的进程空间。

这样，同一块内存块被映射到了不同的进程空间，从而达到多个进程共享同一个内存块的目的。


## 简单示例


## 同步机制

主进程负责写：

这时，需要等待其它进程读操作完毕后，才能写
而且，一旦主进程开始写，其它进程不能再去写

其它进程访问

映射内存

全局事件

读取这部分内存，

读取时，先确保主进程不在同时写


## Inter Computer Read/Write File Lock

https://www.codeproject.com/Articles/49670/Inter-Computer-Read-Write-File-Lock


## 参考资料

http://www.cnblogs.com/dongsheng/p/4460944.html

http://blog.chinaunix.net/uid-26833883-id-3230564.html



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-05-31-Share-Momery.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.codeproject.com/Articles/49670/Inter-Computer-Read-Write-File-Lock]({% include relrefx.html url="/backup/2022-05-31-Share-Momery.md/www.codeproject.com/5204d1cf.html" %})
- [http://www.cnblogs.com/dongsheng/p/4460944.html]({% include relrefx.html url="/backup/2022-05-31-Share-Momery.md/www.cnblogs.com/44de51f5.html" %})
- [http://blog.chinaunix.net/uid-26833883-id-3230564.html]({% include relrefx.html url="/backup/2022-05-31-Share-Momery.md/blog.chinaunix.net/28af4862.html" %})
