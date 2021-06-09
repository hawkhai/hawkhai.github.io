---
layout: post
title: "调试 Memory -- Windows Windbg 崩溃分析 CASES 一些案例"
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


## 野指针 QString::toStdString().c_str()

危险的：`QString::toStdString().c_str()`，他的定义是：
```cpp
inline std::string QString::toStdString() const
{ return toUtf8().toStdString(); }
inline std::wstring QString::toStdWString() const {
    std::wstring str;
    str.resize(length());
#if __cplusplus >= 201703L
    str.resize(toWCharArray(str.data()));
#else
    if (length())
        str.resize(toWCharArray(&str.front()));
#endif
    return str;
}
```

```cpp
void testmain(QString& qstr) {
    const char* p = qstr.toStdString().c_str();
    std::cout << p;
}
```
上面这段代码是存在问题的，生成的汇编为：
{% include image.html url="/assets/images/210602-win-windbg-cases/20210609095612.png" %}

换一种写法：
```cpp
void testmain2(QString& qstr) {
    const std::string str = qstr.toStdString();
    std::cout << str.c_str();
}
```
生成的代码是：
{% include image.html url="/assets/images/210602-win-windbg-cases/20210609100048.png" %}


## 崩溃 空指针问题

```
FAULTING_IP:
dbapp!EnginePdfiumTransformByPageCTM+89
00501379 8b7004          mov     esi,dword ptr [eax+4]

EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 00501379 (dbapp!EnginePdfiumTransformByPageCTM+0x00000089)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 00000004
Attempt to read from address 00000004

BUGCHECK_STR:  ACCESS_VIOLATION

STACK_TEXT:
01efcccc 0034fc3a 01efcd10 0ee95c88 01efcd00 dbapp!EnginePdfiumTransformByPageCTM+0x89
01efcd28 00351ef1 01efcd48 3e9baddd 00000000 dbapp!DisplayModel::CvtToScreen+0x18a
```

**Attempt to read from address 00000004** 尝试读取内存 `00000004`，而此时
`mov esi,dword ptr [eax+4]`，寄存器 `eax=00000000`，`[eax+4]` 就是 `00000004`。

```
This dump file has an exception of interest stored in it.
The stored exception information can be accessed via .ecxr.
(2c9c.2d6c): Access violation - code c0000005 (first/second chance not available)
eax=00000000 ebx=0ee95c88 ecx=00000001 edx=00000002 esi=0f127678 edi=00000001
eip=00501379 esp=01efcbe0 ebp=01efcccc iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00210246
dbapp!EnginePdfiumTransformByPageCTM+0x89:
00501379 8b7004          mov     esi,dword ptr [eax+4] ds:002b:00000004=????????
```

```
System Uptime: 3 days 23:44:37.243
Process Uptime: 0 days 0:01:21.000
```

这个也说明了是进程启动就崩溃了，崩溃到函数 EnginePdfiumTransformByPageCTM 里面的空指针。


## 黑指针问题 StrChrIW

```
eax=00000000 ebx=00000000 ecx=00000000 edx=00000000 esi=00000000 edi=00000490
eip=777e29dc esp=0654cf1c ebp=0654cf8c iopl=0         nv up ei pl nz na po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202
ntdll!ZwWaitForSingleObject+0xc:
777e29dc c20c00          ret     0Ch

eax=ffffffff ebx=0000970d ecx=78d91b15 edx=00020dc5 esi=14f5bffe edi=76c5ca20
eip=76759ed8 esp=0654fc28 ebp=0654fc40 iopl=0         nv up ei ng nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010286
KERNELBASE!StrChrIW+0xa8:
76759ed8 0fb74602        movzx   eax,word ptr [esi+2]     ds:002b:14f5c000=????
ChildEBP RetAddr  Args to Child
0654fc40 76759afc 14f5b9fa 0000970d 16c2a420 KERNELBASE!StrChrIW+0xa8
0654fc60 00e39bed 14f5b9fa 169ddd38 16ad1858 KERNELBASE!StrStrIW+0x2c
fastapp!TextSearch::FindTextInPage+0x7d [E:\src\TextSearch.cpp @ 270]

FAULTING_IP:
KERNELBASE!StrChrIW+a8
76759ed8 0fb74602        movzx   eax,word ptr [esi+2]

EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 76759ed8 (KERNELBASE!StrChrIW+0x000000a8)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 14f5c000
Attempt to read from address 14f5c000

DEFAULT_BUCKET_ID:  INVALID_POINTER_READ
```

