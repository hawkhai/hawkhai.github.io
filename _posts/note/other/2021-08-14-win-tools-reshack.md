---
layout: post
title: "编程笔记 -- Resource Hacker<sup>TM</sup> 修改 PE 描述信息"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
l2dwidget:
---

同样的代码发布三个版本，不同的描述信息，不同的签名，太麻烦！
1. 构建一个，拷贝一下，然后手工改 PE 文件描述信息，手工打签名。麻烦！
2. 构建两次，选择不同的构建配置。时间！时间！

`pecopy.exe` 解决你的烦恼！自动修改文件描述信息！下载地址：<https://sunocean.life/tools/>


## $$Resource Hacker^{TM}$$

图形界面版本。

* 早期版本：<http://www.rpi.net.au/~ajohnson/resourcehacker>
* 后期版本：<http://www.angusj.com/resourcehacker/>

{% include image.html url="/assets/images/210814-win-tools-reshack/rh_scrpt.png" %}


## pecopy.exe

`pecopy.exe` 解决你的烦恼，**通过配置构建生成后事件，同时完成拷贝和修改描述信息**，最后签名。
1. 一气呵成，不用介入。
2. 避免构建多次，崩溃点都变了。

使用文档：
```
usage: pecopy.exe [-h] [-mcn COMPANYNAME] [-mfd FILEDESCRIPTION]
                  [-mvc FILEVERSION] [-min INTERNALNAME] [-mlc LEGALCOPYRIGHT]
                  [-mof ORIGINALFILENAME] [-mpn PRODUCTNAME]
                  [-mpv PRODUCTVERSION] -in INPUTFILE -out OUTPUTFILE
                  [-debug DEBUG]

optional arguments:
  -h, --help            show this help message and exit
  -mcn COMPANYNAME, --CompanyName COMPANYNAME
                        示例：酷哦软件科技有限公司
  -mfd FILEDESCRIPTION, --FileDescription FILEDESCRIPTION
                        示例：酷哦工具箱好帮手
  -mvc FILEVERSION, --FileVersion FILEVERSION
                        示例：2021,08,05,123
  -min INTERNALNAME, --InternalName INTERNALNAME
                        示例：toolhelper
  -mlc LEGALCOPYRIGHT, --LegalCopyright LEGALCOPYRIGHT
                        示例：酷哦软件科技有限公司
  -mof ORIGINALFILENAME, --OriginalFilename ORIGINALFILENAME
                        示例：tool.exe
  -mpn PRODUCTNAME, --ProductName PRODUCTNAME
                        示例：酷哦工具箱
  -mpv PRODUCTVERSION, --ProductVersion PRODUCTVERSION
                        示例：1,0,0,123
  -in INPUTFILE, --InputFile INPUTFILE
                        示例：tool.exe
  -out OUTPUTFILE, --OutputFile OUTPUTFILE
                        示例：shsign\tool.exe
```

示例：
```
C:\test>pecopy.exe -in fastvc.exe -out shsign\fastvc.exe --LegalCopyright "版权测试"
```

构建机构建完成，直接上去拿改好并签好名的文件即可。
**<font color="red">如果这个方案有帮到你，记得往 yangquanhai 的账户打 100+ 豹趣积分。^_^</font>**


### 配置构建生成后任务

1. 把 pecopy.exe 入库到工程合适目录。
2. 配置生成后事件：
```
pecopy.exe -in "$(TargetDir)fastvc.exe" -out "$(TargetDir)shsign\fastvc.exe" --LegalCopyright "版权测试"
```
{% include image.html url="/assets/images/210814-win-tools-reshack/20210814161318.png" %}

下载地址：<https://sunocean.life/tools/>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-08-14-win-tools-reshack.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://www.rpi.net.au/~ajohnson/resourcehacker]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/www.rpi.net.au/ede721e3.html" %})
- [http://www.angusj.com/resourcehacker/]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/www.angusj.com/0cd86f81.html" %})
