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
if not os.getcwd() in sys.path: # fix linux 软连接的 bug
    sys.path.append(os.getcwd())
import time
from pythonx.funclib import *

# filelist -> ((localfile, arcname), (localfile, arcname))
#               arcname -> a\b\c.txt
# ktouch   -> strict_timestamps=2000
# note: remove argv modifyTime(zipName, filelist, modifyTime=None, ktouch=True)
#def gzipflist(zipName, filelist, ktouch=True):
def main():
    rootdir = os.path.split(os.path.abspath(__file__))[0]
    zipName = os.path.join(rootdir, "mytable_sample.zip")

    filelist = []
    rootdir = r"E:\kSource\blog\kvision\ksample\mytable"
    dirs = os.listdir(rootdir)
    dirs.sort()
    for dir in dirs:
        type = dir.split(".")[-1]
        if not type in ("jpg", "png", "jpeg"):
            continue
        fpath = os.path.join(rootdir, dir)
        fname = dir.split(".")[0]
        print(fpath)

        filelist.append([os.path.join(rootdir, dir), dir])
        filelist.append([os.path.join(rootdir, fname+".xlsx"), fname+"_WPS.xlsx"])
        filelist.append([os.path.join(rootdir, "table-recognition", fname+"result.xlsx"), fname+"_CF.xlsx"])

    print("gzipflist", zipName)
    gzipflist(zipName, filelist)

if __name__ == "__main__":
    main()
