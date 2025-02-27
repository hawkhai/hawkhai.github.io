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

穿梭在 App Store 下载就可以
{% include image.html url="/assets/images/240821-vmware-macos/20241206-111232.jpg" %}


### VM 虚拟机黑苹果速度优化，VMware 安装 macOS 卡顿解决办法

<https://www.dhzy.fun/archives/4321.html>


### 虚拟机设置优化

1、由于 VM 虚拟机是以文件的形势存储，所以在运行时就非常吃 IO，也就是存储速度，那将虚拟机位置选在固态硬盘所在的磁盘就很重要，大部分人的固态硬盘都会用来安装系统，也就是 c 盘。同时由于虚拟机是文件的形式，所以即使是已经开始使用的虚拟机也可以很方便的通过复制黏贴转移到任何地方，这才有了大海制作的 VM 虚拟机黑苹果一键安装版。
{% include image.html url="/assets/images/240821-vmware-macos/31e9f0b28e65d73.jpg" %}

当然你会担心几十乃至上百 GB 的虚拟机会把固态硬盘占满，但实际上虚拟机只有在实际用到存储空间时才会占用实际空间。也就是说虽然你将虚拟机大小设置为 80GB，但只要不勾选＂立即分配所有磁盘空间＂，系统一开始也只会占用 10 多个 GB，80GB 只是该虚拟机占用空间的上限。为保证存储效率，应选择“将虚拟磁盘存储为单个文件”。

{% include image.html url="/assets/images/240821-vmware-macos/9ec9581095f32fe.jpg" %}

2、在虚拟机设置中，让处理器和内存尽可能的高，会提升一些性能，但这个东西要根据自己的电脑硬件量力而行，大海一般给虚拟机设置 4 核 8G，设置完别忘了点击确定。
{% include image.html url="/assets/images/240821-vmware-macos/f7e727e1e46230c.jpg" %}
3、在虚拟机设置→选项→高级中，抓取输入内容为高，收集调试信息为无，勾选“禁用内存页面调整”和“为启用了Hyper-v的主机禁用侧通道缓解”，不勾选“定期记录虚拟机进度”，设置完别忘了点击确定。
{% include image.html url="/assets/images/240821-vmware-macos/8dfd37ac4a386cd.jpg" %}


### 苹果系统设置

1、系统左上角苹果图标→系统偏好设置→辅助功能→显示，勾选“减弱动态效果”“减少透明度”和“无需用颜色区分”。
{% include image.html url="/assets/images/240821-vmware-macos/bc04f2ce4bc9418.jpg" %}
2、依旧是在系统偏好设置→程序坞，最小化窗口时使用“缩放效果”，取消勾选“弹跳打开应用程序”。
{% include image.html url="/assets/images/240821-vmware-macos/1325873ca34c5b9.jpg" %}
3、依旧是在系统偏好设置→扩展，挨个点击左侧目录，将不需要的扩展全部去掉勾选。
{% include image.html url="/assets/images/240821-vmware-macos/b8a6d1638db4b20.jpg" %}
4、依旧是在系统偏好设置→用户与群组→登录项，选择用户，左下角开锁后，去掉不需要的登录项。
{% include image.html url="/assets/images/240821-vmware-macos/201661a83a4d8b7.jpg" %}

5、VMware Tools 的安装可以让虚拟机分辨率自适应，文件和剪贴板也可以直接与母鸡共享，属于使用必装，但安装后需要重新设置分辨率，否则画面会一直处于一个比较大的状态，影响体验，同时会有卡顿。
VMware Tools 的安装教程：<https://www.dhzy.fun/archives/4366.html>
依旧是在系统偏好设置→显示器→缩放，分辨率选择带有 (HiDPI) 的选项，然后勾选好，画面中的窗口会放大或者缩小。
{% include image.html url="/assets/images/240821-vmware-macos/97cfb3a9f86b06f.jpg" %}

设置成功后拖动虚拟机窗口边界，虚拟机画面会根据虚拟机窗口大小进行自适应，但不会小于设置分辨率。系统提示“系统偏好设置”正在尝试解锁“安全性与隐私”偏好设置时，输入密码，解锁，将 vmware-tools-daemon 打钩即可。
{% include image.html url="/assets/images/240821-vmware-macos/7ffdd55b403f4b4.jpg" %}


### 最重要的一个更改

{% include image.html url="/assets/images/240821-vmware-macos/20250113151715.png" %}

在进行了一系列设置后，macOS 系统会变得流畅一些，希望你能拥有更好的体验，再见。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-08-21-vmware-macos.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/weixin_48830465/article/details/125050097]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/blog.csdn.net/a0eacf99.html" %})
- [https://pan.baidu.com/s/1iNyVdvzT2iP3Lc6sWM_UVQ]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/pan.baidu.com/244321b6.html" %})
- [https://pan.baidu.com/s/1JJXw0K6l1R2ljLkoKeDUBA]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/pan.baidu.com/f78ee94e.html" %})
- [https://pan.baidu.com/s/12yekpzlrJQZYS_QNS9nN_A]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/pan.baidu.com/de95d1c1.html" %})
- [https://cloud.189.cn/web/share?code=3Eb2Ir7N3QZj]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/cloud.189.cn/cf4b44fe.html" %})
- [https://blog.csdn.net/hubing_hust/article/details/128596690]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/blog.csdn.net/85d83701.html" %})
- [https://www.dhzy.fun/archives/4321.html]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/www.dhzy.fun/e7293f44.html" %})
- [https://www.dhzy.fun/archives/4366.html]({% include relrefx.html url="/backup/2024-08-21-vmware-macos.md/www.dhzy.fun/8df1f17d.html" %})
