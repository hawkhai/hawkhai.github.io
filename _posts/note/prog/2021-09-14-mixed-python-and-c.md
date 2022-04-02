---
layout: post
title: "编程与调试 -- 使用 ctypes 进行 Python 和 C 的混合编程"
author:
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

[官方文档](https://docs.python.org/3/library/ctypes.html)
**Note** Make sure you keep references to CFUNCTYPE() objects as long as they are used from C code.
ctypes doesn’t, and if you don’t, they may be garbage collected, crashing your program when a callback is made.
Also, note that if the callback function is called in a thread created outside of Python’s control (e.g. by the foreign code that calls the callback), ctypes creates a new dummy Python thread on every invocation.
This behavior is correct for most purposes, but it means that values stored with `threading.local` will not survive across different callbacks, even when those calls are made from the same C thread.

<table class="docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 46%">
<col style="width: 30%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>ctypes type</p></th>
<th class="head"><p>C type</p></th>
<th class="head"><p>Python type</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_bool" title="ctypes.c_bool"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_bool</span></code></a></p></td>
<td><p><span class="xref c c-texpr">_Bool</span></p></td>
<td><p>bool (1)</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_char" title="ctypes.c_char"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_char</span></code></a></p></td>
<td><p><span class="xref c c-texpr">char</span></p></td>
<td><p>1-character bytes object</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_wchar" title="ctypes.c_wchar"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_wchar</span></code></a></p></td>
<td><p><code class="xref c c-type docutils literal notranslate"><span class="pre">wchar_t</span></code></p></td>
<td><p>1-character string</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_byte" title="ctypes.c_byte"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_byte</span></code></a></p></td>
<td><p><span class="xref c c-texpr">char</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_ubyte" title="ctypes.c_ubyte"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_ubyte</span></code></a></p></td>
<td><p><span class="xref c c-texpr">unsigned char</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_short" title="ctypes.c_short"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_short</span></code></a></p></td>
<td><p><span class="xref c c-texpr">short</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_ushort" title="ctypes.c_ushort"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_ushort</span></code></a></p></td>
<td><p><span class="xref c c-texpr">unsigned short</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_int" title="ctypes.c_int"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_int</span></code></a></p></td>
<td><p><span class="xref c c-texpr">int</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_uint" title="ctypes.c_uint"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_uint</span></code></a></p></td>
<td><p><span class="xref c c-texpr">unsigned int</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_long" title="ctypes.c_long"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_long</span></code></a></p></td>
<td><p><span class="xref c c-texpr">long</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_ulong" title="ctypes.c_ulong"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_ulong</span></code></a></p></td>
<td><p><span class="xref c c-texpr">unsigned long</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_longlong" title="ctypes.c_longlong"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_longlong</span></code></a></p></td>
<td><p><code class="xref c c-type docutils literal notranslate"><span class="pre">__int64</span></code> or <span class="xref c c-texpr">long long</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_ulonglong" title="ctypes.c_ulonglong"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_ulonglong</span></code></a></p></td>
<td><p><span class="xref c c-texpr">unsigned __int64</span> or
<span class="xref c c-texpr">unsigned long long</span></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_size_t" title="ctypes.c_size_t"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_size_t</span></code></a></p></td>
<td><p><code class="xref c c-type docutils literal notranslate"><span class="pre">size_t</span></code></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_ssize_t" title="ctypes.c_ssize_t"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_ssize_t</span></code></a></p></td>
<td><p><code class="xref c c-type docutils literal notranslate"><span class="pre">ssize_t</span></code> or
<code class="xref c c-type docutils literal notranslate"><span class="pre">Py_ssize_t</span></code></p></td>
<td><p>int</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_float" title="ctypes.c_float"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_float</span></code></a></p></td>
<td><p><span class="xref c c-texpr">float</span></p></td>
<td><p>float</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_double" title="ctypes.c_double"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_double</span></code></a></p></td>
<td><p><span class="xref c c-texpr">double</span></p></td>
<td><p>float</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_longdouble" title="ctypes.c_longdouble"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_longdouble</span></code></a></p></td>
<td><p><span class="xref c c-texpr">long double</span></p></td>
<td><p>float</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_char_p" title="ctypes.c_char_p"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_char_p</span></code></a></p></td>
<td><p><span class="xref c c-texpr">char*</span> (NUL terminated)</p></td>
<td><p>bytes object or <code class="docutils literal notranslate"><span class="pre">None</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ctypes.c_wchar_p" title="ctypes.c_wchar_p"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_wchar_p</span></code></a></p></td>
<td><p><span class="xref c c-texpr">wchar_t*</span> (NUL terminated)</p></td>
<td><p>string or <code class="docutils literal notranslate"><span class="pre">None</span></code></p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ctypes.c_void_p" title="ctypes.c_void_p"><code class="xref py py-class docutils literal notranslate"><span class="pre">c_void_p</span></code></a></p></td>
<td><p><span class="xref c c-texpr">void*</span></p></td>
<td><p>int or <code class="docutils literal notranslate"><span class="pre">None</span></code></p></td>
</tr>
</tbody>
</table>


## 加载

```python
from ctypes import *
dll = cdll.LoadLibrary(dllpath) # stdcall, CDLL(dllpath)
dll = windll.LoadLibrary(dllpath) # cdecl, WinDLL(dllpath)
```

有时动态链接库导出 C++ 函数时，并不是有效的 Python 标识符，例如 "??2@YAPAXI@Z"。这种情况下，必须使用 getattr 获取函数：

```python
func = getattr(cdll.msvcrt, "??2@YAPAXI@Z")
```

在 Windows 上，有些动态链接库导出函数不是用名字，而是用序号 (ordinal)。这时需通过索引获取：

```python
func = cdll.kernel32[1]
```


## 类型

ctypes 支持的原生数据类型如下 :

| ctypes 类型     | C 类型                                   | Python 类型                        |
| --------------- | ---------------------------------------- | -----------------------------------|
| c_char          | char                                     | 1-character string                 |
| c_wchar         | wchar_t                                  | 1-character unicode string         |
| c_byte          | char                                     | int/long                           |
| c_ubyte         | unsigned char                            | int/long                           |
| c_bool          | bool                                     | bool                               |
| c_short         | short                                    | int/long                           |
| c_ushort        | unsigned short                           | int/long                           |
| c_int           | int                                      | int/long                           |
| c_uint          | unsigned int                             | int/long                           |
| c_long          | long                                     | int/long                           |
| c_ulong         | unsigned long                            | int/long                           |
| c_longlong      | \_\_int64 or longlong                    | int/long                           |
| c_ulonglong     | unsigned \_\_int64 or unsigned long long | int/long                           |
| c_float         | float                                    | float                              |
| c_double        | double                                   | float                              |
| c_longdouble    | long double float                        | float                              |
| c_char_p        | char \*                                  | string or None                     |
| c_wchar_p       | wchar_t \*                               | unicode or None                    |
| c_void_p        | void \*                                  | int/long or None                   |

设置函数的参数类型使用函数的 argtypes 属性，直接赋值为一个 ctypes 类型的列表或元组。设置函数的返回值类型使用函数的 restype 属性。下面是示例代码：
Python 中，默认函数返回值是 c_int 型，此类型可以不用显示设置函数的 restype 属性，如果是参数类型是 c_int 型则需要设置。

```python
fun.argtypes = (c_int, c_int, c_int, c_void_p) # 设置函数参数类型为 int, int, int, void *
fun.restype  = c_float # 设置返回值类型为 float
```
None、整数、字节串和（unicode）字符串是可以作为本地 Python 对象直接传递给函数调用的。

- None 是作为 C 的 NULL 指针传递。
- 字节串和字符串作为内存块指针传递（char\* 或 wchar\_t\*）。
- Python 整数作为平台相关的 C 语言 int 类型传递，其值会截断到 C 类型。

除了整数、字节串和字符串以外 Python 类型的参数传递，必须使用 ctypes 类型做包装。

在调用函数时，如果使用了错误的参数数量和调用规范时，ctypes 尝试保护调用。不幸的是该功能仅在 Windows 上有用。
它通过检查函数返回栈来实现，所以尽管发生了错误，但是函数还是调用了。
这很容易导致当前使用的整个 Python 环境崩溃，所以必须很小心的使用。


## 回调函数

```python
import platform
from ctypes import *
if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() =='Linux':
    libc = cdll.LoadLibrary('libc.so.6')

CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int)) # 定义回调函数类型

def py_cmp_func(a, b): # 实现回调函数功能
      print("py_cmp_func", a[0], b[0])
      return a[0] - b[0]

cmp_func = CMPFUNC(py_cmp_func) # 回调函数对象

IntArray5 = c_int * 5
ia = IntArray5(5, 1, 7, 33, 99)
qsort = libc.qsort # 排序函数地址
qsort.restype = None # 排序函数返回值

qsort(ia, len(ia), sizeof(c_int), CMPFUNC(py_cmp_func))
for i in ia:
    print(i, end=" ")

# 输出结果为：1 5 7 33 99
```

**回调函数的重要提示：**

确保你在 C 代码的使用生命周期里保持引用 CFUNCTYPE 对象。ctypes 并不会帮你做这样的事情，如果你没有做保证，它们就会被垃圾回收，然后当你调用这个回调函数时将会导致程序崩溃。


## windows 类型

Windows API 有一些特殊之处，Windows API 函数不使用标准 C 的调用约定（前面已经提到过）。

因此需注意两点：

- LoadLibrary 时不能够使用 cdll.LoadLibrary 而使用 windll.LoadLibrary。
- 在声明回调函数指针类型的时候，不能用 CFUNCTYPE 而是用 WINFUNCTYPE。

Windows API 有很多内建类型，ctypes 内部都已经定义好了，在子模块 wintypes 下，可以直接使用。

代码举例如下：

```python
from ctypes import *
from ctypes import wintypes

# HWND 等类型已定义好了，可直接使用。
WNDENUMPROC = WINFUNCTYPE(wintypes.BOOL, # 定义回调函数类型
                          wintypes.HWND,
                          wintypes.LPARAM)

def EnumWindowsProc(hwnd, lParam): # 实现回调函数功能
    length = user32.GetWindowTextLengthW(hwnd) + 1
    buffer = create_unicode_buffer(length)
    user32.GetWindowTextW(hwnd, buffer, length)
    print(buffer.value)
    return True

user32 = windll.LoadLibrary('user32.dll') # 加载 dll
user32.EnumWindows(WNDENUMPROC(EnumWindowsProc), 0)
```


## 初识

[from {% include relref_cnblogs.html %}](https://www.cnblogs.com/gaowengang/p/7919219.html)
**原文有点老了，针对 Python3 更新了里面的错误。**
Python 和 C 的混合编程工具有很多，这里介绍 Python 标准库自带的 ctypes 模块的使用方法。

Python 的 ctypes 要使用 C 函数，需要先将 C 编译成动态链接库的形式，即 Windows 下的 .dll 文件，或者 Linux 下的 .so 文件。先来看一下 ctypes 怎么使用 C 标准库。

Windows 系统下的 C 标准库动态链接文件为 msvcrt.dll（一般在目录 C:\Windows\System32 和 C:\Windows\SysWOW64 下分别对应 32-bit 和 64-bit，使用时不用刻意区分，Python 会选择合适的）

Linux 系统下的 C 标准库动态链接文件为 libc.so.6（以 64-bit Ubuntu 系统为例，在目录 /lib/x86_64-linux-gnu 下）

例如，以下代码片段导入 C 标准库，并使用 printf 函数打印一条消息：

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() =='Linux':
    libc = cdll.LoadLibrary('libc.so.6')

libc.wprintf('Hello ctypes!\n')
```

另外导入 dll 文件，还有其它方式如下，详细解释请参阅 ctypes module 相关文档，

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
    #libc = windll.LoadLibrary('msvcrt.dll') # Windows only
    #libc = oledll.LoadLibrary('msvcrt.dll') # Windows only
    #libc = pydll.LoadLibrary('msvcrt.dll')

    #libc = CDLL('msvcrt.dll')
    #libc = WinDLL('msvcrt.dll') # Windows only
    #libc = OleDLL('msvcrt.dll') # Windows only
    #libc = PyDLL('msvcrt.dll')
elif platform.system() =='Linux':
    libc = cdll.LoadLibrary('libc.so.6')
    #libc = pydll.LoadLibrary('libc.so.6')

    #libc = CDLL('libc.so.6')
    #libc = PyDLL('libc.so.6')

libc.wprintf('Hello ctypes!\n')
```


## ctypes 数据类型

ctypes 作为 Python 和 C 联系的桥梁，它定义了专有的数据类型来衔接这两种编程语言。如下表，

{% include image.html url="/assets/images/210914-mixed-python-and-c/986259-20171129140831581-1373706197.png" %}

注：Python 中的类型，除了 None，int，long，Byte String，Unicode String 作为 C 函数的参数默认提供转换外，其它类型都必须显式提供转换。

* `None`：对应 C 中的 NULL
* `int, long`：对应 C 中的 int，具体实现时会根据机器字长自动适配。
* `Byte String`：对应 C 中的一个字符串指针 char \*，指向一块内存区域。
* `Unicode String`：对应 C 中一个宽字符串指针 wchar_t \*，指向一块内存区域。

例如：

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary('libc.so.6')

libc.wprintf('%s\n', 'here!')        # here!
libc.wprintf(u'%s\n', u'there!')     # there!
libc.wprintf('%d\n', 42)             # 42
libc.wprintf('%ld\n', 60000000)      # 60000000

#libc.wprintf('%f\n', 3.14)          #>>> ctypes.ArgumentError
#libc.wprintf('%f\n', c_float(3.14)) #>>> dont know why 0.000000
libc.wprintf('%f\n', c_double(3.14)) # 3.140000
```


## 创建可变的 string buffer

Python 默认的 string 是不可变的，所以不能传递 string 到一个 C 函数去改变它的内容，所以需要使用 create_string_buffer，对应 Unicode 字符串，要使用 create_unicode_buffer。
定义和用法如下，

```python
>>> help(create_string_buffer)
Help on function create_string_buffer in module ctypes:

create_string_buffer(init, size=None)
    create_string_buffer(aBytes) -> character array
    create_string_buffer(anInteger) -> character array
    create_string_buffer(aBytes, anInteger) -> character array
```

```python
from ctypes import *

p = create_string_buffer(5)
print(sizeof(p))     # 5
print(repr(p.raw))   # b'\x00\x00\x00\x00\x00'
p.raw = b'Hi'
print(repr(p.raw))   # b'Hi\x00\x00\x00'
print(repr(p.value)) # b'Hi'
```


## 传递自定义参数类型到 C 函数

ctypes 允许你创建自定义参数类型，它会自动去搜索自定义数据的 \_as_parameter 属性，将其作为 C 函数的参数，例如：

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary('libc.so.6')

class Bottles(object):
    def __init__(self, number):
        self._as_parameter_ = number # here only accept integer, string, unicode string
bottles = Bottles(42)
libc.printf(b'%d bottles of beer\n', bottles)
```

输出：

```
42 bottles of beer
```

也可以为你的数据定义 \_as_parameter 属性，如下，

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary('libc.so.6')

class Bottles(object):
    def __init__(self):
        self._as_parameter_ = None  # only accept integer, string, unicode string

    @property
    def aspram(self):
        return self._as_parameter_

    @aspram.setter
    def aspram(self, number):
        self._as_parameter_ = number

bottles = Bottles()
bottles.aspram = 63
libc.printf(b'%d bottles of beer\n', bottles)
```

输出：

```
63 bottles of beer
```


## 指定 C 函数的参数类型

可以指定要调用 C 函数的参数类型，如果传入参数不符合指定的类型，则 ctypes 会尝试转换，如果转换不成功，则抛 ArgumentError，例如：

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary('libc.so.6')

libc.printf.argtypes = [c_char_p, c_char_p, c_int, c_double]

# String is "Hi", Int is 10, Double is 2.200000
libc.printf(b'String is "%s", Int is %d, Double is %f\n', b'Hi', 10, 2.2)
# X, 2, 3.000000
libc.printf(b'%s, %d, %f\n', b'X', 2, 3)
try:
    libc.printf(b"%d %d %d", 1, 2, 3)
except ArgumentError as e:
    # *** ERROR: argument 2: <class 'TypeError'>: wrong type
    print("*** ERROR: %s" % str(e))
```

输出：

```
String is "Hi", Int is 10, Double is 2.200000
X, 2, 3.000000
*** ERROR: argument 2: <class 'TypeError'>: wrong type
```


## 指定 C 函数的返回值类型

如果不指定 C 函数的返回值， ctypes 默认返回 int 类型，如果要返回特定类型，需要指定返回类型 restype。

例如：

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary('libc.so.6')

print '1->', libc.strchr('abcdefghij', c_char('d'))

libc.strchr.restype = c_char_p

print '2->', libc.strchr('abcdefghij', c_char('d'))
print '3->', libc.strchr('abcdefghij', 'd')  # Note, here C function strchr not know what 'd' mean, so rerurn None

libc.strchr.argtypes = [c_char_p, c_char]
print '4->', libc.strchr('abcdefghij', 'd')  # Note, here not use c_char('w')
```

输出：

```
1-> 40291315
2-> defghij
3-> None
4-> defghij
```

按引用传递参数
有些情况下，需要 C 函数修改传入的参数，或者参数过大不适合传值，需要按引用传递，ctypes 提供关键字 byref() 处理这种情况。

例如：

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary('libc.so.6')

i = c_int()
f = c_float()
s = create_string_buffer('\000' * 32)
print 'i.val =', i.value
print 'f.val =', f.value
print 'repr(s.value) =', repr(s.value)
libc.sscanf('1 3.14 Hello', '%d %f %s', byref(i), byref(f), s)
print 'after, i.val =', i.value
print 'after, f.val =', f.value
print 'after, repr(s.value) =', repr(s.value)
```

输出：

```
i.val = 0
f.val = 0.0
repr(s.value) = ''
after, i.val = 1
after, f.val = 3.1400001049
after, repr(s.value) = 'Hello'
```


## 使用结构体

ctypes 支持结构体的使用，从 Structure 类派生，数据放在 \_fields\_ 中。

例如：

```python
class Point(Structure):
    _fields_ = [('x', c_int), ('y', c_int)]

point = Point(10, 20)
print 'point.x =', point.x
print 'point.y =', point.y

point = Point(y=5)
print 'after, point.x =', point.x
print 'after, point.y =', point.y
print

class Rect(Structure):
    _fields_ = [('upperleft', Point), ('lowerright', Point)]

rc = Rect(point)
print 'rc.upperleft.x = %d, rc.upperleft.y = %d' % (rc.upperleft.x, rc.upperleft.y)
print 'rc.lowerright.x = %d, rc.lowerright.y = %d' % (rc.lowerright.x, rc.lowerright.y)

r = Rect(Point(1, 2), Point(3, 4))
print 'r.upperleft.x = %d, r.upperleft.y = %d' % (r.upperleft.x, r.upperleft.y)
print 'r.lowerright.x = %d, r.lowerright.y = %d' % (r.lowerright.x, r.lowerright.y)
```

输出：

```
point.x = 10
point.y = 20
after, point.x = 0
after, point.y = 5

rc.upperleft.x = 0, rc.upperleft.y = 5
rc.lowerright.x = 0, rc.lowerright.y = 0
r.upperleft.x = 1, r.upperleft.y = 2
r.lowerright.x = 3, r.lowerright.y = 4
```


## 位域

ctypes 提供了对位域的支持，例如：

```python
class IntBit(Structure):
    _fields_ = [('x', c_uint, 2), ('y', c_uint, 4)]

IB = IntBit(1, 15)
print 'IB.x = %d' % IB.x
print 'IB.y = %d' % IB.y

IB2 = IntBit(4, 16)
print '-> IB2.x = %d' % IB2.x
print '-> IB2.y = %d' % IB2.y
```

输出：

```
IB.x = 1
IB.y = 15
-> IB2.x = 0
-> IB2.y = 0
```


## 数组

ctypes 提供了对 Array 的支持，例如：

```python
TenIntArrayType = c_int * 10
ta = TenIntArrayType(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for item in ta:
    print item,
print

class PointEx(Structure):
    _fields_ = [('x', c_int), ('y', c_int)]

class MyStruct(Structure):
    _fields_ = [('a', c_int), ('b', c_int), ('pointex_array', PointEx * 4)]

ms = MyStruct(4, 5, ((1,1), (2,2), (3,3), (4,4)))
for item in ms.pointex_array:
    print '(item.x, item.y) = (%d, %d)' % (item.x, item.y)
print
```

输出：

```
1 2 3 4 5 6 7 8 9 10
(item.x, item.y) = (1, 1)
(item.x, item.y) = (2, 2)
(item.x, item.y) = (3, 3)
(item.x, item.y) = (4, 4)
```


## 指针

ctypes 使用关键字 pointer 提供了对指针的支持，注意指针解引用使用 \[0\]，例如：

```python
i = c_int(42)
print 'before, i.value =', i.value
pi = pointer(i)
pi[0] = 57
print 'after, i.value =', i.value

# create NULL pointer, also can use this way, but recommend use 'pointer' not 'POINTER'

null_ptr = POINTER(c_int)()
print 'bool(null_ptr) =', bool(null_ptr)
```

输出：

```
before, i.value = 42
after, i.value = 57
bool(null_ptr) = False
```


## 类型转换

ctypes 提供了类型转换方法 cast()，例如：

```python
class Bar(Structure):
    _fields_ = [('count', c_int), ('value', POINTER(c_int))]

bar = Bar()
bar.count = 3
bar.value = (c_int * 3)(1, 2, 3)
for idx in range(bar.count):
    print 'bar.value[%d] = %d' % (idx, bar.value[idx])

## use cast to convert

try:
    bar.value = (c_byte * 4)()
except TypeError, e:
    print '*** ERROR: %s' % str(e)

bar.value = cast((c_byte * 4)(), POINTER(c_int))
for idx in range(4):
    print 'now, bar.value[%d] = %d' % (idx, bar.value[idx])
print
```

输出：

```
bar.value[0] = 1
bar.value[1] = 2
bar.value[2] = 3
*** ERROR: incompatible types, c_byte_Array_4 instance instead of LP_c_long instance
now, bar.value[0] = 0
now, bar.value[1] = 0
now, bar.value[2] = 0
now, bar.value[3] = 0
```


## 回调函数

ctypes 通过 CFUNCTYPE 支持回调函数，例如：

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary('libc.so.6')

IntArray5 = c_int * 5
ia = IntArray5(5, 1, 7, 33, 99)

# CFUNCTYPE(restype, *argtypes, **kw)

CmpFuncType = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

def py_cmp_func(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        return 0

cmpfunc = CmpFuncType(py_cmp_func)

print 'before sort, the ia list is: ',
for item in ia:
    print item,

# void qsort (void* base, size_t num, size_t size, int (*compar)(const void*,const void*));

libc.qsort(ia, len(ia), sizeof(c_int), cmpfunc)

print '\nafter sort, the ia list is: ',
for item in ia:
    print item,
print
```

输出：

```
before sort, the ia list is:  5 1 7 33 99
after sort, the ia list is:  1 5 7 33 99
```


## Resize Space

ctypes 提供了 resize 变量占用空间的方法 resize()，注意，只能增大，不能小于原始空间，例如：

```python
short_array = (c_short * 4)(1, 2, 3, 4)
print 'sizeof(short_array) =', sizeof(short_array)  # get 8, means short_array take 8-byte memory
print 'len(short_array) =', len(short_array)
print 'before resize, short_array is: ',
for idx in range(len(short_array)):
    print short_array[idx],
print

try:
    resize(short_array, 4)  # resize short_array to 4-byte, raise error, due to cannot resize smaller than original
except ValueError, e:
    print 'ERROR: %s' % str(e)

resize(short_array, 32)
print 'after succeed resize to 32-byte, now sizeof(short_array) =', sizeof(short_array)
print 'after succeed resize to 32-byte, now len(short_array) =', len(short_array)
print 'after reszie, short_array is: ',
for idx in range(len(short_array)):
    print short_array[idx],
```

输出：

```
sizeof(short_array) = 8
len(short_array) = 4
before resize, short_array is:  1 2 3 4
ERROR: minimum size is 8
after succeed resize to 32-byte, now sizeof(short_array) = 32
after succeed resize to 32-byte, now len(short_array) = 4
after reszie, short_array is:  1 2 3 4
```


## Other

```python
class cell(Structure):
    pass
cell._fields_ = [('name', c_char_p), ('next', POINTER(cell))]

c1 = cell()
c2 = cell()
c1.name = 'foo'
c2.name = 'bar'
c1.next = pointer(c2)
c2.next = pointer(c1)

p = c1
for i in range(10):
    print p.name,
    p = p.next[0]
```

输出：

```
foo bar foo bar foo bar foo bar foo bar
```


## 坑

ctypes 相对于其它工具，使用起来有点繁琐，而且有很多坑，需要小心谨慎，例如：

```python
class POINT(Structure):
    _fields_ = [('x', c_int), ('y', c_int)]

class RECT(Structure):
    _fields_ = [('a', POINT), ('b', POINT)]

p1 = POINT(1, 2)
p2 = POINT(3, 4)
rc = RECT(p1, p2)

print 'rc.a.x =', rc.a.x
print 'rc.a.y =', rc.a.y
print 'rc.b.x =', rc.b.x
print 'rc.b.y =', rc.b.y

rc.a, rc.b = rc.b, rc.a

print 'after swap, bad result due to this is the pointer,'
print 'rc.a.x =', rc.a.x
print 'rc.a.y =', rc.a.y
print 'rc.b.x =', rc.b.x
print 'rc.b.y =', rc.b.y
print
```

输出：

```
rc.a.x = 1
rc.a.y = 2
rc.b.x = 3
rc.b.y = 4
after swap, bad result due to this is the pointer,
rc.a.x = 3
rc.a.y = 4
rc.b.x = 3
rc.b.y = 4
```


## Load 自定义 DLL

以 C 函数文件 needforspeed.c 为例，

```cpp
//----------------------------------------------------------------------------
// Purpose: this c module is used to speed up the Python program, should be
//          compiled into dll, and then load into Python module with ctypes
//          method.
//
// Compile Methods:
//
//    ======================
//    Windows: use MSVC, x64
//    ======================
//
//    C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64> cl /LD needforspeed.c /o nfs.dll
//
//    ======
//    Linux:
//    ======
//
//    $ gcc -fPIC -shared needforspeed.c -o nfs.so
//----------------------------------------------------------------------------

#include <stdio.h>

// Windows need this compile direction for dll compilation, Linux no need
#ifdef _MSC_VER
    #define DLL_EXPORT __declspec( dllexport )
#else
    #define DLL_EXPORT
#endif

DLL_EXPORT void hello_world(void) {
    printf("Hello world!\n");
}

DLL_EXPORT int mod(int m, int n) {
    return m % n;
}

DLL_EXPORT int get_array_elem(int arr[], int idx) {
    return arr[idx];
}

DLL_EXPORT int get_array2D_elem(int arr[][3], int row, int col) {
    return arr[row][col];
}
```

在 Windows 下编译为 nfs.dll, 在 Linux 下编译为 nfs.so，Python 中调用如下，

```python
import platform
from ctypes import *

if platform.system() == 'Windows':
    mylib = cdll.LoadLibrary('./nfs.dll')
elif platform.system() == 'Linux':
    mylib = cdll.LoadLibrary('./nfs.so')

mylib.hello_world()
print

mod_rtv = mylib.mod(c_int(10), c_int(4))
print 'mod_rtv(10 % 4) =', mod_rtv
print

#####################
# 1D array get elem #
#####################

IntArray10Type = c_int * 10
intArray = IntArray10Type()
for idx in range(10):
    intArray[idx] = idx**2

for idx in range(10):
    print 'intArray[%d] = %d' % (idx, mylib.get_array_elem(intArray, idx))
print

#####################
# 2D array get elem #
#####################

IntArray3Col = c_int * 3
IntArray3Row3Col = IntArray3Col * 3
arr2d = IntArray3Row3Col(IntArray3Col(1, 2, 3), IntArray3Col(8, 9, 4), IntArray3Col(7, 6, 5))

print 'arr2d is:'
for r in range(3):
    for c in range(3):
        print '%d ' % mylib.get_array2D_elem(arr2d, r, c),
    print
```

输出：

```
Hello world!

mod_rtv(10 % 4) = 2

intArray[0] = 0
intArray[1] = 1
intArray[2] = 4
intArray[3] = 9
intArray[4] = 16
intArray[5] = 25
intArray[6] = 36
intArray[7] = 49
intArray[8] = 64
intArray[9] = 81

arr2d is:
1  2  3
8  9  4
7  6  5
```

完。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-09-14-mixed-python-and-c.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.python.org/3/library/ctypes.html]({% include relrefx.html url="/backup/2021-09-14-mixed-python-and-c.md/docs.python.org/a9cf72b8.html" %})
- [https://www.cnblogs.com/gaowengang/p/7919219.html]({% include relrefx.html url="/backup/2021-09-14-mixed-python-and-c.md/www.cnblogs.com/4b57faf7.html" %})
