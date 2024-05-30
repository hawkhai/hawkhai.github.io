#encoding=utf8
import re, os, sys
for reldirx, _lidir in (
        (os.path.dirname(os.path.abspath(__file__)), []), # 这个先，规避加载漏洞。
        (os.path.dirname(os.path.abspath(".")), [])):
    while not _lidir and len(reldirx) > 3: # 3 应该所有平台都问题不大。
        reldirx = os.path.dirname(reldirx) # 只尝试 funclib.py，funclib.pyc 存在版本。
        _checkfunc = lambda idir: os.path.exists(os.path.join(reldirx, idir, "pythonx", "funclib.py"))
        _lidir = [os.path.join(reldirx, idir) for idir in os.listdir(reldirx) if _checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
        del _checkfunc
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del _lidir # reldirx 可以继续使用
from pythonx.funclib import *
import time, math

REBUILD = "rebuild" in sys.argv

def mainf2(rootdir, mdfile, tabledir):

    fdata = readfile(mdfile, True, "utf8")
    fdata = fdata.split("-----")
    assert len(fdata) == 2, len(fdata)
    tailsep = "<hr class='reviewline'/>"
    ftail = "" if fdata[-1].find(tailsep) == -1 else fdata[-1].split(tailsep)[-1]
    fdata = fdata[0].strip()
    fdata += r"""

-----
"""

    dirs = os.listdir(rootdir)
    dirs.sort()
    for dir in dirs:
        if not dir.split(".")[-1] in ("jpg", "png", "jpeg"):
            continue

        fname = dir
        fpath = os.path.join(rootdir, fname)
        fnamec = fname.split(".")[0]
        ftype = fname.split(".")[-1]

        """
E:\kSource\blog\kvision\ksample\mytable\table-recognition\001_8e68c_baidu.png
E:\kSource\blog\kvision\ksample\mytable\table-recognition\001_8e68c_MS.png
E:\kSource\blog\kvision\ksample\mytable\table-recognition\001_8e68c_MSv11.png
        """
        item = r"""
{} include imagek5.html
url="/{}/table-recognition/{}_baidu.{}" width="40%"
url2="/{}/table-recognition/{}_MSv11.{}" width2="40%"
thumbnail="/thumbnail.png"
{}
""".format("{%",
                tabledir, fnamec, ftype,
                tabledir, fnamec, ftype,
           "%}",)

        fdata += item

    if ftail:
        fdata += "\r\n\r\n\r\n{}{}".format(tailsep, ftail)
    print(writefile(mdfile, fdata, "utf8"))
    #openTextFile(mdfile)

if __name__ == "__main__":
    from pythonx.note.kvision.pack import LcMapPath
    mainf2(LcMapPath(r"E:\kSource\blog\kvision\ksample\mytable"),
           LcMapPath(r"E:\kSource\blog\invisible\kvision\mytableborder.md"), "mytable")
    print("ok")
