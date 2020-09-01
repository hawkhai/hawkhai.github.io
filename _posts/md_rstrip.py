#encoding=utf8
import re, os, sys
sys.path.append("../../")
from pythonx.funclib import *

OPENFILE = "openfile" in sys.argv
AUTOFORMAT = "format" in sys.argv

def getLeftSpaceCount(line):
    line = line[:]
    assert not line.startswith("\t"), line
    count = 0
    while line and line[0] == ' ':
        line = line[1:]
        count += 1
    return count

g_cnchar = []
g_enchar = []
g_xychar = []
def mainfile(fpath, fname, ftype):
    if not ftype in ("md", "py", "php",):
        return

    if fpath.find("\\backup\\") != -1:
        return
    if fpath.find("\\d2l-zh\\") != -1:
        return

    print(fpath)
    lines = readfileLines(fpath, False, False, "utf8")
    lines = [line.rstrip() for line in lines]

    codestate = False
    for index, line in enumerate(lines):
        count = getLeftSpaceCount(line)

        if line and line.split()[0] in ("*", "-",):
            idtcnt = 2
        else:
            idtcnt = 4

        cnsign = "，；：、。？—×【】《》（）“”"
        cnregex = "\u4e00-\u9fa5" + cnsign
        ensign = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        liw = re.findall("[{}]+".format(cnregex,), line, re.IGNORECASE)
        g_cnchar.extend(liw)
        lia = re.findall("[^{}]+".format(cnregex,), line, re.IGNORECASE)
        g_enchar.extend(lia)

        lix1 = re.findall("[{}][^{} *]".format(cnregex, cnregex), line, re.IGNORECASE)
        lix2 = re.findall("[^{} *][{}]".format(cnregex, cnregex), line, re.IGNORECASE)
        lix = []
        lix.extend(lix1)
        lix.extend(lix2)

        for ix in lix:
            cx, cy = ix
            if cy in cnsign or cx in cnsign:
                continue
            if cy in "-<]" or cx in "->[":
                continue
            if cx in ('"', "[") and (" "+line).find(" "+ix) != -1:
                continue
            if cy in ('"', "]") and (line+" ").find(ix+" ") != -1:
                continue
            if cx in ('"',) and ("["+line).find("["+ix) != -1:
                continue
            if cy in ('"',) and (line+"]").find(ix+"]") != -1:
                continue
            g_xychar.append(ix)
            print(ix, "\t", line)
            if AUTOFORMAT:
                line = line.replace(ix, cx+" "+cy)
                lines[index] = line

        fxline = "".join(line.split())
        if fxline.startswith("{%highlight"):
            codestate = True
        if fxline.startswith("{%endhighlight%}"):
            codestate = False

        if codestate:
            continue

        if count > 12 or count % idtcnt == 0:
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

def viewchar(lichar, xfile):
    li = list(set("".join(lichar)))
    li.sort()
    page = ""
    minv, maxv = 1024, 0
    for index, cnchar in enumerate(li):
        page += cnchar
        minv = min(minv, ord(cnchar))
        maxv = max(maxv, ord(cnchar))
        if (index + 1) % 50 == 0:
            page += "\r\n"
    tempfile = os.path.join("tempdir", xfile)
    writefile(tempfile, page.encode("utf8"))

    if OPENFILE:
        openTextFile(tempfile)
    print(minv, maxv)

def main():
    print(parsePythonCmdx(__file__, retmap=True))
    searchdir("..", mainfile)

    viewchar(g_cnchar, "cnfile.txt")
    viewchar(g_enchar, "enfile.txt")

if __name__ == "__main__":
    main()
