#encoding=utf8
import re, os, sys
for reldirx, _lidir in (("./", []), (os.path.split(__file__)[0]+"/", [])):
    while not _lidir and len(reldirx) <= 100:
        reldirx += "../"
        checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx)
from pythonx.funclib import *

from PIL import Image

def copyimg(xfile, yfile):
    img = Image.open(xfile)
    print(img.size, xfile)
    #img.save(yfile)
    width, height = img.size
    ratio = 1.0
    while width * height * ratio * ratio > 256 * 256:
        ratio *= 0.99
    width = round(width * ratio)
    height = round(height * ratio)
    img = img.resize((width, height))
    if img.mode != "RGB":
        img = img.convert("RGB")

    img.save(yfile)
    print(img.size, yfile)

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir2(srcdir, dstdir):
    statx = {}
    config = readfileJson("scene_categories.json")
    def mainfile(fpath, fname, ftype):

        subdir = config[fname]
        if not subdir in statx:
            statx[subdir] = 0
        statx[subdir] = statx[subdir] + 1

        ifile = os.path.relpath(fpath, srcdir)
        assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
        xfile = os.path.join(srcdir, ifile)
        md5 = getFileMd5(xfile)[:7]

        mydir = os.path.join(dstdir, "cadb_"+subdir)
        yfile = os.path.join(mydir, md5+"."+ftype)
        yfile2 = os.path.join(mydir, "cadb_"+md5+"."+ftype)
        if os.path.exists(yfile):
            os.rename(yfile, yfile2)
            return
        yfile = yfile2

        if os.path.exists(yfile):
            return
        if not os.path.exists(mydir):
            os.makedirs(mydir)

        copyimg(xfile, yfile)

    searchdir(srcdir, mainfile)
    print(srcdir)
    print(statx)
    print()

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir(srcdir, dstdir):
    statx = {}
    def mainfile(fpath, fname, ftype):
        if not ftype in statx:
            statx[ftype] = 0
        statx[ftype] = statx[ftype] + 1

        ifile = os.path.relpath(fpath, srcdir)
        assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
        xfile = os.path.join(srcdir, ifile)
        md5 = getFileMd5(xfile)[:7]

        yfile = os.path.join(dstdir, md5+"."+ftype)
        yfile2 = os.path.join(dstdir, "pp_"+md5+"."+ftype)
        if os.path.exists(yfile):
            os.rename(yfile, yfile2)
            return
        yfile = yfile2

        if os.path.exists(yfile):
            return
        if not os.path.exists(dstdir):
            os.makedirs(dstdir)

        copyimg(xfile, yfile)

    searchdir(srcdir, mainfile)
    print(srcdir)
    print(statx)
    print()

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def checkimg(rootdir):
    def mainfile(fpath, fname, ftype):
        if ftype in ("txt", "json"):
            return
        img = Image.open(fpath)
        width, height = img.size
        if width / height < 1/3 or height / width < 1/3:
            img.close()
            os.remove(fpath)
            print("REMOVE", (width, height), fpath)

    searchdir(rootdir, mainfile)
    
def main():
    if False:
        copydir(r"D:\BaiduNetdiskDownload\dataset\animals",   r"dataset\animal")
        copydir(r"D:\BaiduNetdiskDownload\dataset\food",      r"dataset\food")
        copydir(r"D:\BaiduNetdiskDownload\dataset\people",    r"dataset\people")
        copydir(r"D:\BaiduNetdiskDownload\dataset\scenery",   r"dataset\scenery")
        copydir(r"D:\BaiduNetdiskDownload\dataset\text",      r"dataset\text")

    if False:
        copydir2(r"D:\BaiduNetdiskDownload\CADB_Dataset\images", r"dataset")

    checkimg(r"dataset")

if __name__ == "__main__":
    main()
