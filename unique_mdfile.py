#encoding=utf8
import re, os, sys
for reldirx, _lidir in (
        (os.path.split(os.path.abspath(__file__))[0]+"/", []), # 这个先，规避加载漏洞。
        (os.path.split(os.path.abspath("."))[0]+"/", [])):
    while not _lidir and len(reldirx) > 3: # 3 应该所有平台都问题不大。
        reldirx = os.path.split(reldirx)[0] # 只尝试 funclib.py，funclib.pyc 存在版本。
        _checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if _checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
        del _checkfunc
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del _lidir # reldirx 可以继续使用
from pythonx.funclib import *

def main():
    fpath = r"/Users/apple/Desktop/cfcode/blog/_posts/deep/2022-10-11-ml-DL-AndrewNg.md"
    fdata = readfile(fpath, True, "utf8")
    # ## 5 2.3 监督学习 part 2 07:17 2.3 监督学习 part 2
    li = re.findall("## ([0-9]+) ([0-9.]+ .*) ([0-9:]+) ([0-9.]+ .*)", fdata)
    for i in li:
        n, x, t, y = i
        if x == y:
            print(i)
            a = "## {} {} {} {}".format(n, x, t, y)
            b = "## {} {} {}".format(n, x, t)
            fdata = fdata.replace(a, b)

    writefile(fpath, fdata, "utf8")

if __name__ == "__main__":
    main()
