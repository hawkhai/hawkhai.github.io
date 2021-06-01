#encoding=utf8
import sys
import re, os, sys
sys.path.append("../")
import datetime, time
from pythonx.funclib import *

AUTOFORMAT = "format" in sys.argv

def mainfilew(fpath, fname, ftype):
    if not ftype in ("md",): return
    fdata = readfile(fpath, True)
    fdatabak = fdata[:]

    li = fdata.split("\r\n")
    li2 = []
    first = True
    for line in li:
        result = re.findall("^({})\\s+({})$".format("[^ ]+\\.(?:png|jpg|jpeg|webp|gif)", "[0-9.]+"), line)
        if result:
            result = result[0]
            if first:
                print(fpath)
                first = False
            img, idx = result
            line = r"""{{% include image.html url="/images/{}" relocate="{}" %}}""".format(img, idx)
            if idx == "0":
                line = r"""{{% include image.html url="/images/{}" %}}""".format(img,)
            print("\t"*1, result, line)
            assert os.path.exists("./images/"+img), "./images/"+img
            li2.append(line)
        else:
            li2.append(line)
    fdata = "\r\n".join(li2)

    if fdata != fdatabak and AUTOFORMAT:
        print("writefile", fpath)
        writefile(fpath, fdata)

def main():
    print(parsePythonCmdx(__file__))
    searchdir(".", mainfilew, ignorelist=(
        "backup", "d2l-zh", "mathjax", "tempdir", "msgboard",
        "Debug", "Release", ".vs", "openglcpp", "opengl-3rd", "opengles3-book", "opengles-book-samples",
        "UserDataSpider", "docs.gl",
        ), reverse=True)

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) >= 2 and os.path.isdir(sys.argv[1]):
        workdir = sys.argv[1]
        @CwdDirRun(workdir)
        def maingo():
            main()
        maingo()
    else:
        main()
    print(parsePythonCmdx(__file__))