汇编指令：`MOVZX OPD, OPS`
将 8 位或 16 位的 OPS 零扩展为 16 位或 32 位，在传给 OPD。
相当于 函数 FindTextInPage 里面用了一个 **被释放** 或者 **未初始化** 的指针 并 调用了 **StrChrIW**。


## 崩溃 QList\<QString\> 非多线程安全

**`QCoreApplication::processEvents();` 这玩意不能轻易用，容易造成失控。**
<font color="red">为啥堆栈里面看不到？有机会了要好好研究验证一下。</font>


### 崩溃现场

这个崩溃只在特定电脑，Release 版本反复操作，一定概率出现。

```
EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 00000000
   ExceptionCode: 80000003 (Break instruction exception)
  ExceptionFlags: 00000000
NumberParameters: 0

DEFAULT_BUCKET_ID:  INVALID_POINTER_READ
ERROR_CODE: (NTSTATUS) 0x80000003 - {

eax=65ecefd4 ebx=69284bd4 ecx=022fdb00 edx=58dd6f68 esi=65ecefd4 edi=65eceff8
eip=7aaa11f4 esp=022fdae8 ebp=022fdb18 iopl=0         nv up ei ng nz ac po cy
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010293
qt5core!QString::QString+0x4:
7aaa11f4 8b00            mov     eax,dword ptr [eax]  ds:002b:65ecefd4=????????
Minidump doesn't have an exception context
Unable to get exception context, HRESULT 0x80004002
ChildEBP RetAddr  Args to Child
WARNING: Stack unwind information not available. Following frames may be wrong.
022fdb18 0082a30d 4676af70 022fdc01 0fd14e80 qt5core!QString::QString+0x4
022fdb48 7ac3fced 022ffec0 00000000 00000002 fastapp!QMainClient::qt_static_metacall+0x9d [E:\moc\moc_QMainClient.cpp @ 107]
022fdbec 7ac41c12 0fd14e80 00000011 022fdc24 qt5core!QObject::qt_static_metacall+0x10fd
022fdc34 00762844 4bc92fd4 022fdce8 7ac3fc97 qt5core!QMetaObject::activate+0x42
022fdc40 7ac3fc97 00000001 449e0ff0 0fd14e80 fastapp!QtPrivate::QSlotObject<void (__thiscall MainFrame::*)(QString const &),
                                                        QtPrivate::List<QString const &>,void>::impl+0x54
                                                    [D:\include\QtCore\qobjectdefs_impl.h @ 425]
022fdce8 7ac41c12 4bc92f58 00000007 022fdd38 qt5core!QObject::qt_static_metacall+0x10a7
022fdd54 007ee935 00000001 00000000 000001cd qt5core!QMetaObject::activate+0x42
022fdd6c 7ac4772b 00000001 43c18ff0 4bc92f58 fastapp!QtPrivate::QSlotObject<void (__thiscall PDFPage::*)(bool,bool,int),
                                                        QtPrivate::List<bool,bool,int>,void>::impl+0x65
                                                    [D:\include\QtCore\qobjectdefs_impl.h @ 418]
022fddc8 7b5b0e55 49124fb8 4bc92f58 09f0dff8 qt5core!QMetaCallEvent::placeMetaCall+0x1b
022fdde4 7ac257ba 4bc92f58 49124fb8 4bc92f58 Qt5Widgets!QWidget::event+0xcd5
022fde14 7b592a53 7b592a6d 49124fb8 49124fb8 qt5core!QCoreApplicationPrivate::sendThroughApplicationEventFilters+0x8a
022fde18 7b592a6d 49124fb8 49124fb8 4bc92f58 Qt5Widgets!QApplicationPrivate::notify_helper+0xb3
022fde30 7b591be4 4bc92f58 49124fb8 4bc92f58 Qt5Widgets!QApplicationPrivate::notify_helper+0xcd
022fde54 77b65181 f3f738d1 00000001 00000000 Qt5Widgets!QApplication::notify+0x1874
77c56894 00000000 00000000 00000000 00000000 ntdll!TppPoolpReferenceGlobalPool+0x74
```


