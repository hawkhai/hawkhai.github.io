#encoding=utf8
import re, os, sys
sys.path.append("../../")
from pythonx.funclib import *

def mainfile(fpath, fname, ftype):
    if not ftype in ("md",):
        return

    print(fpath)
    lines = readfileLines(fpath, False, False, "utf8")
    lines = [line if line.endswith(" = ") else line.rstrip() for line in lines]

    writefile(fpath, "\r\n".join(lines).encode("utf8"))

def main():
    searchdir(".", mainfile)

if __name__ == "__main__":
    main()
