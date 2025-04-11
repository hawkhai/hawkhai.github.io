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

import requests
import base64

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main():

    imgdirs = [
        r"E:\kSource\blog\kvision\imgclassify\mydata\val",
        r"E:\kSource\blog\kvision\imgclassify\mydata\train",
    ] if IS_WINDOWS else [
        r"/home/yqh/code/blog/kvision/imgclassify/mydata/val",
        r"/home/yqh/code/blog/kvision/imgclassify/mydata/train",
    ]

    valdir, traindir = imgdirs
    if "datax" in sys.argv:
        valdir = valdir.replace("mydata", "mydatax")
        traindir = traindir.replace("mydata", "mydatax")
    trains = [i for i in os.listdir(traindir) if os.path.isdir(os.path.join(traindir, i))]
    vals   = [i for i in os.listdir(valdir) if os.path.isdir(os.path.join(valdir, i))]

    trains.sort()
    vals.sort()
    print(trains)
    print(vals)
    assert len(trains) == len(vals)

    for idir in trains:
        traincnt, valcnt = (len(os.listdir(os.path.join(traindir, idir))),
                            len(os.listdir(os.path.join(valdir, idir))))
        total = traincnt + valcnt
        print("%12s"%idir, "|", "%4d"%traincnt, "|", "%4d"%valcnt, "|", "%4d"%total, "|", "%.2f"%(valcnt/total))

if __name__ == "__main__":
    main()
