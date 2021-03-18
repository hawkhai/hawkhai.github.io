#encoding=utf8
import re, os, sys
sys.path.append("../")
from pythonx.funclib import *

KEY_OR       = "or"
KEY_OPENFILE = "openfile"
KEY_REMOVE   = "removefile"
KEY_BACKUPDIR = "backupdir"
KEY_LIST     = (KEY_OR, KEY_OPENFILE, KEY_REMOVE, KEY_BACKUPDIR)

OPENFILE = KEY_OPENFILE in sys.argv
OP_OR    = KEY_OR in sys.argv
REMOVEFILE = KEY_REMOVE in sys.argv
BACKUPDIR = KEY_BACKUPDIR in sys.argv

keywords = sys.argv[1:]
keywords = [bytesToString(key.encode("utf8")).lower() for key in keywords if key not in KEY_LIST]
print("SEARCH", keywords)
print(r"""使用方法：
保留关键字：{}
不区分大小写。
""".format(" ".join(KEY_LIST)))

def readfileIglist(fpath):
    li = readfile(fpath, True, "utf8").split("\n")
    li = [i.strip().split("#")[0].strip() for i in li if i.strip().split("#")[0].strip()]
    assert li, fpath
    return li

# 无法访问此网站
# ERR_CONNECTION_TIMED_OUT
def mainsearch():

    def mainfile(fpath, fname, ftype):
        sdoc = False
        if ftype.lower() in ("md",): sdoc = True
        if fpath.find("backup") != -1 and BACKUPDIR: sdoc = True
        if fpath.find("_site") != -1: sdoc = False
        if not sdoc: return

        fdata = readfile(fpath, True).lower()

        itag = bytesToString("无法访问此网站".encode("utf8"))
        if fdata.find("ERR_CONNECTION_TIMED_OUT".lower()) != -1 or fdata.find(itag) != -1:
            if not fpath in readfileIglist("mdrstrip_InvalidURL.txt"):
                print("无法访问此网站", fpath)
                if OPENFILE:
                    openTextFile(fpath)
                elif REMOVEFILE:
                    osremove(fpath)

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
