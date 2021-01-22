#encoding=utf8
import re, os, sys
sys.path.append("../../")
from pythonx.funclib import *

def main():
    fpath = r"2021-01-22-shader-OpenGL-ex-irrlicht.md"
    fdata = readfileLines(fpath, True)

    cmtx = set()
    for line in fdata:
        if line.find("//") == -1: continue
        ax, bx = line.split("//")
        ax, bx = ax.strip(), bx.strip()
        if bx in cmtx:
            print(line)
        cmtx.add(bx)

    countset = set()
    for line in fdata:
        line = line.strip()
        line = line.split("//")[0].strip()
        if line.startswith("* "):
            line = line[2:]
        for i in line.split(","):
            i = i.strip()
            if i.startswith("egl") or i.startswith("wgl") or i.startswith("gl"):
                if re.findall("gl[A-Z]", i):
                    countset.add(i)
    print(len(countset))
    assert len(countset) == 284

if __name__ == "__main__":
    main()
