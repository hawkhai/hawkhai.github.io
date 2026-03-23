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
