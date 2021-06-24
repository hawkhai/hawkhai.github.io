---
layout: post
title: "调试 Memory -- Windows Windbg 堆栈跟踪 UnhandledExceptionFilter"
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

WinDbg 查找问题异常堆栈，堆栈跟踪 UnhandledExceptionFilter。[堆栈查看 {% include relref_cnblogs.html %}](https://www.cnblogs.com/yilang/p/11531740.html)：

* `.exr (Display Exception Record)` .exr 命令显示异常记录的内容。
* `.cxr (Display Context Record)` .cxr 命令显示保存在指定地址的上下文记录。
* `.ecxr` 命令定位当前异常的上下文信息，并显示指定记录中的重要寄存器。

Windows 的设计体系会回调两次：
1. 发生崩溃了，代码进入系统；（此时是真正的崩溃堆栈）
2. 系统记录现在的上下文，再次调用软件的代码进行崩溃处理。（此时是 dumper 堆栈，需要 `.ecxr` 回到崩溃时的上下文）

一个崩溃：
C:\Users\ADMIN\Downloads\3070_b97e108a64f671bb23ca1ff244f5c93d_fastapp.exe_2021.5.8.479_271139_fastapp.exe_2021.5.8.479_0_win10_64_1858570_20_0_1_210519080829@3416591882__d3d72f2c586e324e0a5c897786ea8aa1.dmp

先自动分析一轮 [dubadumper.exe](https://sunocean.life/tools/) 异常线程堆栈：

```
.reload;
.printf"\n==================== 自动分析定位 “~0s; .ecxr; kb” ====================\n\n";
~0s;
.ecxr;
kb; // 打印出前 3 个函数参数的当前调用堆栈，kb 5 // 只显示最上的 5 层调用堆栈
dds esp l100;
q
```
```
.reload;
!analyze -v;
.printf"\n==================== 异常线程堆栈 ====================\n";
kv;
.printf"\n==================== 所有线程堆栈 ====================\n";
~* kv;
q
```

```
ChildEBP RetAddr  Args to Child
022fa928 76a2e269 000003e4 00000000 00000000 ntdll!ZwWaitForSingleObject+0xc (FPO: [3,0,0])
022fa99c 76a2e1c2 000003e4 ffffffff 00000000 KERNELBASE!WaitForSingleObjectEx+0x99 (FPO: [SEH])
022fa9b0 100104f2 000003e4 ffffffff 42da795f KERNELBASE!WaitForSingleObject+0x12 (FPO: [Non-Fpo])
WARNING: Stack unwind information not available. Following frames may be wrong.
022fcef4 10010d2b 022fcfcc 022fcf9c 76ada7d0 kdump!KxEOpenDumpMonitor+0xa0ab
022fcf00 76ada7d0 022fcfcc 24629122 00000000 kdump!KxEOpenDumpMonitor+0xa8e4
022fcf9c 77a128e8 022fcfcc 779e6312 022ffdc0 KERNELBASE!UnhandledExceptionFilter+0x1a0 (FPO: [Non-Fpo])
022ffdc0 779d7b44 ffffffff 779f8f08 00000000 ntdll!__RtlUserThreadStart+0x3ada3
022ffdd0 00000000 00c9c7da 02157000 00000000 ntdll!_RtlUserThreadStart+0x1b (FPO: [Non-Fpo])
```

自动分析定位 “!analyze -v;” 已经很准确了，“~0s; .ecxr; kb”：
```
FAULTING_IP:
fastapp!EnginePdfiumTransformByPageCTM+89
008e1139 8b7004          mov     esi,dword ptr [eax+4]

EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 008e1139 (fastapp!EnginePdfiumTransformByPageCTM+0x00000089)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 00000004
Attempt to read from address 00000004

DEFAULT_BUCKET_ID:  APPLICATION_FAULT

PROCESS_NAME:  fastapp.exe

ERROR_CODE: (NTSTATUS) 0xc0000005 - 0x%p

READ_ADDRESS:  00000004

BUGCHECK_STR:  ACCESS_VIOLATION

LAST_CONTROL_TRANSFER:  from 0073ee5a to 008e1139

STACK_TEXT:
022fd6a4 0073ee5a 022fd6e8 02404248 022fd6d8 fastapp!EnginePdfiumTransformByPageCTM+0x89
022fd700 007410fa 022fd720 00000000 00000000 fastapp!DisplayModel::CvtToScreen+0x18a [E:\src\DisplayModel.cpp @ 1150]
022fd770 7549a9f6 00000000 00000007 000000f0 fastapp!DisplayModel::SetScrollState+0xba [E:\src\DisplayModel.cpp @ 2033]
022fd78c 42c80000 42c80000 41280000 3f800000 ucrtbase!_malloc_base+0x26
WARNING: Frame IP not in any known module. Following frames may be wrong.
022fd794 41280000 3f800000 3fc00000 00000000 0x42c80000
022fd798 3f800000 3fc00000 00000000 00000000 0x41280000
022fd79c 3fc00000 00000000 00000000 00000000 0x3f800000
022fd7a0 00000000 00000000 00000000 00000000 0x3fc00000

STACK_COMMAND:  ~0s; .ecxr ; kb

FOLLOWUP_IP:
fastapp!EnginePdfiumTransformByPageCTM+89
008e1139 8b7004          mov     esi,dword ptr [eax+4]

SYMBOL_STACK_INDEX:  0

FOLLOWUP_NAME:  MachineOwner

MODULE_NAME: fastapp

IMAGE_NAME:  fastapp.exe

DEBUG_FLR_IMAGE_TIMESTAMP:  60967ecc

FAULTING_THREAD:  00003da0

SYMBOL_NAME:  fastapp!EnginePdfiumTransformByPageCTM+89

FAILURE_BUCKET_ID:  ACCESS_VIOLATION_fastapp!EnginePdfiumTransformByPageCTM+89

BUCKET_ID:  ACCESS_VIOLATION_fastapp!EnginePdfiumTransformByPageCTM+89

Followup: MachineOwner
---------
```

* 切换到该线程（在此示例中，线程是 "~0s"）。
* 显示内存内容的第一个参数指定位置处 Kernel32! UnhandledExceptionFilter 通过使用 dd 第一个参数。这指向 EXCEPTION_POINTERS 结构 "dd 022fcfcc"
  ```
0:000> dd 022fcfcc
022fcfcc  022fd108 022fd158 77a762e8 00000001
022fcfdc  77a762d8 0097dae0 022fd004 779e9fa0
022fcfec  77a93360 779e3ea0 022fd108 022ffdb0
022fcffc  022fd158 022fd094 022fd028 779f8da2
022fd00c  022fd108 022ffdb0 022fd158 022fd094
022fd01c  022fd98c 779f8dc0 022ffdb0 022fd0f0
022fd02c  779f8d74 022fd108 022ffdb0 022fd158
022fd03c  022fd094 779e9f80 022ffdb0 022fd108
```
  ```
typedef struct _EXCEPTION_POINTERS {
  PEXCEPTION_RECORD ExceptionRecord;
  PCONTEXT          ContextRecord;
} EXCEPTION_POINTERS, *PEXCEPTION_POINTERS;
```
* 第一个 dword 值表示异常记录。若要获取有关异常的类型的信息。
  ```
0:000> .exr 022fd108
ExceptionAddress: 008e1139 (fastapp!EnginePdfiumTransformByPageCTM+0x00000089)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 00000004
Attempt to read from address 00000004
```
* 第二个 dword 值是上下文记录。
  ```
0:000> .cxr 022fd158
eax=00000000 ebx=02404248 ecx=00000001 edx=023fd208 esi=023baaf0 edi=00000001
eip=008e1139 esp=022fd5b8 ebp=022fd6a4 iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010246
fastapp!EnginePdfiumTransformByPageCTM+0x89:
008e1139 8b7004          mov     esi,dword ptr [eax+4] ds:002b:00000004=????????
```
* 运行 kv 命令以获得实际的异常的调用堆栈。这可以帮助您识别可能不具有被正确处理过程中的实际问题。
  ```
0:000> kv
  *** Stack trace for last set context - .thread/.cxr resets it
ChildEBP RetAddr  Args to Child
022fd6a4 0073ee5a 022fd6e8 02404248 022fd6d8 fastapp!EnginePdfiumTransformByPageCTM+0x89
022fd700 007410fa 022fd720 00000000 00000000 fastapp!DisplayModel::CvtToScreen+0x18a (FPO: [Non-Fpo]) (CONV: thiscall) [E:\src\DisplayModel.cpp @ 1150]
022fd770 7549a9f6 00000000 00000007 000000f0 fastapp!DisplayModel::SetScrollState+0xba (FPO: [Non-Fpo]) (CONV: thiscall) [E:\src\DisplayModel.cpp @ 2033]
022fd78c 42c80000 42c80000 41280000 3f800000 ucrtbase!_malloc_base+0x26 (FPO: [Non-Fpo])
WARNING: Frame IP not in any known module. Following frames may be wrong.
022fd794 41280000 3f800000 3fc00000 00000000 0x42c80000
022fd798 3f800000 3fc00000 00000000 00000000 0x41280000
022fd79c 3fc00000 00000000 00000000 00000000 0x3f800000
022fd7a0 00000000 00000000 00000000 00000000 0x3fc00000
```

[WinDbg 查找问题异常堆栈，堆栈跟踪 UnhandledExceptionFilter {% include relref_csdn.html %}](https://blog.csdn.net/mergerly/article/details/5521111)

崩溃原因：
在执行
`fastapp!EnginePdfiumTransformByPageCTM+89` 的时候 `mov esi,dword ptr [eax+4]` 然后 `READ_ADDRESS: 00000004`。
由于 Release 优化内联，定位到的函数可能不准确，但是一看就是一个空指针读取造成的崩溃。指针是空，然后读取内存 +4 的位置。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-20-win-windbg-UnhandledExceptionFilter.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/yilang/p/11531740.html]({% include relrefx.html url="/backup/2021-05-20-win-windbg-UnhandledExceptionFilter.md/www.cnblogs.com/5b3f9222.html" %})
- [https://blog.csdn.net/mergerly/article/details/5521111]({% include relrefx.html url="/backup/2021-05-20-win-windbg-UnhandledExceptionFilter.md/blog.csdn.net/df835688.html" %})
