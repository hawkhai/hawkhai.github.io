#encoding=utf8
import re, os, sys
for reldirx, _lidir in (("./", []), (os.path.split(__file__)[0]+"/", [])):
    while not _lidir and len(reldirx) <= 100:
        reldirx += "../"
        checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
        if _lidir: reldirx = _lidir[0]
    if _lidir: break
sys.path.append(reldirx)
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
