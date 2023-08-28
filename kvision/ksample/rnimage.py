#encoding=utf8
import re, os, sys
for reldirx, _lidir in (("./", []), (os.path.split(__file__)[0]+"/", [])):
    while not _lidir and len(reldirx) <= 100:
        reldirx += "../"
        checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
        if _lidir: reldirx = _lidir[0]
    if _lidir: break
sys.path.append(reldirx)
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

        znamek = "_{}.{}".format(getmd5(sign)[:5], ftype)
        if znamek in ksetk:
            assert getFileMd5(fpath) == getFileMd5(ksetk[znamek]), fpath
            os.unlink(fpath)
            return

        nonlocal count
        count += 1
        zname = "{}_{}.{}".format("%03d"%count, getmd5(sign)[:5], ftype)
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
