#encoding=utf8
import re, os, sys
from pathlib import Path
check_pythonx_dir = lambda x: x and os.path.exists(os.path.join(x, "funclib.py"))
check_ksource_dir = lambda x: x and check_pythonx_dir(os.path.join(x, "pythonx"))
for reldirx in (os.path.dirname(os.path.abspath(__file__)), # 这个先，规避加载漏洞。
                os.path.abspath(".")):
    while len(reldirx) > 3: # 3 应该所有平台都问题不大。
        if check_ksource_dir(reldirx): break # YES!!
        reldirx = os.path.dirname(reldirx) # 只尝试 funclib.py，funclib.pyc 存在版本问题。
    if check_ksource_dir(reldirx): break # YES!!
for devdirx in [r"E:\kSource", r"D:\kSource", r"C:\kSource"]:
    if not check_ksource_dir(reldirx):
        reldirx = devdirx
if check_ksource_dir(reldirx) and not reldirx in sys.path:
    sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del devdirx # reldirx 可以继续使用
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
