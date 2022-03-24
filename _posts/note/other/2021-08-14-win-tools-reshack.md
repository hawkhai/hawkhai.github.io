---
layout: post
title: "编程与调试 -- Resource Hacker 修改 PE 描述信息"
author:
location: "珠海"
categories: ["编程与调试"]
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
<https://sunocean.life/tools/pecopy.exe>


## Resource Hacker

~~图形界面版本。~~

* ~~早期版本：<http://www.rpi.net.au/~ajohnson/resourcehacker>~~
* ~~后期版本：<http://www.angusj.com/resourcehacker/>~~

{% include image.html url="/assets/images/210814-win-tools-reshack/rh_scrpt.png" %}


## pecopy.exe

`pecopy.exe` 解决你的烦恼，**通过配置构建生成后事件，同时完成拷贝和修改描述信息**，最后签名。
1. 一气呵成，不用介入。
2. 避免构建多次，崩溃点都变了。

使用文档：
```bat
usage: "pecopy.exe" [-h] [-mcn COMPANYNAME] [-mfd FILEDESCRIPTION]
                  [-mvc FILEVERSION] [-min INTERNALNAME] [-mlc LEGALCOPYRIGHT]
                  [-mof ORIGINALFILENAME] [-mpn PRODUCTNAME]
                  [-mpv PRODUCTVERSION] [-icon ICONFILE] [-mask ICONMASK]
                  [-mcp CODEPAGE] -in INPUTFILE -out OUTPUTFILE [-debug DEBUG]

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
  -icon ICONFILE, --IconFile ICONFILE
                        示例：mainicon.ico
  -mask ICONMASK, --IconMask ICONMASK
                        示例：ICONGROUP,107,2052（同时多个用半角分号隔开）
  -mcp CODEPAGE, --CodePage CODEPAGE
                        示例：65001
  -in INPUTFILE, --InputFile INPUTFILE
                        示例：tool.exe
  -out OUTPUTFILE, --OutputFile OUTPUTFILE
                        示例：shsign\tool.exe
  -debug DEBUG, --Debug DEBUG
```


### 示例 1 修改版权

```bat
C:\test>"pecopy.exe" -in "fastvc.exe" \
                     -out "shsign\fastvc.exe" \
                     --LegalCopyright "版权测试"
```

构建机构建完成，直接上去拿改好并签好名的文件即可。


### 示例 2 修改描述信息

```bat
"pecopy.exe" -in "$(TargetDir)\test.dll" \
             -out "$(TargetDir)\shsign\test.dll" \
             -mpn "TEST 模块" \
             -mcn "哇哦软件科技有限公司" \
             -mfd "哇哦模块" \
             -mlc "哇哦软件科技有限公司"
```
{% include image.html url="/assets/images/210814-win-tools-reshack/20210818115642.png" %}

已知缺陷：语言都会变成中性。这个应该影响不大。
如果此方案有帮助到项目组，记得豹趣积分打到 quanhai 账上。^_^


### 示例 3 修改图标

先要用 resourcehacker 看好要替换图标的 mask 是多少，比如：`ICONGROUP,107,2052`。

{% include image.html url="/assets/images/210814-win-tools-reshack/20220117-160930.png" %}

```bat
"pecopy.exe" -in "pecopy.exe" \
             -out "..\..\dist\pecopy.exe" \
             -icon "..\image\icon\iconall\shitou.ico" \
             -mask ICONGROUP,107,2052
```

