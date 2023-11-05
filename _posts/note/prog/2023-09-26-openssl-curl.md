---
layout: post
title: "编程与调试 -- openssl & curl"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
---

Openssl 库编译篇（Windows 平台）
<https://www.jianshu.com/p/d5e5e5039a40>
<https://www.cnblogs.com/jiaheshang/p/15098075.html>

* cmd 终端验证 nasm --version
* cmd 终端验证 perl --version

C:\Strawberry\perl\bin\perl.exe
E:\kSource\dist\nasm.exe

set PATH=%PATH%;C:\Strawberry\perl\bin;E:\kSource\dist;
E:
cd E:\kSource\pythonx\cppx\cppx\openssl-3.1.3

管理员启动：
{% include image.html url="/assets/images/230926-openssl-curl/20230926170040.png" %}

curl-8.3.0.tar.gz
openssl-3.1.3.tar.gz


## x64md

```
nmake clean
perl configure VC-WIN64A no-asm --prefix="D:\3rdparty\openssl_lib\release64"
```
VC-WIN64A 表示 Windows 64 位系统，32 位系统请换成 VC-WIN32，若要使用 debug 版本，请使用 debug-VC-WIN64A 或 debug-VC-WIN32
```
nmake
nmake install
```
同一个目录下编译不同版本 (win32\|64\|release\|debug) 时需要先 nmake clean

```
nmake clean
perl Configure debug-VC-WIN64A no-asm --prefix="D:\3rdparty\openssl_lib\debug64"
nmake
nmake install
```
把 `D:\3rdparty\openssl_lib\debug64` 改名为 `D:\3rdparty\openssl_lib\debug64_mdd`

完了之后把 makefile 文件以及 configdata.pm 文件里面的 /MDD 改为 MTD
```
nmake clean
nmake
nmake install
```
把 `D:\3rdparty\openssl_lib\debug64` 改名为 `D:\3rdparty\openssl_lib\debug64_mtd`

```
nmake clean
perl Configure VC-WIN64A no-asm --prefix="D:\3rdparty\openssl_lib\release64"
nmake
nmake install
```
把 `D:\3rdparty\openssl_lib\release64` 改名为 `D:\3rdparty\openssl_lib\release64_md`

完了之后把 makefile 文件以及 configdata.pm 文件里面的 /MD 改为 MT
```
nmake clean
nmake
nmake install
```
把 `D:\3rdparty\openssl_lib\release64` 改名为 `D:\3rdparty\openssl_lib\release64_mt`

<https://github.com/supercodechen/win32_openssl_prebuild>
<https://github.com/kiyolee/openssl3-win-build>
<https://github.com/kiyolee/openssl1_1-win-build/tree/main/build-VS2019>

使用 libcurl 在 windows 平台遇到的问题
<https://blog.csdn.net/wquasdf/article/details/113625080>
<https://blog.csdn.net/q610098308/article/details/88569866>
链接问题
1、首先出现的连接问题是：
* error LNK2001: 无法解析的外部符号 \_\_imp_curl_easy_perform
* error LNK2001: 无法解析的外部符号 \_\_imp_curl_easy_init
* error LNK2001: 无法解析的外部符号 \_\_imp_curl_slist_append
* error LNK2001: 无法解析的外部符号 \_\_imp_curl_slist_free_all
* error LNK2001: 无法解析的外部符号 \_\_imp_curl_easy_cleanup
* error LNK2001: 无法解析的外部符号 \_\_imp_curl_easy_setopt

解决方案：加入预编译选项：项目右键 --> 属性 --> 配置属性 --> C/C++ --> 预处理器 --> 预处理器，把 BUILDING_LIBCURL 或 CURL_STATICLIB。

```
// 添加依赖库
#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib, "crypt32.lib")
#pragma comment(lib, "winmm.lib")
#pragma comment(lib, "wldap32.lib")
```


## openssl3x

{% include image.html url="/assets/images/230926-openssl-curl/11806352-d91518eabf5fc72e.webp" %}

**问题原因是 perl 太老了，安装最新的即可。**
{% include image.html url="/assets/images/230926-openssl-curl/11806352-116010dc41dbc3e3.webp" %}

这一步得到 Makefile
{% include image.html url="/assets/images/230926-openssl-curl/11806352-6bed6d757a9be707.webp" %}

{% include image.html url="/assets/images/230926-openssl-curl/11806352-d9b32160699eb3cb.webp" %}

{% include image.html url="/assets/images/230926-openssl-curl/11806352-150b88ff287987c4.webp" %}

{% include image.html url="/assets/images/230926-openssl-curl/11806352-9dadf5013c46aece.webp" %}

Can't locate Win32/Console.pm in @INC (you may need to install the Win32::Console module) (@INC contains: third_party/openssl-3.1.4/util/perl C:/Perl64/site/lib C:/Perl64/lib third_party/openssl-3.1.4/external/perl/Text-Template-1.56/lib) at C:/Perl64/site/lib/ActivePerl/Config.pm line 400.

cpan Win32::Console
ppm install Win32-Console

**问题原因是 perl 太老了，安装最新的即可。**

<https://strawberryperl.com/>
strawberry-perl-5.38.0.1-64bit.msi



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-09-26-openssl-curl.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.jianshu.com/p/d5e5e5039a40]({% include relrefx.html url="/backup/2023-09-26-openssl-curl.md/www.jianshu.com/de228cae.html" %})
- [https://www.cnblogs.com/jiaheshang/p/15098075.html]({% include relrefx.html url="/backup/2023-09-26-openssl-curl.md/www.cnblogs.com/4ad99998.html" %})
- [https://github.com/supercodechen/win32_openssl_prebuild]({% include relrefx.html url="/backup/2023-09-26-openssl-curl.md/github.com/312d3b15.html" %})
- [https://github.com/kiyolee/openssl3-win-build]({% include relrefx.html url="/backup/2023-09-26-openssl-curl.md/github.com/69241155.html" %})
- [https://github.com/kiyolee/openssl1_1-win-build/tree/main/build-VS2019]({% include relrefx.html url="/backup/2023-09-26-openssl-curl.md/github.com/d4c83e4d.html" %})
- [https://blog.csdn.net/wquasdf/article/details/113625080]({% include relrefx.html url="/backup/2023-09-26-openssl-curl.md/blog.csdn.net/fe91eddf.html" %})
- [https://blog.csdn.net/q610098308/article/details/88569866]({% include relrefx.html url="/backup/2023-09-26-openssl-curl.md/blog.csdn.net/cb73cdcf.html" %})
- [https://strawberryperl.com/]({% include relrefx.html url="/backup/2023-09-26-openssl-curl.md/strawberryperl.com/e1481598.html" %})
