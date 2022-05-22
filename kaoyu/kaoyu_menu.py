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

total = 30
subnum = 3

def mainsplit(rootdir, imgpath, num):
    width = 3174
    height = 4490
    twidth = int(width * 2 / 3)
    theight = height
    base = num * subnum

    targetimg = Image.new(mode="RGB", size=(twidth * subnum, theight), color="#FFFFFF")
    for i in range(subnum):
        srcimg = Image.open(rootdir+ (imgpath % (base+i + 1)))
        img = srcimg.crop((int(width/6), 0, int(width * 5 / 6), height))
        targetimg.paste(img, (twidth*i, 0))
    targetimg = targetimg.resize((int(6348/2), int(4490/2)))
    targetimg.save(rootdir+ ("kz\\.%d.jpg" % num))

if __name__ == "__main__":
    for i in range(int(total/subnum)):
        mainsplit(r"D:\kSource\blog\现杀现烤 _ 重庆烤鱼·扎啤\\", r"现杀现烤 _ 重庆烤鱼·扎啤_%d.png", i)
