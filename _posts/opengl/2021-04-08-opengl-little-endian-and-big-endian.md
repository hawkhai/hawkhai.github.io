---
layout: post
title: "图形学笔记 -- Little-Endian 和 Big-Endian （大小字节序、大小端）"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

这个问题还是很麻烦的。
* 文件存储，一般是 大端模式，二进制查看更直观。
* Irrlicht 内存。ECF_A1R5G5B5 ECF_R5G6B5 ECF_A8R8G8B8 可能封装成 short，int 之类的，就是小端模式，方便运算速度，位运算更直观。
    * ECF_R8G8B8 # 这个是大端存储的，蛋疼。因为是 3 个 8，没法封装加速运算，数组格式查看更直观。
* 然后是传递给 GPU glTexImage2D(format, type)。
    * GPU 内部格式主要包含 GL_ALPHA, GL_RGB, GL_RGBA 等。
    * 传给 GPU 的格式主要包含：GL_RGB, GL_RGBA, GL_BGR_EXT, GL_BGRA_EXT, GL_ABGR_EXT, 等等。
    * 传给 GPU 的格式 type 还包含：GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT_5_5_5_1, GL_UNSIGNED_SHORT_5_6_5, GL_UNSIGNED_INT_8_8_8_8 外加各自的反转：
        GL_UNSIGNED_SHORT_1_5_5_5_REV, GL_UNSIGNED_INT_8_8_8_8_REV, 等等。
    * 定义了 format 是 GL_RGB，同时定义 type 是 GL_UNSIGNED_SHORT_5_6_5_REV，那么在解析的时候等同于：定义 format 是 GL_BGR type 是 GL_UNSIGNED_SHORT_5_6_5。
* 上面这些情况全部各种组合、互转，一个 3D 引擎里面的格式支持，就眼花缭乱了。

{% include image.html url="/assets/images/210408-opengl-little-endian-an~c1/20210408174115.png" caption="让人头疼的颜色处理" %}


## 概念

endian：字节存储顺序，端模式。

Little-Endian 和 Big-Endian 表示的是计算机字节顺序，
所谓的字节顺序指的是长度跨越多个字节的数据的存放形式（若只有一个字节则不需考虑字节序的问题）。
对于整型、长整型等数据类型，Big endian 认为第一个字节是最高位字节（按照从低地址到高地址的顺序存放数据的高位字节到低位字节）；
而 Little endian 则相反，它认为第一个字节是最低位字节（按照从低地址到高地址的顺序存放数据的低位字节到高位字节）。

大部分人在实际的开发中都很少会直接和字节序打交道。唯有在跨平台以及网络程序中字节序才是一个应该被考虑的问题。
TCP/IP 各层协议将字节序定义为 Big-Endian，因此 TCP/IP 协议中使用的字节序通常称之为网络字节序。


## 举例

例如，假设从内存地址 0x0000 开始有以下数据：0x12 0x34 0xab 0xcd。
如果我们去读取一个地址为 0x0000 的四个字节变量，若字节序为 big-endian，则读出结果为 0x1234abcd；
若字节序位 little-endian，则读出结果为 0xcdab3412。

* 采用 Little-Endian 的 操作系统：FreeBSD, Linux, Windows x86 的机器；
* 采 Big-Endian 的操作系统：MAC OS, ARM, Alpha，摩托罗拉的 PowerPC, Network 中的变量，Java 语言。


## Code

```cpp
bool IsBig_Endian()
{
    unsigned short test = 0x1122;
    if (*( (unsigned char*) &test ) == 0x11)
        return TRUE;
    else
        return FALSE; // windows
}
```


## 应用

```cpp
//! Converts a 32bit (A8R8G8B8) color to a 16bit A1R5G5B5 color
inline u16 A8R8G8B8toA1R5G5B5(u32 color)
{
    return (u16)(( color & 0x80000000) >> 16|
        ( color & 0x00F80000) >> 9 |
        ( color & 0x0000F800) >> 6 |
        ( color & 0x000000F8) >> 3);
}

void CColorConverter::convert_R8G8B8A8toA1B5G5R5(const void* sP, s32 sN, void* dP)
{
    u8 * sB = (u8 *)sP;
    u16* dB = (u16*)dP;

    for (s32 x = 0; x < sN; ++x)
    {
        s32 r = sB[3] >> 3; // Little-Endian
        s32 g = sB[2] >> 3;
        s32 b = sB[1] >> 3;
        s32 a = sB[0] >> 3;

        dB[0] = (a << 15) | (b << 10) | (g << 5) | (r);

        sB += 4;
        dB += 1;
    }
}

void CColorConverter::convert_A8R8G8B8toR5G6B5(const void* sP, s32 sN, void* dP)
{
    u8 * sB = (u8 *)sP;
    u16* dB = (u16*)dP;

    for (s32 x = 0; x < sN; ++x)
    {
        s32 r = sB[2] >> 3;
        s32 g = sB[1] >> 2;
        s32 b = sB[0] >> 3;

        dB[0] = (r << 11) | (g << 5) | (b);

        sB += 4;
        dB += 1;
    }
}

void CColorConverter::convert_R8G8B8toR8G8B8A8(const void* sP, s32 sN, void* dP)
{
    u8*  sB = (u8*)sP;
    u32* dB = (u32*)dP;

    for (s32 x = 0; x < sN; ++x)
    {
        *dB = 0x000000ff | (sB[0] << 24) | (sB[1] << 16) | (sB[2] << 8);

        sB += 3;
        ++dB;
    }
}
```


## Irrlicht

吭人的 Irrlicht。

enum ECOLOR_FORMAT
NOTE: Byte order in memory is usually flipped (it's probably correct in bitmap files, but flipped on reading).
So for example ECF_A8R8G8B8 is BGRA in memory same as in DX9's D3DFMT_A8R8G8B8 format.

* ECF_A1R5G5B5 # Little-Endian
* ECF_R5G6B5 # Little-Endian
* ECF_R8G8B8 # 这个是大端存储的，蛋疼。
* ECF_A8R8G8B8 # Warning: This tends to be BGRA in memory (it's ARGB on file, but with usual big-endian memory it's flipped)
    * 内存里面为了速度，是小端存储的，存储到文件是大端的。小端的根本目的，可以用 int 加速运算。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-08-opengl-little-endian-and-big-endian.md.js" %}'></script></p>
