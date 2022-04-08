---
layout: post
title: "编程与调试 -- 使用 ctypes 进行 Python 和 C 的混合编程"
author: yqh
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "Python"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid: true
glslcanvas:
codeprint:
---

尝试解决的问题：Python 调用 C++，C++ 回调 Python，并传递参数。
1. Python 能调用 C 语言的函数；
    * 支持 Python 调用 C++，支持传入 json 参数，传出 json 参数，灵活且内存管理正确。
2. Python 通过调用 C 函数，并注册 Python 的回调函数，C 代码通过 Python 回调函数告诉 Python 当前实时进度和状态。
    * 支持 C++ 回调 Python，支持传入 json 参数，传出 json 参数，灵活且内存管理正确。
3. 改进了一下，支持多线程并发。

早期也实现了一个 C# 版本，这里要实现一个 Python 版本。
[官方文档](https://docs.python.org/3/library/ctypes.html)
Python ctypes 像天书一般，后来慢慢明白了它面临的问题，以及解决的思路，才算彻底的理解了。

[这篇文章 {% include relref_cnblogs.html %}](https://www.cnblogs.com/gaowengang/p/7919219.html) 不错，主要是 Python2 的。


## 数据类型

ctypes 支持的原生数据类型如下：
{% include image.html url="/assets/images/210914-mixed-python-and-c/986259-20171129140831581-1373706197.png" %}

Python 中的类型，除了 None、int、long、Byte String、Unicode String 作为 C 函数的参数默认提供转换外，其它类型都必须显式提供转换。
* None 是作为 C 的 NULL 指针传递。
* 字节串和字符串作为内存块指针传递（char* 或 wchar_t*）。
* Python 整数作为平台相关的 C 语言 int 类型传递，其值会截断到 C 类型。


## 函数设置

如果不指定 C 函数的返回值， ctypes 默认返回 int 类型，如果要返回特定类型，需要指定返回类型 `restype`。
参数类型通过 `argtypes` 指定。

```python
# 设置函数参数类型为 int, int, int, void*
fun.argtypes = (c_int, c_int, c_int, c_void_p)
# 设置返回值类型为 float
fun.restype  = c_float
```


## 回调函数

**Note** Make sure you keep references to `CFUNCTYPE()` objects as long as they are used from C code.
ctypes doesn’t, and if you don’t, they may be garbage collected, crashing your program when a callback is made.
Also, note that if the callback function is called in a thread created outside of Python’s control (e.g. by the foreign code that calls the callback), ctypes creates a new dummy Python thread on every invocation.
This behavior is correct for most purposes, but it means that values stored with `threading.local` will not survive across different callbacks, even when those calls are made from the same C thread.

**回调函数的重要提示：**
确保你在 C 代码的使用生命周期里保持引用 CFUNCTYPE 对象。ctypes 并不会帮你做这样的事情，如果你没有做保证，它们就会被垃圾回收，然后当你调用这个回调函数时将会导致程序崩溃。


## Windows 类型

Windows API 有一些特殊之处，Windows API 函数不使用标准 C 的调用约定。
- LoadLibrary 时不能够使用 cdll.LoadLibrary 而使用 windll.LoadLibrary。
- 在声明回调函数指针类型的时候，不能用 CFUNCTYPE 而是用 WINFUNCTYPE。

Windows API 有很多内建类型，ctypes 内部都已经定义好了，在子模块 wintypes 下，可以直接使用。
`DWORD`
`HANDLE`
`BOOL`
`WORD`
`LPCWSTR`
`_COORD`
`SMALL_RECT`
`LPWSTR`
`LPCSTR`
`UINT`
`WCHAR`
`HWND`
`LPVOID`
`LONG`
`ULONG`
`HINSTANCE`
`BYTE`
`LPARAM`
`WPARAM`
`MSG`
`VARIANT_BOOL`
`HMODULE`
`INT`
`SHORT`
`HKEY`
`LPDWORD`
`LPSTR`
`LARGE_INTEGER`
`RECT`
`HDC`
`LPCVOID`
`USHORT`
`BOOLEAN`
`WIN32_FIND_DATAW`

比如 Windows API：
```python
import ctypes
import ctypes.wintypes

GENERIC_WRITE = 0x40000000
CREATE_ALWAYS = 0x00000002
FILE_ATTRIBUTE_NORMAL = 0x00000080
LOCKFILE_EXCLUSIVE_LOCK = 0x00000002
LOCKFILE_FAIL_IMMEDIATELY = 0x00000001

class Overlapped(ctypes.Structure):
    """Overlapped is required and used in LockFileEx and UnlockFileEx."""
    _fields_ = [('Internal', ctypes.wintypes.LPVOID),
                ('InternalHigh', ctypes.wintypes.LPVOID),
                ('Offset', ctypes.wintypes.DWORD),
                ('OffsetHigh', ctypes.wintypes.DWORD),
                ('Pointer', ctypes.wintypes.LPVOID),
                ('hEvent', ctypes.wintypes.HANDLE)]

# https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew
CreateFileW = ctypes.windll.kernel32.CreateFileW
CreateFileW.argtypes = [
    ctypes.wintypes.LPCWSTR,  # lpFileName
    ctypes.wintypes.DWORD,  # dwDesiredAccess
    ctypes.wintypes.DWORD,  # dwShareMode
    ctypes.wintypes.LPVOID,  # lpSecurityAttributes
    ctypes.wintypes.DWORD,  # dwCreationDisposition
    ctypes.wintypes.DWORD,  # dwFlagsAndAttributes
    ctypes.wintypes.LPVOID,  # hTemplateFile
]
CreateFileW.restype = ctypes.wintypes.HANDLE

# https://docs.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-closehandle
CloseHandle = ctypes.windll.kernel32.CloseHandle
CloseHandle.argtypes = [
    ctypes.wintypes.HANDLE,  # hFile
]
CloseHandle.restype = ctypes.wintypes.BOOL

# https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-lockfileex
LockFileEx = ctypes.windll.kernel32.LockFileEx
LockFileEx.argtypes = [
    ctypes.wintypes.HANDLE,  # hFile
    ctypes.wintypes.DWORD,  # dwFlags
    ctypes.wintypes.DWORD,  # dwReserved
    ctypes.wintypes.DWORD,  # nNumberOfBytesToLockLow
    ctypes.wintypes.DWORD,  # nNumberOfBytesToLockHigh
    ctypes.POINTER(Overlapped),  # lpOverlapped
]
LockFileEx.restype = ctypes.wintypes.BOOL

# Commonly used functions are listed here so callers don't need to import
# ctypes.
GetLastError = ctypes.GetLastError
Handle = ctypes.wintypes.HANDLE
```

甚至实现一个 完美的 文件锁：
```python
from __future__ import print_function

import contextlib
import logging
import os
import sys
import time

class LockError(Exception):
    pass

if sys.platform.startswith('win'):
    # Windows implementation
    try:
        from . import win32imports
    except ImportError: # attempted relative import with no known parent package
        import win32imports

    BYTES_TO_LOCK = 1

    def _open_file(lockfile):
        return win32imports.Handle(
            win32imports.CreateFileW(
                lockfile,  # lpFileName
                win32imports.GENERIC_WRITE,  # dwDesiredAccess
                0,  # dwShareMode=prevent others from opening file
                None,  # lpSecurityAttributes
                win32imports.CREATE_ALWAYS,  # dwCreationDisposition
                win32imports.FILE_ATTRIBUTE_NORMAL,  # dwFlagsAndAttributes
                None  # hTemplateFile
            ))

    def _close_file(handle, lockfile):
        # CloseHandle releases lock too.
        win32imports.CloseHandle(handle)
        try:
            os.remove(lockfile)
        except:
            pass

    def _lock_file(handle):
        ret = win32imports.LockFileEx(
            handle,  # hFile
            win32imports.LOCKFILE_FAIL_IMMEDIATELY
            | win32imports.LOCKFILE_EXCLUSIVE_LOCK,  # dwFlags
            0,  #dwReserved
            BYTES_TO_LOCK,  # nNumberOfBytesToLockLow
            0,  # nNumberOfBytesToLockHigh
            win32imports.Overlapped()  # lpOverlapped
        )
        # LockFileEx returns result as bool, which is converted into an integer
        # (1 == successful; 0 == not successful)
        if ret == 0:
            error_code = win32imports.GetLastError()
            raise OSError('Failed to lock handle (error code: %d).' % error_code)
else:
    # Unix implementation
    import fcntl

    def _open_file(lockfile):
        open_flags = (os.O_CREAT | os.O_WRONLY)
        return os.open(lockfile, open_flags, 0o644)

    def _close_file(fd, lockfile):
        os.close(fd)
        try:
            os.remove(lockfile)
        except:
            pass

    def _lock_file(fd):
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)

def _try_lock(lockfile):
    f = _open_file(lockfile)
    try:
        _lock_file(f)
    except Exception:
        _close_file(f, lockfile)
        raise
    return lambda: _close_file(f, lockfile)

def _lock(path, timeout=0):
    """_lock returns function to release the lock if locking was successful.

    _lock also implements simple retry logic."""
    elapsed = 0
    while True:
        try:
            return _try_lock(path + '.lockedfile') # 不要改后缀，funclib 忽略这个文件。
        except (OSError, IOError) as e:
            if elapsed < timeout:
                sleep_time = min(10, timeout - elapsed)
                logging.info(
                    'Could not create git cache lockfile; '
                    'will retry after sleep(%d).', sleep_time)
                elapsed += sleep_time
                time.sleep(sleep_time)
                continue
            raise LockError("Error locking %s (err: %s)" % (path, str(e)))

@contextlib.contextmanager
def lock(path, timeout=0):
    """Get exclusive lock to path.

    Usage:
      import lockfile
      with lockfile.lock(path, timeout):
        # Do something
        pass

     """
    release_fn = _lock(path, timeout)
    try:
        yield
    finally:
        release_fn()
```


## 内部实现

结构体的外皮，实质是指针。

```python
class POINT(Structure):
    _fields_ = [('x', c_int), ('y', c_int)]

class RECT(Structure):
    _fields_ = [('a', POINT), ('b', POINT)]

p1 = POINT(1, 2)
p2 = POINT(3, 4)
rc = RECT(p1, p2)

print('rc.a.x =', rc.a.x)
print('rc.a.y =', rc.a.y)
print('rc.b.x =', rc.b.x)
print('rc.b.y =', rc.b.y)

rc.a, rc.b = rc.b, rc.a

print('after swap, bad result due to this is the pointer.')
print('rc.a.x =', rc.a.x)
print('rc.a.y =', rc.a.y)
print('rc.b.x =', rc.b.x)
print('rc.b.y =', rc.b.y)
```

输出：

```
rc.a.x = 1
rc.a.y = 2
rc.b.x = 3
rc.b.y = 4
after swap, bad result due to this is the pointer.
rc.a.x = 3
rc.a.y = 4
rc.b.x = 3
rc.b.y = 4
```


## C 接口定义

```c
// C++ 回调 Python，支持传入 json，传出 json，传出的 outstr，需要 Python 用 MarioAlloc 申请，并在 C++ 里面合理释放。
typedef int (*MarioCallback)(int code, int subcode, int taskid, const wchar_t* instr, wchar_t*& outstr);
typedef int (*MarioCallback2)(int code, int subcode, int taskid, const wchar_t* instr, wchar_t** outstr);

// Python 调用 C++，支持传入 json，传出 json，需要 Python 调用 MarioRelease 及时释放 outstr。
MARIO_API int MarioFun(MarioCallback callback, int code, int taskid, const wchar_t* instr, wchar_t*& outstr);
// 释放 json 内存。
MARIO_API int MarioRelease(wchar_t*& outstr);
// 申请 json 内存。
MARIO_API int MarioAlloc(wchar_t*& newstr, const wchar_t* instr);
MARIO_API int MarioAlloc2(wchar_t** newstr, const wchar_t* instr);

MARIO_API int MarioPython();
```

遇到一个问题，就是回调的的时候，Python 必须是 `wchar_t**`，才支持反向得到输出，C# 可以支持 `wchar_t*&`。
总结一句话就是：C++ 可以拿到 Python 对象的引用，Python 拿不到 C++ 回调对象的引用（已经被转成了 Python 对象）。
1. Python 调用 C++ 接口，需要告诉 Python 接口参数类型和返回类型，Python 可以做处理，C++ 能拿到 Python 的引用。
2. C++ 调用 Python 接口，真正调用到我们的函数的时候，Python 已经根据 CFUNCTYPE 做了数据处理，是拿不到 `wchar_t*&` 的，但是指针的指针可以解决这个问题。

C# 可以定义回调函数对象引用：
```c#
using System;
using System.Runtime.InteropServices;

public class mario
{
    // C++ 回调 C#，支持传入 json，传出 json，传出的 outstr，需要 C# 用 MarioAlloc 申请，并在 C++ 里面合理释放。
    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate int MarioCallback(
        int code, int subcode, int taskid,
        [MarshalAs(UnmanagedType.LPWStr)] string wstr,
        ref IntPtr outstr);

    // C# 调用 C++，支持传入 json，传出 json，需要 C# 调用 MarioRelease 及时释放 outstr。
    [DllImport("mario.dll", EntryPoint = "MarioFun", CharSet = CharSet.Unicode,
        CallingConvention = CallingConvention.Cdecl)]
    public static extern int MarioFun(
        MarioCallback callback, int code, int taskid,
        [MarshalAs(UnmanagedType.LPWStr)] string instr, ref IntPtr outstr);

    [DllImport("mario.dll", EntryPoint = "MarioRelease", CharSet = CharSet.Unicode,
        CallingConvention = CallingConvention.Cdecl)]
    public static extern int MarioRelease(ref IntPtr pstr);

    [DllImport("mario.dll", EntryPoint = "MarioAlloc", CharSet = CharSet.Unicode,
        CallingConvention = CallingConvention.Cdecl)]
    public static extern int MarioAlloc(ref IntPtr newstr,
        [MarshalAs(UnmanagedType.LPWStr)] string instr);
}
```


## 内存管理

内存都放在 C++ 堆上自己管理。非常对称的内存管理，跑了几百万次，零泄露。

1. Python 调用 `MarioFun`，C++ 里面的内存通过 `MarioAlloc` 申请，返回后 Python 再通过 `MarioRelease` 释放。
   ```cpp
   // C++ 申请内存。
   int fpconvert::MarioFun(fpconvert::MarioCallback callback, int code, int taskid, //
       return MarioAlloc(outstr, outjson.c_str());
   }
   ```
   ```python
   retv = mydll.MarioFun(MarioCallback(funMarioCallback), code, taskid, instr, ctypes.byref(outstr))
   print(outstr.value)
   # Python 释放内存。
   mydll.MarioRelease(ctypes.byref(outstr))
   ```
2. C++ 调用 `MarioCallback2` 到 Python，Python 里面的内存通过 `MarioAlloc2` 申请，返回后 C++ 再通过 `MarioRelease` 释放。
   ```python
   # Python 申请内存。
   def funMarioCallback(code, subcode, tasdid, instr, outstr):
       mydll.MarioAlloc2(outstr, instr)
   ```
   ```cpp
   wchar_t** tempstr = &outstr; // MarioCallback2
   callback(data->fpcode, subcode, (int)taskid, instr, tempstr);
   if (outstr) {
       // C++ 释放内存。
       fpconvert::MarioRelease(outstr);
   }
   ```


## Python 实现

```python
MarioCallback = ctypes.CFUNCTYPE(
        ctypes.c_int,
        ctypes.c_int, # code
        ctypes.c_int, # subcode
        ctypes.c_int, # taskid
        ctypes.c_wchar_p, # instr
        ctypes.POINTER(ctypes.c_wchar_p), # outstr
        )

def mariotest(debug):
    dllpath, dllx64 = getMarioDll(debug)
    mydll = ctypes.cdll.LoadLibrary(dllpath)
    mydll.MarioPython()

    instr = ctypes.create_unicode_buffer(jsondumps({"key": "中文"}))
    outstr = ctypes.c_wchar_p(0)
    print(mydll.MarioAlloc(ctypes.byref(outstr), instr))
    print(outstr.value)
    print(mydll.MarioRelease(ctypes.byref(outstr)))

    def funMarioCallback(code, subcode, tasdid, instr, outstr):
        print("funMarioCallback", code, subcode, tasdid, instr, outstr)
        print(type(outstr), outstr)
        print(mydll.MarioAlloc2(outstr, instr))
        return 1

    code = MARIO_CODE_TEST
    taskid = 2
    instr = ctypes.create_unicode_buffer(jsondumps({"key": "中文"}))
    outstr = ctypes.c_wchar_p(0)
    # MarioCallback(funMarioCallback) 存在生命周期。
    retv = mydll.MarioFun(MarioCallback(funMarioCallback), code, taskid, instr, ctypes.byref(outstr))
    print(outstr.value)
    mydll.MarioRelease(ctypes.byref(outstr))

if __name__ == "__main__":
    mariotest(DEBUG)
```


## C++ 实现

```cpp
#include <assert.h>
#include <iostream>
#include <string>
#include <unordered_map>

#include <functional>
#include "nlohmann/json.hpp"

int g_python = 0; // python 环境

// 回调上下文
struct CallbackContext {
    fpconvert::MarioCallback callback = nullptr; // 回调函数
    int fpcode = -1; // 回调 code
    bool cberr = false; // 是否发生错误。
    CallbackContext(int fpcode, fpconvert::MarioCallback callback) {
        this->fpcode = fpcode;
        this->callback = callback;
    }
};

KLockerCS g_locker;
std::unordered_map<int, CallbackContext*> g_callback;

void SetCallbackContext(int taskid, CallbackContext* data) {
    KLocker locker(&g_locker);
    assert(g_callback.find(taskid) == g_callback.end());
    g_callback[taskid] = data;
}
void ClearCallbackContext(int taskid) {
    KLocker locker(&g_locker);
    assert(g_callback.find(taskid) != g_callback.end());
    g_callback.erase(taskid);
}
bool GetCallbackContext(int taskid, CallbackContext*& data) {
    KLocker locker(&g_locker);
    assert(g_callback.find(taskid) != g_callback.end());
    if (g_callback.find(taskid) != g_callback.end()) {
        data = g_callback[taskid];
        return true;
    }
    else {
        return false;
    }
}

bool ProgressCallback(void* taskid, int progress, int errorcode, const wchar_t* errorfile) {
    CallbackContext* data = nullptr;
    if (GetCallbackContext((int)taskid, data) && data && data->callback) {
        nlohmann::json result;
        result["progress"] = progress;
        result["errorcode"] = errorcode;
        result["errorfile"] = UTF8_ENCODE(errorfile);
        std::string retv = result.dump();
        std::wstring outjson = UTF8_DECODE(retv.c_str());

        int subcode = 1;
        const wchar_t* instr = outjson.c_str();
        wchar_t* outstr = nullptr;
        int retcode = -1;
        if (g_python) {
            wchar_t** tempstr = &outstr; // MarioCallback2
            retcode = ((fpconvert::MarioCallback2)data->callback)(data->fpcode, subcode, (int)taskid, instr, tempstr);
        }
        else {
            retcode = data->callback(data->fpcode, subcode, (int)taskid, instr, outstr);
        }
        if (outstr) {
            fpconvert::MarioRelease(outstr);
        }
        bool isok = retcode == 0 && errorcode == 0;
        if (!isok) {
            data->cberr = true;
        }
        return isok;
    }
    return false;
}

// C++ 回调 Python，支持传入 json，传出 json，传出的 outstr，需要 Python 用 MarioAlloc 申请，并在 C++ 里面合理释放。
nlohmann::json fpconvertdll(fpconvert::MarioCallback callback, int code, int taskid, nlohmann::json& config) {
    CallbackContext data(code, callback);

    SetCallbackContext(taskid, &data);

    bool result = false;
    if (code == CODE_TEST) {
        int progress = 100;
        int errorcode = 1;
        const wchar_t* errorfile = L"errorfile";
        ProgressCallback((void*)taskid, progress, errorcode, errorfile);
        result = 0;
    }
    else {
        assert(false);
    }

    ClearCallbackContext(taskid);
    nlohmann::json retjson;
    retjson["ret"] = result && !data.cberr;
    return retjson;
}

// Python 调用 C++，支持传入 json，传出 json，需要 Python 调用 MarioRelease 及时释放 outstr。
int fpconvert::MarioFun(fpconvert::MarioCallback callback, int code, int taskid, //
    const wchar_t* instr, wchar_t*& outstr) {
    assert(instr && !outstr);
    if (!instr || outstr) {
        return -1;
    }

    std::string injson = UTF8_ENCODE(instr);
    nlohmann::json argv = nlohmann::json::parse(injson); // 必须 utf8 编码。
    nlohmann::json result = fpconvertdll(callback, code, taskid, argv);

    std::string retv = result.dump();
    std::wstring outjson = UTF8_DECODE(retv.c_str());
    return MarioAlloc(outstr, outjson.c_str());
}
int fpconvert::MarioAlloc(wchar_t*& newstr, const wchar_t* instr) {
    assert(!newstr && instr);
    if (newstr || !instr) {
        return -1;
    }
    int size = wcslen(instr);
    newstr = new wchar_t[size + 1];
    wcscpy_s(newstr, size + 1, instr);
    newstr[size] = 0;
    return 0;
}
int fpconvert::MarioAlloc2(wchar_t** newstr, const wchar_t* instr) {
    assert(newstr);
    if (!newstr) {
        return -1;
    }
    return MarioAlloc(*newstr, instr);
}
int fpconvert::MarioRelease(wchar_t*& outstr) {
    assert(outstr);
    if (!outstr) {
        return -1;
    }
    delete[] outstr;
    outstr = nullptr;
    return 0;
}
int fpconvert::MarioPython() {
    g_python = 1;
    return 0;
}
```


## 不定长数据传输

[note {% include relref_cnblogs.html %}](https://www.cnblogs.com/iclodq/p/9216763.html)
实现一个二进制输入，二进制输出的版本。
* 变长输入，Python -> C++，直接调用就好了。
* 变长回调，C++ -> Python，回调两次就好了。


### Python

```python
# 变长输入，Python -> C++，直接调用就好了。
# 变长回调，C++ -> Python，回调两次就好了。
def mariotest3(data):
    dllpath, dllx64 = getMarioDll(DEBUG)
    mydll = ctypes.cdll.LoadLibrary(dllpath)
    mydll.MarioPython()

    MarioCallbackTest = ctypes.CFUNCTYPE(
        ctypes.c_int,
        ctypes.c_size_t,
        ctypes.POINTER(ctypes.c_char_p),
        )

    result = None
    def funMarioCallbackTest(size, pdata): # <__main__.LP_c_char_p object at>
        #print("funMarioCallbackTest", size, pdata)

        MarioCallbackRCB = ctypes.CFUNCTYPE(
            ctypes.c_int,
            ctypes.c_size_t,
            ctypes.POINTER(ctypes.c_char * size),
        )

        def funMarioCallbackRCB(size, mdata): # <__main__.LP_c_char_Array_10 object at>
            #print("funMarioCallbackRCB", size, mdata)
            #print(mdata.contents.raw)
            nonlocal result
            result = mdata.contents.raw
            return 0
        # 根据参数，再次构造 Python 回调函数。
        mydll.MarioReCallback(MarioCallbackRCB(funMarioCallbackRCB), pdata, size)
        return 0

    datasize = len(data)
    mydll.MarioTest(MarioCallbackTest(funMarioCallbackTest), data, datasize)
    #print(data) -- Python 内存传入，是可以直接被修改的。
    print("Python print", "\t", result)
    return result

if __name__ == "__main__":
    #mariotest2(b"abc")
    #mariotest2(b"abcdef")
    #mariotest(DEBUG)
    mariotest3(b"ab\x00\x01")
```


### C++

```cpp
// https://www.cnblogs.com/iclodq/p/9216763.html
typedef int (*MarioCallbackTest)(size_t size, const char** pdata);
MARIO_API int MarioTest(MarioCallbackTest callback, char* input, size_t size);

typedef int (*MarioCallbackRCB)(size_t size, const char* mdata);
MARIO_API int MarioReCallback(MarioCallbackRCB callback, const char** data, size_t size);
```

```cpp
// https://www.cnblogs.com/iclodq/p/9216763.html
int fpconvert::MarioTest(MarioCallbackTest callback, char* input, size_t size) {
    if (!callback || !input) {
        return -1;
    }
    printf("C++ printf \t b'");
    for (int i = 0; i < size; i++) {
        printf("\\x%02x", input[i]);
        //input[i]++; -- 这里是可以直接改 Python 内存的。
    }
    printf("'\r\n");
    if (callback) {
        const int size = 10;
        char temp[size];
        strcpy_s(temp, size, "mario");
        temp[1] = 0;
        const char* tempp = temp;
        const char** ptemp = &tempp;
        callback(size, ptemp);
    }
    return 0;
}

int fpconvert::MarioReCallback(MarioCallbackRCB callback, const char** data, size_t size) {
    if (!callback || !data) {
        return -1;
    }
    const char* pdata = *data;
    if (!pdata) {
        return -1;
    }
    callback(size, pdata);
    return 0;
}
```


### 结果输出

```
C:\kSource\pythonx>python3 mario.py
MarioDll C:\kSource\pythonx\note\pythonx\mario\Debug\mario.dll
C++ printf       b'\x61\x62\x00\x01'
Python print     b'm\x00rio\x00\xfe\xfe\xfe\xfe'
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-09-14-mixed-python-and-c.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.python.org/3/library/ctypes.html]({% include relrefx.html url="/backup/2021-09-14-mixed-python-and-c.md/docs.python.org/a9cf72b8.html" %})
- [https://www.cnblogs.com/gaowengang/p/7919219.html]({% include relrefx.html url="/backup/2021-09-14-mixed-python-and-c.md/www.cnblogs.com/4b57faf7.html" %})
- [https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew]({% include relrefx.html url="/backup/2021-09-14-mixed-python-and-c.md/docs.microsoft.com/598632a2.html" %})
- [https://docs.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-closehandle]({% include relrefx.html url="/backup/2021-09-14-mixed-python-and-c.md/docs.microsoft.com/2b6cd75d.html" %})
- [https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-lockfileex]({% include relrefx.html url="/backup/2021-09-14-mixed-python-and-c.md/docs.microsoft.com/95fd3989.html" %})
- [https://www.cnblogs.com/iclodq/p/9216763.html]({% include relrefx.html url="/backup/2021-09-14-mixed-python-and-c.md/www.cnblogs.com/5d790fbb.html" %})
