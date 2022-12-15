---
layout: post
title: "编程与调试 C++ -- 多平台字符编码转换（Building iconv for Android）"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++", "Android"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

一个支持多平台的字符编码转换还挺麻烦得。
**Android NDK 自带的 iconv 链接，代码能编译链接成功，但是无法实现 gbk/utf8 编码的正常转换。需要自己编译一个 libiconv。**

* GB2312 是中国规定的汉字编码，也可以说是简体中文的字符集编码。
    GBK 是 GB2312 的扩展，除了兼容 GB2312 外，它还能显示繁体中文，还有日文的假名。
* cp936：中文本地系统是 Windows 中的 cmd，默认 codepage 是 CP936，cp936 就是指系统里第 936 号编码格式，即 GB2312 的编码。
    当然有其它编码格式：cp950 繁体中文、cp932 日语、cp1250 中欧语言。
* Unicode 是国际组织制定的可以容纳世界上所有文字和符号的字符编码方案。UTF-8、UTF-16、UTF-32 都是将数字转换到程序数据的编码方案。
    * UTF-8（8-bit Unicode Transformation Format）是最流行的一种对 Unicode 进行传播和存储的编码方式。
        它用不同的 bytes 来表示每一个代码点。ASCII 字符每个只需要用一个 byte，与 ASCII 的编码是一样的。所以说 ASCII 是 UTF-8 的一个子集。

```cpp
#include "kminwindef.h"

#include "kIrrCompileConfig.h"
#ifdef _KIRR_WINDOWS_
#ifdef _KIRR_ANDROID_PLATFORM_
#ifdef _KIRR_WINDOWS_API_

// 常用的几个。
#ifdef _MSC_VER /* Visual Studio */
#ifdef __ANDROID__
// 不常用不建议采用的。
#ifdef _WIN32 // _WINDOWS
```


## libiconv build in android

android 编译 iconv 库，实现 gbk 与 utf8 之间的转换。
<https://www.gnu.org/software/libiconv/> [doc](https://my.oschina.net/u/1538135/blog/4686164)

这玩意需要先跑 `$ sudo sh ./configure`
Android 配置不了，配置生成 linux 环境下的 config.h 文件，反正 Android 和 Ubuntu 也差不多。
找了台 Ubuntu 64 位 系统配置，配置好后入库。

