#encoding=utf8
import re, os, sys
reldirx, _lidir = "", []
while not _lidir and len(reldirx) <= 100:
    reldirx += "../"
    checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
    _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
    if _lidir: reldirx = _lidir[0]
sys.path.append(reldirx)
from pythonx.funclib import *

from PIL import Image

total = 12
subnum = 3

targetmap = [
[( 1, 20), ( 2, 19), ( 3, 18)], [( 4, 17), ( 5, 16), (-1, -1)],
[( 6, 25), ( 7, 24), ( 8, 23)], [( 9, 22), (10, 21), (-1, -1)],
[(11, 30), (12, 29), (13, 28)], [(14, 27), (15, 26), (-1, -1)],
]

def mainsplit(rootdir, imgpath, num):
    width = 3174
    height = 4490
    twidth = int(width * 2 / 3)
    theight = height
    base = num * subnum

    assert abs(twidth / theight - 140 / 297) <= 0.01, (twidth, theight)

    targetimg = Image.new(mode="RGB", size=(twidth * subnum, theight), color="#FFFFFF")
    for i in range(subnum):
        srcimg = Image.open(rootdir+ (imgpath % (base+i + 1)))
        tmpimg = srcimg.crop((int(width/6), 0, int(width * 5 / 6), height))
        targetimg.paste(tmpimg, (twidth*i, 0))

    print(targetimg.size)
    # 210mm×297mm  2479×3508
    # 420mm×297mm  4960×3508
    resize = (round(3508*140*3/297), 3508)
    print(resize)
    targetimg = targetimg.resize(resize)
    # https://www.bilibili.com/read/cv10342533
    targetimg = targetimg.convert("CMYK")
    targetpath = rootdir+ ("kz\\rst.%d.jpg" % num)
    writefile(targetpath, "")
    osremove(targetpath)
    targetimg.save(targetpath, "jpeg")

if __name__ == "__main__":
    for idx in range(int(total/subnum)):
        mainsplit(r"C:\kSource\blog\kaoyu\现杀现烤 _ _br__重庆烤鱼·猪肚鸡\\",
                  r"现杀现烤 _ _br__重庆烤鱼·猪肚鸡_%d.png", idx)
