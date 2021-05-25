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

- [https://github.com/Tencent/secguide/blob/main/C%2CC%2B%2B%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md]({% include relrefx.html url="/backup/2021-05-25-prog-secguide.md/github.com/a22343f4.html" %})
