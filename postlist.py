#encoding=utf8
import re, os, sys
sys.path.append("../")
from pythonx.funclib import *
import json

def regularTitle(fpath):
    """
---
layout: post
title: "Windows 跨模块内存管理"
location: "珠海"
categories: ["编程"]
tags: [Windows Prog, Memory, C++]
toc: true
---
    """
    title = getPostValue(fpath, "title")
    categories = getPostValue(fpath, "categories")
    print(title, categories)
    categories = json.loads(categories)
    category = categories[0]
    regex = "^.*?{}.*? --( |《)[^《]".format(category)
    assert re.findall(regex, title), regex

def getPostValue(fpath, xkey):
    fdata = readfile(fpath).decode("utf8")
    fdata = fdata.split("---")[1]
    for line in fdata.split("\n"):
        line = line.strip()
        if not line: continue
        key, value = line.split(":", 1)
        if key == xkey:
            return value.strip()
    return None

def main():
    print(parsePythonCmdx(__file__))
    fnamelist = []
    def mainfile(fpath, fname, ftype):
        regularTitle(fpath)
        # print(fname[11:])
        fnamelist.append("%-64s"%fname[11:] + "\t" + getPostValue(fpath, "title"))
    searchdir("_posts", mainfile)

    fnamelist.sort()
    print("\n".join(fnamelist))

if __name__ == "__main__":
    main()
