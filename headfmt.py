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
    fdata = readfile(fpath, True, "utf8")
    if len(fdata.split("---")) <= 1:
        print(fpath)
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
        if ftype in ("py",): return
        regularTitle(fpath)
        # print(fname[11:])
        fnamelist.append("%-64s"%fname[11:] + "\t" + getPostValue(fpath, "title"))
    searchdir("_posts", mainfile)

    fnamelist.sort()
    print("\r\n".join(fnamelist))

def formatValue(value):
    if not value: return value
    if value[0] != "[": return value
    try:
        json.loads(value)
        return value
    except:
        print(value)
        assert value[0] == "[" and value[-1] == "]", value
        value = value[1:-1].split(",")
        return "[{}]".format(", ".join(["\"{}\"".format(i.strip()) for i in value]))

gkvmap = {}
def formatkv(fpath, fname, ftype, fsecli):
    li = [line.strip() for line in fsecli.split("\n") if line.strip()]

    _posts = "_posts" in fpath.split("\\")
    mdkeylist = """
layout title author location
categories tags toc toclistyle
comments visibility
mathjax mermaid glslcanvas
codeprint
""".split()
    if not _posts:
        mdkeylist.extend("""
permalink
""".split())
    igkeylist = """
l2dwidget cluster
sortrefs archived date
""".split()

    kvmap = {}
    for line in li:
        if len(line.split(":", 1)) == 1:
            print(fpath)
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        value = formatValue(value)
        if key == "date":
            assert re.findall("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} \\+[0-9]{4}$", value), value
        if not key in igkeylist:
            assert key in mdkeylist, line
        else:
            mdkeylist.append(key)
        kvmap[key] = value
        if not key in gkvmap.keys():
            gkvmap[key] = []
        if value and not value in gkvmap[key]:
            gkvmap[key].append(value)
    newli = []
    for key in mdkeylist:
        value = kvmap[key] if key in kvmap else ""
        line = key + ": " + value.strip()
        newli.append(line.strip())
    return "\r\n".join(newli)

def mainxkeyfile(fpath, fname, ftype):
    if ftype not in ("md",):
        return
    fdata = readfile(fpath, True, "utf8")

    fsecli = fdata.split("---", 2)
    if len(fsecli) <= 2 or len(fsecli[0]) > 3: return

    fsecli[1] = "\r\n{}\r\n".format(formatkv(fpath, fname, ftype, fsecli[1]),)

    fsecli = "---".join(fsecli)
    writefile(fpath, fsecli, "utf8")

def mainxkey():
    print("***" * 30)
    searchdir(".", mainxkeyfile, ignorelist=("backup", "_site", "_drafts", "opengl-3rd"))

    headnote = []
    for key in gkvmap.keys():
        key, value = key, gkvmap[key][:5]
        print(key, value, "..." if len(gkvmap[key]) > 5 else "")
        headnote.append("{} {}".format(key, value))
    writefile("headnote.txt", "\r\n".join(headnote), "utf8")

if __name__ == "__main__":
    main()
    mainxkey()
