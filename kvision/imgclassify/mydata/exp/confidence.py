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

def main():
    def mainfile(fpath, fname, ftype):
        if fname not in "resultconfidence.json".split():
            return

        fjson = readfileJson(fpath)
        print("x,", end=" ")
        for i in range(101):
            print("%d"%i + ",", end=" ")
        print()

        for key in fjson.keys():
            print(key + ",", end=" ")
            val = fjson[key]
            vkeys = val.keys()

            for i in range(101):
                okcnt, errcnt = 0, 0
                total = 0
                for vkey in vkeys:
                    total += val[vkey]["ok"] + val[vkey]["err"]
                    if float(vkey) * 100 >= i:
                        okcnt += val[vkey]["ok"]
                        errcnt += val[vkey]["err"]
                if okcnt + errcnt == 0:
                    print("0" + ",", end=" ")
                else:
                    print("%.2f"%round(okcnt / (okcnt + errcnt), 3) + ",", end=" ")

            print()

    searchdir(".", mainfile)

if __name__ == '__main__':
    main()
    print("ok")
