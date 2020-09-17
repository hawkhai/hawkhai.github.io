---
layout: post
title: "Windows 的快捷方式，符号链接，软链接和硬链接"
location: "珠海"
categories: ["配置"]
tags: [Windows Note]
toc: true
---


## Linux 下面的 ln 命令

[理解 Linux 的硬链接与软链接](https://www.ibm.com/developerworks/cn/linux/l-cn-hardandsymb-links/)

{% highlight shell %}
ln -s source dist        # 建立软连接
ln source dist           # 建立硬连接
{% endhighlight %}


## Windows 下面的链接

Windows 7 下面，在 NTFS 文件系统下面，如果把快捷方式也算是一种链接的话，共有快捷方式，符号链接，软链接和硬链接四种方式。


## Windows 下面的 mklink 命令

{% highlight shell %}
创建符号链接。

MKLINK [[/D] | [/H] | [/J]] Link Target

        /D      符号链接（Symbolic Link）。创建目录符号链接。默认为文件符号链接。
        /H      硬链接（Hard Link）。创建硬链接而非符号链接。
        /J      目录联接（Junction Point）。创建目录联接。
        Link    指定新的符号链接名称。
        Target  指定新链接引用的路径（相对或绝对）。
{% endhighlight %}

1. `MKLINK Link Target` # 创建指向文件的符号链接
2. `MKLINK /D Link Target` # 创建指向文件夹的符号链接
3. `MKLINK /J Link Target` # 创建指向文件夹的软链接（联接）
4. `MKLINK /H Link Target` # 创建指向文件的硬链接


## 符号链接

**符号链接支持文件和文件夹**。符号链接在创建时候可以使用相对路径和绝对路径，创建成功后也就是对应的相对路径和绝对路径。符号链接属性是一个快捷方式类似的。


## 软链接

**软链接只是支持文件夹**。软链接不管在创建的时候使用的是相对路径还是绝对路径，创建后全部转换为绝对路径。软链接类型是一个和指向文件没有区别的类型。


## 硬链接

**硬链接是不支持文件夹（目录）的，这和文件系统是有关系的，硬链接和软链接的区别就是硬链接完全就是一个文件**，和从指向的文件是处在同级的，两个文件指向了同一块物理路径而已，所以删除任意一个，对另外一个都没有影响，而且一个文件更新，另外一个也会同样恨着更新。正因为如此，所以硬链接只能创建在同一个分区中。


## 横向对比

<style>
table th:first-of-type {
    width: 16%;
}
table th:nth-of-type(2) {
    width: 28%;
}
table th:nth-of-type(3) {
    width: 28%;
}
table th:nth-of-type(4) {
    width: 28%;
}
</style>

|  | 硬链接（Hard Link） | 目录联接（Junction Point） | 符号链接（Symbolic Link） |
| ---- | ---- | ---- | ---- |
| 链接到文件 | ✔️ | ❌ | ✔️ |
| 链接到文件夹 | ❌ | ✔️ | ✔️ |
| 跨驱动器卷（盘符） | ❌ | ✔️（仅本地计算机） | ✔️（包括 SMB 文件或路径） |
| 操作系统支持 | Windows NT 3.1 开始支持<br/>Windows 2000 开始有 API CreateHardLink()<br/>Windows NT 6.0 开始能使用 mklink /H | Windows 2000+ | 	Windows Vista+ |
| 可链接到不存在的目标 | ❌ | ✔️ | ✔️ |
| 当链接被单独删除后 | 只有所有指向原始文件的硬链接和原始文件全部删除后文件数据才会被删除。 | Windows Vista 之后原始文件夹不受影响；Windows 2000/XP/2003 会导致原始子文件夹被删除。 | 原始文件夹不受影响。 |
| 当原始文件被单独删除后 | 硬链接依然能正常访问到文件的数据。 | 目录联接失效，指向不存在的目录。 | 符号链接失效，指向不存在的目录。 |

[Mklink in Windows](http://www.maxi-pedia.com/mklink)


## 限制

[link](https://blog.csdn.net/u010977122/article/details/86518967) 符号链接在系统启动的时候是不工作的，所以下面这些文件（夹）是不可以作为符号链接替换的：

* \Windows
* \Windows\system32
* \Windows\system32\config

Windows Install 并不完全支持符号链接，所以，如果将 \Windows\Installer 使用符号链接替换将会导致大多数基于 .msi 的 Windows Install 安装程序出错失败，错误码为 2755 或 1632。

以下文件（夹）可以被符号链接替换：

* \Documents and Settings
* \ProgramData
* \Program Files
* \Program Files (x86)
* \Users

但是注意：

* 将 \Users 和 \ProgramData 使用符号链接替换是不推荐的，这会破坏 Windows Update 自动更新和 Windows Store 中的应用。
* 将 \Users、\ProgramData、"\Program Files" 或 "\Program Files (x86)" 使用符号链接替换将会破坏 Windows 的安装、部署和升级。
* 将 "\Program Files" 或 "\Program Files (x86)" 使用符号链接替换将会破坏那些从 \Windows\WinSxS 仓库中硬性链接了文件到安装目录中的基于 Windows 组件的服务。


## 目录符号链接与目录连接点的区别

目录符号链接（/D）与目录连接点（/J）非常相似，但是本质是不同的。目录符号链接依旧是符号链接，是指向目录的符号链接，而目录连接点不属于符号链接。

目录符号链接允许 Target 使用相对路径，当使用相对路径时创建目录符号链接之后，如果移动了符号链接文件，操作系统将无法再找到原来的目标。

目录连接点只允许 Target 使用绝对路径，当创建目录连接点时，如果传入的参数是相对路径，mklink 命令会自动将相对路径补全为绝对路径。

当目录符号链接使用绝对路径时，其行为与目录连接点完全一样。

此外，目录符号链接还可以指定 SMB 远程网络中的路径，而目录连接点不可以。


## 符号链接与快捷方式的区别

NTFS 符号链接与 Windows 快捷方式文件不同，这是一个普通的文件。

Windows 快捷方式文件可以在任何文件系统（比如早期的 FAT32）下创建，可以包含元数据（比如在 Windows 资源管理器中显示的图标），并且不是对应用程序透明的。当应用程序访问 Windows 快捷方式的时候，默认情况下访问到的是快捷方式文件，而不会自动指向目标文件。

NTFS 符号链接是对用户透明的，也就是说，在绝大多数情况下，访问 NTFS 符号链接与访问目标是完全相同的。当应用程序访问 NTFS 符号链接的时候，操作系统会自动将其指向目标，此时应用程序访问到的就是目标而不是 NTFS 符号链接了。


## 循环挂载的情况

`os.path.realpath(path)` Return the canonical path of the specified filename, eliminating any symbolic links encountered in the path (if they are supported by the operating system).

> Note When symbolic link cycles occur, the returned path will be one member of the cycle, but no guarantee is made about which member that will be.


## GetSymbolicLinkTarget

`GetFinalPathNameByHandle` API Hungs. At the time when I was checking this problem in Windows Vista, I remember atleast the `GetFileInformationByHandleEx` worked in all cases. But now I experience the same problem in Windows 7.

为了最大可能避免被挂起，首先尝试 `GetFileInformationByHandleEx`，再尝试 `GetFinalPathNameByHandle`，用线程跑，发现挂起了就 `TerminateThread`。

有非常好的源码可以参考：`DWORD psutil_threaded_get_filename(HANDLE hFile)` from <https://github.com/giampaolo/psutil.git>。

<https://github.com/giampaolo/psutil/blob/release-5.6.0/psutil/arch/windows/process_handles.c>


## C++ 判断代码

If you can write native code in JNA, you can directly call the Win32 API `GetFileAttributes()` function and check for the `FILE_ATTRIBUTE_REPARSE_POINT` flag (junctions are implemented as reparse points).

Update: To differentiate between different types of reparse points, you have to retreive the `ReparseTag` of the actual reparse point. For a junction point, it will be set to `IO_REPARSE_TAG_MOUNT_POINT` (0xA0000003).

There are two ways to retreive the ReparseTag:

1. Use `DeviceIoControl()` with the `FSCTL_GET_REPARSE_POINT` control code to obtain an `REPARSE_DATA_BUFFER` struct, which as a ReparseTag field. You can see an example of an `IsDirectoryJunction()` implementation using this technique in the following article:

    [NTFS Hard Links, Directory Junctions, and Windows Shortcuts](http://www.flexhex.com/docs/articles/hard-links.phtml)

2. Use `FindFirstFile()` to obtain a `WIN32_FIND_DATA` struct. If the path has the `FILE_ATTRIBUTE_REPARSE_POINT` attribute, the `dwReserved0` field will contain the `ReparseTag`.

3. `bool LocalFileHandle::isSymbolicLink() const` from open source cppfs: <https://github.com/cginternals/cppfs/blob/master/source/cppfs/source/windows/LocalFileHandle.cpp>

    {% highlight cpp %}
bool LocalFileHandle::isSymbolicLink() const {
    readFileInfo();
    if (m_fileInfo) {
        return (((WIN32_FILE_ATTRIBUTE_DATA *)m_fileInfo)->dwFileAttributes & FILE_ATTRIBUTE_REPARSE_POINT) != 0;
    }
    return false;
}
{% endhighlight %}


## Python 版本代码

{% highlight python %}
#encoding=utf8
import re, os, sys
# https://pypi.org/project/ntfsutils/
# https://github.com/juntalis/ntfslink-python
# https://stackoverflow.com/questions/1143260/create-ntfs-junction-point-in-python/10221068
from win32file import * # pip install pywin32
from winioctlcon import *
import struct

__all__ = ['islink', 'readlink']

# Win32file doesn't seem to have this attribute.
FILE_ATTRIBUTE_DIRECTORY     = 0x00000010
FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400
IO_REPARSE_TAG_MOUNT_POINT   = 0xA0000003
IO_REPARSE_TAG_SYMLINK       = 0xA000000C
# To make things easier.
REPARSE_FOLDER = (FILE_ATTRIBUTE_DIRECTORY | FILE_ATTRIBUTE_REPARSE_POINT)

# For the parse_reparse_buffer function
SYMBOLIC_LINK  = 'symbolic'
MOUNTPOINT     = 'mountpoint'
GENERIC        = 'generic'

def mklinkd(link, target):
    child = subprocess.Popen(['MKLINK', '/D', link, target],
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT,
        shell = True)
    streamdata = child.communicate()[0]
    return streamdata

def islink(fpath): # 原版存在 bug，修复了一下。
    """ Windows islink implementation. """
    attr = GetFileAttributes(fpath)
    if attr & FILE_ATTRIBUTE_REPARSE_POINT == FILE_ATTRIBUTE_REPARSE_POINT:
        return True
    return False

def parse_reparse_buffer(original):
    """ Implementing the below in Python:

    typedef struct _REPARSE_DATA_BUFFER {
        ULONG  ReparseTag;
        USHORT ReparseDataLength;
        USHORT Reserved;
        union {
            struct {
                USHORT SubstituteNameOffset;
                USHORT SubstituteNameLength;
                USHORT PrintNameOffset;
                USHORT PrintNameLength;
                ULONG Flags;
                WCHAR PathBuffer[1];
            } SymbolicLinkReparseBuffer;
            struct {
                USHORT SubstituteNameOffset;
                USHORT SubstituteNameLength;
                USHORT PrintNameOffset;
                USHORT PrintNameLength;
                WCHAR PathBuffer[1];
            } MountPointReparseBuffer;
            struct {
                UCHAR  DataBuffer[1];
            } GenericReparseBuffer;
        } DUMMYUNIONNAME;
    } REPARSE_DATA_BUFFER, *PREPARSE_DATA_BUFFER;

    """
    # Size of our data types
    SZULONG = 4 # sizeof(ULONG)
    SZUSHORT = 2 # sizeof(USHORT)

    # Our structure.
    # Probably a better way to iterate a dictionary in a particular order,
    # but I was in a hurry, unfortunately, so I used pkeys.
    buffer = {
        'tag' : SZULONG,
        'data_length' : SZUSHORT,
        'reserved' : SZUSHORT,
        SYMBOLIC_LINK : {
            'substitute_name_offset' : SZUSHORT,
            'substitute_name_length' : SZUSHORT,
            'print_name_offset' : SZUSHORT,
            'print_name_length' : SZUSHORT,
            'flags' : SZULONG,
            'buffer' : u'',
            'pkeys' : [
                'substitute_name_offset',
                'substitute_name_length',
                'print_name_offset',
                'print_name_length',
                'flags',
            ]
        },
        MOUNTPOINT : {
            'substitute_name_offset' : SZUSHORT,
            'substitute_name_length' : SZUSHORT,
            'print_name_offset' : SZUSHORT,
            'print_name_length' : SZUSHORT,
            'buffer' : u'',
            'pkeys' : [
                'substitute_name_offset',
                'substitute_name_length',
                'print_name_offset',
                'print_name_length',
            ]
        },
        GENERIC : {
            'pkeys' : [],
            'buffer': ''
        }
    }

    # Header stuff
    buffer['tag'] = struct.unpack('L', original[:SZULONG])[0]

    reparsetype = SYMBOLIC_LINK
    if buffer['tag'] == IO_REPARSE_TAG_SYMLINK:
        reparsetype = SYMBOLIC_LINK
    elif buffer['tag'] == IO_REPARSE_TAG_MOUNT_POINT:
        reparsetype = MOUNTPOINT
    else:
        assert False, buffer['tag']

    buffer['data_length'] = original[SZULONG:SZUSHORT]
    buffer['reserved'] = original[SZULONG+SZUSHORT:SZUSHORT]
    original = original[8:]

    # Parsing
    k = reparsetype
    for c in buffer[k]['pkeys']:
        if type(buffer[k][c]) == int:
            sz = buffer[k][c]
            bytes = original[:sz]
            buffer[k][c] = 0
            for b in bytes:
                n = b # ord(b)
                if n:
                    buffer[k][c] += n
            original = original[sz:]

    # Using the offset and length's grabbed, we'll set the buffer.
    buffer[k]['buffer'] = original
    return reparsetype, buffer

def readlink(fpath):
    """ Windows readlink implementation. """
    # This wouldn't return true if the file didn't exist, as far as I know.
    if not islink(fpath):
        return None

    if os.path.isdir(fpath):
        dwFlagsAndAttributes = FILE_FLAG_OPEN_REPARSE_POINT | FILE_FLAG_BACKUP_SEMANTICS
    else:
        dwFlagsAndAttributes = FILE_FLAG_OPEN_REPARSE_POINT

    # Open the file correctly depending on the string type.
    handle = CreateFileW(fpath, GENERIC_READ, 0, None, OPEN_EXISTING, dwFlagsAndAttributes, 0) \
                if type(fpath) == type("unicode") else \
            CreateFile(fpath, GENERIC_READ, 0, None, OPEN_EXISTING, dwFlagsAndAttributes, 0)
    if handle == INVALID_HANDLE_VALUE:
        return None

    # MAXIMUM_REPARSE_DATA_BUFFER_SIZE = 16384 = (16*1024)
    buffer = DeviceIoControl(handle, FSCTL_GET_REPARSE_POINT, None, 16*1024)
    # Above will return an ugly string (byte array), so we'll need to parse it.

    # But first, we'll close the handle to our file so we're not locking it anymore.
    CloseHandle(handle)

    # Minimum possible length (assuming that the length of the target is bigger than 0)
    if len(buffer) < 9:
        return None
    # Parse and return our result.
    reparsetype, result = parse_reparse_buffer(buffer)
    offset = result[reparsetype]['substitute_name_offset']
    ending = offset + result[reparsetype]['substitute_name_length']
    rpath = result[reparsetype]['buffer'][offset:ending].replace(b'\x00', b'')
    if len(rpath) > 4 and rpath[0:4] == b'\\??\\':
        rpath = rpath[4:]
    return rpath.decode("gbk")

def realpath(fpath):
    from os import path
    while islink(fpath):
        rpath = readlink(fpath)
        if not path.isabs(rpath):
            rpath = path.abspath(path.join(path.dirname(fpath), rpath))
        fpath = rpath
    return fpath

def dprint(link):
    linklen = len(link)
    linelen = 80
    sepleft = int((linelen - 2 - linklen) / 2)
    sepright = linelen - 2 - linklen - sepleft
    islinkp = islink(link)
    print('-' * sepleft, link, '-' * sepright)

    if islinkp:
        print('IsLink: %s ReadLink: %s' % (islinkp, readlink(link)))
    else:
        print('IsLink: %s' % islinkp)

    print('RealPath: %s' % realpath(link))

    # https://docs.python.org/3/library/os.path.html
    # os.path.islink(path)      判断路径是否为链接
    # os.path.ismount(path)     判断路径是否为挂载点
    # os.path.realpath(path)    返回 path 的真实路径
    print(">>", os.path.islink(link),
          link, "->", os.path.realpath(link))

    link = os.path.normpath(os.path.abspath(link))
    while link and len(link) > 3: # E:\
        link = os.path.split(link)[0]
        if islink(link):
            print('Parent IsLink: %s -> %s' % (link, realpath(link)))
    print('-' * linelen)

def example():

    from os import system, unlink
    clear = "clear" in sys.argv

    system('cmd.exe /c echo test.txt > test.txt')
    system('mklink test-link.txt test.txt') # 文件类型为 .symlink
    dprint("test.txt")
    dprint("test-link.txt")
    if clear:
        unlink('test-link.txt')
        unlink('test.txt')

    # MKLINK /D Link Target # 创建指向文件夹的符号链接
    # MKLINK /J Link Target # 创建指向文件夹的软链接（联接）
    system("mkdir test")
    system("mkdir test\\subtest")
    system('cmd.exe /c echo test\\subtest.txt > test\\subtest.txt')
    system('cmd.exe /c echo test\\subtest\\subtest.txt > test\\subtest\\subtest.txt')

    system("mklink /D D:\\test-dlink {}".format(os.path.abspath("test")))
    system("mklink /J D:\\test-jlink test")
    dprint("D:\\test-dlink")
    dprint("D:\\test-jlink")

    dprint("test\\subtest\\subtest.txt")
    dprint("D:\\test-dlink\\subtest\\subtest.txt")
    dprint("D:\\test-jlink\\subtest\\subtest.txt")

    if clear:
        unlink('test\\subtest.txt')
        unlink('test\\subtest\\subtest.txt')
        # os.rmdir(path) # removedirs
        os.rmdir("test\\subtest")
        os.rmdir("test")
        os.rmdir("D:\\test-dlink")
        os.rmdir("D:\\test-jlink")

if __name__=='__main__':
    example()

{% endhighlight %}


### 运行结果

{% highlight shell %}
E:\kSource\pythonx>python pymklink.py clear
为 test-link.txt <<===>> test.txt 创建的符号链接
----------------------------------- test.txt -----------------------------------
IsLink: False
RealPath: test.txt
>> False test.txt -> E:\kSource\pythonx\test.txt
--------------------------------------------------------------------------------
-------------------------------- test-link.txt ---------------------------------
IsLink: True ReadLink: test.txt
RealPath: E:\kSource\pythonx\test.txt
>> True test-link.txt -> E:\kSource\pythonx\test.txt
--------------------------------------------------------------------------------
为 D:\test-dlink <<===>> E:\kSource\pythonx\test 创建的符号链接
为 D:\test-jlink <<===>> test 创建的联接
-------------------------------- D:\test-dlink ---------------------------------
IsLink: True ReadLink: E:\kSource\pythonx\test
RealPath: E:\kSource\pythonx\test
>> True D:\test-dlink -> E:\kSource\pythonx\test
--------------------------------------------------------------------------------
-------------------------------- D:\test-jlink ---------------------------------
IsLink: True ReadLink: E:\kSource\pythonx\test
RealPath: E:\kSource\pythonx\test
>> False D:\test-jlink -> E:\kSource\pythonx\test
--------------------------------------------------------------------------------
--------------------------- test\subtest\subtest.txt ---------------------------
IsLink: False
RealPath: test\subtest\subtest.txt
>> False test\subtest\subtest.txt -> E:\kSource\pythonx\test\subtest\subtest.txt
--------------------------------------------------------------------------------
---------------------- D:\test-dlink\subtest\subtest.txt -----------------------
IsLink: False
RealPath: D:\test-dlink\subtest\subtest.txt
>> False D:\test-dlink\subtest\subtest.txt -> E:\kSource\pythonx\test\subtest\subtest.txt
Parent IsLink: D:\test-dlink -> E:\kSource\pythonx\test
--------------------------------------------------------------------------------
---------------------- D:\test-jlink\subtest\subtest.txt -----------------------
IsLink: False
RealPath: D:\test-jlink\subtest\subtest.txt
>> False D:\test-jlink\subtest\subtest.txt -> E:\kSource\pythonx\test\subtest\subtest.txt
Parent IsLink: D:\test-jlink -> E:\kSource\pythonx\test
--------------------------------------------------------------------------------

{% endhighlight %}

dlink 和 jlink 还是存在差异，dlink 更像一个 symlink，而 jlink 跟真正的文件夹差不多了。

{% include image.html url="/images/win-mklink/dlink.png"
url2="/images/win-mklink/jlink.png" %}


## 参考

* [1] [Windows 的快捷方式，符号链接，软链接和硬链接](https://blog.alphatr.com/windows-mklink.html)
* [2] [比较 Windows 上四种不同的文件（夹）链接方式（NTFS 的硬链接、目录联接、符号链接，和大家熟知的快捷方式）](https://blog.walterlv.com/post/ntfs-link-comparisons.html)
* [3] [Determine whether a file is a junction \(in Windows\) or not?](https://stackoverflow.com/questions/13733275/determine-whether-a-file-is-a-junction-in-windows-or-not)
* [4] [NTFS Links, Directory Junctions, and Windows Shortcuts](http://www.flexhex.com/docs/articles/hard-links.phtml)
* [5] [Listing Used Files](https://www.codeproject.com/Articles/18975/Listing-Used-Files)
