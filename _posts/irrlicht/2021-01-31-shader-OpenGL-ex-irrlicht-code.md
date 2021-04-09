---
layout: post
title: "图形学笔记 -- Irrlicht 源码整理笔记"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL", "Irrlicht"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

一些很有意思的代码片段。


## GetStringUTFChars

```cpp
const char* GetStringUTFChars(JNIEnv*env, jstring string, jboolean *isCopy);
```

当从 JNI 函数 GetStringUTFChars 函数中返回得到字符串 B 时，
1. 如果 B 是原始字符串 java.lang.String 的一份拷贝，则 isCopy 被赋值为 JNI_TRUE。
2. 如果 B 是和原始字符串指向的是 JVM 中的同一份数据，则 isCopy 被赋值为 JNI_FALSE。当 isCopy 为 JNI_FALSE 时，本地代码绝不能修改字符串的内容，否则 JVM 中的原始字符串也会被修改，这会打破 Java 语言中字符串不可变的规则。
3. 通常，我们不必关心 JVM 是否会返回原始字符串的拷贝，只需要为 isCopy 传递 NULL 作为参数。


## stringaling.h

```cpp
#ifndef __STRINGALING_H
#define __STRINGALING_H

#include <string>
#include <sstream>

template<typename T>
inline std::string stringify(const T& x) {
    std::ostringstream o;
    if (!(o << x)) return "";
    return o.str();
}

template<typename T>
inline T fromString(char *s) {
    std::string str = s;
    std::istringstream i(str);
    T x;
    i >> x;
    return x;
}

inline std::string strparty(const char *str1, int n, const char *str2) {
    std::string str = str1;
    str += stringify(n);
    str += str2;
    return str;
}

#endif
```


## irrString.h

```cpp
namespace irr
{
namespace core
{
//! Convert this utf-8-encoded string to the platform's wchar.
/** The resulting string is always NULL-terminated and well-formed.
\param len The size of the output buffer in bytes.
*/
IRRLICHT_API void utf8ToWchar(const char *in, wchar_t *out, const u64 len);

//! Convert this wchar string to utf-8.
/** The resulting string is always NULL-terminated and well-formed.
\param len The size of the output buffer in bytes.
*/
IRRLICHT_API void wcharToUtf8(const wchar_t *in, char *out, const u64 len);

template <typename T, typename TAlloc>
class string
{
};

//! Typedef for character strings
typedef string<c8> stringc;

//! Typedef for wide character strings
typedef string<wchar_t> stringw;

//! Convert multibyte string to wide-character string
/** Wrapper around mbstowcs from standard library, but directly using Irrlicht string class.
What the function does exactly depends on the LC_CTYPE of the current c locale.
\param destination Wide-character string receiving the converted source
\param source multibyte string
\return The number of wide characters written to destination, not including the eventual
    terminating null character or -1 when conversion failed */
static inline size_t multibyteToWString(string<wchar_t>& destination, const core::string<c8>& source);

//! Convert multibyte string to wide-character string
/** Wrapper around mbstowcs from standard library, but directly writing to Irrlicht string class.
What the function does exactly depends on the LC_CTYPE of the current c locale.
\param destination Wide-character string receiving the converted source
\param source multibyte string
\return The number of wide characters written to destination, not including the eventual
    terminating null character  or -1 when conversion failed. */
static inline size_t multibyteToWString(string<wchar_t>& destination, const char* source);

//! Internally used by the other multibyteToWString functions
static size_t multibyteToWString(string<wchar_t>& destination, const char* source, u32 sourceSize);

} // end namespace core
} // end namespace irr

#endif
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-31-shader-OpenGL-ex-irrlicht-code.md.js" %}'></script></p>
