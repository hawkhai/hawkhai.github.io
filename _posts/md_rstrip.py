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
        count += 1
    return count

def mainfile(fpath, fname, ftype):
    if not ftype in ("md", "py", "php",):
        return

    if fpath.find("\\backup\\") != -1:
        return
    if fpath.find("\\d2l-zh\\") != -1:
        return

    print(fpath)
    lines = readfileLines(fpath, False, False, "utf8")
    lines = [line if line.endswith(" = ") else line.rstrip() for line in lines]

    index = 0
    codestate = False
    for line in lines:
        count = getLeftSpaceCount(line)

        if line and line.split()[0] in ("*", "-",):
            kxcnt = 2
        else:
            kxcnt = 4

        index += 1

        fxline = "".join(line.split())
        if fxline.startswith("{%highlight"):
            codestate = True
        if fxline.startswith("{%endhighlight%}"):
            codestate = False

        if codestate:
            continue

        if count >= 10 or count % kxcnt == 0:
            pass # ok
        else:
            openTextFile(fpath)
            assert False, "{}:{} {}".format(fpath, index, line)

    page = "\r\n".join(lines)
    while page.find("\r\n" * 4) != -1:
        page = page.replace("\r\n" * 4, "\r\n" * 3)

    #page = page.replace("\r\n### ", "\r\n\r\n### ")
    #page = page.replace("\r\n## ",  "\r\n\r\n## ")
    #page = page.replace("\r\n# ",   "\r\n\r\n# ")

    writefile(fpath, page.encode("utf8"))

def main():
    searchdir("..", mainfile)

if __name__ == "__main__":
    main()
