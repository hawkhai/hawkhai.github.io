---
layout: post
title: "编程与调试 -- C/C++ 编程指南 & Microsoft Writing Clean Code"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "编程指南"
---

```cpp
std::lock_guard<std::mutex> locker(m_mutex);
std::unique_lock<std::mutex> locker(m_mutex);
std::wstring_convert<std::codecvt_utf8<wchar_t>> strConvert;
std::unique_ptr<EngineBase> srcEngine;
std::make_shared<SelectAreaRecognition>(selector, parent);
std::make_tuple(printerInfo, false);
```

最近一直在思考大型工程的维护。
1. 保证 Debug 版本能编译出来。更多的运行时检查。
2. 保证 x64 版本能编译出来。页堆才能顺利开启。
3. 优选 MT 版本。将来可以单模块升级编译器。
4. 编译器及时升级，提升工作效率。新的软硬件特性能及时用上。


## 使用断言

* 断言 assert 是仅在 Debug 版本起作用的宏，它用于检查“不应该”发生的情况。
    * 如果程序在 assert 处终止了，并不是说含有该 assert 的函数有错误，而是调用者出了差错，assert 可以帮助我们找到发生错误的原因。
    * 使用断言捕捉不应该发生的非法情况。不要混淆非法情况与错误情况之间的区别，后者是必然存在的并且是一定要作出处理的。
    * 当进行防错设计时，如果“不可能发生”的事情的确发生了，则要使用断言进行报警。然后 release 版本给予合理的处理。
        * 从源头去分析断言发生的条件是否合理，区分好究竟是异常还是断言。

  ```cpp
  // const 保证参数不会搞反。
  char* strcpy(char* dest, const char* src) {
      // 断言，Debug 版本生效。
      assert((dest != NULL) && (src != NULL));
      // 入参检查，特殊情况处理。
      if (src == NULL || dest == NULL) return dest;
      char* address = dest; // 功能逻辑
      while ((*dest++ = *src++) != '\0')
          NULL;
      return address;
  }
```

* 要使用断言对函数参数进行确认，利用断言来检查不可能发生的情况。
    * 要从程序中删去无定义的特性，或者在程序中使用断言来检查出无定义特性的非法使用。
    * 断言不是用来检查错误的。用来检查在该程序正常工作时绝不应该发生的非法情况，不是所测试的是错误情况，是在其最终产品中肯定会出现并且必须对其进行处理的错误情况。
    * 消除所做的隐式假定，或者利用断言检查其正确性，这些措施使得该程序极少可能被不正确地使用。

* 假如你受雇为核反应堆编写软件，就必须对堆芯过热这一情况进行处理。
    * 某些程序员解决这个问题的方法可以是自动地向堆芯灌水、插入冷却棒或者是能使反应堆冷却下来的一些其他什么方法。而且，只要程序已经控制了势态就不必向有关人员发出警报。
    * 另一些程序员可能会选择另一种方法，即只要堆芯过热就向反应堆工作人员发出警报。虽然相应的处理仍由计算机自动进行，不同的是操作员总是知道这件事。
    * **在进行防错性程序设计时，不要隐瞒错误。** 堆芯不会无缘无故地出现过热现象，一定是发生了某种不同寻常的事情，才会引起这一故障。因此在计算机进行相应处理的同时，最好使操作人员搞清楚发生了什么事情以避免事故的再次发生。


## 为子系统设防

* 要记住调试代码是多余的代码，而不是不同的代码。

```cpp
Flag fResizeMemory(void** ppv, size_t sizeNew) {

    byte** ppb = (byte**) ppv;

    ASSERT(ppb != NULL && sizeNew != 0);
#ifdef DEBUG
    {
        // 如果不是 realloc 扩大内存块时使原有存储位置发生移动这种现象很罕见。
        // 如果某件事甚少发生的话，设法使其经常发生。
        size_t sizeOld = sizeofBlock(*ppb);
        /*
         * 如果缩小，先把将被释放的内存空间填写上废料
         * 如果扩大，通过模拟 realloc 的操作来迫使新的内存块产生移动
         *（不让它在原有的位置扩展）如果新块和老块的长度相同，不做任何事情
         */

        if (sizeNew < sizeOld)
            memset((*ppb)+sizeNew, bGarbage, sizeOld-sizeNew);
        else if (sizeNew > sizeOld) {
            byte* pbNew;
            if ( fNewMemory(&pbNew, sizeNew) ) {
                memcpy(pbNew, *ppb, sizeOld);
                FreeMemory(*ppb);
                *ppb = pbNew;
            }
        }
    }
#endif

    byte* pbResize = (byte*) realloc(*ppb, sizeNew);
    // ……
}
```


