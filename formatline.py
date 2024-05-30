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
