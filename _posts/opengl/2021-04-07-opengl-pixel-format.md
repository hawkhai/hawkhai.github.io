---
layout: post
title: "图形学笔记 -- OpenGL 像素格式 与 图像格式"
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

像素数据一般会在 CPU 和 GPU 中进行传输，如果传输过程是从 GPU 到 CPU 一般称为压包（pack），从 CPU 到 GPU 的传输称为解包（unpack）。
[glTexImage2D](https://docs.microsoft.com/en-us/windows/win32/opengl/glteximage2d)

```cpp
WINGDIAPI void APIENTRY glTexImage2D (
    GLenum target,
    GLint level,
    GLint internalformat, // OpenGL 内部存储格式
    GLsizei width,
    GLsizei height,
    GLint border,
    GLenum format, GLenum type, // 定义了 pixels 内存结构
    const GLvoid *pixels
);
```

* internalformat 是指 OpenGL 内部存储这个纹理时所用的格式，同时指定了哪些分量以及每个分量对应的 bit 数，可以理解为显存中存储的格式，形如 GL_RGB, GL_RGB32F, GL_COMPRESSED_RGB。
    格式形如 GL_R32F，表示这个纹理只有一个分量，分量为 32 位浮点数，OpenGL 网站上有详细说明。
    值得注意的是，如果该格式为 GL_RGB，GL_RGBA，GL_DEPTH_COMPONENT 等这种只指定分量个数的，
    那么 OpenGL 中会自动对每个分量进行截断（clamp），保证其范围为 [0, 1]。
    因此如果不需要 OpenGL 自动截断，则应指定 internalformat 为 GL_RGB16F 类似的格式。
* format 和 type 指定的是 client 内存中存储的格式，也就是 data 指针中的所存放的 texture 的格式。
    * format 形如 GL_RG, GL_RED 等，即指定哪些颜色分量。
* type 是像素数据的 bit depth，包括 GL_UNSIGNED_BYTE，GL_FLOAT，GL_UNSIGNED_SHORT_5_6_5 等。

类似的，glReadPixels() 函数中也有一个 format 和 type，和上述的 type, format 含义相同，
即按照指定的格式从 OpenGL 显存内部读出到 buffer 中，也就是 pack 操作的格式。

[glTexImage2D 中 format internalformat type 参数的含义 {% include relref_csdn.html %}](https://blog.csdn.net/w450468524/article/details/51649065)
[GL_RGBA8 & GL_RGBA 的探讨](https://cainiaojiaocheng.com/questions/6636847/odd-results-using-glteximage2d)

glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, 256, 256, 0, GL_RGBA, GL_UNSIGNED_BYTE, (GLvoid*)data);
首先是积极的事情。 您使用内部尺寸格式（GL_RGBA8，而不是 GL_RGBA）。
这是非常好的，继续这样做。 您对内部格式（GL_RGBA8）和像素传输格式（GL_RGBA）之间的区别有清楚的了解。 这也很好。

**internalformat**

The number of color components in the texture. Must be 1, 2, 3, or 4, or one of the following symbolic constants: GL_ALPHA, GL_ALPHA4, GL_ALPHA8, GL_ALPHA12, GL_ALPHA16, GL_LUMINANCE, GL_LUMINANCE4, GL_LUMINANCE8, GL_LUMINANCE12, GL_LUMINANCE16, GL_LUMINANCE_ALPHA, GL_LUMINANCE4_ALPHA4, GL_LUMINANCE6_ALPHA2, GL_LUMINANCE8_ALPHA8, GL_LUMINANCE12_ALPHA4, GL_LUMINANCE12_ALPHA12, GL_LUMINANCE16_ALPHA16, GL_INTENSITY, GL_INTENSITY4, GL_INTENSITY8, GL_INTENSITY12, GL_INTENSITY16, GL_R3_G3_B2, GL_RGB, GL_RGB4, GL_RGB5, GL_RGB8, GL_RGB10, GL_RGB12, GL_RGB16, GL_RGBA, GL_RGBA2, GL_RGBA4, GL_RGB5_A1, GL_RGBA8, GL_RGB10_A2, GL_RGBA12, or GL_RGBA16.

**format**

The format of the pixel data. It can assume one of nine symbolic values.
GL_COLOR_INDEX
GL_RED
GL_GREEN
GL_BLUE
GL_ALPHA
GL_RGB
GL_RGBA
GL_BGR_EXT
GL_BGRA_EXT
GL_LUMINANCE
GL_LUMINANCE_ALPHA

The **format** (7th argument), together with the **type** argument, describes the data you pass in as the last argument.
So the **format/type** combination defines the memory layout of the data you pass in.

**internalFormat** (2nd argument) defines the format that OpenGL should use to store the data internally.

Often times, the two will be very similar. And in fact, it is beneficial to make the two formats directly compatible.
Otherwise there will be a conversion while loading the data, which can hurt performance.
Full OpenGL allows combinations that require conversions, while OpenGL ES limits the supported combinations so that conversions are not needed in most cases.

The reason GL_RGBA_INTEGER is not legal in this case that there are rules about which conversions between format and internalFormat are supported.
In this case, GL_RGBA for the internalFormat specifies a normalized format, while GL_RGBA_INTEGER for format specifies that the input consists of values that should be used as integers. There is no conversion defined between these two.

While GL_RGBA for internalFormat is still supported for backwards compatibility, sized types are generally used for internalFormat in modern versions of OpenGL. For example, if you want to store the data as an 8-bit per component RGBA image, the value for internalFormat is GL_RGBA8.

Frankly, I think there would be cleaner ways of defining these APIs. But this is just the way it works. Partly it evolved this way to maintain backwards compatibility to OpenGL versions where features were much more limited. Newer versions of OpenGL add the glTexStorage\*() entry points, which make some of this nicer because it separates the internal data allocation and the specification of the data.

格式（第 7 个参数）与类型参数一起描述了您作为最后一个参数传入的数据。因此，格式 / 类型组合定义了您传入的数据的内存布局。

internalFormat（第二个参数）定义了 OpenGL 内部存储数据时应使用的格式。

通常，两者会非常相似。实际上，使两种格式直接兼容是有益的。否则，在加载数据时会发生转换，这会损害性能。
完整的 OpenGL 允许需要转换的组合，而 OpenGL ES 限制了受支持的组合，因此在大多数情况下不需要转换。

在这种情况下，GL_RGBA_INTEGER 不合法是因为存在关于支持格式和 internalFormat 之间的转换的规则。
在这种情况下，internalFormat 的 GL_RGBA 指定规范化的格式，而 format 的 GL_RGBA_INTEGER 指定输入由应该用作整数的值组成。
两者之间没有定义转换。

虽然仍支持向内部兼容的 GL_RGBA 以实现向后兼容性，但在现代 OpenGL 版本中，大小类型通常用于 internalFormat。
例如，如果要将数据存储为每个组件 RGBA 图像 8 位，则 internalFormat 的值为 GL_RGBA8。

坦白说，我认为会有更干净的方法来定义这些 API。但这只是它的工作方式。它在某种程度上发展了这种方式，
以保持与功能受限得多的 OpenGL 版本的向后兼容性。较新版本的 OpenGL 添加了 glTexStorage\*() 入口点，

这些入口点变得更好，因为它将内部数据分配和数据规范分开了。

1. 压包操作：
    glReadpixels
    glGetTexImage
2. 解包操作：
    glTexImage*
    glTexSubImage*

定义了 format 是 GL_RGB，同时定义 type 是 GL_UNSIGNED_SHORT_5_6_5_REV，那么在解析的时候等同于：
定义 format 是 GL_BGR type 是 GL_UNSIGNED_SHORT_5_6_5。

```cpp
// ES 2.0 says internalFormat must match pixelFormat (chapter 3.7.1 in Spec).
// Doesn't mention if "match" means "equal" or some other way of matching, but
// some bug on Emscripten and browsing discussions by others lead me to believe
// it means they have to be equal. Note that this was different in OpenGL.
internalFormat = pixelFormat;
```

OpenGL:

```cpp
/* PixelFormat */
#define GL_RED                            0x1903
#define GL_GREEN                          0x1904
#define GL_BLUE                           0x1905
#define GL_ALPHA                          0x1906
#define GL_RGB                            0x1907
#define GL_RGBA                           0x1908

/* EXT_bgra pixelFormat */
#define GL_BGR_EXT                        0x80E0
#define GL_BGRA_EXT                       0x80E1

#define GL_ABGR_EXT                       0x8000 // GL_EXT_abgr
#define GL_BGRA8_EXT                      0x93A1 // 不常用

/* texture */
#define GL_ALPHA4                         0x803B
#define GL_ALPHA8                         0x803C
#define GL_ALPHA12                        0x803D
#define GL_ALPHA16                        0x803E
#define GL_R3_G3_B2                       0x2A10
#define GL_RGB4                           0x804F
#define GL_RGB5                           0x8050
#define GL_RGB8                           0x8051
#define GL_RGB10                          0x8052
#define GL_RGB12                          0x8053
#define GL_RGB16                          0x8054
#define GL_RGBA2                          0x8055
#define GL_RGBA4                          0x8056
#define GL_RGB5_A1                        0x8057
#define GL_RGBA8                          0x8058
#define GL_RGB10_A2                       0x8059
#define GL_RGBA12                         0x805A
#define GL_RGBA16                         0x805B
```

像素格式明确了 OpenGL 绘制平面的特性，如象素缓冲区是单缓冲还是双缓冲，数据是 RGBA 方式还是 Color Index 方式等。
每个 OpenGL 显示设备一般用名为 PIXELFORMATDESCRIPTOR 的结构来表示某个的像素格式，这个结构包含 26 个属性信息。
Win32 定义 PIXELFORMATDESCRIPTOR 如下所示：

```cpp
typedef struct tagPIXELFORMATDESCRIPTOR { // pfd
    WORD nSize; // nSize 是象素格式描述子结构的大小，sizeof(PIXELFORMATDESCRIPTOR) 设定其值 ;
    WORD nVersion; // nVersion 是 PIXELFORMATDESCRIPTOR 结构的版本，一般设为 1;
    DWORD dwFlags;  // dwFlags 是一组表明象素缓冲特性的标志位，如缓冲是否支持 GDI 或 OpenGL 等 ;
    BYTE iPixelType;  // iPixelType 说明象素数据类型是 RGBA 还是颜色索引 ;
    BYTE cColorBits; // cColorBits 每个颜色缓冲区中颜色位平面的数目，对颜色索引方式是缓冲区大小 ;
    BYTE cRedBits; // cRedBits 每个 RGBA 颜色缓冲区中红色位平面的数目 ;
    BYTE cRedShift; // cRedShift 每个 RGBA 颜色缓冲区中红色位平面的偏移数 ;
    BYTE cGreenBits; // cGreenBits 每个 RGBA 颜色缓冲区中绿色位平面的数目 ;
    BYTE cGreenShift; // cGreenShift 每个 RGBA 颜色缓冲区中绿色位平面的偏移数 ;
    BYTE cBlueBits; // cBlueBits 每个 RGBA 颜色缓冲区中蓝色位平面的数目 ;
    BYTE cBlueShift; // cBlueShift 每个 RGBA 颜色缓冲区中蓝色位平面的偏移数 ;
    BYTE cAlphaBits; // cAlphaBits 每个 RGBA 颜色缓冲区中 alpha 位平面的数目（保留的，现不支持）;
    BYTE cAlphaShift; // cAlphaShift 每个 RGBA 颜色缓冲区中 alpha 位平面的偏移数（保留的，现不支持）;
    BYTE cAccumBits; // cAccumBits 累加缓冲区中全部位平面的数目 ;
    BYTE cAccumRedBits; // cAccumRedBits 累加缓冲区中红色位平面的数目 ;
    BYTE cAccumGreenBits; // cAccumGreenBits 累加缓冲区中绿色位平面的数目 ;
    BYTE cAccumBlueBits; // cAccumBlueBits 累加缓冲区中蓝色位平面的数目 ;
    BYTE cAccumAlphaBits; // cAccumAlphaBits 累加缓冲区中 alpha 位平面的数目 ;
    BYTE cDepthBits; // cDepthBits Z（深度）缓冲区的深度 ;
    BYTE cStencilBits; // cStencilBits 模板缓冲区的深度 ;
    BYTE cAuxBuffers; // cAuxBuffers 轴向缓冲区的数量（一般 1.0 版本不支持）;
    BYTE iLayerType; // iLayerType 被忽略，为了一致性而包含的 ;
    BYTE bReserved; // bReserved 表层和底层平面的数量::位 0-3 表最多 15 层表层平面，位 4-7 表底层 ;
    DWORD dwLayerMask; // dwLayerMask 被忽略，为了一致性而包含的 ;
    DWORD dwVisibleMask; // dwVisibleMask 是透明色彩的值（RGBA 方式）或是一个底层平面的索引（Index）;
    DWORD dwDamageMask; // dwDamageMask 被忽略，为了一致性而包含的。
} PIXELFORMATDESCRIPTOR;
```

Irrlicht:
内存中为：BGRA，文件存储通常 big-endian，为 ARGB。刚好是内存的反转。OpenGLColor RGBA。

```cpp
//! An enum for the color format of textures used by the Irrlicht Engine.
/** A color format specifies how color information is stored.
    NOTE: Byte order in memory is usually flipped (it's probably correct in bitmap files, but flipped on reading).
    So for example ECF_A8R8G8B8 is BGRA in memory same as in DX9's D3DFMT_A8R8G8B8 format.
*/
enum ECOLOR_FORMAT {

//! Default 32 bit color format. 8 bits are used for every component: red, green, blue and alpha.
//! Warning: This tends to be BGRA in memory (it's ARGB on file, but with usual big-endian memory it's flipped)
    ECF_A8R8G8B8,
};

//! Converts color to OpenGL color format
/** From ARGB to RGBA in 4 byte components for endian aware passing to OpenGL
\param dest: address where the 4x8 bit OpenGL color is stored.
*/
void toOpenGLColor(u8* dest) const
{
    *dest =   (u8)getRed();
    *++dest = (u8)getGreen();
    *++dest = (u8)getBlue();
    *++dest = (u8)getAlpha();
}

#ifdef __BIG_ENDIAN__
    ((u32*)out)[x] = c << 24 | c << 16 | c << 8 | 0x000000FF;
#else
    ((u32*)out)[x] = 0xFF000000 | c << 16 | c << 8 | c;
#endif
```

If you have GL_RGBA and GL_UNSIGNED_INT_8_8_8_8, that means that pixels are stored in 32-bit integers, and the colors are in the logical order RGBA in such an integer, e.g. the red is in the high-order byte and the alpha is in the low-order byte.

But if the machine is little-endian (as with Intel CPUs), it follows that the actual order in memory is ABGR. Whereas, GL_RGBA with GL_UNSIGNED_BYTE will store the bytes in RGBA order regardless whether the computer is little-endian or big-endian.

GL_BGRA with GL_UNSIGNED_INT_8_8_8_8_REV would store colors in an integer in the logical order ARGB, but then on a little-endian machine, you get BGRA order in memory.

```cpp
#if OGRE_ENDIAN == ENDIAN_BIG
    /// 3 byte pixel format, 1 byte for red, 1 byte for green, 1 byte for blue
    PF_BYTE_RGB = PF_R8G8B8,
    /// 3 byte pixel format, 1 byte for blue, 1 byte for green, 1 byte for red
    PF_BYTE_BGR = PF_B8G8R8,
    /// 4 byte pixel format, 1 byte for blue, 1 byte for green, 1 byte for red and one byte for alpha
    PF_BYTE_BGRA = PF_B8G8R8A8,
#else
    /// 3 byte pixel format, 1 byte for red, 1 byte for green, 1 byte for blue
    PF_BYTE_RGB = PF_B8G8R8,
    /// 3 byte pixel format, 1 byte for blue, 1 byte for green, 1 byte for red
    PF_BYTE_BGR = PF_R8G8B8,
    /// 4 byte pixel format, 1 byte for blue, 1 byte for green, 1 byte for red and one byte for alpha
    PF_BYTE_BGRA = PF_A8R8G8B8,
#endif
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-07-opengl-pixel-format.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.microsoft.com/en-us/windows/win32/opengl/glteximage2d]({% include relrefx.html url="/backup/2021-04-07-opengl-pixel-format.md/docs.microsoft.com/102f1a99.html" %})
- [https://blog.csdn.net/w450468524/article/details/51649065]({% include relrefx.html url="/backup/2021-04-07-opengl-pixel-format.md/blog.csdn.net/a319243a.html" %})
- [https://cainiaojiaocheng.com/questions/6636847/odd-results-using-glteximage2d]({% include relrefx.html url="/backup/2021-04-07-opengl-pixel-format.md/cainiaojiaocheng.com/1bba254e.html" %})
