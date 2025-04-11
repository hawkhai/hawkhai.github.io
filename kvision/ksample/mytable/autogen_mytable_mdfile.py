#encoding=utf8
import re, os, sys
from pathlib import Path
check_pythonx_dir = lambda x: x and os.path.exists(os.path.join(x, "funclib.py"))
check_ksource_dir = lambda x: x and check_pythonx_dir(os.path.join(x, "pythonx"))
for reldirx in (os.path.dirname(os.path.abspath(__file__)), # 这个先，规避加载漏洞。
                os.path.abspath(".")):
    while len(reldirx) > 3: # 3 应该所有平台都问题不大。
        if check_ksource_dir(reldirx): break # YES!!
        reldirx = os.path.dirname(reldirx) # 只尝试 funclib.py，funclib.pyc 存在版本问题。
    if check_ksource_dir(reldirx): break # YES!!
for devdirx in [r"E:\kSource", r"D:\kSource", r"C:\kSource"]:
    if not check_ksource_dir(reldirx):
        reldirx = devdirx
if check_ksource_dir(reldirx) and not reldirx in sys.path:
    sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del devdirx # reldirx 可以继续使用
from pythonx.funclib import *
import time, math

REBUILD = "rebuild" in sys.argv

def mainf2(rootdir, mdfile, tabledir, my2x, baidudir="baidu"):
    fdata = readfile(mdfile, True, "utf8")
    fdata = fdata.split("-----")
    assert len(fdata) == 2, len(fdata)
    tailsep = "<hr class='reviewline'/>"
    ftail = "" if fdata[-1].find(tailsep) == -1 else fdata[-1].split(tailsep)[-1]
    fdata = fdata[0].strip()
    fdata += r"""

-----
"""

    xtime = time.time()
    svgtrue = {}

    dirs = os.listdir(rootdir)
    dirs.sort()
    for dir in dirs:
        if not dir.split(".")[-1] in ("jpg", "png", "jpeg"):
            continue

        imgurl = "https://cvsample.sunocean.life/{}/{}".format(tabledir, dir)

        fname = dir
        fpath = os.path.join(rootdir, fname)
        fnamec = fname.split(".")[0]

        item = r"""
{}.xlsx 下载
<a href="//cvsample.sunocean.life/{}/table-recognition/linux/resultv3/{}_MSv11.xlsx">自研 xlsx</a> /
<a href="//cvsample.sunocean.life/{}/table-recognition/linux/resultv3/{}_MSv11.html">自研 html</a> /
<a href="//cvsample.sunocean.life/{}/{}/{}.xlsx">百度</a> /
<a href="//cvsample.sunocean.life/{}/quark/{}.xlsx">夸克</a>。

{} include imagek5.html
url="/{}/{}" width="21%"
url2="/{}/table-recognition/linux/resultv3/{}_MSv11.xlsx.svg" width2="21%"
url3="/{}/{}/{}.xlsx.png" width3="21%"
url4="/{}/quark/{}.xlsx.png" width4="21%"
thumbnail="/thumbnail.png"
{}
""".format(fnamec,
                tabledir+"_2x" if my2x else tabledir, fnamec,
                tabledir+"_2x" if my2x else tabledir, fnamec,
                tabledir, baidudir, fnamec,
                tabledir, fnamec,
           "{%",
           tabledir, fname,
                tabledir+"_2x" if my2x else tabledir, fnamec,
                tabledir, baidudir, fnamec,
                tabledir, fnamec,
           "%}",)

        fdata += item

        # tabledir/docmind/007_c5918.xlsx.svg
        # tabledir/docmind/007_c5918.xlsx.svg/70401f2d8e4971c3a1fe179c661e2e27.007_c5918.xlsx.svg
        docmind_svgfile = os.path.join(rootdir, "docmind", "{}.xlsx.svg".format(fnamec))
        baidu_svgfile = os.path.join(rootdir, "BaiduOCRConverter_Excel", "{}.xlsx.svg".format(fnamec))
        my_svgfile = os.path.join(rootdir, "result", "{}.xlsx.svg".format(fnamec))
        for svgfile in (my_svgfile, baidu_svgfile, docmind_svgfile):
            #assert os.path.exists(svgfile)
            #fmd5 = getFileMd5(svgfile)
            ipath = os.path.relpath(svgfile, rootdir).replace("\\", "/")
            #osspath = ipath + "/{}.{}.xlsx.svg".format(fmd5, fnamec)
            #print(fmd5, osspath)
            #svgtrue[ipath] = osspath

    #print(writefile(mdfile, fdata, "utf8"))

    fdata = fdata.replace(".xlsx.png", ".xlsx.svg")
    #for key in svgtrue.keys():
    #    fdata = fdata.replace(key, svgtrue[key])

    if ftail:
        fdata += "\r\n\r\n\r\n{}{}".format(tailsep, ftail)
    print(writefile(mdfile, fdata, "utf8"))
    #openTextFile(mdfile)

if __name__ == "__main__":
    from pythonx.note.kvision.pack import LcMapPath
    mainf2(LcMapPath(r"E:\kSource\blog\kvision\ksample\mytable"),
           LcMapPath(r"E:\kSource\blog\invisible\kvision\mytable.md"), "mytable", False,
           baidudir="BaiduOCRConverter_Excel")
    mainf2(LcMapPath(r"E:\kSource\blog\kvision\ksample\imgtable"),
           LcMapPath(r"E:\kSource\blog\invisible\kvision\imgtable.md"), "imgtable", True)
    print("ok")
