---
layout: post
title: "搭建 Windows Jekyll 环境"
location: "珠海"
categories: ["配置"]
tags: [Windows, Jekyll]
toc: true
---

Windows 搭建 Jekyll 环境。`bundle install` 的时候，`libv8` 和 `therubyracer` 会失败，主要是工程配置和源代码 Windows 平台的兼容性么有做好。

{% highlight plaintext %}
Installing libv8 3.16.14.19 with native extensions
../src/objects.h: At global scope:
../src/objects.h:5252:44: error: left operand of shift expression '(-1 << 3)' is negative [-fpermissive]
 5252 |   static const int kElementsKindMask = (-1 << kElementsKindShift) &
      |                                        ~~~~^~~~~~~~~~~~~~~~~~~~~~
../src/objects.h:7386:36: error: left operand of shift expression '(-8 << 26)' is negative [-fpermissive]
 7386 |       (~kMaxCachedArrayIndexLength << kArrayIndexHashLengthShift) |
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make[1]: *** [tools/gyp/v8_base.target.x64.mk:197：/c/Ruby25-x64/lib/ruby/gems/2.5.0/gems/libv8-3.16.14.19/vendor/v8/out/x64.release/obj.target/v8_base/src/accessors.o] 错误 1
make[1]: 离开目录“/c/Ruby25-x64/lib/ruby/gems/2.5.0/gems/libv8-3.16.14.19/vendor/v8/out”
make: *** [Makefile:195：x64.release] 错误 2
{% endhighlight %}

在基于源码的编译构建过程中，代码是临时释放的，mk 配置也是临时释放的，对于编译不过的地方，即使修改了，也会被 bundle 覆盖回滚。后来把这些改动过的代码和配置都拷贝出来，用脚本不停的尝试写入替换对应的文件，最终编译链接成功。

{% include image.html url="/images/win-jekyll/win-jekyll.png" %}


## 1. 安装 ruby & gem

从 <https://rubyinstaller.org/downloads/> 下载，Ruby+Devkit 2.5.8-1 (x64) rubyinstaller-devkit-2.5.8-1-x64.exe。
因为 github-pages depends on ruby (>= 2.2, < 2.6) x64-mingw32，安装 MSYS2，选择 `3 - MSYS2 and MINGW development toolchain`，安装完成要选择“运行”。

{% highlight shell %}
ruby -v
gem -v
{% endhighlight %}


## 2. 安装 bundler

{% highlight shell %}
ridk install
gem install bundler # 安装 bundler
gem install bundler:1.16.1
chcp 850 # 多语种 (MS-DOS Latin1)
gem install jekyll # 安装 jekyll
jekyll -v
{% endhighlight %}


## 3. 工程 bundle install

libv8 构建不成功，therubyracer 也构建不成功。网上的办法都行不通。必须先装好 Python2 环境，如果是 Python3，要改环境变量 Path，还有 PYTHONPATH & PYTHONHOME（也可能没有），否则 Python 报错：`No module named site`。

{% highlight shell %}
bundle install # Need python 2!!
# https://qiita.com/south37/items/9a3269c28d9fba80f0b7
# bundle config build.libv8 --with-system-v8
# bundle config build.therubyracer --with-v8-dir=/usr/local/opt/v8-315/
# 这个方法理论可行，没有成功。
# 灵感来自于 https://issues.adblockplus.org/ticket/4950
# gem install libv8 -v '3.16.14.19' -- --with-system-v8
# gem install therubyracer -v '0.12.3' -- --with-system-v8
{% endhighlight %}

**最终方案：**

先构建一次，把所有影响构建的源代码和工程配置（mk 文件）都拷贝出来，改动点具体见 python 代码。platform-win32.cc 里面的 `localtime_s` 和 include/time.h 里面的冲突，改个新名字，等等。
然后写个脚本（libv8.gem.py），不停的尝试写入替换这些文件；同时开启构建，一旦构建系统创建 / 释放 / 修改了这几个文件，马上替换掉，最终就可以顺利完成构建了。

建议用 [Everything](https://www.voidtools.com/zh-cn/) 把编译不过的问题文件找出来。

{% highlight python %}
#encoding=utf8
import os, sys
import time

def readfile(fpath):
    with open(fpath, "rb") as fin:
        return fin.read()

def copyfile(fpath, tpath):
    fdata = readfile(fpath)
    ftarget = readfile(tpath)
    if fdata == ftarget:
        return False
    fout = open(tpath, "wb")
    fout.write(fdata)
    fout.close()
    return True

def fmain(fpath, tpath):

    if os.path.isdir(fpath):
        for _dir in os.listdir(fpath):
            _fpath = os.path.join(fpath, _dir)
            _tpath = os.path.join(tpath, _dir)
            fmain(_fpath, _tpath)
        return

    try:
        # time.sleep(0.001)
        if not os.path.exists(tpath):
            return
        if copyfile(fpath, tpath):
            print(fpath)
    except Exception, ex:
        print(ex, fpath)


# libv8 编译不过的问题文件
def fmain_libv8():
    # CFLAGS_Release := -fpermissive
    # CFLAGS_Debug := -fpermissive
    fpath = r"D:\kSource\blog\source\gyp"
    tpath = r"C:\Ruby25-x64\lib\ruby\gems\2.5.0\gems\libv8-3.16.14.19\vendor\v8\out\tools\gyp"
    fmain(fpath, tpath)
    fpath = r"D:\kSource\blog\source\src"
    tpath = r"C:\Ruby25-x64\lib\ruby\gems\2.5.0\gems\libv8-3.16.14.19\vendor\v8\out\src"
    fmain(fpath, tpath)

    # localtime_s -> localtime_sx
    # #pragma comment(lib, "winmm.lib")
    fpath = r"D:\kSource\blog\source\libv8-therubyracer\platform-win32.cc"
    tpath = r"C:\Ruby25-x64\lib\ruby\gems\2.5.0\gems\libv8-3.16.14.19\vendor\v8\src\platform-win32.cc"
    fmain(fpath, tpath)


# therubyracer 编译不过的问题文件
def fmain_therubyracer():
    # remove command line option '-rdynamic'
    # LIBS => -lwinmm 新增。
    fpath = r"D:\kSource\blog\source\libv8-therubyracer\Makefile"
    tpath = r"C:\Ruby25-x64\lib\ruby\gems\2.5.0\gems\therubyracer-0.12.3\ext\v8\Makefile"
    fmain(fpath, tpath)

    # Accessor access(get, set, data); -> Accessor accessor(get, set, data);
    fpath = r"D:\kSource\blog\source\libv8-therubyracer\object.cc"
    tpath = r"C:\Ruby25-x64\lib\ruby\gems\2.5.0\gems\therubyracer-0.12.3\ext\v8\object.cc"
    fmain(fpath, tpath)

while __name__ == "__main__":
    fmain_libv8()
    fmain_therubyracer()

{% endhighlight %}


## 4. 先把 libv8 编译过，再把 therubyracer 编译过

{% include image.html url="/images/win-jekyll/win-jekyll2.png" %}
