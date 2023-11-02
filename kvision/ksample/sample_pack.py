#encoding=utf8
import re, os, sys
reldirx, _lidir = "", []
while not _lidir and len(reldirx) <= 100:
    reldirx += "../"
    checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
    _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
    assert len(_lidir) in (0, 1), _lidir
    if _lidir: reldirx = _lidir[0]
sys.path.append(reldirx)
if not os.getcwd() in sys.path: # fix linux 软连接的 bug
    sys.path.append(os.getcwd())
import time
try:
    from pythonx.funclib import *
except ModuleNotFoundError: # No module named 'pythonx'
    reldirx, _lidir = os.path.split(os.path.abspath(__file__))[0] + "/", []
    while not _lidir and len(reldirx) <= 100:
        reldirx += "../"
        checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = _lidir[0]
    sys.path.append(reldirx)

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
