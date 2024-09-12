#encoding=utf8
import re, os, sys
for reldirx, _lidir in (
        (os.path.dirname(os.path.abspath(__file__)), []), # 这个先，规避加载漏洞。
        (os.path.dirname(os.path.abspath(".")), [])):
    while not _lidir and len(reldirx) > 3: # 3 应该所有平台都问题不大。
        reldirx = os.path.dirname(reldirx) # 只尝试 funclib.py，funclib.pyc 存在版本。
        _checkfunc = lambda idir: os.path.exists(os.path.join(reldirx, idir, "pythonx", "funclib.py"))
        _lidir = [os.path.join(reldirx, idir) for idir in os.listdir(reldirx) if _checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
        del _checkfunc
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del _lidir # reldirx 可以继续使用
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
