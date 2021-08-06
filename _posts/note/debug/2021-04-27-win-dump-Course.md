---
layout: post
title: "调试 Memory -- Windows Windbg dump 崩溃分析（课程笔记）"
author:
location: "珠海"
categories: ["调试"]
tags: ["调试", "Memory"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "WinDBG"
---

崩溃，高 CPU 占用，死锁，内存泄漏。
感觉最难处理的就是堆破坏，因为不知道被哪个线程写坏了的。
本文收集了几个例子。

* 堆破坏 谁破坏了堆内存
* 指针破坏 谁动了我的指针


## Windbg 调试技巧（taoge）


### dump 中信息获取

* VOID KiUserExceptionDispatcher(in PEXCEPTION_RECORD ExceptionRecord, in PCONTEXT ContextRecord)
* ExceptionRecord ContextRecord 崩溃时的上下文
* kb # 打印当前崩溃堆栈
* k kb = ebp esp eip 显示当前堆栈
* u ub # u\* 命令显示内存中指定程序代码的汇编转换。
* r # 寄存器查看修改
* d da du dd dt d, da, db, dc, dd, dD, df, dp, dq, du, dw（显示查看内存）
    * d 输入 d 在时候，显示格式是最近一次输入 d\* 中的命令，如果没有，则显示的是同 db 一样的内容
    * da 显示 ascii 码字符串，当遇到第一个空字节或者给出范围内的字符全部显示之后回停止显示，默认是 128 个字符
    * db Byte values and ASCII characters
    * dc Double-word values (4 bytes) and ASCII characters
    * dd 双字节
    * dD 按 double 类型浮点数显示
    * df 按 float 类型显示浮点数显示
    * dp 指针
    * dq 显示 8 个字节的 16 进制值
    * du 显示 unicode 字符
    * dw 每一行开头显示地址 ，然后显示每两个字节显示成 4 个 16 进制字符
* lmvm 查看模块信息


### windbg 实时调试

* AEDebug Windbg -I # 注册成实时调试器
* Image File Execution Options # 映像劫持的注册表
* bu # 下断点
* dv dd # 查看
* ba w4 # 比如要对内存 0x0483DFE 进行写操作的时候下断点，可以用命令 ba w4 0x0483DFE
* 在一个单例类的析构内去调用另一个单例 -- 会造成堆问题。
* sxe ld sxe ud
* bp script
* ba

{% include image.html url="/assets/images/210427-win-dump-course/zz1.png" %}

#### 根据模块崩溃偏移地址定位代码位置

1. 加载 pdb 符号表，windbg 运行 exe。
2. 通过 `bp BaseAddr+OffsetAddr` 下断点；
3. 然后通过 `bl` 查看当前断点。


## windbg 分析堆溢出

[windbg 分析堆溢出 {% include relref_csdn.html %}](https://blog.csdn.net/dailongjian2008/article/details/88081507)
《windows 高级调试》第 6.2.2 节，参考书中的方法进行。
1. 通过 windbg 分析堆块
2. 通过 windbg+ 普通页堆分析
3. 通过 windbg+ 完全页堆分析

[Windbg 使用 {% include relref_jianshu.html %}](https://www.jianshu.com/p/56b9afc8ae47)
* 错误代码：0xc0000374
* 错误含义：ACTIONABLE_HEAP_CORRUPTION_heap_failure_buffer_overrun
* 第一步、先用「!analyze -v」分析出错误的地方以及由于什么原因导致程序 Dump 掉的。
    * 无非是内存溢出，访问非法地址等几种。
* 第二步、使用「!heap」找出出错的堆。分析出错的原因。
* 第三步、使用「!for_each_frame dv /t」打印出错函数的局部变量，找出元凶。


## Windbg 调试


### Image File Execution Options

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Image File ExecutionOptions
```

{% include image.html url="/assets/images/210427-win-dump-course/windbg1.png" %}

条件断点：
windbg 调试 test.exe 下条件断点当
CreateFileA 的第三个参数以
FILE_SHARE_READ（1）时断下，否则不断。
```
bp kernel32!CreateFileA ".if (poi(esp+c)=1){}.else{gc;}"
```


### 内存被修改可能的方式

1. 自己进程直接操作内存（memcpy）。
2. 通过 API WriteProcessMemory。


### 如何搭建双机调试环境

```bat
# Bcdedit
bcdedit -set testsigning on
bcdedit /dbgsettings serial baudrate:115200 debugport:2
bcdedit /copy {current} /d DebugEntry
bcdedit /displayorder {current} {GUID}
bcdedit /debug {GUID} ON
# vmware 增加串口：\\.\pipe\com_2
```

{% include image.html url="/assets/images/210427-win-dump-course/20210516164859.png" %}

VirtualKD-2.7 帮你一键搭建 windbg+vm 的双机调试环境。

#### 调试端

{% include image.html url="/assets/images/210427-win-dump-course/virtualkd1.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/virtualkd2.png" %}

#### 被调试端（VM）

{% include image.html url="/assets/images/210427-win-dump-course/virtualkd3.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/virtualkd4.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/virtualkd5.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/virtualkd6.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/virtualkd7.png" %}


## VS 调试器探秘

{% include image.html url="/assets/images/210427-win-dump-course/k1.png" %}


### 断点

1. 普通断点
2. 单步
    * Eflags 寄存器中追踪标志 TF 被置为 1 时，CPU 进入单步执行方式，即每执行一条指令，产生一个单步中断请求。这种方式主要用于程序的调试。
3. 软件断点
    1. INT3 断点 (0xCC)，是专门用来支持调试的指令。这条指令的目的是使 CPU 中断到调试器，以供我们在程序运行过程中中断下来，对执行现场进行分析。
    2. 当我们在调试器中设置断点时实际上也是先保存当前的一个字节，然后在相应代码处写下一条 INT3 指令。在清除掉断点的时候恢复指令继续执行。
    3. 在 VS 中这一切是动态执行的，在程序执行的时候才会落实断点，在这一过程中 VS 会通过 pdb 将代码和指令对应起来，如果无法对应就会报出错误， 这就是为什么我们调试时有时候会出现以下的错误。
        * 出现这种错误的时候我们首先就要考虑文件和当前调试的代码 pdb 是否不对应。<span imgid="3.3" />
4. 条件断点
    1. Hit Count
    2. Condition
    3. Filter
        * 当我们需要限制断点只在某个进程或线程上生效的时候可以用到这个过滤器。
    4. When hit
    5. 条件断点 eg

{% include image.html url="/assets/images/210427-win-dump-course/k2.png" caption="手动插入一个 INT3 断点" relocate="3.1" %}
{% include image.html url="/assets/images/210427-win-dump-course/k3.png" caption="执行效果" relocate="3.1" %}
{% include image.html url="/assets/images/210427-win-dump-course/k4.png" caption="" relocate="3.3" %}

{% include image.html url="/assets/images/210427-win-dump-course/k5.png" caption="" relocate="4.4" %}
{% include image.html url="/assets/images/210427-win-dump-course/k6.png" caption="" relocate="4.4" %}

```
1. iArray[i] == 2
2. (strArray[i])._Bx._Buf[0x00000000] == 'b' && (strArray[i])._Bx._Buf[0x00000001] == '2'
3. *((bstrArray[i]).m_str + 0) == 'b' && *((bstrArray[i]).m_str + 1) == '2'
4. (*(strIter)._Myptr)._Bx._Buf[0x00000000] == 'c' && (*(strIter)._Myptr)._Bx._Buf[0x00000001] == '3'
5. *((*(bstrIter)._Myptr).m_str +0) == 'b' && *((*(bstrIter)._Myptr).m_str + 1) == '2'
6. (*(*(pointVecIter)._Myptr)).i == 2
7. (((strMapIter)._Ptr->_Myval).first)._Bx._Buf[0x00000000] == 'c' && (((strMapIter)._Ptr->_Myval).first)._Bx._Buf[0x00000001] == '3'
8. (((strMapIter)._Ptr->_Myval).second)._Bx._Buf[0x00000000] == 'b' && (((strMapIter)._Ptr->_Myval).second)._Bx._Buf[0x00000001] == '2'
9. *((((bstrMapIter)._Ptr->_Myval).first).m_str + 0) == 'c' && *((((bstrMapIter)._Ptr->_Myval).first).m_str + 1) == '3'
10. *((((bstrMapIter)._Ptr->_Myval).second).m_str + 0) == 'b' && *((((bstrMapIter)._Ptr->_Myval).first).m_str + 1) == '2'
11. (((pointMapIter)._Ptr->_Myval).first)._Bx._Buf[0x00000000] == 'b' && (((pointMapIter)._Ptr->_Myval).first)._Bx._Buf[0x00000001] == '2'
12. (*(((pointMapIter)._Ptr->_Myval).second)).i == 3
```


### 条件断点的原理

* **内存访问断点**

{% include image.html url="/assets/images/210427-win-dump-course/k7.png" %}


### 堆栈回溯原理

[Windows 栈溢出原理 {% include relref_cnblogs.html %}](https://www.cnblogs.com/wintrysec/p/10616793.html)
进程使用的内存可以分成 4 个部分
* 代码区：存储二进制机器码，存储器在这里取指令
* 数据区：用于存储全局变量
* 堆区：动态分配和全局变量
* 栈区：动态存储函数间的调用关系，保证被调用函数返回时恢复到母函数中继续运行

寄存器与函数栈帧
* ESP：栈顶指针寄存器，永远指向系统栈顶
* EBP：基址指针寄存器，永远指向系统栈最上边一个栈的栈底
* ESP 和 EBP 之间的内存空间为当前栈帧

在 Windows 中，一个线程的栈空间的默认大小是 1MB，对于 MFC UI 主线程，一般其栈空间的大小均为 1MB，当 UI 主线程的数据较大时就可能会造成栈溢出，从而导致程序出现异常。

```cpp
int a = 0; // 全局初始化区
char *p1; // 全局未初始化区
int main()
{
    int b; // 栈
    char s[] = "abc"; // 栈
    char *p2; // 栈
    char *p3 = "123456"; // 123456\0 在常量区，p3 在栈上。
    static int c = 0; // 全局（静态）初始化区
    p1 = (char *)malloc(10);
    p2 = (char *)malloc(20); // 分配得来得 10 和 20 字节的区域就在堆区。
    strcpy(p1, "123456"); // 123456\0 放在常量区，编译器可能会将它与 p3 所指向的"123456"优化成一个地方。
    return 0;
}
```

#### 标准函数头

```
push ebp
mov ebp, esp
```

#### 栈帧 - ebp

* 在同一个函数执行过程中 ebp 不变
* 通过栈帧可以访问返回值 [ebp+4]
* 通过栈帧可以拿到上一层的栈帧 [ebp]

#### 一次堆栈回溯过程

{% include image.html url="/assets/images/210427-win-dump-course/z1.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/z2.png" %}

* 可以看出在当前函数中要取上一层函数的返回地址只需要取 ebp+4 的内容 ([ebp+4])
* 而要取到上一层栈帧 ebp(old), 只需要取 ebp 的内容 ([ebp])
* 然后通过上一层的栈帧又可以取上上一层的返回地址
* 这样就可以完成堆栈回溯


### 观察窗口

1. 观察窗口主要是用于监控我们关注的变量的变化
2. 利用观察窗口可以当前函数可访问的局部或全局变量也可以是表达式的值
3. 观察窗口也可以调用函数
4. 观察窗口格式化输出数据【监视 1】
    1. eg: char\* p = new char[10];
    2. 一般情况下直接添加到观察窗口查看到的数据如下：
    3. 通过在“p,10” 可以将数据转化成大小为 10 的数组
    4. 通过格式化对数据类型进行转换

{% include image.html url="/assets/images/210427-win-dump-course/z3.png" relocate="4.2" %}
{% include image.html url="/assets/images/210427-win-dump-course/z4.png" relocate="4.3" %}
{% include image.html url="/assets/images/210427-win-dump-course/z5.png" relocate="4.4" %}


### 代码的可调试性探讨

* 代码逻辑清晰
* 函数有足够的返回值
* 错误判断最短距离原则
* 为简单功能包装函数
* 确保函数功能单一
* 错误信息或 LOG
* 避免滥用宏函数


## 高 CPU !runaway

{% include image.html url="/assets/images/210427-win-dump-course/1.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/2.png" %}


## 死锁 !locks

{% include image.html url="/assets/images/210427-win-dump-course/3.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/4.png" url2="/assets/images/210427-win-dump-course/5.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/6.png" url2="/assets/images/210427-win-dump-course/7.png" %}


## DllMain 死锁分析

{% include image.html url="/assets/images/210427-win-dump-course/8.png" url2="/assets/images/210427-win-dump-course/9.png" url3="/assets/images/210427-win-dump-course/10.png" %}

{% include image.html url="/assets/images/210427-win-dump-course/11.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/13.png" url2="/assets/images/210427-win-dump-course/14.png" %}

* 进程内所有线程共用了同一个临界区来序列化 DllMain 的执行；
* DllMain 中执行了危险操作导致等待某个锁（最好什么逻辑都没有）；
* 其他线程持有该锁并等待 LdrpLoaderLock。
    * 危险的 SHGetFolderPathW 等函数，可能存在延迟加载的内容，或者隐藏的锁。


### Ntdll!LdrpLoaderLock

```
.load wow64exts
!sw
!cs # 扩展显示一个或多个临界区 (criticalsection) 或者整个临界区树
!cs Address # 指定要显示的临界区地址。如果省略该参数，调试器显示当前进程中所有临界区。
!cs -s # 如果可能的话，显示每个临界区的初始堆栈回溯。
!cs -l # 仅显示锁定的临界区。
!locks
~*kb
```

IDA 反汇编 ntdll!_LdrpInitialize：
{% include image.html url="/assets/images/210427-win-dump-course/15.png" %}

{% include image.html url="/assets/images/210427-win-dump-course/16.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/17.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/18.png" %}


### DllMain 序列化执行

线程在调用 DllMain 之前，要先获取锁，等 DllMain 执行完再解开这个锁。这样不同线程加载 DLL 就可以实现序列化操作。《Windows 核心编程》

The DllMain entry-point function. This function is called by the loader when it loads or unloads a DLL.
The loader serializes calls to DllMain so that only a single DllMain function is run at a time .
微软官方文档《Best Practices for Creating DLLs》

{% include image.html url="/assets/images/210427-win-dump-course/19.png" %}
<https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-best-practices>

The loader lock. This is a process-wide synchronization primitive that the loader uses to ensure serialized loading of DLLs.
Any function that must read or modify the per-process library-loader data structures must acquire this lock before performing such an operation.
The loader lock is recursive, which means that it can be acquired again by the same thread.
《Best Practices for Creating DLLs》

* 进程内所有线程共用了同一个临界区来序列化 DllMain 的执行；
* 线程创建后会调用已经加载了的 DLL 的 DllMain，且调用原因是 DLL_THREAD_ATTACH；
* 主线程进入临界区去调用 DllMain 时进入了临界区，而工作线程也要进入临界区去执行 DllMain。
    但是此时临界区被主线程占用，工作线程便进入等待状态。而主线程却等待工作线程退出才退出临界区。这就是死锁产生的原因。
* Windbg 调试验证结论。


## 资源

{% include image.html url="/assets/images/210427-win-dump-course/a.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/b.png" url2="/assets/images/210427-win-dump-course/c.png" %}
{% include image.html url="/assets/images/210427-win-dump-course/d.png" url2="/assets/images/210427-win-dump-course/e.png" %}

{% include image.html url="/assets/images/210427-win-dump-course/book1.png" %}


## Tools


### Windbg

<http://www.microsoft.com/whdc/devtools/debugging/default.mspx>
<https://developer.microsoft.com/en-us/windows/hardware/windows-driver-kit>


### IDA


### SysinternalsSuite

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-27-win-dump-Course.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/dailongjian2008/article/details/88081507]({% include relrefx.html url="/backup/2021-04-27-win-dump-Course.md/blog.csdn.net/05e5d4e0.html" %})
- [https://www.jianshu.com/p/56b9afc8ae47]({% include relrefx.html url="/backup/2021-04-27-win-dump-Course.md/www.jianshu.com/6cee84b3.html" %})
- [https://www.cnblogs.com/wintrysec/p/10616793.html]({% include relrefx.html url="/backup/2021-04-27-win-dump-Course.md/www.cnblogs.com/797c13b8.html" %})
- [https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-best-practices]({% include relrefx.html url="/backup/2021-04-27-win-dump-Course.md/docs.microsoft.com/9feb9f9f.html" %})
- [http://www.microsoft.com/whdc/devtools/debugging/default.mspx]({% include relrefx.html url="/backup/2021-04-27-win-dump-Course.md/www.microsoft.com/666bc8dd.mspx" %})
- [https://developer.microsoft.com/en-us/windows/hardware/windows-driver-kit]({% include relrefx.html url="/backup/2021-04-27-win-dump-Course.md/developer.microsoft.com/08190143.html" %})
