#encoding=utf8
import re, os, sys
sys.path.append("../")
from pythonx.funclib import *

def getPostTitle(fpath):
    fdata = readfile(fpath).decode("utf8")
    fdata = fdata.split("---")[1]
    for line in fdata.split("\n"):
        line = line.strip()
        if not line: continue
        key, value = line.split(":", 1)
        if key == "title":
            return value.strip()
    return fpath

def main():
    print(parsePythonCmdx(__file__))
    fnamelist = []
    def mainfile(fpath, fname, ftype):
        # print(fname[11:])
        fnamelist.append("%-64s"%fname[11:] + "\t" + getPostTitle(fpath))
    searchdir("_posts", mainfile)

    fnamelist.sort()
    print("\n".join(fnamelist))

if __name__ == "__main__":
    main()
