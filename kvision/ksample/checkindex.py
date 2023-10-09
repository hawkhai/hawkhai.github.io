#encoding=utf8
import re, os, sys
for reldirx, _lidir in (("./", []), (os.path.split(__file__)[0]+"/", [])):
    while not _lidir and len(reldirx) <= 100:
        reldirx += "../"
        checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = _lidir[0]
    if _lidir: break
sys.path.append(reldirx)
from pythonx.funclib import *
from PIL import Image

def mainDatamapJson(fdir, name):
    pass

def mainDatamapText(fdir, name):
    pass

typeset = set()
def mainMd5(fdir, name):
    fpath = os.path.join(fdir, name)
    lines = readfileLines(fpath)
    #01b90fd8d91802839de893282ec35dff "toyimg\hackathon\src\lib\fft.py" 9582
    for line in lines:
        li = re.findall("^([0-9a-f]{32}) \"(.*?)\" [0-9]+$", line)
        assert li, line
        imd5, ipath = li[0]
        #print(imd5, ipath)
        idir, iname = os.path.split(ipath)
        inamec, itype = os.path.splitext(iname)
        if itype.lower() in (".py", ".txt", ".json", ".png", ".jpg", ".jpeg", ".svg", ".ttf",):
            continue
        typeset.add(itype)
        print(idir, inamec, itype)

def maink():
    lines = readfileLines("checkindex.txt")
    for line in lines:
        line = line.strip()
        if not line: continue

        fdir, fname = os.path.split(line)
        print(fdir, fname)
        if fname == "datamap.json":
            mainDatamapJson(fdir, fname)

        elif fname == "datamap.txt":
            mainDatamapText(fdir, fname)

        elif fname == "datamd5.txt":
            mainMd5(fdir, fname)

        else:
            assert False, (fdir, fname)

    print(typeset)

if __name__ == "__main__":
    maink()
    print("ok")
