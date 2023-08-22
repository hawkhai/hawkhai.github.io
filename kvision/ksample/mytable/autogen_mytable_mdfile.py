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

def mainf2(rootdir, mdfile):
    fdata = readfile(mdfile, True, "utf8")
    fdata = fdata.split("-----")
    assert len(fdata) == 2, len(fdata)
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

        imgurl = "https://cvsample.sunocean.life/imgtable/{}".format(dir)

        fname = dir
        fpath = os.path.join(rootdir, fname)
        fnamec = fname.split(".")[0]

        item = r"""
{}.xlsx 下载
<a href="//cvsample.sunocean.life/imgtable/result/{}.xlsx">自研</a> /
<a href="//cvsample.sunocean.life/imgtable/BaiduOCRConverter_Excel/{}.xlsx">百度</a> /
<a href="//cvsample.sunocean.life/imgtable/docmind/{}.xlsx">阿里</a>。

{} include imagek5.html
url="/imgtable/{}" width="22%"
url2="/imgtable/result/{}.xlsx.png" width2="22%"
url3="/imgtable/BaiduOCRConverter_Excel/{}.xlsx.png" width3="22%"
url4="/imgtable/docmind/{}.xlsx.png" width4="22%"
thumbnail="/thumbnail.png"
{}
""".format(fnamec, fnamec, fnamec, fnamec,
           "{%",
           fname, fnamec, fnamec, fnamec,
           "%}",)

        fdata += item

        # imgtable/docmind/007_c5918.xlsx.svg
        # imgtable/docmind/007_c5918.xlsx.svg/70401f2d8e4971c3a1fe179c661e2e27.007_c5918.xlsx.svg
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

    print(writefile(mdfile, fdata, "utf8"))
    #openTextFile(mdfile)

if __name__ == "__main__":
    from pythonx.note.kvision.pack import LcMapPath
    mainf2(LcMapPath(r"E:\kSource\blog\kvision\ksample\imgtable"),
           LcMapPath(r"E:\kSource\blog\invisible\kvision\imgtable.md"))
    print("ok")
