---
layout: post
title: "编程与调试 C++ -- Nemesis blog 杂谈"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
archived: true
---

<https://www.cnblogs.com/suanguade/>
<https://github.com/276793422>


## 内存泄漏

umdh 工具快查内存泄露。
umdh 工具和 gflags 工具都是 WinDBG 工具集里面的工具，去目录里面找就好，这个内存泄漏查询，只能支持正在执行的进程。


## DynamoRIO

插桩库的编译


## clamav

我为啥要弄 clamav 呢，因为这玩意就是个开源杀毒软件啊。


## 三套函数实现应用层做文件监控

* 第一套函数，基于窗口，可以获取修改的文件名和路径，但是可能一些特殊目录的修改无法获取
    * <https://docs.microsoft.com/zh-cn/windows/win32/api/shlobj_core/nf-shlobj_core-shchangenotifyregister>
* 第二套函数，基于 Event，只能获取到目录，无法获取修改的文件
    * <https://docs.microsoft.com/zh-cn/windows/win32/api/fileapi/nf-fileapi-findfirstchangenotificationa>
* 第三套函数，基于 Event，可以根据目录获取修改的文件名
    * <https://docs.microsoft.com/zh-cn/windows/win32/api/winbase/nf-winbase-readdirectorychangesw>


## 下载指定符号

1. 下载 dmp 文件所有相关模块的 symbols，缓存到共享路径，便于其它人快速下载。
  ```
"D:\Debuggers.10\x86\symchk.exe" /id c:\MyApplication.dmp /s SRV*\\symbols_server\WinSymbols\*http://msdl.microsoft.com/download/symbols
```
2. 下载某个已运行进程所有相关模块的 symbols，缓存到共享路径，便于其它人快速下载。
  ```
"D:\Debuggers.10\x86\symchk.exe" /ie qq.exe /s SRV*\\symbols_server\WinSymbols\*http://msdl.microsoft.com/download/symbols
```
3. 下载某个 exe/dll 文件对应的 symbols，例如 user32.dll，输入命令行：
  ```
"D:\Debuggers.10\x86\symchk.exe" c:\windows\system32\user32.dll /s SRV*c:\symbols\*http://msdl.microsoft.com/download/symbols
```
4. 下载整个目录下（例如 system32）所有模块的 symbols：
  ```
"D:\Debuggers.10\x86\symchk.exe" /r c:\windows\system32\ /s SRV*c:\symbols\*http://msdl.microsoft.com/download/symbols
```


## 使用 64 system32 目录下的文件

```cpp
/**
 * @brief 用于在局部区域短暂关闭 Wow64 下的文件重定向功能
 */
class WinFileWow64Guard {

public:

    // Wow64DisableWow64FsRedirection 只对当前线程有效！
    WinFileWow64Guard(BOOL bEnable = TRUE, BOOLEAN forceWow64FsEnableRedirection = FALSE)
        : m_bEnable(bEnable)
        , m_bWow64(FALSE)
        , m_pVoidValue(NULL)
    {
        if (m_bEnable && WinCheckCureentProcessIsWow64Process(&m_bWow64) && m_bWow64)
        {
            // 每次用 m_pVoidValue，可以保证嵌套的情况下可用。
            WinWow64DisableWow64FsRedirection(&m_pVoidValue);

            if (forceWow64FsEnableRedirection) {
                WinWow64EnableWow64FsRedirection(forceWow64FsEnableRedirection);
            }
        }
    }

    virtual ~WinFileWow64Guard()
    {
        if (m_bEnable && m_bWow64)
        {
            // 每次用 m_pVoidValue，可以保证嵌套的情况下可用。
            WinWow64RevertWow64FsRedirection(m_pVoidValue);
        }
    }

private:
    BOOL  m_bEnable;
    BOOL  m_bWow64;
    PVOID m_pVoidValue; // 每次用 m_pVoidValue，可以保证嵌套的情况下可用。
};
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-25-win-cnblogs-suanguade.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/suanguade/]({% include relrefx.html url="/backup/2021-04-25-win-cnblogs-suanguade.md/www.cnblogs.com/e3ef6783.html" %})
- [https://github.com/276793422]({% include relrefx.html url="/backup/2021-04-25-win-cnblogs-suanguade.md/github.com/9a13da93.html" %})
- [https://docs.microsoft.com/zh-cn/windows/win32/api/shlobj_core/nf-shlobj_core-shchangenotifyregister]({% include relrefx.html url="/backup/2021-04-25-win-cnblogs-suanguade.md/docs.microsoft.com/eb9d3894.html" %})
- [https://docs.microsoft.com/zh-cn/windows/win32/api/fileapi/nf-fileapi-findfirstchangenotificationa]({% include relrefx.html url="/backup/2021-04-25-win-cnblogs-suanguade.md/docs.microsoft.com/5328ccc1.html" %})
- [https://docs.microsoft.com/zh-cn/windows/win32/api/winbase/nf-winbase-readdirectorychangesw]({% include relrefx.html url="/backup/2021-04-25-win-cnblogs-suanguade.md/docs.microsoft.com/336092b7.html" %})
- [http://msdl.microsoft.com/download/symbols]({% include relrefx.html url="/backup/2021-04-25-win-cnblogs-suanguade.md/msdl.microsoft.com/9dd253a8.html" %})
