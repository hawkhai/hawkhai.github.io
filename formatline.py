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
from pythonx.funclib import *

def formatRead(fpath, rn):
    fdata = readfile(fpath, True)
    fdata = fdata.replace("\r\n", "\n")
    fdata = fdata.replace("\n", rn)
    return fdata

def maindir(rootdir, rn):
    def mainfile(fpath, fname, ftype):
        if not ftype in "html htm py js css scss fsh vsh svg".split():
            return
        fdata = formatRead(fpath, rn)
        print(fpath)
        print(writefile(fpath, fdata))
    searchdir(rootdir, mainfile)

def main():
    rn = None
    fpath = None
    print(sys.argv)
    for i in sys.argv[1:]:
        if i == "\\n":
            rn = "\n"
        elif i == "\\r\\n":
            rn = "\r\n"
        else:
            if os.path.exists(i):
                fpath = i

    if rn and fpath:
        fdata = formatRead(fpath, rn)
        print(fpath)
        print(writefile(fpath, fdata))
    elif rn:
        maindir(".", rn)
    else:
        print("null")

if __name__ == "__main__":
    main()
