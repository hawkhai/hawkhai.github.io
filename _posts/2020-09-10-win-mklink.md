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
    if attr & REPARSE_FOLDER == REPARSE_FOLDER:
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

    reparse_type = SYMBOLIC_LINK
    if buffer['tag'] == IO_REPARSE_TAG_SYMLINK:
        reparse_type = SYMBOLIC_LINK
    elif buffer['tag'] == IO_REPARSE_TAG_MOUNT_POINT:
        reparse_type = MOUNTPOINT
    else:
        assert False, buffer['tag']

    buffer['data_length'] = original[SZULONG:SZUSHORT]
    buffer['reserved'] = original[SZULONG+SZUSHORT:SZUSHORT]
    original = original[8:]

    # Parsing
    k = reparse_type
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
    return reparse_type, buffer

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
    reparse_type, result = parse_reparse_buffer(buffer)
    offset = result[reparse_type]['substitute_name_offset']
    ending = offset + result[reparse_type]['substitute_name_length']
    rpath = result[reparse_type]['buffer'][offset:ending].replace(b'\x00', b'')
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

def dprint(link, target):
    linklen = len(link)
    linelen = 80
    print('*' * 30, link, '*' * (linelen-30-2-linklen))
    print('IsLink: %s' % islink(link))
    print('ReadLink: %s' % readlink(link))
    print('RealPath: %s' % realpath(link))
    print('*' * linelen)

def example():

    from os import system, unlink
    clear = "clear" in sys.argv

    system('cmd.exe /c echo Hello World > test.txt')
    system('mklink test-link.txt test.txt') # 文件类型为 .symlink
    dprint("test-link.txt", "test.txt")
    if clear:
        unlink('test-link.txt')
        unlink('test.txt')

    # MKLINK /D Link Target # 创建指向文件夹的符号链接
    # MKLINK /J Link Target # 创建指向文件夹的软链接（联接）
    system("mkdir test")
    system('cmd.exe /c echo Hello World > test\\subtest.txt')
    system("mklink /D test-dlink test")
    system("mklink /J test-jlink test")
    dprint("test-dlink", "test")
    dprint("test-jlink", "test")

    if clear:
        unlink('test\\subtest.txt')
        # os.rmdir(path)
        os.removedirs("test")
        os.removedirs("test-dlink")
        os.removedirs("test-jlink")

if __name__=='__main__':
    example()
{% endhighlight %}

### 运行结果

{% highlight shell %}
E:\kSource\pythonx>python pymklink.py clear
为 test-link.txt <<===>> test.txt 创建的符号链接
****************************** test-link.txt ***********************************
IsLink: False
ReadLink: None
RealPath: test-link.txt
********************************************************************************
为 test-dlink <<===>> test 创建的符号链接
为 test-jlink <<===>> test 创建的联接
****************************** test-dlink **************************************
IsLink: True
ReadLink: test
RealPath: E:\kSource\pythonx\test
********************************************************************************
****************************** test-jlink **************************************
IsLink: True
ReadLink: E:\kSource\pythonx\test
RealPath: E:\kSource\pythonx\test
********************************************************************************

{% endhighlight %}

dlink 和 jlink 还是存在差异，dlink 更像一个 symlink，而 jlink 跟真正的文件夹差不多了。

{% include image.html url="/images/win-mklink/dlink.png" %}
{% include image.html url="/images/win-mklink/jlink.png" %}

## 参考

* [1] [Windows 的快捷方式，符号链接，软链接和硬链接](https://blog.alphatr.com/windows-mklink.html)
* [2] [比较 Windows 上四种不同的文件（夹）链接方式（NTFS 的硬链接、目录联接、符号链接，和大家熟知的快捷方式）](https://blog.walterlv.com/post/ntfs-link-comparisons.html)
* [3] [Determine whether a file is a junction \(in Windows\) or not?](https://stackoverflow.com/questions/13733275/determine-whether-a-file-is-a-junction-in-windows-or-not)
* [4] [NTFS Links, Directory Junctions, and Windows Shortcuts](http://www.flexhex.com/docs/articles/hard-links.phtml)
