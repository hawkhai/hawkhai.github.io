---
layout: post
title: "编程与调试 C++ -- 如何刷新托盘区域"
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

以下两种情况需要刷新托盘区域

1、我们自己的托盘异常退出（进程管理器结束）后，依然有托盘图标残留。

2、对抗逻辑，我们强杀了别人的程序，别人的程序是一个托盘程序，会有托盘图标残留。

原理：遍历托盘图标，找出托盘图标所对应的进程 ID，如果该 ID 为 NULL 则删除该图标。

下面是代码样本，仅供参考，来源于网上：

```cpp
int main()
{
    HWND  hStatus = ::FindWindow("Shell_TrayWnd", NULL); // 得到任务栏句柄
    HWND  hNotify = FindWindowEx(hStatus, NULL, "TrayNotifyWnd", NULL); // 右下角区域
    HWND  hNotify1 = FindWindowEx(hNotify, NULL, "SysPager", NULL);
    HWND  hNotify1_0 = FindWindowEx(hNotify1, NULL, "ToolBarWindow32", NULL); // 右下角区域（不包括时间）
    DWORD  pid = 0;
    GetWindowThreadProcessId(hNotify1_0, &pid);
    HANDLE  hProcess = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_ALL_ACCESS, true, pid);
    ::SendMessage(hNotify1_0, WM_PAINT, NULL, NULL);
    CRect rect;
    ::GetWindowRect(hNotify1_0, &rect);
    ::InvalidateRect(hNotify1_0, &rect, false);
    int  iNum = ::SendMessage(hNotify1_0, TB_BUTTONCOUNT, NULL, NULL); // 获取任务栏上图标个数

    unsigned long n = 0;
    TBBUTTON* pButton = new TBBUTTON;
    CString  strInfo = _T("");
    wchar_t  name[256] = { 0 };
    TBBUTTON  BButton;
    unsigned   long    whd, proid;
    CString x;

    for (int i = 0; i < iNum; i++)
    {
        ::SendMessage(hNotify1_0, TB_GETBUTTON, i, (LPARAM)(&BButton));
        ReadProcessMemory(hProcess, &BButton, pButton, sizeof(TBBUTTON), &n);
        if (pButton->iString != 0xffffffff)
        {
            try
            {
                ReadProcessMemory(hProcess, (void*)pButton->iString, name, 255, &n);
            }
            catch (...)
            {
            }
            strInfo.Format("%d : %s\n", i + 1, CString(name));
            TRACE(strInfo);
            cout << strInfo << endl;
        }

        try
        {
            whd = 0;
            ReadProcessMemory(hProcess, (void*)pButton->dwData, &whd, 4, &n);
        }
        catch (...)
        {
        }
        proid = NULL;
        GetWindowThreadProcessId((HWND)whd, &proid);
        if (proid == NULL)
            ::SendMessage(hNotify1_0, TB_DELETEBUTTON, i, 0);
    }
    delete pButton;
    return 0;
}
```

[from](https://twiki.cmcm.com/pages/viewpage.action?pageId=154895089)

**桌面图标清理的刷新机制**
win7\win10 系统，如果删除桌面 \ 任务栏图标文件，需要同时刷新下系统界面，否则可能会有图标残留，刷新 API 为：

```cpp
SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_IDLIST, NULL, NULL)
void SHChangeNotify(
    LONG wEventId,
    UINT uFlags,
    LPCVOID dwItem1,
    LPCVOID dwItem2);
```

Notifies the system of an event that an application has performed.
An application should use this function if it performs an action that may affect the Shell.

其中： **wEventId** :
Describes the event that has occurred. Typically, only one event is specified at a time.
If more than one event is specified, the values contained in the dwItem1 and dwItem2 parameters must be the same,
respectively, for all specified events. This parameter can be one or more of the following values.

**SHCNE_ASSOCCHANGED**
A file type association has changed. SHCNF_IDLIST must be specified in the uFlags parameter.
dwItem1 and dwItem2 are not used and must be NULL.
This event should also be sent for registered protocols.



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-04-win-xp-code.md.js" %}'></script></p>