### 问题分析

这个堆栈和汇编一致，但是和源码不一致，Release 版本经过优化。
在函数 `QMainClient::qt_static_metacall` 里面是找不到 `qt5core!QString::QString+0x4` 构造函数的。
命令：`dds esp` 可以查看到当前堆栈残留，这里面指示的位置是正确的。

```
022fdae8  00744c9d fastapp!QMainClient::slotTabInitFinished+0x22d [E:\src\QMainClient.cpp @ 248]
022fdaec  65ecefd4
022fdaf0  2e63afc8
022fdaf4  022ffec0
022fdaf8  49124fb8
022fdafc  022fdb08
022fdb00  58dd6f68
022fdb04  69284bd4
022fdb08  69284f40
022fdb0c  69284fc0
022fdb10  022ffed8
022fdb14  022ffec0
022fdb18  022fdb48
022fdb1c  0082a30d fastapp!QMainClient::qt_static_metacall+0x9d [E:\moc\moc_QMainClient.cpp @ 107]
022fdb20  4676af70
```

`qt5core!QString::QString+0x4` 出现访问不可读的内存黑指针，第一反应是堆破坏，反复检查相关变量是否线程安全。
尝试了各种可能，后来回家路上突然来了灵感，想起了这个函数 `QCoreApplication::processEvents();`！


### 问题原因

`QList<QString>` 不是线程安全的，迭代的过程中 调用了 `QCoreApplication::processEvents();`，
然后又再次递归触发了当前函数，再次发生了迭代。
在一个线程里面对它发生了 两次迭代，两次迭代也没啥，偏偏又有一个 `.clear();`。

```cpp
QList<QString> m_printFileList;

void QMainClient::slotTabInitFinished() {
    for (auto strfile : m_printFileList) { // 这里崩溃了。
        // 这里很深的一个地方触发了：QCoreApplication::processEvents();
        // 调用过程中，再次递归调用了当前函数，再次迭代了 m_printFileList
        printDlg->addFileTarget(strfile);
    }
    m_printFileList.clear();
}
```

知道原因后，就很好改了，一个方案就是先放到一个临时变量里面，避免迭代：

```cpp
void QMainClient::slotTabInitFinished() {
    QList<QString> pflist;
    for (auto& strfile : m_printFileList) {
        pflist.push_back(strfile);
    }
    m_printFileList.clear();
    // 这个可能对当前函数形成递归崩溃，所以拷贝出来先再执行。
    for (auto& strfile : pflist) {
        printDlg->addFileTarget(strfile);
    }
}
```

我们可以写一段简单的代码模拟这个崩溃：

```cpp
void Test::slotvoid() {
    QString qstra("qstra");
    QString qstrb("qstrb");
    QList<QString> qlist;
    qlist.push_back(qstra);
    qlist.push_back(qstrb);
    for (auto istr : qlist) { // 崩溃到这一行。
        for (auto jstr : qlist) {
            std::cout << istr.toStdString() << "\t" << jstr.toStdString() << std::endl;
        }
        qlist.clear();
    }
    qlist.clear();
}
```

刚好崩溃到 拷贝构造函数：`inline QString::QString(const QString &other);`。

{% include image.html url="/assets/images/210602-win-windbg-cases/20210603114533.png" %}

至于 `QCoreApplication::processEvents();` 为啥会调用到当前槽函数，写一篇 QT 信号槽的深度理解。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-06-02-win-windbg-cases.md.js" %}'></script></p>