这里是标准做法：[Building iconv for Android](https://medium.com/@zw3rk/building-iconv-for-android-e3581a52668f)
编写 ios 和 android 共用的 c/c++ 库时 使用 iconv 的问题，[貌似苹果版本](https://www.itread01.com/content/1550578686.html)

```
./configure --host=$ANDROID_HOST --with-sysroot=$ANDROID_SYSROOT
```


### Building iconv for Android

```shell
hawkhai@ubuntu:~/Desktop/libiconv-1.16$ sudo sh ./configure
hawkhai@ubuntu:~/Desktop/libiconv-1.16$
```

再搞一个 cmake 去编译它。

```cmake
cmake_minimum_required(VERSION 3.4.1)

include_directories(
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        ${CMAKE_CURRENT_SOURCE_DIR}/libcharset
        ${CMAKE_CURRENT_SOURCE_DIR}/lib
        ${CMAKE_CURRENT_SOURCE_DIR}/libcharset/include
        ${CMAKE_CURRENT_SOURCE_DIR}/srclib
)

add_definitions(-frtti -fexceptions
        -Wno-multichar
        -DANDROID
        -DLIBDIR="c"
        -DBUILDING_LIBICONV
        -DIN_LIBRARY)

add_library(
        iconv
        STATIC
        libcharset/lib/localcharset.c
        lib/iconv.c
        lib/relocatable.c
)
```

1. 编译时提示：

```
E:/libiconv-1.16/libcharset/lib/localcharset.c:696: error: undefined reference to 'nl_langinfo'
```

2. 解决方法：

修改目录文件 libcharset/config.h 的宏定义，禁止该宏定义：

```cpp
/* Define if you have <langinfo.h> and nl_langinfo(CODESET). */
#define HAVE_LANGINFO_CODESET 0
```

3. Android 完美呈现

{% include image.html url="/assets/images/210227-mbs-and-wcs-for-android/20210301230434.png" %}


## Windows

简单。WideCharToMultiByte() 和 MultiByteToWideChar()。


### vlocale.h

```cpp
#pragma once

#include <stddef.h>
#include <locale.h>
#include <stdlib.h>
#include <string.h>

#define _ENABLE_PER_THREAD_LOCALE           0x1
#define _DISABLE_PER_THREAD_LOCALE          0x2

// https://www.gnu.org/software/libc/manual/html_node/Setting-the-Locale.html
// https://blog.weghos.com/skia/Skia/src/gpu/GrAutoLocaleSetter.h.html
class LocaleGuard {
private:
#ifdef _MSC_VER
    char* m_localeSaved = nullptr;
    char* m_localeNew = nullptr;
    int m_preLocaleStatus = _DISABLE_PER_THREAD_LOCALE;
#else
    locale_t fOldLocale = 0;
    locale_t fLocale = 0;
#endif
    int m_category = LC_CTYPE; // LC_ALL LC_CTYPE

public:
    LocaleGuard(const char* locale, int category = LC_CTYPE) {
#ifdef _MSC_VER
        m_preLocaleStatus = _configthreadlocale(_ENABLE_PER_THREAD_LOCALE);
        m_category = category;
        char* localeOld = setlocale(m_category, NULL);
        if (localeOld) {
            m_localeSaved = strdup(localeOld);
        }
        char* localeNew = setlocale(m_category, locale);
        if (localeNew) {
            m_localeNew = strdup(localeNew);
        }
#else
        m_category = category;
        fLocale = newlocale(m_category, locale, nullptr);
        if (fLocale) {
            fOldLocale = uselocale(fLocale);
        } else {
            fOldLocale = static_cast<locale_t>(nullptr);
        }
#endif
    }

#ifdef _MSC_VER
    const int getPreLocaleStatus() {
        return m_preLocaleStatus;
    }

    const char* getPreLocaleInfo() {
        return m_localeSaved;
    }

    const char* getLocaleInfo() {
        return m_localeNew;
    }
#else
    locale_t getPreLocaleInfo() {
        return fOldLocale;
    }

    locale_t getLocaleInfo() {
        return fLocale;
    }
#endif

    virtual ~LocaleGuard() {
#ifdef _MSC_VER
        if (m_localeSaved) {
            setlocale(m_category, m_localeSaved);
            free(m_localeSaved);
            m_localeSaved = nullptr;
        }
        if (m_localeNew) {
            free(m_localeNew);
            m_localeNew = nullptr;
        }
        if (m_preLocaleStatus != -1) {
            _configthreadlocale(m_preLocaleStatus);
        }
#else
        if (fLocale) {
            uselocale(fOldLocale);
            freelocale(fLocale);
        }
#endif
    }
};
```


### vmbswcs.h

```cpp
#pragma once

#include <iostream>
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>

#ifdef _MSC_VER
#include <windows.h>
#endif

//
//  Code Page Default Values.
//  Please Use Unicode, either UTF-16 (as in WCHAR) or UTF-8 (code page CP_ACP)
//
#define CP_ACP        ((unsigned) 0)          // default to ANSI code page
#define CP_OEMCP                  1           // default to OEM  code page
#define CP_MACCP                  2           // default to MAC  code page
#define CP_THREAD_ACP             3           // current thread's ANSI code page
#define CP_SYMBOL                 42          // SYMBOL translations
#define CP_UTF7                   65000       // UTF-7 translation
#define CP_UTF8                   65001       // UTF-8 translation

std::wstring strToWstr(const std::string& text, unsigned codepage = CP_UTF8);
std::string wstrToStr(const std::wstring& text, unsigned codepage = CP_UTF8);

//setlocale(LC_CTYPE, "chinese-traditional"); // 认为输入的 MBS 是 Big5 编码
//setlocale(LC_CTYPE, "chinese-simplified");  // 设置输出的 MBS 为 GBK 编码
#define LOCALE_CHINESE_CHINA_936    "Chinese_China.936"
//#define LOCALE_CHINESE_SIMPLIFIED   "chinese-simplified"
#define LOCALE_ZH_CN_UTF8           "zh_CN.utf8"

std::wstring strToWstr(const std::string& text, char const* locale);
std::string wstrToStr(const std::wstring& text, char const* locale);
```


### vmbswcs.cpp

```cpp
#include "vmbswcs.h"
#include "vlocale.h"
#include <assert.h>
#include <string.h>

#ifdef __ANDROID__
#include "iconv.h"
#endif

std::wstring strToWstr(const std::string& text, unsigned codepage/*CP_UTF8*/)
{
#ifdef _MSC_VER
    const int length = ::MultiByteToWideChar(codepage, 0, text.c_str(), (int)text.size(), NULL, 0);
    if (length > 0) {
        std::wstring str;
        str.resize(length);
        if (0 != ::MultiByteToWideChar(codepage, 0, text.c_str(), (int)text.size(), &str[0], (int)str.size()))
            return str;
    }
    return L"";
#endif
    if (CP_ACP == codepage) {
        return strToWstr(text.c_str(), LOCALE_CHINESE_CHINA_936).c_str();
    }
    if (CP_UTF8 == codepage) {
        return strToWstr(text.c_str(), LOCALE_ZH_CN_UTF8).c_str();
    }
    throw "not implement yet.";
    return L"";
}
std::string wstrToStr(const std::wstring& text, unsigned codepage/*CP_UTF8*/)
{
#ifdef _MSC_VER
    const int length = ::WideCharToMultiByte(codepage, 0, text.c_str(), (int)text.size(), NULL, 0, NULL, NULL);
    if (length > 0) {
        std::string str;
        str.resize(length);
        if (0 != ::WideCharToMultiByte(codepage, 0, text.c_str(), (int)text.size(), &str[0], (int)str.size(), NULL, NULL))
            return str;
    }
    return "";
#endif
    if (CP_ACP == codepage) {
        return wstrToStr(text.c_str(), LOCALE_CHINESE_CHINA_936).c_str();
    }
    if (CP_UTF8 == codepage) {
        return wstrToStr(text.c_str(), LOCALE_ZH_CN_UTF8).c_str();
    }
    throw "not implement yet.";
    return "";
}

#ifdef __ANDROID__
int code_convert(
        const char *from_charset,
        const char *to_charset,
        const char *inbuf,
        size_t inlen,
        char *outbuf,
        size_t outlen) {

    const char **pin = &inbuf;
    char **pout = &outbuf;
    memset(outbuf, 0, outlen);

    // https://blog.csdn.net/Sky_qing/article/details/8995201
    iconv_t cd = iconv_open(to_charset, from_charset);
    if (cd == (iconv_t)(-1)) {
        return -1;
    }
    iconv(cd, const_cast<char**>(pin), &inlen, pout, &outlen);
    iconv_close(cd);
    return 0;
}

/* UTF-8 to GBK  */
int code_u2g(const char *inbuf, size_t inlen, char *outbuf, size_t outlen) {
    int retv = code_convert("UTF-8","GBK", inbuf, inlen, outbuf, outlen);
    return retv;
}

/* GBK to UTF-8 */
int code_g2u(const char *inbuf, size_t inlen, char *outbuf, size_t outlen) {
    int retv = code_convert("GBK", "UTF-8", inbuf, inlen, outbuf, outlen);
    return retv;
}
#endif

std::string wstrToStr(const std::wstring& text, char const* locale)
{
#ifdef __ANDROID__
    if (strcmp(LOCALE_CHINESE_CHINA_936, locale) == 0) {
        std::string retv = wstrToStr(text.c_str(), LOCALE_ZH_CN_UTF8);
        int xsize = retv.length() * 2 + 1;
        char* buffer = new char[xsize];
        int rc = code_u2g(retv.c_str(), retv.length(), buffer, xsize);
        retv = buffer;
        delete[] buffer;
        return retv;
    }
#endif

#ifdef _MSC_VER
    if (strcmp(LOCALE_CHINESE_CHINA_936, locale) == 0) {
        return wstrToStr(text, CP_ACP);
    }
    if (strcmp(LOCALE_ZH_CN_UTF8, locale) == 0) {
        return wstrToStr(text, CP_UTF8);
    }
#endif

    LocaleGuard temp(locale, LC_CTYPE);
#ifdef DEBUG_FAKELIB
    printf("Locale information %s %d -> %s\n", temp.getPreLocaleInfo(), temp.getPreLocaleStatus(), temp.getLocaleInfo());
#endif
    int reqsize = wcstombs(NULL, text.c_str(), 0) + 1;
    if (reqsize == 0) {
        return "";
    }
    char* pmb = (char*)malloc(reqsize);
    if (pmb == nullptr) {
        return "";
    }
    size_t size = wcstombs(pmb, text.c_str(), reqsize);
    if (size == (size_t)(-1)) {
        free(pmb);
        return "";
    }

#ifdef DEBUG_FAKELIB
    assert(size + 1 == reqsize);
#endif
    pmb[size] = 0;
    std::string str(pmb);
    free(pmb);
    return str;
}

std::wstring strToWstr(const std::string& text, char const* locale)
{
#ifdef __ANDROID__
    if (strcmp(LOCALE_CHINESE_CHINA_936, locale) == 0) {
        int xsize = text.length() * 2 + 1;
        char* buffer = new char[xsize];
        int rc = code_g2u(text.c_str(), text.length(), buffer, xsize);
        std::wstring retv = strToWstr(buffer, LOCALE_ZH_CN_UTF8);
        delete[] buffer;
        return retv;
    }
#endif

#ifdef _MSC_VER
    if (strcmp(LOCALE_CHINESE_CHINA_936, locale) == 0) {
        return strToWstr(text, CP_ACP);
    }
    if (strcmp(LOCALE_ZH_CN_UTF8, locale) == 0) {
        return strToWstr(text, CP_UTF8);
    }
#endif

    LocaleGuard temp(locale, LC_CTYPE);
#ifdef DEBUG_FAKELIB
    printf("Locale information %s %d -> %s\n", temp.getPreLocaleInfo(), temp.getPreLocaleStatus(), temp.getLocaleInfo());
#endif
    int reqsize = mbstowcs(NULL, text.c_str(), 0) + 1;
    if (reqsize == 0) {
        return L"";
    }
    wchar_t* pwc = (wchar_t*)malloc(reqsize * sizeof(wchar_t));
    if (pwc == nullptr) {
        return L"";
    }
    size_t size = mbstowcs(pwc, text.c_str(), reqsize);
    if (size == (size_t)(-1)) {
        free(pwc);
        return L"";
    }

#ifdef DEBUG_FAKELIB
    assert(size + 1 == reqsize);
#endif
    pwc[size] = 0;
    std::wstring str(pwc);
    free(pwc);
    return str;
}
```


### testmain.cpp

```cpp
#include "vlocale.h"
#include "vmbswcs.h"

void myprint(const char* tag, const wchar_t* pstr)
{
    printf("%8s\t{ ", tag);
    for (int i = 0; i < wcslen(pstr); i++) {
        wprintf(L"%#.x, ", unsigned int(pstr[i]));
    }
    wprintf(L"0 }\n");
}
void myprint(const char* tag, const char* pstr)
{
    printf("%8s\t { ", tag);
    for (int i = 0; i < strlen(pstr); i++) {
        printf("%#.x, ", unsigned char(pstr[i]));
    }
    printf("0 }\n");
}

int maintest()
{
    // const wchar_t* pwchello = L"Hello 世界！";
    wchar_t helloWc[] = { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x4e16, 0x754c, 0xff01, 0, };
    unsigned char helloAcp[] = { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0xca, 0xc0, 0xbd, 0xe7, 0xa3, 0xa1, 0, };
    unsigned char helloUtf8[] = { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0xe4, 0xb8, 0x96, 0xe7, 0x95, 0x8c, 0xef, 0xbc, 0x81, 0, };

    std::string temp1 = wstrToStr(helloWc, LOCALE_CHINESE_CHINA_936);
    std::string temp2 = wstrToStr(helloWc, LOCALE_ZH_CN_UTF8);
    std::wstring temp3 = strToWstr((char*)helloAcp, LOCALE_CHINESE_CHINA_936);
    std::wstring temp4 = strToWstr((char*)helloUtf8, LOCALE_ZH_CN_UTF8);
    return 0;
}

int main()
{
    maintest();

    const wchar_t* pwchello = L"Hello 世界！";
    std::string utf8str = wstrToStr(pwchello, CP_UTF8);
    std::string acpstr = wstrToStr(pwchello, CP_ACP);
    myprint("wchar_t", pwchello);
    myprint("CP_ACP", acpstr.c_str());
    myprint("CP_UTF8", utf8str.c_str());

    std::string temp1 = wstrToStr(pwchello, LOCALE_CHINESE_CHINA_936);
    myprint("wcstombs", temp1.c_str());

    std::string temp2 = wstrToStr(pwchello, LOCALE_ZH_CN_UTF8);
    myprint("wcstombs", temp2.c_str());

    std::wstring temp3 = strToWstr(acpstr.c_str(), LOCALE_CHINESE_CHINA_936);
    myprint("mbstowcs", temp3.c_str());

    std::wstring temp4 = strToWstr(utf8str.c_str(), LOCALE_ZH_CN_UTF8);
    myprint("mbstowcs", temp4.c_str());

    getchar();
    return 0;
}
```


### 输出

```
wchar_t          { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x4e16, 0x754c, 0xff01, 0 }
CP_ACP           { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0xca, 0xc0, 0xbd, 0xe7, 0xa3, 0xa1, 0 }
CP_UTF8          { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0xe4, 0xb8, 0x96, 0xe7, 0x95, 0x8c, 0xef, 0xbc, 0x81, 0 }
Locale information C 2 -> Chinese_China.936
wcstombs         { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0xca, 0xc0, 0xbd, 0xe7, 0xa3, 0xa1, 0 }
Locale information C 2 -> zh_CN.utf8
wcstombs         { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0xe4, 0xb8, 0x96, 0xe7, 0x95, 0x8c, 0xef, 0xbc, 0x81, 0 }
Locale information C 2 -> Chinese_China.936
mbstowcs         { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x4e16, 0x754c, 0xff01, 0 }
Locale information C 2 -> zh_CN.utf8
mbstowcs         { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x4e16, 0x754c, 0xff01, 0 }

```


## Android & Linux

悲剧。mbstowcs() 和 wcstombs()。多线程中这玩意悲剧。

```cpp
size_t mbstowcs(wchar_t *wcstr, const char *mbstr, size_t count);
// 通过这玩意调节编码："zh_CN.utf8" / "Chinese_China.936"
// Android 不支持 "Chinese_China.936"
setlocale(LC_CTYPE, "zh_CN.utf8");
```

Windows 特有 API： `_configthreadlocale` 。

```cpp
setlocale(LC_CTYPE, "chs");
// 使 setlocale 只针对当前线程起作用
_configthreadlocale(_ENABLE_PER_THREAD_LOCALE);
// 使 setlocale 对所有线程的设置都有用（默认值）
_configthreadlocale(_DISABLE_PER_THREAD_LOCALE);
setlocale // 只能在当前进程各自的运行时库里生效
```

Android Java，还可以通过 JNI 去搞。 `new String(str.getBytes(), "UTF-8");`

```java
char* jstringTostring(JNIEnv* env, jstring jstr)
{
    jstring strencode = env->NewStringUTF("utf-8");
    jclass strClass = env->FindClass("java/lang/String");
    jmethodID getBytesId = env->GetMethodID(strClass, "getBytes", "(Ljava/lang/String;)[B");

    jbyteArray barr = (jbyteArray)env->CallObjectMethod(jstr, getBytesId, strencode);
    jsize alen = env->GetArrayLength(barr);
    jbyte* ba = env->GetByteArrayElements(barr, JNI_FALSE);

    char* rtn = NULL;
    if (alen > 0) {
        rtn = (char*)malloc(alen + 1);
        memcpy(rtn, ba, alen);
        rtn[alen] = 0;
    }
    env->ReleaseByteArrayElements(barr, ba, 0);
    return rtn;
}

jstring stringToJstring(JNIEnv* env, const char* pat)
{
    jstring encoding = env->NewStringUTF("utf-8");
    jclass strClass = env->FindClass("Ljava/lang/String;");
    jmethodID initId = env->GetMethodID(strClass, "<init>", "([BLjava/lang/String;)V");

    jbyteArray bytes = env->NewByteArray(strlen(pat));
    env->SetByteArrayRegion(bytes, 0, strlen(pat), (jbyte*)pat);

    return (jstring)env->NewObject(strClass, initId, bytes, encoding);
}
```


### locale

locale 把按照所涉及到的文化传统的各个方面分成 12 个大类，这 12 个大类分别是：

1. 语言符号及其分类 (LC_CTYPE)
2. 数字 (LC_NUMERIC)
3. 比较和排序习惯 (LC_COLLATE)
4. 时间显示格式 (LC_TIME)
5. 货币单位 (LC_MONETARY)
6. 信息主要是提示信息、错误信息、状态信息、标题、标签、按钮和菜单等 (LC_MESSAGES)
7. 姓名书写方式 (LC_NAME)
8. 地址书写方式 (LC_ADDRESS)
9. 电话号码书写方式 (LC_TELEPHONE)
10. 度量衡表达方式 (LC_MEASUREMENT)
11. 默认纸张尺寸大小 (LC_PAPER)
12. 对 locale 自身包含信息的概述 (LC_IDENTIFICATION)

Locale 是软件在运行时的语言环境，它包括语言 (Language)，地域 (Territory) 和字符集 (Codeset)。
一个 locale 的书写格式为： `语言[_地域[.字符集]]` 。

1. 我说中文，身处中华人民共和国，使用国标 2312 字符集来表达字符。 `zh_CN.GB2312` ＝ `中文_中华人民共和国＋国标 2312 字符集` 。
3. 我说中文，身处中华人民共和国台湾省，使用国标 Big5 字符集来表达字符。 `zh_TW.BIG5` ＝ `中文_台湾.大五码字符集` 。


### iconv()

**转换描述符不能再多线程中同时使用。** GBK，UTF−8。

```cpp
#include <iconv.h>
iconv_t iconv_open(const char *tocode, const char *fromcode);
size_t iconv(iconv_t cd, char **inbuf, size_t *inbytesleft, char **outbuf, size_t *outbytesleft);
int iconv_close(iconv_t cd);
```

这个库有意思。[CMake-based MinGW-w64 Cross Toolchain {% include relref_github.html %}](https://github.com/shinchiro/mpv-winbuild-cmake)
里面包含：ANGLE、FFmpeg 等各种库，遗憾没有 Android 版本。


## Refs

- [1] [locale 的设定及 LANG、LC_CTYPE、LC_ALL 环境变量 {% include relref_cnblogs.html %}](https://www.cnblogs.com/xlmeng1988/archive/2013/01/16/locale.html)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-02-27-mbs-and-wcs-for-Android.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.gnu.org/software/libiconv/]({% include relrefx.html url="/backup/2021-02-27-mbs-and-wcs-for-Android.md/www.gnu.org/66303c8e.html" %})
- [https://my.oschina.net/u/1538135/blog/4686164]({% include relrefx.html url="/backup/2021-02-27-mbs-and-wcs-for-Android.md/my.oschina.net/bd649d53.html" %})
- [https://medium.com/@zw3rk/building-iconv-for-android-e3581a52668f]({% include relrefx.html url="/backup/2021-02-27-mbs-and-wcs-for-Android.md/medium.com/5ef0d465.html" %})
- [https://www.itread01.com/content/1550578686.html]({% include relrefx.html url="/backup/2021-02-27-mbs-and-wcs-for-Android.md/www.itread01.com/7d5ac543.html" %})
- [https://www.gnu.org/software/libc/manual/html_node/Setting-the-Locale.html]({% include relrefx.html url="/backup/2021-02-27-mbs-and-wcs-for-Android.md/www.gnu.org/4ee554e9.html" %})
- [https://blog.weghos.com/skia/Skia/src/gpu/GrAutoLocaleSetter.h.html]({% include relrefx.html url="/backup/2021-02-27-mbs-and-wcs-for-Android.md/blog.weghos.com/55bbfd99.html" %})
- [https://blog.csdn.net/Sky_qing/article/details/8995201]({% include relrefx.html url="/backup/2021-02-27-mbs-and-wcs-for-Android.md/blog.csdn.net/f6a36d61.html" %})
- [https://github.com/shinchiro/mpv-winbuild-cmake]({% include relrefx.html url="/backup/2021-02-27-mbs-and-wcs-for-Android.md/github.com/d42e8069.html" %})
- [https://www.cnblogs.com/xlmeng1988/archive/2013/01/16/locale.html]({% include relrefx.html url="/backup/2021-02-27-mbs-and-wcs-for-Android.md/www.cnblogs.com/199de3b0.html" %})
