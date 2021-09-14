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


## C++ String

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



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-09-14-tiny-source-code.md.js" %}'></script></p>
