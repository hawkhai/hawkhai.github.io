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
if not os.getcwd() in sys.path: # fix linux 软连接的 bug
    sys.path.append(os.getcwd())
import time
from pythonx.funclib import *

# filelist -> ((localfile, arcname), (localfile, arcname))
#               arcname -> a\b\c.txt
# ktouch   -> strict_timestamps=2000
# note: remove argv modifyTime(zipName, filelist, modifyTime=None, ktouch=True)
#def gzipflist(zipName, filelist, ktouch=True):
def main():
    rootdir = os.path.split(os.path.abspath(__file__))[0]
    zipName = os.path.join(rootdir, "mytable_sample.zip")

    filelist = []
    rootdir = r"E:\kSource\blog\kvision\ksample\mytable"
    dirs = os.listdir(rootdir)
    dirs.sort()
    for dir in dirs:
        type = dir.split(".")[-1]
        if not type in ("jpg", "png", "jpeg"):
            continue
        fpath = os.path.join(rootdir, dir)
        fname = dir.split(".")[0]
        print(fpath)

        filelist.append([os.path.join(rootdir, dir), dir])
        filelist.append([os.path.join(rootdir, fname+".xlsx"), fname+"_WPS.xlsx"])
        filelist.append([os.path.join(rootdir, "table-recognition", fname+"result.xlsx"), fname+"_CF.xlsx"])

    print("gzipflist", zipName)
    gzipflist(zipName, filelist)

if __name__ == "__main__":
    main()
