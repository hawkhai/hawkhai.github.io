---
layout: post
title: "编程 C++ -- 蛋疼的多平台字符编码转换 for Android"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "C++", "Android"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

一个支持多平台的字符串转换还挺麻烦得。


## Windows

简单。WideCharToMultiByte() 和 MultiByteToWideChar()。

```cpp
// MultiByteAndWideChar.cpp: 定义应用程序的入口点。
//
#include "MultiByteAndWideChar.h"
#include <iostream>
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <wchar.h>

//
//  Code Page Default Values.
//  Please Use Unicode, either UTF-16 (as in WCHAR) or UTF-8 (code page CP_ACP)
//
#define CP_ACP                    0           // default to ANSI code page
#define CP_OEMCP                  1           // default to OEM  code page
#define CP_MACCP                  2           // default to MAC  code page
#define CP_THREAD_ACP             3           // current thread's ANSI code page
#define CP_SYMBOL                 42          // SYMBOL translations
#define CP_UTF7                   65000       // UTF-7 translation
#define CP_UTF8                   65001       // UTF-8 translation
std::wstring to_wpath(const std::string& text, unsigned codepage = CP_UTF8)
{
    const int length = ::MultiByteToWideChar(codepage, 0, text.c_str(), (int)text.size(), NULL, 0);
    if (length > 0) {
        std::wstring wt;
        wt.resize(length);
        if (0 != ::MultiByteToWideChar(codepage, 0, text.c_str(), (int)text.size(), &wt[0], (int)wt.size()))
            return wt;
    }
    return L"";
}
std::string from_wpath(const std::wstring& text, unsigned codepage = CP_UTF8)
{
    const int length = ::WideCharToMultiByte(codepage, 0, text.c_str(), (int)text.size(), NULL, 0, NULL, NULL);
    if (length > 0) {
        std::string str;
        str.resize(length);
        if (0 != ::WideCharToMultiByte(codepage, 0, text.c_str(), (int)text.size(), &str[0], (int)str.size(), NULL, NULL))
            return str;
    }
    return "";
}

void myprint(const char* tag, const wchar_t* pstr)
{
    printf("%8s\t", tag);
    for (int i = 0; i < wcslen(pstr); i++) {
        wprintf(L"%x ", unsigned int(pstr[i]));
    }
    wprintf(L"\r\n");
}
void myprint(const char* tag, const char* pstr)
{
    printf("%8s\t", tag);
    for (int i = 0; i < strlen(pstr); i++) {
        printf("%x ", unsigned int(pstr[i]));
    }
    printf("\r\n");
}

int trytrans(char const* locale, const wchar_t* pwchello) {
    char* localeInfo = setlocale(LC_ALL, locale);
    printf("Locale information set to %s\n", localeInfo);

    int requiredSize = wcstombs(NULL, pwchello, 0);
    unsigned char* pmbhello = (unsigned char*)malloc(requiredSize + 1);
    size_t size = wcstombs((char*)pmbhello, pwchello, requiredSize + 1);
    if (size == (size_t)(-1)) {
        return 1;
    }
    myprint("wcstombs", (const char*)pmbhello);
    free(pmbhello);
    return 0;
}

int trytrans(char const* locale, const char* pmbhello) {
    char* localeInfo = setlocale(LC_ALL, locale);
    printf("Locale information set to %s\n", localeInfo);

    int requiredSize = mbstowcs(NULL, pmbhello, 0);
    wchar_t* pwc = (wchar_t*)malloc((requiredSize + 1) * sizeof(wchar_t));
    size_t size = mbstowcs(pwc, (char const*)pmbhello, requiredSize + 1);
    if (size == (size_t)(-1)) {
        return 1;
    }
    myprint("mbstowcs", pwc);
    free(pwc);
    return 0;
}

int mainz()
{
    const wchar_t* pwchello = L"Hello 世界！";
    std::wstring text = pwchello;
    std::string utf8str = from_wpath(text, CP_UTF8);
    std::string acpstr = from_wpath(text, CP_ACP);
    myprint("Lwchar_t", text.c_str());
    myprint("CP_UTF8", utf8str.c_str());
    myprint("CP_ACP", acpstr.c_str());

    // Locale information set to Chinese_China.936
    trytrans("chinese-simplified", pwchello);

    // Locale information set to zh_CN.utf8
    trytrans("zh_CN.utf8", pwchello);

    //setlocale(LC_CTYPE, "chinese-traditional"); // 认为输入的 MBS 是 Big5 编码
    //setlocale(LC_CTYPE, "chinese-simplified");  // 设置输出的 MBS 为 GBK 编码
    trytrans("chinese-simplified", acpstr.c_str());
    trytrans("zh_CN.utf8", utf8str.c_str());
    return 0;
}

int main()
{
    mainz();
    // 将文件保存为 utf8 编码
    char const* source = "Hello 世界！";

#define BUFFER_SIZE (128)
    wchar_t wc_out[BUFFER_SIZE];
    char    mb_out[BUFFER_SIZE];
    printf("\n%s", source);     // 输出不正常

    // 认为输入的 MBS 是 ?? 编码
    //setlocale(LC_CTYPE, "chinese-traditional");
    setlocale(LC_CTYPE, "chinese-simplified");
    mbstowcs(wc_out, source, BUFFER_SIZE);
    wprintf(L"\n%s", wc_out);     // 正常输出

    // 设置输出的 MBS 为 GBK 编码
    setlocale(LC_CTYPE, "chinese-simplified");
    wcstombs(mb_out, wc_out, BUFFER_SIZE);
    printf("\n%s", mb_out);     // 正常输出
}
```


