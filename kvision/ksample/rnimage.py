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

def main(rootdir):
    print("ROOTDIR", rootdir)
    input("Press Enter to continue...")

    ksetk = {} # exists
    count = 0
    def mainfilep(fpath, fname, ftype, depth):
        if depth != 1: return
        if not ftype in ("png", "webp", "jpg", "jpeg",):
            return
        if re.findall("^[0-9]{3}_[0-9a-f]{5}\\.", fname):
            ksetk[fname[3:]] = fpath
            num = int(fname[:3])
            nonlocal count
            if num > count: count = num
    searchdir(rootdir, mainfilep, numnamesort=False)
    print(count, ksetk)
    #assert False

    def mainfile(fpath, fname, ftype, depth):
        if depth != 1: return
        if not ftype in ("png", "webp", "jpg", "jpeg",):
            return

        img = Image.open(fpath)
        sign = "{} {} {} {}".format(img.size, img.mode, os.path.getsize(fpath), getFileMd5(fpath))
        img.close()

        if re.findall("^[0-9]{3}_[0-9a-f]{5}\\.", fname):
            print("IGNORE", fpath)
            return

        print("FOUND", fpath)

        znamek = "_{}.{}".format(getMd5(sign)[:5], ftype)
        if znamek in ksetk:
            assert getFileMd5(fpath) == getFileMd5(ksetk[znamek]), fpath
            os.unlink(fpath)
            return

        nonlocal count
        count += 1
        zname = "{}_{}.{}".format("%03d"%count, getMd5(sign)[:5], ftype)
        print("RENAME", zname)

        imgdir, imgname = os.path.split(fpath)
        zpath = os.path.join(imgdir, zname)
        copyfile(fpath, zpath)
        os.unlink(fpath)
        # 放入。
        ksetk[zname[3:]] = zpath

    searchdir(rootdir, mainfile, numnamesort=False)

if __name__ == "__main__":
    #main(os.path.dirname(os.path.abspath(__file__)))
    main(os.path.abspath("."))
    print("ok")
