#encoding=utf8
import re, os, sys
reldirx, _lidir = "", []
while not _lidir and len(reldirx) <= 100:
    reldirx += "../"
    checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
    _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
    assert len(_lidir) in (0, 1), _lidir
    if _lidir: reldirx = os.path.abspath(_lidir[0])
if not reldirx in sys.path: sys.path.append(reldirx)
from pythonx.funclib import *

from PIL import Image

def mainsplit(rootdir):
    count = 0
    for tdir in os.listdir(rootdir):
        if not tdir.endswith(".jpg"):
            continue
        fpath = os.path.join(rootdir, tdir)
        image = Image.open(fpath)
        width, height = image.size
        assert width % 3 == 0 and height % 3 == 0, (width, height, fpath)
        w, h = int(width / 3), int(height / 3)
        for j in range(3):
            for i in range(3):
                x0, y0 = i*w, j*h
                x1, y1 = i*w+w, j*h+h
                img = image.crop((x0, y0, x1, y1))
                count += 1
                local = os.path.join("menu", "%02d.png"%(count))
                #img.save(local)
                subimg = Image.open(local)
                image.paste(subimg, (x0, y0))
        image.save(fpath)
    print(count)

if __name__ == "__main__":
    mainsplit(r"C:\kSource\blog\invisible\kaoyu")