### 输出

```
Lwchar_t        48 65 6c 6c 6f 20 4e16 754c ff01
 CP_UTF8        48 65 6c 6c 6f 20 ffffffe4 ffffffb8 ffffff96 ffffffe7 ffffff95 ffffff8c ffffffef ffffffbc ffffff81
  CP_ACP        48 65 6c 6c 6f 20 ffffffca ffffffc0 ffffffbd ffffffe7 ffffffa3 ffffffa1
Locale information set to Chinese_China.936
wcstombs        48 65 6c 6c 6f 20 ffffffca ffffffc0 ffffffbd ffffffe7 ffffffa3 ffffffa1
Locale information set to zh_CN.utf8
wcstombs        48 65 6c 6c 6f 20 ffffffe4 ffffffb8 ffffff96 ffffffe7 ffffff95 ffffff8c ffffffef ffffffbc ffffff81
Locale information set to Chinese_China.936
mbstowcs        48 65 6c 6c 6f 20 4e16 754c ff01
Locale information set to zh_CN.utf8
mbstowcs        48 65 6c 6c 6f 20 4e16 754c ff01

Hello
Hello 世界！
Hello 世界！
```


## Android & Linux

悲剧。mbstowcs() 和 wcstombs()。

```cpp
size_t mbstowcs(wchar_t *wcstr, const char *mbstr, size_t count);
// 通过这玩意调节编码："zh_CN.utf8" / "Chinese_China.936"
setlocale(LC_CTYPE, "zh_CN.utf8");
```

```cpp
inline std::string wstr2str(const std::wstring& xsistr)
{
    if (xsistr.empty()) {
        return "";
    }

    size_t c = ::wcstombs(0, xsistr.c_str(), 0);
    char* tmp = new char[c + 1];
    ::wcstombs(tmp, xsistr.c_str(), c);
    tmp[c] = '\0';

    std::string ret(tmp);
    delete[] tmp;
    return ret;
}

inline std::wstring str2wstr(const std::string& str)
{
    if (str.empty()) {
        return L"";
    }

    size_t c = ::mbstowcs(0, str.c_str(), 0);
    wchar_t* tmp = new wchar_t[c + 1];
    ::mbstowcs(tmp, str.c_str(), c);
    tmp[c] = '\0';

    std::wstring ret(tmp);
    delete[] tmp;
    return ret;
}
```

Android JAVA，通过 JNI 去搞。

```java
new String(str.getBytes(), "UTF-8");

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

jstring stoJstring(JNIEnv* env, const char* pat)
{
    jstring encoding = env->NewStringUTF("utf-8");
    jclass strClass = env->FindClass("Ljava/lang/String;");
    jmethodID initId = env->GetMethodID(strClass, "<init>", "([BLjava/lang/String;)V");

    jbyteArray bytes = env->NewByteArray(strlen(pat));
    env->SetByteArrayRegion(bytes, 0, strlen(pat), (jbyte*)pat);

    return (jstring)env->NewObject(strClass, initId, bytes, encoding);
}
```


### iconv()

转换描述符不能再多线程中同时使用。GBK，UTF−8。

```cpp
#include <iconv.h>
iconv_t iconv_open(const char *tocode, const char *fromcode);
size_t iconv(iconv_t cd, char **inbuf, size_t *inbytesleft, char **outbuf, size_t *outbytesleft);
int iconv_close(iconv_t cd);
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-02-27-mbs-and-wcs-for-Android.md.js" %}'></script></p>
