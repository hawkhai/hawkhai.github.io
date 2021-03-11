#encoding=utf8
import re, os, sys
sys.path.append("../")
from pythonx.funclib import *

KEY_OR       = "or"
KEY_OPENFILE = "openfile"
KEY_LIST     = (KEY_OR, KEY_OPENFILE)

OPENFILE = KEY_OPENFILE in sys.argv
OP_OR    = KEY_OR in sys.argv
print(r"""使用方法：
保留关键字：{}
不区分大小写。
""".format(" ".join(KEY_LIST)))

def mainsearch():

    def mainfile(fpath, fname, ftype):
        if not ftype.lower() in ("md",):
            return
        fdata = readfile(fpath, True).lower()
        keywords = sys.argv[1:]
        keywords = [key.lower() for key in keywords
            if key not in KEY_LIST]
        if not keywords: return
        findkeys = []
        for key in keywords:
            if fdata.find(key) != -1:
                findkeys.append(key)
        if not OP_OR and len(findkeys) != len(keywords):
            findkeys = []
        if findkeys:
            print("***" * 40)
            print(fpath, findkeys)
            if OPENFILE:
                openTextFile(fpath)
    searchdir(".", mainfile)

if __name__ == "__main__":
    print(parsePythonCmdx(__file__))
    mainsearch()
