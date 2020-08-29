#encoding=utf8
import re, os, sys
sys.path.append("../../")
from pythonx.funclib import *

def getLeftSpaceCount(line):
    line = line[:]
    assert not line.startswith("\t"), line
    count = 0
    while line and line[0] == ' ':
        line = line[1:]
    return count

def mainfile(fpath, fname, ftype):
    if not ftype in ("md", "py",):
        return

    print(fpath)
    lines = readfileLines(fpath, False, False, "utf8")
    lines = [line if line.endswith(" = ") else line.rstrip() for line in lines]

    for line in lines:
        count = getLeftSpaceCount(line)
        assert count % 4 == 0, line

    writefile(fpath, "\r\n".join(lines).encode("utf8"))

def main():
    searchdir("..", mainfile)

if __name__ == "__main__":
    main()