## 糖果机界面

* 接口设计的，想用错都很难。一个深刻的例子是油门和刹车都是右脚踩。
    * 如果设计的左脚刹车右脚油门，当人在慌张的时候，会两只脚踩下去，直接爆缸。
    * 当油门和刹车都是右脚踩，这两种操作就天然互斥了，同时被踩下的可能就没有了。
    * 一个非常糟糕的例子就是标准 C 里面的：`int ch = getchar();`。

* 要使用户不容易忽视错误情况，不要在正常地返回值中隐藏错误代码。
* 要不遗余力地寻找并消除函数界面中的缺陷。


## 内存管理

注意当数组作为函数的参数进行传递时，该数组自动退化为同类型的指针。

```cpp
// 计算数组和指针的内存容量
char a[] = "hello world";
char *p  = a;
cout << sizeof(a) << endl;   // 12 字节
cout << sizeof(p) << endl;   // 4 字节

// 数组退化为指针
void Func(char a[100]) {
    cout<< sizeof(a) << endl;   // 4 字节而不是 100 字节
}
```

malloc 与 free 是 C++/C 语言的标准库函数，new/delete 是 C++ 的运算符。它们都可用于申请动态内存和释放内存。


### 单一功能的内存管理程序

反例：`void* realloc( void* pv, size_t size );`
* 如果该内存块的新长度小于老长度，realloc 释放该块尾部不再想要的内存空间，返回的 pv 不变。
* 如果该内存块的新长度大于老长度，扩大后的内存块有可能被分配到新的地址处，该块的原有内容被拷贝到新的位置。
    返回的指针指向扩大后的内存块，并且该块扩大部分的内容未经初始化。
* 如果满足不了扩大内存块的请求，realloc 返回 NULL，当缩小内存块时，realloc 总会成功。
* 如果 pv 为 NULL，那么 realloc 的作用相当于调用 malloc(size)，并返回指向新分配内存块的指针，或者在该请求无法满足时返回 NULL。
* 如果 pv 不是 NULL，但新的块长为零，那么 realloc 的作用相当于调用 free(pv) 并且总是返回 NULL。
* 如果 pv 为 NULL 且当前的内存块长为零，结果无定义。


## 成员函数的重载、覆盖与隐藏

* 如果派生类的函数与基类的函数同名，但是参数不同。此时，不论有无 virtual 关键字，基类的函数将被隐藏（注意别与重载混淆）。
* 如果派生类的函数与基类的函数同名，并且参数也相同，但是基类函数没有 virtual 关键字。此时，基类的函数被隐藏（注意别与覆盖混淆）。
    * 无论是否 virtual，都可以用父类名 ::Func 调用到具体的实现。

```cpp
#include <iostream>

using namespace std;

class Base
{
public:
    virtual void f(float x) { cout << "Base::f(float) " << x << endl; }
    void g(float x) { cout << "Base::g(float) " << x << endl; }
    void h(float x) { cout << "Base::h(float) " << x << endl; }
};

class Derived : public Base
{
public:
    virtual void f(float x) { cout << "Derived::f(float) " << x << endl; } // 重载
    void g(int x) { cout << "Derived::g(int) " << x << endl; }
    void h(float x) { cout << "Derived::h(float) " << x << endl; }
};

int main()
{
    Derived d;
    Base* pb = &d;
    Derived* pd = &d;
    // Good : behavior depends solely on type of the object
    pb->f(3.14f); // Derived::f(float) 3.14
    pd->f(3.14f); // Derived::f(float) 3.14
    // Bad : behavior depends on type of the pointer
    pb->g(3.14f); // Base::g(float) 3.14
    pd->g(3.14f); // Derived::g(int) 3        (surprise!)
    // Bad : behavior depends on type of the pointer
    pb->h(3.14f); // Base::h(float) 3.14      (surprise!)
    pd->h(3.14f); // Derived::h(float) 3.14
    return 0;
}
```


