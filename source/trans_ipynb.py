#encoding=utf8
import re, os, sys
sys.path.append("../../")
from pythonx.funclib import *

def mainfile(fpath, fname, ftype):
    if not ftype in ("ipynb",):
        return
    fjson = readfileJson(fpath)

    page = ""
    cells = fjson["cells"]
    for cell in cells:
        source = cell["source"]
        page += "".join(source)

    mdfile = os.path.splitext(fpath)[0] + ".md"
    print(mdfile)
    writefile(mdfile, page)

def main():
    searchdir("d2l-zh", mainfile)

if __name__ == "__main__":
    main()
