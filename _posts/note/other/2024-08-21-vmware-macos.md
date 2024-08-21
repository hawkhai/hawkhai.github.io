---
layout: post
title: "编程与调试 -- VMware虚拟机安装macOS 10.15"
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

[VMware虚拟机安装macOS 10.15（教unlock，调整分辨率） csdn](https://blog.csdn.net/weixin_48830465/article/details/125050097)



## 下载并使用Unlock工具

unlocker-3.0.3.zip

百度w链接：https://pan.baidu.com/s/1iNyVdvzT2iP3Lc6sWM_UVQ 
提取码：988a

解压缩，拷贝到VMware目录，如 E:\VMware15.5


## 下载darwin.iso和darwinPre15.iso

把darwin.iso和darwinPre15.iso放到VMware目录，如E:\VMware15.5

百度网盘链接：https://pan.baidu.com/s/1JJXw0K6l1R2ljLkoKeDUBA 
提取码：5s2j

如下图两个文件，如果链接失效百度搜索这两个文件名字即可。

## 管理员权限运行VMware目录的两个程序

先运行unlocker.exe，再运行win-install.cmd

执行这两个文件很快就完成了，我也就花了几分钟。

到此VMware即可支持安装macOS了。



## 准备macOS镜像文件

有.dmg、.iso、.cdr后缀的，我使用的是.cdr镜像文件，另外两个可行性有待测试。

百度网盘链接：https://pan.baidu.com/s/12yekpzlrJQZYS_QNS9nN_A 
提取码：e2r5

天翼云盘链接：https://cloud.189.cn/web/share?code=3Eb2Ir7N3QZj
访问码：qk26


## 使用VMware安装macOS

除了分配硬盘，不要太小了，我分配了40G。
安装VMwareTools，修改分辨率。








