---
layout: post
title: "编程与调试 Memory -- 危险的 QT 工程 全局对象"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["调试", "Memory", "QT"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
cluster: "WinDBG"
---

发了一个版本，一堆崩溃上涨。
```
qt5core.dll_5.15.0.0_1839eb_fastapp.exe_2021.12.17.1038_aad436e.txt
qt5core.dll_5.15.0.0_cc5ea_fastapp.exe_2021.12.17.1038_fac3a9f.txt
qt5core.dll_5.15.0.0_cc5ea_fastapp.exe_2021.12.17.1038_731aaa5.txt
qt5core.dll_5.15.0.0_cc5ea_fastapp.exe_2021.12.17.1038_2bab1f2.txt
qt5core.dll_5.15.0.0_cc5ea_fastapp.exe_2021.12.17.1038_1866fdc.txt
qt5core.dll_5.15.0.0_cc5ea_fastapp.exe_2021.12.17.1038_6477f95.txt
```

```
CONTEXT:  (.ecxr)
eax=0110f8c8 ebx=015c5200 ecx=00000000 edx=015965b8 esi=015c5200 edi=0110f974
eip=7bbcc5ea esp=0110f85c ebp=0110f8c0 iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00210246
qt5core!operator<<+0xa:
7bbcc5ea 8b11            mov     edx,dword ptr [ecx]  ds:002b:00000000=????????
Resetting default scope

EXCEPTION_RECORD:  (.exr -1)
ExceptionAddress: 7bbcc5ea (qt5core!operator<<+0x0000000a)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 00000000
Attempt to read from address 00000000
```

代码堆栈：
```
ChildEBP RetAddr  Args to Child
019cf8e8 019cfa04 7aebedfc 019cfa04 019cf958 qt5core!operator<<+0xa [C:\Users\qt\work\qt\qtbase\src\corelib\time\qtimezone.cpp @ 971]
WARNING: Frame IP not in any known module. Following frames may be wrong.
019cf950 7af9117a 00000000 04687638 586d2c93 0x19cfa04
(Inline) -------- -------- -------- -------- qt5core!`anonymous-namespace'::FilteredOperatorSwitch<QDateTime,1>::save+0xd [C:\Users\qt\work\qt\qtbase\src\corelib\kernel\qmetatype.cpp @ 1466]
(Inline) -------- -------- -------- -------- qt5core!`anonymous-namespace'::SaveOperatorSwitch::delegate+0xd [C:\Users\qt\work\qt\qtbase\src\corelib\kernel\qmetatype.cpp @ 1508]
019cf97c 7af94f6c 019cf990 00000010 04687638 qt5core!QMetaTypeSwitcher::switcher<bool,`anonymous namespace'::SaveOperatorSwitch>+0x28a [C:\Users\qt\work\qt\qtbase\src\corelib\kernel\qmetatypeswitcher_p.h @ 74]
019cf994 7afbb579 019cfa04 00000010 04687638 qt5core!QMetaType::save+0x2c [C:\Users\qt\work\qt\qtbase\src\corelib\kernel\qmetatype.cpp @ 1616]
019cf9e0 7afb79ed 019cfa04 7af33580 019cfa04 qt5core!QVariant::save+0x1b9 [C:\Users\qt\work\qt\qtbase\src\corelib\kernel\qvariant.cpp @ 2599]
019cf9e8 7af33580 019cfa04 04687638 586d2fbb qt5core!operator<<+0xd [C:\Users\qt\work\qt\qtbase\src\corelib\kernel\qvariant.cpp @ 2626]
019cfa54 7af340d7 019cfab0 04687638 586d2f07 qt5core!QSettingsPrivate::variantToString+0x3e0 [C:\Users\qt\work\qt\qtbase\src\corelib\io\qsettings.cpp @ 460]
019cfae8 7af32865 019cfb24 0000001b 586d2e97 qt5core!QConfFileSettingsPrivate::writeIniFile+0x8d7 [C:\Users\qt\work\qt\qtbase\src\corelib\io\qsettings.cpp @ 1897]
019cfb78 7af323c4 01f4c698 586d2e43 ffffffff qt5core!QConfFileSettingsPrivate::syncConfFile+0x455 [C:\Users\qt\work\qt\qtbase\src\corelib\io\qsettings.cpp @ 1515]
019cfbac 7af29c5f 586d2e37 ffffffff 01f4cdac qt5core!QConfFileSettingsPrivate::sync+0x64 [C:\Users\qt\work\qt\qtbase\src\corelib\io\qsettings.cpp @ 1368]
Unable to load image C:\Program Files (x86)\fastapp\fastapp.exe, Win32 error 0n2
019cfbd8 00c0a5dc 01f4cda0 019cfc34 00bf89db qt5core!QSettings::~QSettings+0x4f [C:\Users\qt\work\qt\qtbase\src\corelib\io\qsettings.cpp @ 2763]
019cfbe4 00bf89db 00000000 012c975e 012c9740 fastapp!QSettings::`scalar deleting destructor'+0xc
(Inline) -------- -------- -------- -------- fastapp!std::_Destroy_in_place+0xb [D:\Program Files\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\include\xmemory @ 311]
019cfbec 012c975e 012c9740 01f44934 7614aab2 fastapp!std::_Ref_count_obj2<QNetworkAccessManager>::_Destroy+0xb [D:\Program Files\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\include\memory @ 2048]
(Inline) -------- -------- -------- -------- fastapp!std::_Ref_count_base::_Decref+0x13 [D:\Program Files\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\include\memory @ 1109]
(Inline) -------- -------- -------- -------- fastapp!std::_Ptr_base<QSettings>::_Decref+0x1e [D:\Program Files\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\include\memory @ 1339]
(Inline) -------- -------- -------- -------- fastapp!std::shared_ptr<QSettings>::{dtor}+0x1e [D:\Program Files\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\include\memory @ 1628]
(Inline) -------- -------- -------- -------- fastapp!UserDataParser::{dtor}+0x1e [D:\x\x\x\pdfreader\pdfreader\public\cfgparser\UserDataParser.cpp @ 33]
019cfbf8 7614aab2 5ec3edf4 019cfd1c 5f5f11c0 fastapp!`SingleTon<RecordReadModeStatus>::GetInstance'::`2'::`dynamic atexit destructor for 'obj''+0x1e
019cfc34 7614a9ac 5ec3eda8 019cfd1c 5f5f11c0 ucrtbase!<lambda_f03950bc5685219e0bcd2087efbe011e>::operator()+0xc2
019cfc68 761644d1 019cfcac 019cfcb0 019cfcb4 ucrtbase!__crt_seh_guarded_call<int>::operator()<<lambda_69a2805e680e0e292e8ba93315fe43a8>,<lambda_f03950bc5685219e0bcd2087efbe011e> &,<lambda_03fcd07e894ec930e3f35da366ca99d6> >+0x30
019cfcd4 76164428 5ec3ecc4 00000000 00000000 ucrtbase!<lambda_ad52fe89635f51ec3b38e9c3ac6dac81>::operator()+0x76
019cfd04 761643e3 019cfd28 019cfd1c 019cfd2c ucrtbase!__crt_seh_guarded_call<void>::operator()<<lambda_a715b363f4867c8a5326adff5c70bf54>,<lambda_ad52fe89635f51ec3b38e9c3ac6dac81> &,<lambda_a0b8da23a0f8cfcbbddd2fe776355bab> >+0x2c
019cfd38 76164391 00000000 019cfd84 01248996 ucrtbase!common_exit+0x4f
019cfd44 01248996 00000000 7d2750e8 0124899f ucrtbase!exit+0x11
019cfd84 7537fa29 01a0e000 7537fa10 019cfdf0 fastapp!__scrt_common_main_seh+0x173 [d:\a01\_work\5\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl @ 310]
019cfd94 774c7a9e 01a0e000 ee5dfe19 00000000 kernel32!BaseThreadInitThunk+0x19
019cfdf0 774c7a6e ffffffff 774e8a6c 00000000 ntdll!__RtlUserThreadStart+0x2f
019cfe00 00000000 0124899f 01a0e000 00000000 ntdll!_RtlUserThreadStart+0x1b
```

很奇怪，这玩意崩溃了。

{% include image.html url="/assets/images/211223-win-windbg-qt-global-obj/z1.png" %}
{% include image.html url="/assets/images/211223-win-windbg-qt-global-obj/z2.png" %}
{% include image.html url="/assets/images/211223-win-windbg-qt-global-obj/z3.png" %}
{% include image.html url="/assets/images/211223-win-windbg-qt-global-obj/z4.png" %}
{% include image.html url="/assets/images/211223-win-windbg-qt-global-obj/z5.png" %}
{% include image.html url="/assets/images/211223-win-windbg-qt-global-obj/z6.png" caption="配置文件乱码 -> 导致生成默认的 QTimeZone -> 默认 QTimeZone 序列化崩溃" %}



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-12-23-win-windbg-qt-global-obj.md.js" %}'></script></p>
