---
layout: post
title: "编程与调试 -- VMware 虚拟机安装 macOS 10.15"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
l2dwidget: true
---

[VMware 虚拟机安装 macOS 10.15（教 unlock，调整分辨率） {% include relref_csdn.html %}](https://blog.csdn.net/weixin_48830465/article/details/125050097)


## 下载并使用 Unlock 工具

unlocker-3.0.3.zip

百度 w 链接：<https://pan.baidu.com/s/1iNyVdvzT2iP3Lc6sWM_UVQ>
提取码：988a

解压缩，拷贝到 VMware 目录，如 E:\VMware15.5


## 下载 darwin.iso 和 darwinPre15.iso

把 darwin.iso 和 darwinPre15.iso 放到 VMware 目录，如 E:\VMware15.5

百度网盘链接：<https://pan.baidu.com/s/1JJXw0K6l1R2ljLkoKeDUBA>
提取码：5s2j

如下图两个文件，如果链接失效百度搜索这两个文件名字即可。


## 管理员权限运行 VMware 目录的两个程序

先运行 unlocker.exe，再运行 win-install.cmd

执行这两个文件很快就完成了，我也就花了几分钟。

到此 VMware 即可支持安装 macOS 了。


## 准备 macOS 镜像文件

有 .dmg、.iso、.cdr 后缀的，我使用的是 .cdr 镜像文件，另外两个可行性有待测试。

百度网盘链接：<https://pan.baidu.com/s/12yekpzlrJQZYS_QNS9nN_A>
提取码：e2r5

天翼云盘链接：<https://cloud.189.cn/web/share?code=3Eb2Ir7N3QZj>
访问码：qk26

启动系统，选择磁盘工具抹掉刚刚分配的 40G，为硬盘起个名。如下图。

{% include image.html url="/assets/images/240821-vmware-macos/20240822173829.png" %}

关闭磁盘工具，安装系统，剩下的过程随自己选择即可。


## 使用 VMware 安装 macOS

除了分配硬盘，不要太小了，我分配了 40G。
安装 VMwareTools，修改分辨率。

{% include image.html url="/assets/images/240821-vmware-macos/20240822180734.png" %}


## 另外的版本

[如何在 windows 上使用 VMware 安装 macOS 虚拟机 {% include relref_csdn.html %}](https://blog.csdn.net/hubing_hust/article/details/128596690)

unlocker424.zip



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-08-21-vmware-macos.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/weixin_48830465/article/details/125050097]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/blog.csdn.net/a0eacf99.html" %})
- [https://pan.baidu.com/s/1iNyVdvzT2iP3Lc6sWM_UVQ]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/pan.baidu.com/244321b6.html" %})
- [https://pan.baidu.com/s/1JJXw0K6l1R2ljLkoKeDUBA]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/pan.baidu.com/f78ee94e.html" %})
- [https://pan.baidu.com/s/12yekpzlrJQZYS_QNS9nN_A]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/pan.baidu.com/de95d1c1.html" %})
- [https://cloud.189.cn/web/share?code=3Eb2Ir7N3QZj]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/cloud.189.cn/cf4b44fe.html" %})
- [https://blog.csdn.net/hubing_hust/article/details/128596690]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/blog.csdn.net/85d83701.html" %})
