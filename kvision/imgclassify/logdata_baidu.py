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

    checkok = readfile("checkok.txt", True)
    checktag = False
    def mainfile2(fpath, fname, ftype):

        nonlocal checktag
        if not checkok or checkok == fpath:
            checktag = True
        if not checktag:
            return

        if not re.findall("[a-f0-9]{7}.json$", fname):
            return
        print(fpath)
        fjson = readfileJson(fpath, "utf8")
        result = fjson["result"]

        keyword0 = result[0]["keyword"]
        root0 = result[0]["root"].split("-")[0]

        keyword1 = result[1]["keyword"]
        root1 = result[1]["root"].split("-")[0]

        rootall = [i["root"].split("-")[0] for i in result]
        rootall = list(set(rootall))
        rootall.sort()

        if root0 and root0 == root1:
            return

        if root0 == "动物" and rootall in (
                ["动物", "建筑"],
                ["动物", "商品"],):
            return
        print(rootall)

        # D:\kSource\blog\kvision\imgclassify\dataset\animal\cadb_018c8fe.jpg
        # D:\kSource\blog\kvision\imgclassify\logdata\baidu\dataset\animal\cadb_018c8fe.json
        imgfile = fpath.replace(r"logdata\baidu\dataset", r"dataset")
        imgfilec, imgfilet = os.path.splitext(imgfile)
        for ft in (".jpg", ".jpeg", ".webp", ".png", ".bmp"):
            if os.path.exists(imgfilec+ft):
                imgfile = imgfilec+ft
            if os.path.exists(imgfile):
                break
        assert os.path.exists(imgfile), imgfile

        openTextFile(fpath)
        openFileWithDefault(imgfile)
        assert False, fpath

        writefile("checkok.txt", fpath)

    if False:
        searchdir(r"logdata\baidu\dataset", mainfile)

        writefileJson(r"logdata\baidu\rootmap.json", rootmap, "utf8")
        writefileJson(r"logdata\baidu\keywordmap.json", keywordmap, "utf8")
    else:
        rootmap = readfileJson(r"logdata\baidu\rootmap.json", "utf8")
        keywordmap = readfileJson(r"logdata\baidu\keywordmap.json", "utf8")

        cats = set()
        for key in rootmap.keys():
            cats.add(key.split("-")[0])
        cats = list(cats)

        print("\r\n".join(cats))

    searchdir(r"logdata\baidu\dataset", mainfile2)

if __name__ == "__main__":
    main()
