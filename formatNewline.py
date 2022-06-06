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

def main():
    rn = None
    fpath = None
    print(sys.argv)
    for i in sys.argv:
        if i == "n":
            rn = "\n"
        elif i == "rn":
            rn = "\r\n"
        else:
            if os.path.exists(i):
                fpath = i

    if rn and fpath:
        fdata = readfile(fpath, True)
        fdata = fdata.replace("\r\n", "\n")
        fdata = fdata.replace("\n", rn)
        print(fpath)
        print(writefile(fpath, fdata))


if __name__ == "__main__":
    main()
