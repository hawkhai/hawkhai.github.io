#encoding=utf8
import sys
import re, os, sys
sys.path.append("../")
from pythonx.funclib import *
import json

OPENFILE = "openfile" in sys.argv
#IGNORE_CONFIG = readfileJson(os.path.join("config", "ignore_config.txt"))

def regularTitle(fpath):
    title = getPostValue(fpath, "title")
    categories = getPostValue(fpath, "categories")
    print(title, categories)
    categories = json.loads(categories)
    category = categories[0]
    regex = "^.*?{}.*? --( |《)[^《]".format(category)
    if getPostValue(fpath, "titlecheck"):
        return
    if not re.findall(regex, title):
        openTextFile(fpath)
        assert False, regex

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

def mainxtitle():
    print(parsePythonCmdx(__file__))
    fnamelist = []
    def mainfile(fpath, fname, ftype):
        if ftype in ("py",): return
        if ftype in ("mdtag",): return
        if fpath.endswith(".spaceback.json"):
            return
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

def analyzehead(fpath, fname, ftype, newmap):
    fpath = os.path.relpath(fpath, ".")
    print(fpath)
    if fpath.startswith("_posts\\"):
        pass
    elif fpath.startswith("invisible\\"):
        pass
    else:
        assert fpath in ("about.md", "bookshelf.md", "index.md", "disclaimer.md"), fpath

    if not newmap["categories"] or not newmap["tags"]:
        openTextFile(fpath)

gkvmap = {}
def formatkv(fpath, fname, ftype, fsecli, setkv={}):
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
layoutclear titlecheck
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
            assert len(fpath.split("invisible")) == 2, fpath
            magic = normalPath(fpath).split("invisible\\")[-1].split("\\")

            # date: 2021-02-06 15:29:00 +0800
            pWordSize = 3
            def calcSignHalf(name):
                intv = 0
                count = 0
                while name and count < pWordSize:
                    intv = (intv << 8) + ord(name[0])
                    name = name[1:]
                    count = count + 1
                intv = intv >> (4 * pWordSize)
                assert(intv <= 0xffffff, "%x" % intv)
                return intv & 0xffffff
            intsign = 0
            while magic:
                intsign = (intsign << int(pWordSize * 8 / 2)) + calcSignHalf(magic[0])
                magic = magic[1:]
            value = "{} +0800".format(formatTimeStamp(intsign))

            frelgit = os.path.relpath(fpath, ".")
            cmdx = '''cd {} & git log -n 10000 --pretty=format:"%ad" --date=format:%Y-%m-%d_%H:%M:%S -- "{}"'''.format(*frelgit.split("\\", 1))
            datestr = popenCmd(cmdx)
            datestr = bytesToString(datestr)
            # date: 1970-03-23 20:17:42 +0800
            datestr = datestr.replace("_", " ")
            datestr = datestr.strip().split("\n")[-1]
            assert datestr, frelgit
            #assert False, (datestr, frelgit)
            value = "{} +0800".format(datestr)

            print(magic, value)
        if not key in igkeylist:
            assert key in mdkeylist, line
        else:
            mdkeylist.append(key)
        kvmap[key] = value
        if not key in gkvmap.keys():
            gkvmap[key] = []

        def appvalue(value):
            if value and not value in gkvmap[key]:
                gkvmap[key].append(value)

        if value:
            if value.startswith("\"") and value.endswith("\""):
                value = value[1:-1]
                appvalue(value)
            elif value.startswith("["):
                for val in json.loads(value):
                    appvalue(val)
            elif re.findall("^[a-z]+$", value):
                appvalue(value)
            elif key in ('title', 'permalink', 'date', 'author'):
                appvalue(value)
            else:
                assert False, (key, value)

    newli = []
    newmap = {}
    for key in mdkeylist:
        value = kvmap[key] if key in kvmap else ""
        if key in setkv.keys():
            value = setkv[key]
        line = key + ": " + value.strip()
        newli.append(line.strip())
        newmap[key] = value.strip()
    analyzehead(fpath, fname, ftype, newmap)
    return "\r\n".join(newli), newmap

def parseHeadKeyValueRaw(fpath, fname, ftype):
    if ftype not in ("md",):
        return
    fdata = readfile(fpath, True, "utf8")

    fsecli = fdata.split("---", 2)
    if len(fsecli) <= 2 or len(fsecli[0]) > 3: return
    return fsecli

def parseHeadKeyValue(fpath, fname, ftype):
    fsecli = parseHeadKeyValueRaw(fpath, fname, ftype)
    if not fsecli: return
    return formatkv(fpath, fname, ftype, fsecli[1])[1]

gkvconfig = readfileJson("config/headnote.json", "utf8")
gkvconfig = gkvconfig if gkvconfig else {}
def mainxkeyfile(fpath, fname, ftype, depth=-1, setkv={}):
    if ftype in ("mdtag",): return
    if fpath.endswith(".spaceback.json"):
        return

    fpath = os.path.relpath(fpath, ".")
    fsecli = parseHeadKeyValueRaw(fpath, fname, ftype)
    if not fsecli: return

    if OPENFILE:
        openTextFile(fpath)

    mdtagfile = (fpath+".tag").replace(".md.tag", ".mdtag").replace("-", "")
    #writefile(mdtagfile, "")
    fsecli[1] = "\r\n{}\r\n".format(formatkv(fpath, fname, ftype, fsecli[1], setkv)[0],)

    fsecli = "---".join(fsecli)
    writefile(fpath, fsecli, "utf8")
    if not fpath in gkvconfig.keys():
        gkvconfig[fpath] = { "taged": False }

def mainxkey():
    print("***" * 30)
    searchdir(".", mainxkeyfile, ignorelist=("backup", "_site", "_drafts", "opengl-3rd"))
    writefileJson("config/headnote.json", gkvconfig)

    nctrl = {
        "title": 2,
        "date": 2,
    }

    headnote = {}
    for key in gkvmap.keys():
        gkvmap[key].sort()
        ctrln = 1000
        if key in nctrl.keys():
            ctrln = nctrl[key]
        key, value = key, gkvmap[key]

        testset = set()
        for tt in value:
            testset.add(tt.lower())
        assert len(testset) == len(value), (key, value)

        key, value = key, gkvmap[key][:ctrln]
        print(key, value, "..." if len(gkvmap[key]) > ctrln else "")
        headnote[key] = value
    # (path, data, encoding="ISO8859-1", ascii=True):
    writefileJson("config/headnote.txt", headnote, "utf8", False)

if __name__ == "__main__":
    mainxtitle()
    mainxkey()
    print(parsePythonCmdx(__file__))
    os.system(r"cd invisible & {} tempd.py encrypt".format(getPythonExe(),))
