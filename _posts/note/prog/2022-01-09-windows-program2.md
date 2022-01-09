---
layout: post
title: "编程与调试 -- Windows 编程知识点（文档整理）2/2 逆向 & 驱动"
author: yqh
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid: true
glslcanvas:
codeprint:
cluster: "Windows 编程知识点"
---


## 浅析逆向分析


### ELF(linux) 和 PE(windows)

{% include image.html url="/assets/images/220109-windows-program2/img_0d335cb525dc4ed2bece08855aa251e1.png" %}

{% include image.html url="/assets/images/220109-windows-program2/img_cba9aa9667b44125934478368847a72f.png" caption="PE 格式总览" %}


### PE 头

* PE 结构相关头文件
    * Windows-sdk 下 \include\winnt.h
* 关键结构
    * DosHeader
    * NtHeader
        * FileHeader
        * OptionalHeader
            * DataDirectory
    * SectionTable


### DOS 头

* 作用
    * 文件头，兼容 DOS 模式
    * DOS 下默认显示 This program must be run under win32
* 重要字段
    * e_magic 标记 MZ(4D5A)，MS-DOS 创建者 Mark Zbikowski
    * e_lfanew 指向真正的 PEHeader

{% include image.html url="/assets/images/220109-windows-program2/img_dcbba4e657d14ddb89907b51285f162a.png" caption="DOS 头" %}


### FileHeader

* 作用
    * 描述 PE 基础信息
* 重要字段
    * Machine
    * NumberOfSections，节数量
    * SizeOfOptionalHeader，可选头大小
    * Characteristics，PE 属性


### OptionalHeader

* 作用
    * 描述 PE 详细信息
* 重要字段
    * Magic
        * PE32/64
    * Subsystem
        * Console/win
    * DataDirectory
    * AddressOfEntryPoint(OEP)
        * 入口点，编译器特征
        * 劫持修改（感染型）
        * Main 和 OEP

{% include image.html url="/assets/images/220109-windows-program2/img_ac2054f4819042acaa386ec63e141433.png" caption="main 和 OEP" %}

* main 是不是第一行执行的代码？
    * OEP(crt/src/cr0.c)
        * mainCRTStartup/WinMainCRTStartup
    * main
        * main/WinMain
* 编译运行过程
    * 编译链接过程 ENTRY 选项指定入口函数，默认为 main
    * OEP 指定为 libc.lib 中的 mainCRTStartup(console)
    * mainCRTStartup 完成初始化后调用 main
* 备注
    * 文件特征注意


### DataDirectory

* 作用
    * 导入、导出、资源等关键结构的总索引
* 介绍
    * DataDirectory 位于 OptionalHeader 末尾
    * 共 16 组，每组指定一个重要数据结构
* 重要字段
    * 导出表，导出函数
    * 导入表，引用外部 DLL 信息
    * 调试表，PDB 等调试信息
    * 资源表，图标，对话框，版本信息等
    * 安全表，数字签名


### SectionTable

* 作用
    * 除文件头外的代码、数据、资源分段存储索引
    * 便于系统安全性设置
* 重要字段
    * VirtualAddress，节区在内存中的偏移
    * PointerToRawData，节区在文件偏移
    * Characteristics，描述该节的 rwx 属性

{% include image.html url="/assets/images/220109-windows-program2/img_49bc33aaa7dd48cea48bb76232346316.png" caption="源码与 PE" %}


### PE 文件映射

{% include image.html url="/assets/images/220109-windows-program2/img_27b4d651d500450fad5e4943189d4289.png" %}

* PE-Section
    * .text，二进制代码，x 属性
    * .data，全局变量、字符串、预定义数据，rw 属性
    * .rsrc，资源图标、对话框资源、版本信息等，r 属性
* TIPS
    * 对齐粒度
        * 0x200->0x1000
    * 节名无实质意义，不同的编译器喜好不同
        * .text(vc)
        * .CODE(delphi)
* 节空隙
    * 恶意代码寄生

{% include image.html url="/assets/images/220109-windows-program2/img_6f9d487018ff4e17a28fa22b2be5c3b3.png" caption="感染型病毒" %}

ntcore CFF-Explorer


### x86 指令编码

反汇编过程即二进制转汇编助记符，参考 intel 指令集手册 X86 为变长指令（灵活），arm 为定长指令（高效）[4G 寻址问题]

{% include image.html url="/assets/images/220109-windows-program2/img_0a12e635211a4c2686b7909f1665f1a8.png" caption="x86 指令编码" %}


### 指令编码

* 作用
    * 实现虚拟机（bochs) / 沙箱
        * 精准控制每个指令执行，OS 开发
    * 恶意代码仿真执行
        * 对抗混淆、加密
    * 反汇编，机读指令转人读指令
        * 安全必备
    * vulnerability/shellcode/inline-hook
        * 核心安全分析、防御

{% include image.html url="/assets/images/220109-windows-program2/img_0930cb7fa94b43ea813ba24a5eb36059.png" %}


### 汇编简介

{% include image.html url="/assets/images/220109-windows-program2/img_3301cf6f12aa4c26b69156794495c25f.png" %}

* 指令分类
    * 计算
        * Add/adc/inc/sub/mul/…
    * 读写
        * Mov/lea/push/pop/xchg/…
    * 控制
        * Jmp/jcc/loop/call/ret/…
    * 其他
        * clc/stc/cld/cupid/…
* 备注
    * 仅寄存器可参与计算
    * 地址间不能直接操作


### 反汇编 — call stack

{% include image.html url="/assets/images/220109-windows-program2/img_1a01faaae0ea411a8a3e09f42dbecc1a.png" %}
{% include image.html url="/assets/images/220109-windows-program2/img_72d1459ae6b94c52b26c98ba8ab1551d.png" %}

* 寄存器
    * Ebp 指向当前函数栈基址
        * [ebp+xx] 参数 / [ebp-xx] 变量
    * Esp 指向当前函数栈顶
* 进入 / 退出函数时构建和释放栈帧
    * 仅改变 ebp/esp 即可
    * 返回地址
* 如何平衡堆栈
    * 根据调用类型


### 反汇编案例

{% include image.html url="/assets/images/220109-windows-program2/img_c7ea0bdfdc0e4fa493f314960985b3a2.png" %}
{% include image.html url="/assets/images/220109-windows-program2/img_5a7df3420fe04996abe2773d7fde2bdb.png" %}


### 动态调试 & 静态分析

TIPS
* 资源 DLLFindResourceA/W
    * LoadStringA/W(user32.dll)
* 调用栈结构
* Ctrl+F9 执行到返回
* 关注前置跳转
* 分析建立在开发 / 系统的理解之上

多层封装
异步调用
动态加载
加密解密
自定义接口
壳
反调试


### 代码防护

* 关键函数 / 文件采用无意义名字
* 避免明文存储，配置文件 hash 化
* 尽量减少无用提示
* 无关代码注释删除



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-01-09-windows-program2.md.js" %}'></script></p>
