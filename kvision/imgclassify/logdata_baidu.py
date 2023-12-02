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

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main():

    def addkey(keyword, keywordmap):
        if not keyword in keywordmap:
            keywordmap[keyword] = 0
        keywordmap[keyword] = keywordmap[keyword] + 1

    keywordmap = {}
    rootmap = {}

    def mainfile(fpath, fname, ftype):
        if not re.findall("[a-f0-9]{7}.json$", fname):
            return
        print(fpath)
        fjson = readfileJson(fpath, "utf8")
        result = fjson["result"]
        for item in result:
            keyword = item["keyword"]
            root = item["root"]
            addkey(keyword, keywordmap)
            addkey(root, rootmap)

    searchdir(r"logdata\baidu\dataset", mainfile)

    writefileJson(r"logdata\baidu\rootmap.json", rootmap, "utf8")
    writefileJson(r"logdata\baidu\keywordmap.json", keywordmap, "utf8")

if __name__ == "__main__":
    main()
