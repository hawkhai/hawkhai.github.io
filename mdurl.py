#encoding=utf8
import sys
import re, os, sys
sys.path.append("../")
import datetime, time
from pythonx.funclib import *

AUTOFORMAT = "format" in sys.argv
URL_REGEX = r"""(
                    (https?)://
                        ([a-z0-9\.-]+\.[a-z]{2,6})
                        (:[0-9]{1,4})?
                    (/[a-z0-9\&%_\./~=+:@–-]*)?
                    (\?[a-z0-9\&%_\./~=:-]*)?
                    (#[a-z0-9\&%_\./~=:-]*)?
                )"""
URL_REGEX = "".join(URL_REGEX.split())
#li = re.findall(regex, line, re.IGNORECASE)

def mainfilew(fpath, fname, ftype):
    if not ftype in ("md",): return
    fdata = readfile(fpath, True)
    fdatabak = fdata[:]

    li = fdata.split("\r\n")
    li2 = []
    first = True

    chekurlx = set()
    for line in li:
        for url in re.findall(URL_REGEX, line, re.IGNORECASE):
            chekurlx.add(url[0])
    for url in chekurlx:
        urlx = url + "/"
        if urlx in chekurlx:
            openTextFile(fpath)
            assert False, urlx

    for line in li:
        result = re.findall("\\s(%s)\\s"%URL_REGEX, " %s "%line, re.IGNORECASE)
        if result:
            if first:
                print(fpath, result)
                first = False
            assert len(result) == 1
            result = result[0]
            url = result[0]
            line = url.replace(url, "<{}>".format(url))
            print("\t"*1, url, line)
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
