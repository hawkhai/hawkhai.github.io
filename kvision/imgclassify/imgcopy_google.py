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

import requests
import base64
from imgcopy_baidu import *

def maingo(rootdir, category):
    for subdir in os.listdir(rootdir):
        subdir = os.path.join(rootdir, subdir)
        if not os.path.isdir(subdir):
            continue

        for ifile in os.listdir(subdir):
            ifile = os.path.join(subdir, ifile)
            if not os.path.isfile(ifile):
                continue

            yfile = os.path.join(rootdir, "{}_google.jpg".format(getFileMd5(ifile)[:16]))
            copyimg(ifile, yfile)

def main():
    rootdir = r"E:\kSource\blog\kvision\imgclassify\valset"
    for category in os.listdir(rootdir):
        subdir = os.path.join(rootdir, category)
        if not os.path.isdir(subdir):
            continue
        maingo(subdir, category)

if __name__ == "__main__":
    main()
