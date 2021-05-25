---
layout: post
title: "编程笔记 -- C / C++ 代码安全指南"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## 变量名

[Code reivew 质量保证](https://cheetahfun.feishu.cn/docs/doccnqqrovuzyC5mPw5QEdzDq5F)
- 变量的命名遵从匈牙利记法。即：前缀 + 类型 + 名称。
- 格式：\[m_\|ms_\|s_\|g_\] type [class name \| struct name] variable name

前缀 explame:
- m_ ：类的成员变量
- ms_：类的静态成员变量
- s_ ：静态全局变量
- g_ ：普通全局变量

类型 explame:
- char、TCHAR、wchar_t：ch
- 字符串数组：sz
- int、int64……：n
- unsigned：u
- long：l
- double、float：f
- WORD：w
- DWORD：dw
- function：fn
- pointer：p

```cpp
// 变量名组合 explame
char* pszExplame;
unsigned long long ullExplame;
```


## 注意隐式符号转换

两个无符号数相减为负数时，结果应当为一个很大的无符号数，但是小于 int 的无符号数在运算时可能会有预期外的隐式符号转换。

```cpp
// 1
unsigned char a = 1;
unsigned char b = 2;
auto c = a - b; // int
if (a - b < 0)  // a - b = -1 (signed int)
    a = 6; // target
else
    a = 8;
// 2
unsigned char a = 1;
unsigned short b = 2;
auto c = a - b; // int
if (a - b < 0)  // a - b = -1 (signed int)
    a = 6; // target
else
    a = 8;
```
上述结果均为 a=6

```cpp
// 3
unsigned int a = 1;
unsigned short b = 2;
auto c = a - b; // unsigned int
if (a - b < 0)  // a - b = 0xffffffff (unsigned int)
    a = 6;
else
    a = 8; // target
// 4
unsigned int a = 1;
unsigned int b = 2;
auto c = a - b; // unsigned int
if (a - b < 0)  // a - b = 0xffffffff (unsigned int)
    a = 6;
else
    a = 8; // target
```
上述结果均为 a=8

如果预期为 8，则错误代码：

```cpp
// Bad
unsigned short a = 1;
unsigned short b = 2;
auto c = a - b; // int
if (a - b < 0)  // a - b = -1 (signed int)
    a = 6; // target
else
    a = 8;
```

正确代码：

```cpp
// Good
unsigned short a = 1;
unsigned short b = 2;
auto c = (unsigned int)a - (unsigned int)b; // unsigned int
if ((unsigned int)a - (unsigned int)b < 0)  // a - b = 0xffff (unsigned short)
    a = 6;
else
    a = 8; // target
```


## 断言

debug 版本进行 JIT 检查。

```cpp
// Good
const int nWeekdays[] = { 1, 2, 3, 4, 5, 6, 7 };
const char* sWeekdays[] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};
assert(ARRAY_SIZE(nWeekdays) == ARRAY_SIZE(sWeekdays));
for (int x = 0; x < ARRAY_SIZE(sWeekdays); x++) {
    if (strcmp(sWeekdays[x], input) == 0) {
        return nWeekdays[x];
    }
}
```

个人理解：内部逻辑，断言（这个就不该发生）；外部逻辑，抛出异常（发生了，需要得到处理）。


## 校验内存相关函数的返回值

与内存分配相关的函数需要检查其返回值是否正确，以防导致程序崩溃或逻辑错误。

```cpp
// Bad
void Foo() {
    char* bar = mmap(0, 0x800000, .....);
    *(bar + 0x400000) = '\x88'; // Wrong
}
```
如上例 mmap 如果失败，bar 的值将是 0xffffffff (ffffffff)，第二行将会往 0x3ffffff 写入字符，导致越界写。

```cpp
// Good
void Foo() {
    char* bar = mmap(0, 0x800000, .....);
    if(bar == MAP_FAILED) {
        return;
    }

    *(bar + 0x400000) = '\x88';
}
```


## rand() 类函数应正确初始化

```cpp
// Good
int main() {
    srand(time(0));
    int foo = rand();
    return foo;
}
```


## 编译警告

* 编译期函数返回值检查 `-Wreturn-type`
* 不得使用栈上未初始化的变量 `-Wuninitialized`
* 不要在 if 里面赋值 `-Wparentheses`
* 检查直接将数组和 0 比较的代码 `-Waddress`

```cmake
# MacOS     -Winconsistent-missing-override
# GCC 5.1   -Werror=suggest-override
# -pthread for g++
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x -pthread -Werror=return-type")
# error: format string is not a string literal (potentially insecure) [-Werror,-Wformat-security]
# APP_CLAGS：列出编译器标识，在编译任何模块的 C 和 C++ 源文件时这些标志都会被传给编译器
# APP_CPPFLAGS：列出编译器标识，在编译任何模块的 C++ 源文件时这些标志都会被传给编译器
LOCAL_CFLAGS += -Wno-error=format-security -Wreturn-type
LOCAL_CPPFLAGS += -Wno-error=c++11-narrowing -Wno-error=format-security -Wreturn-type
# 增加对 异常 和 rtti 的支持
LOCAL_CPPFLAGS += -fexceptions -frtti
```


## 匹对逻辑应该设计为 RAII，防止写漏


## concurrent_unordered_map

Concurrent data structures in C++
https://github.com/preshing/junction
concurrent_unordered_map
concurrent_unordered_multimap
concurrent_hash_map
https://github.com/oneapi-src/oneTBB


## 字符串拷贝

[C/C++ 安全指南 .md {% include relref_github.html %}](https://github.com/Tencent/secguide/blob/main/C%2CC%2B%2B%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md)
```cpp
// Good
char a[4] = {0};
_snprintf(a, sizeof(a), "%s", "AAAA");
a[sizeof(a) - 1] = '\0';
foo = strlen(a);
```


## 多线程


### 变量应确保线程安全性

```cpp
// Good
volatile char g_somechar;
void foo_thread1() {
    __sync_fetch_and_add(&g_somechar, 3);
}

void foo_thread2() {
    __sync_fetch_and_add(&g_somechar, 1);
}
```


## 避免相对路径导致的安全问题（DLL、EXE 劫持等问题）

在程序中，使用相对路径可能导致一些安全风险，例如 DLL、EXE 劫持等问题。
例如以下代码，可能存在劫持问题：
```cpp
int Foo() {
    // 传入的是 dll 文件名，如果当前目录下被写入了恶意的同名 dll，则可能导致 dll 劫持
    HINSTANCE hinst = ::LoadLibrary("dll_nolib.dll");
    if (hinst != NULL) {
        cout << "dll loaded!" << endl;
    }
    return 0;
}
```

针对 DLL 劫持的安全编码的规范：

1. 调用 LoadLibrary，LoadLibraryEx，CreateProcess，ShellExecute 等进行模块加载的函数时，指明模块的完整（全）路径，
    禁止使用相对路径，这样就可避免从其它目录加载 DLL。
2. 在应用程序的开头调用 SetDllDirectory(TEXT("")); 从而将当前目录从 DLL 的搜索列表中删除。
    结合 SetDefaultDllDirectories，AddDllDirectory，RemoveDllDirectory 这几个 API 配合使用，可以有效的规避 DLL 劫持问题。
    这些 API 只能在打了 KB2533623 补丁的 Windows7，2008 上使用。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-25-prog-secguide.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/preshing/junction]({% include relrefx.html url="/backup/2021-05-25-prog-secguide.md/github.com/f3798178.html" %})
- [https://github.com/oneapi-src/oneTBB]({% include relrefx.html url="/backup/2021-05-25-prog-secguide.md/github.com/acfc8855.html" %})
- [https://github.com/Tencent/secguide/blob/main/C%2CC%2B%2B%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md]({% include relrefx.html url="/backup/2021-05-25-prog-secguide.md/github.com/a22343f4.html" %})
