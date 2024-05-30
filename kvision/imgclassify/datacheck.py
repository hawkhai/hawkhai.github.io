#encoding=utf8
import re, os, sys
for reldirx, _lidir in (
        (os.path.split(os.path.abspath(__file__))[0]+"/", []), # 这个先，规避加载漏洞。
        (os.path.split(os.path.abspath("."))[0]+"/", [])):
    while not _lidir and len(reldirx) > 3: # 3 应该所有平台都问题不大。
        reldirx = os.path.split(reldirx)[0] # 只尝试 funclib.py，funclib.pyc 存在版本。
        _checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if _checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
        del _checkfunc
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del _lidir # reldirx 可以继续使用
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
