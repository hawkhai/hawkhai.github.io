---
layout: post
title: "编程与调试 C++ -- 一些奇奇怪怪的编程知识"
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


## ssdeep、tlsh、vhash、mmdthash

* 准确率 ACC
* 召回率 REC
* 精确率 PRE

mmdthash
ssdeep
vhash
tlsh


## quic 协议

Quic 全称 quick udp internet connection，“快速 UDP 互联网连接”，（和英文 quick 谐音，简称“快”）是由 google 提出的使用 udp 进行多路并发传输的协议。
一种基于 UDP 的传输协议，用于提升网络加载速度，在弱网环境下表现较好。
Quic 相比现在广泛应用的 http2+tcp+tls 协议有如下优势：

* 减少了 TCP 三次握手及 TLS 握手时间。
* 改进的拥塞控制。
* 避免队头阻塞的多路复用。
* 连接迁移。
* 前向冗余纠错。


## 进程注入

进程注入的方法非常之多，很多与 DLL 注入有关，比如注册表（Image File Execution Options）、DLL 劫持、输入法、COM、LSP 劫持（LayerService Provider，与 winsock 有关）

除了 DLL 注入，还有 shellcode 注入，因为 shellcode 更小，所以 shellcode 的使用也更加多样。

2017 年，在黑客大会上 Eugene Kogan 和 Tal Liberman 又分享了更加隐蔽和特别的方法，比如 Process Doppelganging。


## 基于 LSTM 的二进制代码相似性检测


## 逆向某平台分析过程指导

[note {% include relref_weixin.html %}](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458434317&idx=1&sn=0a0f3bcee1cdd99c2f2db1a2fd899619&chksm=b18f8b8786f802919884f0682fe9fb38c0971e3e7de732ec11f35cbd994b87fc12c3e758b344&scene=178&cur_album_id=2293635948628279298)
扔到 ida 看导出函数发现是 jni 动态注册没找到 getServerApi() 这个方法，接下来使用 unidbg 进行分析 call_jni_onload 后找到偏移地址 0x12795。

在 ida 中 G 跳转到偏移地址。

查看 sub_4DF0 函数 F5 生成伪代码。


## 逆向角度看 C++ 部分特性

[note {% include relref_weixin.html %}](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458436558&idx=1&sn=770b20ad3eb60dbb20c83a59f83c8b48&chksm=b18ff34486f87a52514c67a59d4702e7f2ffc59b9a13f8cd4718b7ec28b79c38ae304eb4167c&scene=178&cur_album_id=2293635948628279298)

[start24. {% include relref_weixin.html %}](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5NTc2MDYxMw==&action=getalbum&album_id=2293635948628279298&scene=173&from_msgid=2458436731&from_itemidx=1&count=3&nolastread=1)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-05-24-snowflake-notes.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458434317&idx=1&sn=0a0f3bcee1cdd99c2f2db1a2fd899619&chksm=b18f8b8786f802919884f0682fe9fb38c0971e3e7de732ec11f35cbd994b87fc12c3e758b344&scene=178&cur_album_id=2293635948628279298]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/mp.weixin.qq.com/6eb26110.html" %})
- [https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458436558&idx=1&sn=770b20ad3eb60dbb20c83a59f83c8b48&chksm=b18ff34486f87a52514c67a59d4702e7f2ffc59b9a13f8cd4718b7ec28b79c38ae304eb4167c&scene=178&cur_album_id=2293635948628279298]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/mp.weixin.qq.com/0075049f.html" %})
- [https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5NTc2MDYxMw==&action=getalbum&album_id=2293635948628279298&scene=173&from_msgid=2458436731&from_itemidx=1&count=3&nolastread=1]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/mp.weixin.qq.com/78332679.html" %})