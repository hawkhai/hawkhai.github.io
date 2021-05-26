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


## C++11 新特性快速一览


### 关键字及新语法

#### auto 关键字

#### nullptr 关键字

#### for 循环语法


### STL 容器

#### std::array

#### std::forward_list

#### std::unordered_map

#### std::unordered_set


### 多线程

#### std::thread

#### std::atomic

#### std::condition_variable


### 智能指针

#### std::shared_ptr

#### std::weak_ptr


### 其它

#### std::function

#### std::bind 封装可执行对象

#### lambda 表达式


## C++11 中的四种智能指针

std | boost | 功能说明
---- | ---- | ----
unique_ptr | scoped_ptr | 独占指针对象，并保证指针所指对象生命周期与其一致
shared_ptr | shared_ptr | 可共享指针对象，可以赋值给 shared_ptr 或 weak_ptr。<br/>指针所指对象在所有的相关联的 shared_ptr 生命周期结束时结束，是强引用。
weak_ptr | weak_ptr | 它不能决定所指对象的生命周期，引用所指对象时，需要 lock() 成 shared_ptr 才能使用。

* **auto_ptr** **不再推荐**。赋值转移后，指针会置空。因为 auto_ptr 有拷贝语义，拷贝后原对象变得无效，再次访问原对象时会导致程序崩溃；
    * 智能指针不能指向数组。因为其实现中调用的是 delete 而非 delete[]。
* **unique_ptr** unique_ptr 则禁止了拷贝语义，但提供了移动语义，即可以使用 std::move() 进行控制权限的转移。

  ```cpp
  #include <iostream>
  #include <memory>

  unique_ptr<string> upt(new string("lvlv"));
  unique_ptr<string> upt1(upt);   // 编译出错，已禁止拷贝
  unique_ptr<string> upt1 = upt;  // 编译出错，已禁止拷贝
  unique_ptr<string> upt1 = std::move(upt);   // 控制权限转移
  if (upt.get() != nullptr) {                 // 判空操作更安全
      // do something
  }
  upt1.release(); // 释放所有权

  auto_ptr<string> apt(new string("lvlv"));
  auto_ptr<string> apt1(apt);     // 编译通过
  auto_ptr<string> apt1 = apt;    // 编译通过
```
* **shared_ptr** 不要用一个原始指针初始化多个 shared_ptr，否则会造成二次释放同一内存。
    * 模型循环依赖（互相引用或环引用）时，计数会不正常。

  ```cpp
  shared_ptr<Resourse> CreateResourse() {
      return make_shared<Resourse>(1);
  }
```
    * 注册销毁函数

  ```cpp
  #include<iostream>
  #include<memory>

  using namespace std;

  struct MyStruct {
      int *p;
      MyStruct():p(new int(10)) {}
  };

  int main() {
      MyStruct st;
      {
          shared_ptr<MyStruct> sp(&st, [](MyStruct *ptr) {
              delete(ptr->p);
              ptr->p = nullptr;
              cout<<"destructed"<<endl;
          });
      }
      if(st.p != nullptr)
          cout << "no destroyed" << endl;
      else
          cout << "be destroyed" << endl;
      return 0;
  }
  // 运行结果:
  // destructed
  // be destroyed
```
* **weak_ptr**
    * 循环引用问题

  ```cpp
  class Monster {
      // 尽管父子可以互相访问，但是彼此都是独立的个体，无论是谁都不应该拥有另一个人的所有权。
      std::weak_ptr<Monster> m_father;    // 所以都把 shared_ptr 换成了 weak_ptr
      std::weak_ptr<Monster> m_son;       // 同上
  public:
      void setFather(std::shared_ptr<Monster>& father);   // 实现细节懒得写了
      void setSon(std::shared_ptr<Monster>& son);         // 懒
      ~Monster(){std::cout << "A monster die!";}          // 析构时发出死亡的悲鸣
  };

  void runGame(){
      std::shared_ptr<Monster> father = new Monster();
      std::shared_ptr<Monster> son = new Monster();
      father->setSon(son);
      son->setFather(father);
  }

  void runGame(){
      std::shared_ptr<Monster> monster1 = new Monster();
      std::weak_ptr<Monster> r_monster1 = monster1;
      r_monster1->doSomething(); // Error! 编译器出错！weak_ptr 没有重载 * 和 -> ，无法直接当指针用
      std::shared_ptr<Monster> s_monster1 = r_monster1.lock(); // OK! 可以通过 weak_ptr 的 lock 方法获得 shared_ptr。
  }
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

- [https://github.com/preshing/junction]({% include relrefx.html url="/backup/2021-05-25-prog-secguide.md/github.com/f3798178.html" %})
- [https://github.com/oneapi-src/oneTBB]({% include relrefx.html url="/backup/2021-05-25-prog-secguide.md/github.com/acfc8855.html" %})
- [https://github.com/Tencent/secguide/blob/main/C%2CC%2B%2B%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md]({% include relrefx.html url="/backup/2021-05-25-prog-secguide.md/github.com/a22343f4.html" %})