## 内联函数的编程风格

关键字 inline 必须与函数定义体放在一起才能使函数成为内联，仅将 inline 放在函数声明前面不起任何作用。

```cpp
void Foo(int x, int y);

// inline 是一种“用于实现的关键字”，而不是一种“用于声明的关键字”。
inline void Foo(int x, int y) { // inline 与函数定义体放在一起
    // …
}
```


## 类的构造函数、析构函数与赋值函数

对于任意一个类 A，如果不想编写上述函数，C++ 编译器将自动为 A 产生四个缺省的函数，如：
```cpp
A(void);                   // 缺省的无参数构造函数
A(const A &a);             // 缺省的拷贝构造函数
~A(void);                  // 缺省的析构函数
A& operator=(const A &a);  // 缺省的赋值函数，如果包含成员类，会递归调用成员类的 赋值函数
```

内存泄漏：
* 如果不主动编写拷贝构造函数和赋值函数，编译器将以“位拷贝”的方式自动生成缺省的函数。倘若类中含有指针变量，那么这两个缺省的函数就隐含了错误。
    以类 String 的两个对象 a,b 为例，假设 a.m_data 的内容为“hello”，b.m_data 的内容为“world”。
    现将 a 赋给 b，缺省赋值函数的“位拷贝”意味着执行 b.m_data = a.m_data。这将造成三个错误：
    * 一是 b.m_data 原有的内存没被释放，造成内存泄露；
    * 二是 b.m_data 和 a.m_data 指向同一块内存，a 或 b 任何一方变动都会影响另一方；
    * 三是在对象被析构时，m_data 被释放了两次。
* 拷贝构造函数和赋值函数非常容易混淆，常导致错写、错用。拷贝构造函数是在对象被创建时调用的，而赋值函数只能被已经存在了的对象调用。
    * C++11 还有一个移动拷贝函数。

```cpp
String a("hello");
String b("world");
String c = a; // 调用了拷贝构造函数，最好写成 c(a);
c = b; // 调用了赋值函数
```


## 类的继承与组合

只要是可能被继承的类，析构都需要是虚的。
基类与派生类的析构函数应该为虚（即加 virtual 关键字）。
* 正常的 C++ 类都是派生类的析构执行后再自动执行基类的析构，如果析构不带 virtual 关键字，那么就不符合 C++ 类的标准行为，可能会导致基类的内存没有机会释放。

* Review by 豪哥

{% include image.html url="/assets/images/210526-prog-microsoft-cpp-styl~3c/microsoft-cpp-styleguide.jpg" caption="微软 C 编程精粹 -- Microsoft 编写优质无错 C 程序秘诀.pdf" %}

编程精粹 Microsoft 编写优质无错代码的秘诀 (Writing Clean Code)
这本书的内容大多观点在微软编译器 debug & release 版本里面得到了实践。

* [高质量 C/C++ 编程指南 {% include relref_csdn.html %}](https://blog.csdn.net/x_iya/article/details/8714362)
* [编程精粹 -- Microsoft 编写优质无错 C 程序秘诀 {% include relref_csdn.html %}](https://blog.csdn.net/okcai/article/details/186241)
* [编程精粹 -- Microsoft 编写优质无错代码的秘诀 {% include relref_github.html %}](https://dirtysalt.github.io/html/writing-clean-code.html)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-26-prog-Microsoft-cpp-styleguide.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/x_iya/article/details/8714362]({% include relrefx.html url="/backup/2021-05-26-prog-Microsoft-cpp-styleguide.md/blog.csdn.net/6c268139.html" %})
- [https://blog.csdn.net/okcai/article/details/186241]({% include relrefx.html url="/backup/2021-05-26-prog-Microsoft-cpp-styleguide.md/blog.csdn.net/347ffe95.html" %})
- [https://dirtysalt.github.io/html/writing-clean-code.html]({% include relrefx.html url="/backup/2021-05-26-prog-Microsoft-cpp-styleguide.md/dirtysalt.github.io/c2b4a624.html" %})
