---
layout: post
title: "生活 -- Tiny Source Code, Tiny My Life"
author:
location: "Japan"
categories: ["生活"]
tags: ["生活"]
toc: true
toclistyle:
comments: true
visibility:
mathjax: true
mermaid: true
glslcanvas:
codeprint:
---

Hey, there! Welcome to my blog. I hope you enjoy reading the stuff in here. Nothing fancy, really. Just bits and bobs about tech and random topics.<br/><br/>
Enjoy!

* [编程精粹 -- Microsoft 编写优质无错 C 程序秘诀 {% include relref_csdn.html %}](https://blog.csdn.net/okcai/article/details/186241)
* [编程精粹 -- Microsoft 编写优质无错代码的秘诀 (Writing Clean Code) {% include relref_github.html %}](https://dirtysalt.github.io/html/writing-clean-code.html)

```cpp
wchar_t* pstr = nullptr;
CString exe = pstr; // 不会崩溃。
exe.Append(L"test");

// 0xC0000005: 读取位置 0x00000000 时发生访问冲突。
std::wstring tempexe = pstr; // 会崩溃。
tempexe.append(L"test");
```


## bsearch & qsort

* <https://www.tutorialspoint.com/c_standard_library/c_function_bsearch.htm>
* <https://www.tutorialspoint.com/c_standard_library/c_function_qsort.htm>

```c
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}
int cmpfunc(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}
qsort(ali, size, sizeof(int), compare);
qsort(values, 5, sizeof(int), cmpfunc);
```

```cpp
#include <stdio.h>
#include <stdlib.h>

int cmpfunc(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int values[] = { 5, 20, 29, 32, 63 };

int main () {
   int *item;
   int key = 32;

   /* using bsearch() to find value 32 in the array */
   item = (int*) bsearch (&key, values, 5, sizeof (int), cmpfunc);
   if ( item != NULL ) {
      printf("Found item = %d\n", *item);
   } else {
      printf("Item = %d could not be found\n", *item);
   }

   return(0);
}
```


## log C#

```c#
using System.IO;
using System.Diagnostics;

private static bool m_bLocalDebug = true;

public static void WriteLog(string strLog)
{
    if (!m_bLocalDebug) {
        return;
    }
    string sFilePath = "D:\\" + DateTime.Now.ToString("yyyyMM");
    string sFileName = "logfile" + Process.GetCurrentProcess().Id + "-" + DateTime.Now.ToString("dd") + ".log";
    sFileName = sFilePath + "\\" + sFileName; // 文件的绝对路径
    if (!Directory.Exists(sFilePath)) { // 验证路径是否存在
        Directory.CreateDirectory(sFilePath);
    }
    FileStream fs;
    bool create = false;
    if (File.Exists(sFileName)) {
        fs = new FileStream(sFileName, FileMode.Append, FileAccess.Write);
    }  else {
        fs = new FileStream(sFileName, FileMode.Create, FileAccess.Write);
        create = true;
    }
    StreamWriter sw = new StreamWriter(fs);
    if (create) {
        String commandLineString = System.Environment.CommandLine;
        String[] args = System.Environment.GetCommandLineArgs();
        sw.WriteLine(commandLineString);
        for (int i = 0; i < args.Length; i++) {
            sw.WriteLine(args[i]);
        }
        sw.WriteLine("--------");
    }
    sw.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH-mm-ss") + "   ---   " + strLog);
    sw.Close();
    fs.Close();
}
```


## log C++

```cpp
FILE *fp = NULL;
fp = fopen("D:\\camera.txt", "a");
if (fp)
{
    fprintf(fp, "%s %d \n", __FILE__, __LINE__);
    fclose(fp);
}

FILE* fp = NULL;
errno_t err = fopen_s(&fp, "E:\\irrlicht.txt", "a");
if (err == 0 && fp)
{
    fprintf(fp, "%s@x\n", lpcstr);
    fclose(fp);
}

char fpath[1024] = "";
_fullpath(fpath, fileLocation, 1024);
```


## C++ File

* ‘r’ 读
* ‘w’ 写
* ‘a’ 追加
* ‘r+’ == r+w（读写，可读可写，文件若不存在就报错 IOError）
* ‘w+’ == w+r（写读，可读可写，文件若不存在就创建）
* ‘a+’ == a+r（可追加可写，文件若不存在就创建）
* 对应的，如果是二进制文件，需要加一个 b：
* ‘rb’　　‘wb’　　‘ab’　　‘rb+’　　‘wb+’　　‘ab+’
* 注意！‘w’会抹去文件原有的内容，如果只是加新的内容应该用‘a’

```cpp
long getfilesize(const char* fpath) {
    FILE* fs = fopen(fpath, "rb");
    assert(fs);
    if (!fs) return -1;
    fseek(fs, 0, SEEK_END);
    long length = ftell(fs);
    // rewind(fs);
    fclose(fs);
    return length;
}

bool readfileSeek(const char* fpath, char* buffer, long readsize, long seek) {
    FILE* fs = fopen(fpath, "rb");
    assert(fs);
    if (!fs) return false;
    fseek(fs, seek, SEEK_SET);
    fread(buffer, 1, readsize, fs);
    fclose(fs);
    return true;
}

char* readfile(const char* fpath, long& length) {
    FILE* fs = fopen(fpath, "rb");
    assert(fs);
    if (!fs) return nullptr;
    fseek(fs, 0, SEEK_END);
    length = ftell(fs);
    rewind(fs);
    char* data = new char[length + 1];
    fread(data, 1, length, fs);
    data[length] = 0;
    fclose(fs);
    return data;
}

// 返回开始写文件的地址偏移。
long appendfile(const char* fpath, const char* data, long length) {
    FILE* fs = fopen(fpath, "ab");
    assert(fs);
    if (!fs) return -1;
    fseek(fs, 0, SEEK_END);
    long offset = ftell(fs);
    fwrite(data, 1, length, fs);
    fclose(fs);
    return offset;
}
```

```c++
bool IsFileRegular(const std::string &path) {
    struct stat st;
    if (stat(path.c_str(), &st))
        return false;
    return S_ISREG(st.st_mode);
}

bool IsDirectory(const std::string &path)
{
    struct stat st;
    if (stat(path.c_str(), &st))
        return false;
    return S_ISDIR(st.st_mode);
}

bool IsFilePathExists(const char* path, bool exdir) // exdir 表示进行文件夹检查，不能是 文件夹
{
    // 如果指定的存取方式有效，则函数返回 0，否则函数返回 -1。
    int code = ::access(path, 0);
    if (0 == code) {
        if (exdir && IsDirectory(path)) {
            return false;
        }
        return true;
    }
    return false;
}

bool CreateDeepDirectory(const char* szPath)
{
    if (IsDirectory(szPath)) {
        return true;
    }
    if (IsFilePathExists(szPath, false))
        return false;

#ifdef __ANDROID__
    if (0 != ::mkdir(szPath, 0777))
#else
    if (0 != ::mkdir(szPath))
#endif
    {
        StringDup strPath(szPath);
        if (!PathRemoveFileName(strPath) || IsFilePathEmpty(strPath)) {
            return false;
        }

        if (!CreateDeepDirectory(strPath))
            return false;

#ifdef __ANDROID__
        if (0 != ::mkdir(szPath, 0777))
#else
        if (0 != ::mkdir(szPath))
#endif
            return false;
    }
    return true;
}

std::string GetAbsolutePath(const std::string& filename)
{
    if (filename.empty())
        return filename;
#if defined(_WIN32)
    char fpath[_MAX_PATH] = { 0 };
    char* p = _fullpath(fpath, filename.c_str(), _MAX_PATH);
    std::string tmp(p);
    return tmp;
#else
    char fpath[4096] = { 0 };
    char* p = realpath(filename.c_str(), fpath);
    std::string tmp(p);
    return tmp;
#endif
}
```


## C++ String

```cpp
#include <string>
#include <sstream>

template<typename T>
inline std::string stringify(const T& x)
{
    std::ostringstream o;
    if (!(o << x)) return "";
    return o.str();
}

template<typename T>
inline T fromString(char *s)
{
    std::string str = s;
    std::istringstream i(str);
    T x;
    i >> x;
    return x;
}
```

```cpp
#include <iostream>
#include <string>
#include <locale>
#include <codecvt>
#include <iomanip>

// wide to UTF-8
static std::string wstring_to_stringUTF8(const std::wstring& wstr) {
    std::wstring_convert<std::codecvt_utf8<wchar_t>, wchar_t>() conv;
    return conv.to_bytes(wstr);
}

// wide to UTF-16le
static std::string wstring_to_stringUTF16le(const std::wstring& wstr) {
    std::wstring_convert<std::codecvt_utf16<wchar_t, 0x10ffff, std::little_endian>> conv;
    return conv.to_bytes(wstr);
}

std::wstring utf8_to_wstr( const std::string& utf8 ) {
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> wcu8;
    return wcu8.from_bytes( utf8 );
}

std::string wstr_to_utf8( const std::wstring& utf16 ) {
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> wcu8;
    return wcu8.to_bytes( utf16 );
}
```

```cpp
#include "stdafx.h"
#include <assert.h>
#include <string>

// 有的字符串可能会编码失败。
std::wstring CharToWChar(const char* str, size_t encode = CP_ACP) {
    int srclen = strlen(str);
    int len = MultiByteToWideChar(encode, 0, str, srclen, NULL, 0);
    if (len <= 0) {
        return L"";
    }
    wchar_t* temp = new wchar_t[len + 1];
    MultiByteToWideChar(encode, 0, str, srclen, temp, len);
    temp[len] = '\0';
    std::wstring wstr = temp;
    delete[] temp;
    return wstr;
}

// 有的字符串可能会编码失败。
std::string WCharToChar(const wchar_t* wstr, size_t encode = CP_ACP) {
    int srclen = wcslen(wstr);
    int len = WideCharToMultiByte(encode, 0, wstr, srclen, NULL, 0, NULL, NULL);
    if (len <= 0) {
        return "";
    }
    char* temp = new char[len + 1];
    WideCharToMultiByte(encode, 0, wstr, srclen, temp, len, NULL, NULL);
    temp[len] = '\0';
    std::string str = temp;
    delete[] temp;
    return str;
}
```


## 字符串加解密

这个存在缺陷，如果转码失败会不可逆：

```cpp
wchar_t bkHexWChar(const wchar_t* buffer, int cntlen = 4) {
    wchar_t* num = new wchar_t[cntlen + 1];
    memcpy(num, buffer, cntlen * sizeof(wchar_t));
    num[cntlen] = 0;
    wchar_t ch = wcstol(num, NULL, 16);
    delete[] num;
    return ch;
}

int bkHexChar(const char* buffer, int cntlen = 2) {
    char* num = new char[cntlen + 1];
    memcpy(num, buffer, cntlen * sizeof(char));
    num[cntlen] = 0;
    int ch = strtol(num, NULL, 16);
    delete[] num;
    return ch;
}

CString toHexString(CString str) {
    std::string strk = WCharToChar(str.GetString());
    const int length = strk.length();
    const char* buffer = strk.c_str();
    assert(length >= 0 && length <= 0xffff);
    CString retv;
    retv.AppendFormat(L"%04x", length);
    for (int i = 0; i < length; i++) {
        // 宽字符型 wchar_t (unsigned short.)
        // wchar_t ch = buffer[i];
        // assert(ch >= 0 && ch <= 0xffff);
        unsigned char ch = buffer[i];
        assert(ch >= 0 && ch <= 0xff);
        retv.AppendFormat(L"%02x", ch);
    }
    return retv;
}

CString bkHexString(CString str) {
    std::string strk = WCharToChar(str.GetString());
    int srclen = strk.length();
    assert((srclen - 4) % 2 == 0 && srclen >= 4);
    if ((srclen - 4) % 2 != 0 || srclen < 4) {
        return L"";
    }
    const char* buffer = strk.c_str();
    const int length = bkHexChar(&buffer[0], 4);
    assert(length == (srclen - 4) / 2);
    if (length != (srclen - 4) / 2) {
        return L"";
    }
    CStringA retv;
    for (int i = 0; i < length; i++) {
        char ch = bkHexChar(&buffer[4 + i * 2]);
        retv.AppendChar(ch);
    }
    std::wstring temp = CharToWChar(retv.GetString());
    CString wstr = temp.c_str();
    return wstr;
}

int _tmain(int argc, _TCHAR* argv[])
{
    CString test = L"中文 123";

    test = toHexString(test);
    test = bkHexString(test);

    test = bkHexString(L"0004ffffff01");
    test = toHexString(test);
    return 0;
}
```

这个方案，加密字符串长一点，但是肯定没问题：

<div class="highlighter-rouge" foldctrl="1"></div>

```cpp
#include <assert.h>

#define ALG_TYPE 0x321

class b62 {
  public:
    static int ParseBase62(wchar_t ch) {
        if (ch >= L'0' && ch <= L'9') {
            return ch - L'0';
        }
        if (ch >= L'a' && ch <= L'z') {
            return ch - L'a' + 10;
        }
        if (ch >= L'A' && ch <= L'Z') {
            return ch - L'A' + 10 + 26;
        }
        return -1;
    }

    static int appendHex(CString& retv, unsigned long value) {
        int len = 0;
        for (unsigned long temp = value; len == 0 || temp; temp /= 62) {
            len++;
        }

        static wchar_t SZ_BASE62_TAB[] = L"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        retv.AppendChar(SZ_BASE62_TAB[len]);
        for (int i = 0; i < len; i++) {
            int node = value % 62;
            retv.AppendChar(SZ_BASE62_TAB[node]);
            value /= 62;
        }
        return len;
    }

    static unsigned long eatupHex(const wchar_t* ptr, unsigned int& index) {
        int len = ParseBase62(ptr[index++]);
        unsigned long value = 0;
        unsigned long mulval = 1;
        for (int i = 0; i < len; i++) {
            int node = ParseBase62(ptr[index++]);
            value += node * mulval;
            mulval *= 62;
        }
        return value;
    }

    static CString toHexString(CString str) {
        const int length = str.GetLength();
        const wchar_t* buffer = str.GetString();

        CString retv;
        appendHex(retv, ALG_TYPE);
        appendHex(retv, length);
        wchar_t check = 0;
        for (int i = 0; i < length; i++) {
            wchar_t ch = buffer[i]; // <= 0xffff
            appendHex(retv, ch ^ ALG_TYPE);
            check ^= ch;
        }
        appendHex(retv, check);
        return retv;
    }

    static CString bkHexString(CString str) {
        unsigned int index = 0;

        const wchar_t* buffer = str.GetString();
        const int algType = eatupHex(buffer, index);
        if (algType != ALG_TYPE) {
            return L"??<unknow type>";
        }

        CString retv;
        wchar_t check = 0;
        const int length = eatupHex(buffer, index);
        for (int i = 0; i < length; i++) {
            wchar_t ch = eatupHex(buffer, index) ^ ALG_TYPE;
            retv.AppendChar(ch);
            check ^= ch;
        }

        wchar_t checkz = eatupHex(buffer, index);
        assert(checkz == check);
        if (checkz != check) {
            return L"??<check error>";
        }
        return retv;
    }

}; // namespace b62
```


## StringHelper

```cpp
#pragma once

#include <string>
#include <sstream>
#include <vector>
#include <stdexcept>
#include <cctype>
#include <algorithm>
#include <codecvt>

class StringHelper
{
public:
    static std::wstring toLower(std::wstring source)
    {
        std::transform(source.begin(), source.end(), source.begin(), [](unsigned char c){ return std::tolower(c); });
        return source;
    }

    static std::wstring toUpper(std::wstring source)
    {
        std::transform(source.begin(), source.end(), source.begin(), [](unsigned char c){ return std::toupper(c); });
        return source;
    }

    static std::wstring trimStart(std::wstring source, const std::wstring &trimChars = L" \t\n\r\v\f")
    {
        return source.erase(0, source.find_first_not_of(trimChars));
    }

    static std::wstring trimEnd(std::wstring source, const std::wstring &trimChars = L" \t\n\r\v\f")
    {
        return source.erase(source.find_last_not_of(trimChars) + 1);
    }

    static std::wstring trim(std::wstring source, const std::wstring &trimChars = L" \t\n\r\v\f")
    {
        return trimStart(trimEnd(source, trimChars), trimChars);
    }

    static std::wstring replace(std::wstring source, const std::wstring &find, const std::wstring &replace)
    {
        std::size_t pos = 0;
        while ((pos = source.find(find, pos)) != std::wstring::npos)
        {
            source.replace(pos, find.length(), replace);
            pos += replace.length();
        }
        return source;
    }

    static bool startsWith(const std::wstring &source, const std::wstring &value)
    {
        if (source.length() < value.length())
            return false;
        else
            return source.compare(0, value.length(), value) == 0;
    }

    static bool endsWith(const std::wstring &source, const std::wstring &value)
    {
        if (source.length() < value.length())
            return false;
        else
            return source.compare(source.length() - value.length(), value.length(), value) == 0;
    }

    static std::vector<std::wstring> split(const std::wstring &source, wchar_t delimiter)
    {
        std::vector<std::wstring> output;
        std::wistringstream ss(source);
        std::wstring nextItem;

        while (std::getline(ss, nextItem, delimiter))
        {
            output.push_back(nextItem);
        }

        return output;
    }

    template<typename T>
    static std::wstring toString(const T& subject)
    {
        std::wostringstream ss;
        ss << subject;
        return ss.str();
    }

    template<typename T>
    static std::string toStringA(const T& subject)
    {
        std::ostringstream ss;
        ss << subject;
        return ss.str();
    }

    template<typename T>
    static T fromString(const std::wstring &subject)
    {
        std::wistringstream ss(subject);
        T target;
        ss >> target;
        return target;
    }

    template<typename T>
    static T fromStringA(const std::string &subject)
    {
        std::istringstream ss(subject);
        T target;
        ss >> target;
        return target;
    }

    static bool isEmptyOrWhiteSpace(const std::wstring &source)
    {
        if (source.length() == 0)
            return true;
        else
        {
            for (std::size_t index = 0; index < source.length(); index++)
            {
                if (!std::isspace(source[index]))
                    return false;
            }

            return true;
        }
    }
};
```

```cpp
class StringHelper
{
public:
    template<typename T>
    static std::wstring formatSimple(const std::wstring &input, T arg)
    {
        std::wostringstream ss;
        std::size_t lastCloseBrace = std::wstring::npos;
        std::size_t openBrace = std::wstring::npos;
        while ((openBrace = input.find(L'{', openBrace + 1)) != std::wstring::npos)
        {
            if (openBrace + 1 < input.length())
            {
                if (input[openBrace + 1] == L'{')
                {
                    openBrace++;
                    continue;
                }

                std::size_t closeBrace = input.find(L'}', openBrace + 1);
                if (closeBrace != std::wstring::npos)
                {
                    ss << input.substr(lastCloseBrace + 1, openBrace - lastCloseBrace - 1);
                    lastCloseBrace = closeBrace;

                    std::wstring index = trim(input.substr(openBrace + 1, closeBrace - openBrace - 1));
                    if (index == L"0")
                        ss << arg;
                    else
                        throw std::runtime_error("Only simple positional format specifiers are handled by the 'formatSimple' helper method.");
                }
            }
        }

        if (lastCloseBrace + 1 < input.length())
            ss << input.substr(lastCloseBrace + 1);

        return ss.str();
    }

    template<typename T>
    static std::wstring formatSimple(const std::wstring &input, const std::vector<T> &args)
    {
        std::wostringstream ss;
        std::size_t lastCloseBrace = std::wstring::npos;
        std::size_t openBrace = std::wstring::npos;
        while ((openBrace = input.find(L'{', openBrace + 1)) != std::wstring::npos)
        {
            if (openBrace + 1 < input.length())
            {
                if (input[openBrace + 1] == L'{')
                {
                    openBrace++;
                    continue;
                }

                std::size_t closeBrace = input.find(L'}', openBrace + 1);
                if (closeBrace != std::wstring::npos)
                {
                    ss << input.substr(lastCloseBrace + 1, openBrace - lastCloseBrace - 1);
                    lastCloseBrace = closeBrace;
                    std::wstring index = trim(input.substr(openBrace + 1, closeBrace - openBrace - 1));
                    ss << args[std::stoi(index)];
                }
            }
        }

        if (lastCloseBrace + 1 < input.length())
            ss << input.substr(lastCloseBrace + 1);

        return ss.str();
    }

    template<typename T1, typename T2>
    static std::wstring formatSimple(const std::wstring &input, T1 arg1, T2 arg2)
    {
        std::wostringstream ss;
        std::size_t lastCloseBrace = std::wstring::npos;
        std::size_t openBrace = std::wstring::npos;
        while ((openBrace = input.find(L'{', openBrace + 1)) != std::wstring::npos)
        {
            if (openBrace + 1 < input.length())
            {
                if (input[openBrace + 1] == L'{')
                {
                    openBrace++;
                    continue;
                }

                std::size_t closeBrace = input.find(L'}', openBrace + 1);
                if (closeBrace != std::wstring::npos)
                {
                    ss << input.substr(lastCloseBrace + 1, openBrace - lastCloseBrace - 1);
                    lastCloseBrace = closeBrace;

                    std::wstring index = trim(input.substr(openBrace + 1, closeBrace - openBrace - 1));
                    if (index == L"0")
                        ss << arg1;
                    else if (index == L"1")
                        ss << arg2;
                    else
                        throw std::runtime_error("Only simple positional format specifiers are handled by the 'formatSimple' helper method.");
                }
            }
        }

        if (lastCloseBrace + 1 < input.length())
            ss << input.substr(lastCloseBrace + 1);

        return ss.str();
    }

    template<typename T1, typename T2, typename T3>
    static std::wstring formatSimple(const std::wstring &input, T1 arg1, T2 arg2, T3 arg3)
    {
        std::wostringstream ss;
        std::size_t lastCloseBrace = std::wstring::npos;
        std::size_t openBrace = std::wstring::npos;
        while ((openBrace = input.find(L'{', openBrace + 1)) != std::wstring::npos)
        {
            if (openBrace + 1 < input.length())
            {
                if (input[openBrace + 1] == L'{')
                {
                    openBrace++;
                    continue;
                }

                std::size_t closeBrace = input.find(L'}', openBrace + 1);
                if (closeBrace != std::wstring::npos)
                {
                    ss << input.substr(lastCloseBrace + 1, openBrace - lastCloseBrace - 1);
                    lastCloseBrace = closeBrace;

                    std::wstring index = trim(input.substr(openBrace + 1, closeBrace - openBrace - 1));
                    if (index == L"0")
                        ss << arg1;
                    else if (index == L"1")
                        ss << arg2;
                    else if (index == L"2")
                        ss << arg3;
                    else
                        throw std::runtime_error("Only simple positional format specifiers are handled by the 'formatSimple' helper method.");
                }
            }
        }

        if (lastCloseBrace + 1 < input.length())
            ss << input.substr(lastCloseBrace + 1);

        return ss.str();
    }
};
```


## pystring

```cpp
#ifndef INCLUDED_PYSTRING_H
#define INCLUDED_PYSTRING_H

#include <string>
#include <vector>

namespace pystring
{
    #define MAX_32BIT_INT 2147483647

    bool startswith( const std::string & str, const std::string & prefix, int start = 0, int end = MAX_32BIT_INT );
    bool endswith( const std::string & str, const std::string & suffix, int start = 0, int end = MAX_32BIT_INT );

    std::string strip( const std::string & str, const std::string & chars = "" );
    std::string lstrip( const std::string & str, const std::string & chars = "" );
    std::string rstrip( const std::string & str, const std::string & chars = "" );

    std::string upper( const std::string & str );
    std::string lower( const std::string & str );

    std::string mul( const std::string & str, int n);
    std::string join( const std::string & str, const std::vector< std::string > & seq );
    void split( const std::string & str, std::vector< std::string > & result, const std::string & sep = "", int maxsplit = -1);
    void splitlines(  const std::string & str, std::vector< std::string > & result, bool keepends = false );

    std::string replace( const std::string & str, const std::string & oldstr, const std::string & newstr, int count = -1);

    bool isalnum( const std::string & str );
    bool isalpha( const std::string & str );
    bool isdigit( const std::string & str );
    bool isspace( const std::string & str );
    bool islower( const std::string & str );
    bool isupper( const std::string & str );

namespace os
{
namespace path
{
    std::string basename(const std::string & path);
    std::string dirname(const std::string & path);
    std::string abspath(const std::string & path, const std::string & cwd);
    std::string join(const std::string & path1, const std::string & path2);
    std::string join(const std::vector< std::string > & paths);
    std::string normpath(const std::string & path);
    void split(std::string & head, std::string & tail, const std::string & path);
} // namespace path
} // namespace os

} // namespace pystring

#endif
```

```cpp
#include "pystring.h"

#include <algorithm>
#include <cctype>
#include <cstring>
#include <iostream>
#include <sstream>

namespace pystring
{

#if defined(_WIN32) || defined(_WIN64) || defined(_WINDOWS) || defined(_MSC_VER)
#ifndef WINDOWS
#define WINDOWS
#endif
#endif

typedef int Py_ssize_t;
const std::string forward_slash = "/";
const std::string double_forward_slash = "//";
const std::string triple_forward_slash = "///";
const std::string double_back_slash = "\\";
const std::string empty_string = "";
const std::string dot = ".";
const std::string double_dot = "..";
const std::string colon = ":";

#define ADJUST_INDICES(start, end, len)     \
    if (end > len)                          \
        end = len;                          \
    else if (end < 0) {                     \
        end += len;                         \
        if (end < 0)                        \
        end = 0;                            \
    }                                       \
    if (start < 0) {                        \
        start += len;                       \
        if (start < 0)                      \
        start = 0;                          \
    }

    namespace {

        void split_whitespace( const std::string & str, std::vector< std::string > & result, int maxsplit )
        {
            std::string::size_type i, j, len = str.size();
            for (i = j = 0; i < len; )
            {
                while ( i < len && ::isspace( str[i] ) ) i++;
                j = i;

                while ( i < len && ! ::isspace( str[i]) ) i++;

                if (j < i)
                {
                    if ( maxsplit-- <= 0 ) break;

                    result.push_back( str.substr( j, i - j ));

                    while ( i < len && ::isspace( str[i])) i++;
                    j = i;
                }
            }
            if (j < len)
            {
                result.push_back( str.substr( j, len - j ));
            }
        }

    } // anonymous namespace

    void split( const std::string & str, std::vector< std::string > & result, const std::string & sep, int maxsplit )
    {
        result.clear();

        if ( maxsplit < 0 ) maxsplit = MAX_32BIT_INT;//result.max_size();

        if ( sep.size() == 0 )
        {
            split_whitespace( str, result, maxsplit );
            return;
        }

        std::string::size_type i,j, len = str.size(), n = sep.size();

        i = j = 0;

        while ( i+n <= len )
        {
            if ( str[i] == sep[0] && str.substr( i, n ) == sep )
            {
                if ( maxsplit-- <= 0 ) break;

                result.push_back( str.substr( j, i - j ) );
                i = j = i + n;
            }
            else
            {
                i++;
            }
        }

        result.push_back( str.substr( j, len-j ) );
    }

    #define LEFTSTRIP 0
    #define RIGHTSTRIP 1
    #define BOTHSTRIP 2

    std::string do_strip( const std::string & str, int striptype, const std::string & chars  )
    {
        Py_ssize_t len = (Py_ssize_t) str.size(), i, j, charslen = (Py_ssize_t) chars.size();

        if ( charslen == 0 )
        {
            i = 0;
            if ( striptype != RIGHTSTRIP )
            {
                while ( i < len && ::isspace( str[i] ) )
                {
                    i++;
                }
            }

            j = len;
            if ( striptype != LEFTSTRIP )
            {
                do
                {
                    j--;
                }
                while (j >= i && ::isspace(str[j]));

                j++;
            }

        }
        else
        {
            const char * sep = chars.c_str();

            i = 0;
            if ( striptype != RIGHTSTRIP )
            {
                while ( i < len && memchr(sep, str[i], charslen) )
                {
                    i++;
                }
            }

            j = len;
            if (striptype != LEFTSTRIP)
            {
                do
                {
                    j--;
                }
                while (j >= i &&  memchr(sep, str[j], charslen)  );
                j++;
            }

        }

        if ( i == 0 && j == len )
        {
            return str;
        }
        else
        {
            return str.substr( i, j - i );
        }

    }

    std::string strip( const std::string & str, const std::string & chars )
    {
        return do_strip( str, BOTHSTRIP, chars );
    }

    std::string lstrip( const std::string & str, const std::string & chars )
    {
        return do_strip( str, LEFTSTRIP, chars );
    }

    std::string rstrip( const std::string & str, const std::string & chars )
    {
        return do_strip( str, RIGHTSTRIP, chars );
    }

    std::string join( const std::string & str, const std::vector< std::string > & seq )
    {
        std::vector< std::string >::size_type seqlen = seq.size(), i;

        if ( seqlen == 0 ) return empty_string;
        if ( seqlen == 1 ) return seq[0];

        std::string result( seq[0] );

        for ( i = 1; i < seqlen; ++i )
        {
            result += str + seq[i];

        }
        return result;
    }

    namespace
    {
        /* Matches the end (direction >= 0) or start (direction < 0) of self
         * against substr, using the start and end arguments. Returns
         * -1 on error, 0 if not found and 1 if found.
         */

        int _string_tailmatch(const std::string & self, const std::string & substr,
                              Py_ssize_t start, Py_ssize_t end,
                              int direction)
        {
            Py_ssize_t len = (Py_ssize_t) self.size();
            Py_ssize_t slen = (Py_ssize_t) substr.size();

            const char* sub = substr.c_str();
            const char* str = self.c_str();

            ADJUST_INDICES(start, end, len);

            if (direction < 0) {
                // startswith
                if (start+slen > len)
                    return 0;
            } else {
                // endswith
                if (end-start < slen || start > len)
                    return 0;
                if (end-slen > start)
                    start = end - slen;
            }
            if (end-start >= slen)
                return (!std::memcmp(str+start, sub, slen));

            return 0;
        }
    }

    bool endswith( const std::string & str, const std::string & suffix, int start, int end )
    {
        int result = _string_tailmatch(str, suffix,
                                       (Py_ssize_t) start, (Py_ssize_t) end, +1);
        //if (result == -1) // TODO: Error condition
        return static_cast<bool>(result);
    }

    bool startswith( const std::string & str, const std::string & prefix, int start, int end )
    {
        int result = _string_tailmatch(str, prefix,
                                       (Py_ssize_t) start, (Py_ssize_t) end, -1);
        //if (result == -1) // TODO: Error condition
        return static_cast<bool>(result);
    }

    bool isalnum( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;

        if ( len == 1 )
        {
            return ::isalnum( str[0] );
        }

        for ( i = 0; i < len; ++i )
        {
            if ( !::isalnum( str[i] ) ) return false;
        }
        return true;
    }

    bool isalpha( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::isalpha( (int) str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( !::isalpha( (int) str[i] ) ) return false;
        }
        return true;
    }

    bool isdigit( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::isdigit( str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( ! ::isdigit( str[i] ) ) return false;
        }
        return true;
    }

    bool islower( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::islower( str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( !::islower( str[i] ) ) return false;
        }
        return true;
    }

    bool isspace( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::isspace( str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( !::isspace( str[i] ) ) return false;
        }
        return true;
    }

    bool isupper( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::isupper( str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( !::isupper( str[i] ) ) return false;
        }
        return true;
    }

    std::string lower( const std::string & str )
    {
        std::string s( str );
        std::string::size_type len = s.size(), i;

        for ( i = 0; i < len; ++i )
        {
            if ( ::isupper( s[i] ) ) s[i] = (char) ::tolower( s[i] );
        }

        return s;
    }

    std::string upper( const std::string & str )
    {
        std::string s( str ) ;
        std::string::size_type len = s.size(), i;

        for ( i = 0; i < len; ++i )
        {
            if ( ::islower( s[i] ) ) s[i] = (char) ::toupper( s[i] );
        }

        return s;
    }

    std::string replace( const std::string & str, const std::string & oldstr, const std::string & newstr, int count )
    {
        int sofar = 0;
        int cursor = 0;
        std::string s( str );

        std::string::size_type oldlen = oldstr.size(), newlen = newstr.size();

        cursor = find( s, oldstr, cursor );

        while ( cursor != -1 && cursor <= (int)s.size() )
        {
            if ( count > -1 && sofar >= count )
            {
                break;
            }

            s.replace( cursor, oldlen, newstr );
            cursor += (int) newlen;

            if ( oldlen != 0)
            {
                cursor = find( s, oldstr, cursor );
            }
            else
            {
                ++cursor;
            }

            ++sofar;
        }

        return s;

    }

    void splitlines(  const std::string & str, std::vector< std::string > & result, bool keepends )
    {
        result.clear();
        std::string::size_type len = str.size(), i, j, eol;

         for (i = j = 0; i < len; )
         {
            while (i < len && str[i] != '\n' && str[i] != '\r') i++;

            eol = i;
            if (i < len)
            {
                if (str[i] == '\r' && i + 1 < len && str[i+1] == '\n')
                {
                    i += 2;
                }
                else
                {
                    i++;
                }
                if (keepends)
                eol = i;

            }

            result.push_back( str.substr( j, eol - j ) );
            j = i;

        }

        if (j < len)
        {
            result.push_back( str.substr( j, len - j ) );
        }

    }

    std::string mul( const std::string & str, int n )
    {
        // Early exits
        if (n <= 0) return empty_string;
        if (n == 1) return str;

        std::ostringstream os;
        for(int i=0; i<n; ++i)
        {
            os << str;
        }
        return os.str();
    }
} // namespace pystring
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-09-14-tiny-source-code.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/okcai/article/details/186241]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/blog.csdn.net/347ffe95.html" %})
- [https://dirtysalt.github.io/html/writing-clean-code.html]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/dirtysalt.github.io/c2b4a624.html" %})
- [https://www.tutorialspoint.com/c_standard_library/c_function_bsearch.htm]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/www.tutorialspoint.com/c5079b0f.htm" %})
- [https://www.tutorialspoint.com/c_standard_library/c_function_qsort.htm]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/www.tutorialspoint.com/0bec0743.htm" %})
