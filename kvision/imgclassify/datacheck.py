#encoding=utf8
import re, os, sys
for reldirx, _lidir in (("./", []), (os.path.split(__file__)[0]+"/", [])):
    while not _lidir and len(reldirx) <= 100:
        reldirx += "../"
        checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx)
from pythonx.funclib import *

import requests
import base64

def main():
    fpath = r"D:\kSource\blog\kvision\imgclassify\logdata\baidu\dataset\animal\cadb_f3b8c0e.json"
    fdata = readfile(fpath)
    fdata = bytesToString(fdata, "utf8")
    print(fdata)

if __name__ == "__main__":
    main()
