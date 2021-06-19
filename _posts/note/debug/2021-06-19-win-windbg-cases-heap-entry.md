---
layout: post
title: "调试 Memory -- Windows Windbg 编码后的 HEAP_ENTRY 结构"
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

{% include image.html url="/assets/images/210619-win-windbg-cases-heap-e~16/20200312111504316.png" %}

每个堆块的前 8 个字节是一个 HEAP_ENTRY 结构体，头部的结构，记录了这块内存 de 信息。
Vista 引入了很多新的东西，对堆块的块头结构（HEAP_ENTRY）编码，编码的目的是引入随机性，增强堆的安全性，防止黑客轻易就可以预测堆的数据内容而实施攻击。
其中的 EncodeFlagMask 用来指示是否启用编码功能；Encoding 字段是用来编码的，编码的方法就是用这个 Encoding 结构与每个堆块的头结构做异或（XOR）。
* [Windows Heap Chunk Header Parsing and Size Calculation](https://stackoverflow.com/questions/28483473/windows-heap-chunk-header-parsing-and-size-calculation)
* [解读编码后的 HEAP_ENTRY 结构](http://advdbg.org/blogs/advdbg_system/articles/5152.aspx)
* [!heap 和 _HEAP_ENTRY {% include relref_cnblogs.html %}](https://www.cnblogs.com/xumaojun/p/8544089.html)
* VS2019 编译，ntdll!_HEAP_ENTRY **4f8adefe 88001769** 找规律：
    * 88 -- 88 表示没有补齐，8c 表示补齐 4 位，凑齐 8 的倍数；XOR 后刚好相差 4。
    * 17 -- 感觉是索引，距离下一个内存 +1?

《Windows 核心编程》
《深入解析 Windows 操作系统 - Windows Internals》
**155ff48e 18003ec6** `int* pChar = new int[2];`
```
Detailed information for block entry 00ae6d90
Assumed heap       : 0x00ae0000 (Use !heap -i NewHeapHandle to change)
Header content     : 0x155FF48E 0x18003EC6 (decoded : 0x03070004 0x1800000A)
Owning segment     : 0x00ae0000 (offset 0)
Block flags        : 0x7 (busy extra fill )
Total block size   : 0x4 units (0x20 bytes)
Requested size     : 0x8 bytes (unused 0x18 bytes)
Previous block size: 0xa units (0x50 bytes)
Block CRC          : OK - 0x3
Previous block     : 0x00ae6d40
Next block         : 0x00ae6db0
```

* 如果是 12 位：
    * `2d252b1f 8c002500 02020202 02020202 02020202 005ce6d8 2d262b1c 88002600 ` -- char 数组

```
g // 开始运行。
!heap -x 00343818
dt _HEAP_ENTRY 00343810
dd 00343810
!heap -i 00343810
```


## C++

```cpp
#include <stdio.h>
#include <windows.h>

int main() {
    int* pChar = new int[2];

    pChar[0] = 2;
    pChar[1] = 3;

    printf("%p", pChar);
    fflush(stdout);
    Sleep(100);
    __asm {
        int 3; // 中断。
    }

    delete[] pChar;
    return 0;
}
```


## 查看堆信息

```
0:000> !heap
        Heap Address      NT/Segment Heap
              cc0000              NT Heap
```

```
0:000> !heap cc0000 -A
Index   Address  Name      Debugging options enabled
  1:   00cc0000
    Segment at 00cc0000 to 00dbf000 (00012000 bytes committed)
    Flags:                40000062
    ForceFlags:           40000060
    Granularity:          8 bytes
    Segment Reserve:      00100000
    Segment Commit:       00002000
    DeCommit Block Thres: 00000200
    DeCommit Total Thres: 00002000
    Total Free Size:      000003f0
    Max. Allocation Size: 7ffdefff
    Lock Variable at:     00cc0248
    Next TagIndex:        0000
    Maximum TagIndex:     0000
    Tag Entries:          00000000
    PsuedoTag Entries:    00000000
    Virtual Alloc List:   00cc009c
    Uncommitted ranges:   00cc008c
            00cd2000: 000ed000  (970752 bytes)
    FreeList[ 00 ] at 00cc00c0: 00cd1000 . 00ccb1f8
        00ccb1f0: 00070 . 00010 [104] - free
        00cc9a40: 00038 . 00010 [104] - free
        00cc9eb8: 00038 . 00010 [104] - free
        00cc9f10: 00048 . 00010 [104] - free
        00cc9288: 000b8 . 00010 [104] - free
        00cc5808: 00040 . 00010 [104] - free
        00cc9400: 00028 . 00018 [104] - free
        00cc8698: 00030 . 00018 [104] - free
        00cc4fe0: 000b8 . 00018 [104] - free
        00cc9718: 000b8 . 00030 [104] - free
        00cc9818: 00048 . 00048 [104] - free
        00ccadf8: 00048 . 00048 [104] - free
        00cca978: 00048 . 00048 [104] - free
        00ccb0e8: 00060 . 00048 [104] - free
        00ccee80: 00458 . 00da0 [104] - free
        00cd0ff8: 01018 . 00fe8 [104] - free

    Segment00 at 00cc0000:
        Flags:           00000000
        Base:            00cc0000
        First Entry:     00cc0498
        Last Entry:      00dbf000
        Total Pages:     000000ff
        Total UnCommit:  000000ed
        Largest UnCommit:00000000
        UnCommitted Ranges: (1)

    Heap entries for Segment00 in Heap 00cc0000
         address: psize . size  flags   state (requested size)
        00cc6d40: 00080 . 00050 [107] - busy (34), tail fill
        00cc6d90: 00050 . 00020 [107] - busy (8), tail fill
        00cc6db0: 00020 . 000c0 [107] - busy (a8), tail fill
```

申请的内存是：00CC6D98。
对应的堆地是：00cc6d90。

```
0:000> !heap -x 00cc6d90
Entry     User      Heap      Segment       Size  PrevSize  Unused    Flags
-----------------------------------------------------------------------------
00cc6d90  00cc6d98  00cc0000  00cc0000        20        50        18  busy extra fill
```

观察原始结构：
```
0:000> dt _heap_entry 00cc6d90
ntdll!_HEAP_ENTRY
   +0x000 Size             : 0x9eff
   +0x002 Flags            : 0x3b ';'
   +0x003 SmallTagIndex    : 0xc0 ''
   +0x000 SubSegmentCode   : 0xc03b9eff
   +0x004 PreviousSize     : 0xe2e8
   +0x006 SegmentOffset    : 0 ''
   +0x006 LFHFlags         : 0 ''
   +0x007 UnusedBytes      : 0x18 ''
   +0x000 FunctionIndex    : 0x9eff
   +0x002 ContextValue     : 0xc03b
   +0x000 InterceptorValue : 0xc03b9eff
   +0x004 UnusedBytesLength : 0xe2e8
   +0x006 EntryOffset      : 0 ''
   +0x007 ExtendedBlockSignature : 0x18 ''
   +0x000 Code1            : 0xc03b9eff
   +0x004 Code2            : 0xe2e8
   +0x006 Code3            : 0 ''
   +0x007 Code4            : 0x18 ''
   +0x004 Code234          : 0x1800e2e8
   +0x000 AgregateCode     : 0x1800e2e8`c03b9eff
```

读取堆信息：
```
0:000> dt _HEAP 00cc0000
ntdll!_HEAP
   +0x000 Entry            : _HEAP_ENTRY
   +0x008 SegmentSignature : 0xffeeffee
   +0x00c SegmentFlags     : 2
   +0x010 SegmentListEntry : _LIST_ENTRY [ 0xcc00a4 - 0xcc00a4 ]
   +0x018 Heap             : 0x00cc0000 _HEAP
   +0x01c BaseAddress      : 0x00cc0000 Void
   +0x020 NumberOfPages    : 0xff
   +0x024 FirstEntry       : 0x00cc0498 _HEAP_ENTRY
   +0x028 LastValidEntry   : 0x00dbf000 _HEAP_ENTRY
   +0x02c NumberOfUnCommittedPages : 0xed
   +0x030 NumberOfUnCommittedRanges : 1
   +0x034 SegmentAllocatorBackTraceIndex : 0
   +0x036 Reserved         : 0
   +0x038 UCRSegmentList   : _LIST_ENTRY [ 0xcd1ff0 - 0xcd1ff0 ]
   +0x040 Flags            : 0x40000062
   +0x044 ForceFlags       : 0x40000060
   +0x048 CompatibilityFlags : 0x20000000
   +0x04c EncodeFlagMask   : 0x100000
   +0x050 Encoding         : _HEAP_ENTRY
   +0x058 Interceptor      : 0
   +0x05c VirtualMemoryThreshold : 0xfe00
   +0x060 Signature        : 0xeeffeeff
   +0x064 SegmentReserve   : 0x100000
   +0x068 SegmentCommit    : 0x2000
   +0x06c DeCommitFreeBlockThreshold : 0x200
   +0x070 DeCommitTotalFreeThreshold : 0x2000
   +0x074 TotalFreeSize    : 0x3f0
   +0x078 MaximumAllocationSize : 0x7ffdefff
   +0x07c ProcessHeapsListIndex : 1
   +0x07e HeaderValidateLength : 0x248
   +0x080 HeaderValidateCopy : (null)
   +0x084 NextAvailableTagIndex : 0
   +0x086 MaximumTagIndex  : 0
   +0x088 TagEntries       : (null)
   +0x08c UCRList          : _LIST_ENTRY [ 0xcd1fe8 - 0xcd1fe8 ]
   +0x094 AlignRound       : 0x17
   +0x098 AlignMask        : 0xfffffff8
   +0x09c VirtualAllocdBlocks : _LIST_ENTRY [ 0xcc009c - 0xcc009c ]
   +0x0a4 SegmentList      : _LIST_ENTRY [ 0xcc0010 - 0xcc0010 ]
   +0x0ac AllocatorBackTraceIndex : 0
   +0x0b0 NonDedicatedListLength : 0
   +0x0b4 BlocksIndex      : 0x00cc0260 Void
   +0x0b8 UCRIndex         : (null)
   +0x0bc PseudoTagEntries : (null)
   +0x0c0 FreeLists        : _LIST_ENTRY [ 0xccb1f8 - 0xcd1000 ]
   +0x0c8 LockVariable     : 0x00cc0248 _HEAP_LOCK
   +0x0cc CommitRoutine    : 0x3cc8c60f     long  +3cc8c60f
   +0x0d0 FrontEndHeap     : (null)
   +0x0d4 FrontHeapLockCount : 0
   +0x0d6 FrontEndHeapType : 0 ''
   +0x0d7 RequestedFrontEndHeapType : 0 ''
   +0x0d8 FrontEndHeapUsageData : 0x00cc04a0  -> 0
   +0x0dc FrontEndHeapMaximumIndex : 0x80
   +0x0de FrontEndHeapStatusBitmap : [257]  ""
   +0x1e0 Counters         : _HEAP_COUNTERS
   +0x23c TuningParameters : _HEAP_TUNING_PARAMETERS
```

其中得到：
```
+0x04c EncodeFlagMask   : 0x100000
+0x050 Encoding         : _HEAP_ENTRY
```

```
0:000> dd 00cc0000+50
00cc0050  c33c9efb 0000e2e2 00000000 0000fe00
00cc0060  eeffeeff 00100000 00002000 00000200
00cc0070  00002000 000003f0 7ffdefff 02480001
00cc0080  00000000 00000000 00000000 00cd1fe8
00cc0090  00cd1fe8 00000017 fffffff8 00cc009c
00cc00a0  00cc009c 00cc0010 00cc0010 00000000
00cc00b0  00000000 00cc0260 00000000 00000000
00cc00c0  00ccb1f8 00cd1000 00cc0248 3cc8c60f
```

XOR 操作数为：`c33c9efb 0000e2e2`。
原始数据：
```
0:000> dd 00cc6d90
00cc6d90  c03b9eff 1800e2e8 00000002 00000003
00cc6da0  abababab abababab 00000000 00000000
00cc6db0  dc3b9ee3 1800e2e6 6dc8b9b4 6dc8bb80
00cc6dc0  6dc8b720 770dc5c0 00000000 00cc6e78
00cc6dd0  6dc8b9b4 6dc8bb90 6dc8b540 770dc2e0
00cc6de0  00000000 00cc6ea0 6dc8b9b4 6dc8bba8
00cc6df0  6dc8c900 770dc670 00000000 00cc6ec8
00cc6e00  6dc8bbb8 6dc8bbc4 6dce0e40 00000000
```

头部信息为：`c03b9eff 1800e2e8`

做异或运算进行解码：
```
0:000> ? c03b9eff^c33c9efb
Evaluate expression: 50790404 = 03070004
0:000> ? 1800e2e8^0000e2e2
Evaluate expression: 402653194 = 1800000a
```

低地址的 word 是 Size 字段，所以 Size 字段是 0x4，因为是以粒度 8 为单位的，所以字节大小是：
```
0:000> ? 4*8
Evaluate expression: 32 = 00000020
```

也可以直接解码：
```
0:000> !heap -i 00cc6d90
Detailed information for block entry 00cc6d90
Assumed heap       : 0x00cc0000 (Use !heap -i NewHeapHandle to change)
Header content     : 0xC03B9EFF 0x1800E2E8 (decoded : 0x03070004 0x1800000A)
Owning segment     : 0x00cc0000 (offset 0)
Block flags        : 0x7 (busy extra fill )
Total block size   : 0x4 units (0x20 bytes)
Requested size     : 0x8 bytes (unused 0x18 bytes)
Previous block size: 0xa units (0x50 bytes)
Block CRC          : OK - 0x3
Previous block     : 0x00cc6d40
Next block         : 0x00cc6db0
```

三种方法结果都是：`Total block size   : 0x4 units (0x20 bytes)`
还原后的头部信息：`0x03070004 0x1800000A`


## 头部结构

{% include image.html url="/assets/images/210619-win-windbg-cases-heap-e~16/20200312111504316.png" %}

`0x03070004 0x1800000A`
* 0004 -- 大小是 4 字节。
* 0307 -- 前一个堆块的大小。
* 0A -- 堆溢出检查 cookie
* 00 -- Flags
* 00 -- 补齐未使用的字节。
* 18 -- 这个堆块的序号。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-06-19-win-windbg-cases-heap-entry.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://stackoverflow.com/questions/28483473/windows-heap-chunk-header-parsing-and-size-calculation]({% include relrefx.html url="/backup/2021-06-19-win-windbg-cases-heap-entry.md/stackoverflow.com/797c2d6f.html" %})
- [http://advdbg.org/blogs/advdbg_system/articles/5152.aspx]({% include relrefx.html url="/backup/2021-06-19-win-windbg-cases-heap-entry.md/advdbg.org/df049c84.aspx" %})
- [https://www.cnblogs.com/xumaojun/p/8544089.html]({% include relrefx.html url="/backup/2021-06-19-win-windbg-cases-heap-entry.md/www.cnblogs.com/36e9d8f7.html" %})