* 微软图标格式文档：[Icons](https://docs.microsoft.com/en-us/previous-versions/ms997538%28v=msdn%2e10%29)
* png2ico 代码工具：<http://www.winterdrache.de/freeware/png2ico/>
    * <a href="{% include relref.html url="/source/png2ico/png2ico-win-2002-12-08.zip" %}">png2ico-win-2002-12-08.zip</a> (90K)
    * <a href="{% include relref.html url="/source/png2ico/png2ico-src-2002-12-08.tar.gz" %}">png2ico-src-2002-12-08.tar.gz</a> (26K)
* 微软图标设计文档：[Icons (Design basics)](https://docs.microsoft.com/en-us/windows/win32/uxguide/vis-icons)
* C++ 如何将 Icon 转成 Bitmap，保留 Alpha 通道。<http://www.noobyard.com/article/p-odzsipgl-hw.html>
* 默认图标貌似是：`ICONGROUP,MAINICON,0`。


### 配置构建生成后任务

1. 把 pecopy.exe 入库到工程合适目录（建议入到 git，这样本机和构建机可以同时完成 pecopy）。
2. 把 `tempdir` 添加到根 `.gitignore`。
3. 配置生成后事件（一般根据工程当前的工程目录然后找到 pecopy.exe 的相对路径）：
```bat
"pecopy.exe" -in "$(TargetDir)fastvc.exe" \
             -out "$(TargetDir)shsign\fastvc.exe" \
             --LegalCopyright "版权测试"
```
{% include image.html url="/assets/images/210814-win-tools-reshack/20210814161318.png" %}

下载地址：<https://sunocean.life/tools/>
<https://sunocean.life/tools/pecopy.exe>


### 其它

如果存在签名，修改描述前，最后用 VS 自带工具 `signtool.exe` 移除签名先。
```bat
signtool.exe remove /s target.dll
```


## 多个 png 图片压缩成一个 ico


### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.10.2)
project(icopack)
add_executable(icopack icopack.cpp)
# cmake .. -G "Visual Studio 16 2019" -A Win32
```


### icopack.cpp

编译好的，方便直接食用：<a href="{% include relref.html url="/source/png2ico/icopack.zip" %}">icopack.zip</a> (65K)
多张 png 图片压缩成一个 ico 文件，参考代码：

`icopack out.ico favicon1.png favicon2.png favicon3.png`

<div class="highlighter-rouge" foldctrl="1"></div>
```cpp
//
// icopack - pack multiple PNG images into an ICO file
//
// Copyright (c) 2021 Optidash GmbH
//
// Licensed under the GNU General Public License, Version 3 (the "License");
// you may not use this file except in compliance with the License.
//
// You may obtain a copy of the License at
//    https://www.gnu.org/licenses/gpl-3.0.en.html
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int get_png_info(unsigned char *pIn, int iSize, int *width, int *height, int *bpp)
{
    int w, h, i, j, bits=0;
    if (pIn[0] != 0x89 || pIn[1] != 0x50 || pIn[2] != 0x4e || pIn[3] != 0x47) {
        // PNG signature not present - not a PNG file
        return 1;
    }
    // Parse enough of the PNG file to get to the image header (IHDR) to get
    // the image size and bit depth
    w = (pIn[16] << 24) | (pIn[17] << 16) | (pIn[18] << 8) | pIn[19];
    h = (pIn[20] << 24) | (pIn[21] << 16) | (pIn[22] << 8) | pIn[23];
    i = pIn[24]; // bits per pixel
    j = pIn[25]; // pixel type
    switch (j) {
        case 0: // grayscale
        case 3: // palette image
            bits = i;
            break;
        case 2: // RGB triple
            bits = i * 3;
            break;
        case 4: // grayscale + alpha channel
            bits = i * 2;
            break;
        case 6: // RGB + alpha
            bits = i * 4;
            break;
    }
    *width = w; *height = h; *bpp = bits;
    return 0;
} /* get_png_info() */
//
// Main program entry point
//
int main(int argc, char *argv[])
{
    int i, j, iSize, iFileCount;
    int width, height, bpp;
    int iOffset;
    FILE *ihandle, *ohandle;
    unsigned char *pIn;
    unsigned char ucTemp[512];

    if (argc < 3 || argc > 16)
    {
        printf("icopack Copyright (c) 2021 Optidash GmbH\n");
        printf("Combines multiple PNG images into a single ICO file\n");
        printf("Source images must be <= 256 pixels in each dimension\n\n");
        printf("Usage: icopack <outfile> <infile_1> <infile_2> <infile_N>\n");
        printf("example:\n\n");
        printf("icopack out.ico favicon1.png favicon2.png favicon3.png\n");
        return 0; // no filenames passed
    }
    iFileCount = argc - 2;
    ohandle = fopen(argv[1], "w+b");
    if (ohandle == NULL) {
        fprintf(stderr, "Unable to open output file: %s\n", argv[1]);
        return -1; // bad filename passed
    }
    // write an empty header; we'll fill it in later
    fwrite(ucTemp, 1, 6 + (iFileCount * 16), ohandle);
    ucTemp[0] = 0; // ICONDIR structure starts with 0,0
    ucTemp[1] = 0;
    ucTemp[2] = 1; // ICON file (2 = cursor file)
    ucTemp[3] = 0; // 2-byte int
    ucTemp[4] = (unsigned char)iFileCount;
    ucTemp[5] = 0; // 2-byte int
    iOffset = 6 + (iFileCount * 16); // starting offset of first file data
    for (i=2; i<argc; i++) { // collect all of the input files
        ihandle = fopen(argv[i],"rb");
        if (ihandle == NULL)
        {
            fprintf(stderr, "Unable to open input file: %s\n", argv[i]);
            return -1; // bad filename passed
        }
        fseek(ihandle, 0L, SEEK_END); // get the file size
        iSize = (int)ftell(ihandle);
        fseek(ihandle, 0, SEEK_SET);
        pIn = (unsigned char*)malloc(iSize);
        if (pIn == NULL) {
            fprintf(stderr, "Memory allocation error: size = %d\n", iSize);
            return -1; // bad filename passed
        }
        fread(pIn, 1, iSize, ihandle);
        if (get_png_info(pIn, iSize, &width, &height, &bpp)) {
            fprintf(stderr, "Input files must be PNG; exiting...\n");
            return -1; // bad filename passed
        }
        if (width > 256 || height > 256) {
            fprintf(stderr, "image files cannot be larger than 256x256; exiting...\n");
            return -1; // bad filename passed
        }
        // Fill in ICONDIRENTRY for this image
        j = 6 + (i-2) * 16;
        ucTemp[j] = (unsigned char)width;
        ucTemp[j+1] = (unsigned char)height;
        if (bpp < 8)
            ucTemp[j+2] = (1 << bpp); // number of colors
        else if (bpp == 8)
            ucTemp[j+2] = 255;
        else
            ucTemp[j+2] = 0; // non-palette image
        ucTemp[j+3] = 0; // reserved
        ucTemp[j+4] = 1; // color planes
        ucTemp[j+5] = 0; // 2-byte int
        ucTemp[j+6] = bpp;
        ucTemp[j+7] = 0; // 2-byte int
        *(uint32_t *)&ucTemp[j+8] = iSize; // image file size
        *(uint32_t *)&ucTemp[j+12] = iOffset; // offset to this image
        iOffset += iSize;
        // Write this image to the output file
        fwrite(pIn, 1, iSize, ohandle);
        free(pIn);
        fclose(ihandle);
    }
    // Seek to the beginning and update the ICONDIR and ICONDIRENTRY structures
    fseek(ohandle, 0, SEEK_SET);
    fwrite(ucTemp, 1, 6 + (iFileCount * 16), ohandle);
    fclose(ohandle);
    return 0;
} /* main() */
```


### icopack.py

单张图片自动生成 (16, 20, 24, 32, 40, 48, 64, 128, 256,) 各个级别的图片，然后压缩成一个 ico 文件。
如果图片不透明，顺便加一个圆角边框。参考代码：

<div class="highlighter-rouge" foldctrl="1"></div>
```py
#encoding=utf8
import re, os, sys
reldirx, _lidir = "", []
while not _lidir and len(reldirx) <= 100:
    reldirx += "../"
    checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
    _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
    if _lidir: reldirx = _lidir[0]
sys.path.append(reldirx)
from pythonx.funclib import *

from PIL import Image, ImageDraw

# https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi
def addCorners(im, rad):
    rad = max(rad, 3) # 防御。
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

# https://docs.microsoft.com/en-us/windows/win32/uxguide/vis-icons
def mainfile(fpath, fname, ftype):
    if not ftype in ("png", "jpg",):
        return

    if fpath.find("tempdir") != -1:
        return

    img = Image.open(fpath)
    if img.mode == "RGB":
        print("addCorners", fpath)
        #img = img.convert('RGBA')
        img = addCorners(img, int(img.size[0] / 8))

    assert img.mode == "RGBA", img.mode
    alpha = img.split()[-1]
    total = 0
    width, height = alpha.size
    for x in range(width):
        for y in range(height):
            total += alpha.getpixel((x, y))
    if total == width * height * 255:
        print("addCorners", fpath)
        img = img.convert('RGB')
        img = addCorners(img, int(img.size[0] / 8))

    imglist = []
    for size in (16, 20, 24, 32, 40, 48, 64, 128, 256,):
        newsize = (size, size)
        # 用于表示改变图像过程用的差值方法。0：双线性差值。1：最近邻居法。2：双三次插值法。3：面积插值法。
        #print(Image.BICUBIC) # 3
        #print(Image.ANTIALIAS) # 1
        temp = img.resize(newsize, resample=2)
        local = os.path.join("tempdir", "icopack", fname, "%dx%d.png" % (size, size))
        writefile(local, "")
        osremove(local)
        temp.save(local)
        imglist.append(local)

    target = fpath[:-4] + ".ico"
    icodir = os.path.split(os.path.abspath(__file__))[0]
    icopack = os.path.join(icodir, "icopack.exe")
    cmdx = "\"{}\" ".format(icopack,) + target + " " + " ".join(imglist)
    os.system(cmdx)

def main(rootdir):
    print("rootdir", rootdir)
    searchdir(rootdir, mainfile)

if __name__ == "__main__":
    main(".")
    main(os.path.split(os.path.abspath(__file__))[0])
```

<div class="highlighter-rouge" foldctrl="1"></div>
看起来很优秀，没有试过的代码：

```python
def bake_one_big_png_to_ico(sourcefile, targetfile, sizes=None):
    """Converts one big PNG into one ICO file.

    args:
        sourcefile (str): Pathname of a PNG file.
        targetfile (str): Pathname of the resulting ICO file.
        sizes (list of int): Requested sizes of the resulting
            icon file, defaults to [16, 32, 48].

    Use this function if you have one big, square PNG file
    and don’t care about fine-tuning individual icon sizes.

    Example::

        sourcefile = "Path/to/high_resolution_logo_512x512.png"
        targetfile = "Path/to/logo.ico"
        sizes = [16, 24, 32, 48, 256]
        bake_one_big_png_to_ico(sourcefile, targetfile, sizes)
    """
    if sizes is None:
        sizes = [16, 32, 48]
    icon_sizes = [(x, x) for x in sizes]
    Image.open(sourcefile).save(targetfile, icon_sizes=icon_sizes)
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-08-14-win-tools-reshack.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://www.rpi.net.au/~ajohnson/resourcehacker]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/www.rpi.net.au/ede721e3.html" %})
- [http://www.angusj.com/resourcehacker/]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/www.angusj.com/0cd86f81.html" %})
- [https://docs.microsoft.com/en-us/previous-versions/ms997538%28v=msdn%2e10%29]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/docs.microsoft.com/a304a57f.html" %})
- [http://www.winterdrache.de/freeware/png2ico/]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/www.winterdrache.de/aa729e8b.html" %})
- [https://docs.microsoft.com/en-us/windows/win32/uxguide/vis-icons]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/docs.microsoft.com/5ee989bc.html" %})
- [http://www.noobyard.com/article/p-odzsipgl-hw.html]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/www.noobyard.com/daa7ba18.html" %})
- [https://www.gnu.org/licenses/gpl-3.0.en.html]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/www.gnu.org/2ecb6aab.html" %})
- [https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi]({% include relrefx.html url="/backup/2021-08-14-win-tools-reshack.md/stackoverflow.com/666fc2b7.html" %})
