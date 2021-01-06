#encoding=utf8
import re, os, sys
sys.path.append("../../../")
from pythonx.funclib import *

def main():
    cmtmap = {}
    def mainfile(fpath, fname, ftype):
        if not ftype in ("vsh", "fsh",):
            return
        lines = readfileLines(fpath, False, False, decode="utf8")
        for line in lines:
            if line.find("//") == -1: continue
            line, cmt = line.strip().split("//", 1)
            line = line.strip()
            cmt = cmt.strip()
            if not line: continue
            if not line.split()[0] in ("uniform", "attribute", "varying", "#define",): continue
            if cmt:
                cmtmap[line] = cmt
    searchdir(".", mainfile)
    for key in cmtmap.keys():
        print(key, "//", cmtmap[key])

    def mainfile2(fpath, fname, ftype):
        if not ftype in ("vsh", "fsh",):
            return
        lines = readfileLines(fpath, False, False, decode="utf8")
        for index, line in enumerate(lines):
            srcline = line[:]
            line = line.strip().split("//", 1)[0]
            if not line: continue
            if not line.split()[0] in ("uniform", "attribute", "varying", "#define",): continue
            if line in cmtmap.keys():
                newline = srcline.split("//", 1)[0] + " // " + cmtmap[line]
                lines[index] = newline
        fdata = "\r\n".join(lines)
        writefile(fpath, fdata, "utf8")
    searchdir(".", mainfile2)

if __name__ == "__main__":
    main()
