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
