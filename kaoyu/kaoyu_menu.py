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

    targetimg = Image.new(mode="CMYK", size=(twidth * subnum, theight), color="#FFFFFFFF")
    for i in range(subnum):
        srcimg = Image.open(rootdir+ (imgpath % (base+i + 1)))
        tmpimg = srcimg.crop((int(width/6), 0, int(width * 5 / 6), height))
        targetimg.paste(tmpimg, (twidth*i, 0))

    print(targetimg.size, targetimg.mode)
    # 210mm×297mm  2479×3508
    # 420mm×297mm  4960×3508
    resize = (round(3508*140*3/297), 3508)
    print(resize)
    targetimg = targetimg.resize(resize)

    #from PIL import ImageFont, ImageDraw # 导入模块
    #draw = ImageDraw.Draw(targetimg, "CMYK") # 修改图片
    #font = ImageFont.truetype(r"..\..\assets\logos\方正楷体_GB2312.ttf", size = 100)
    #draw.text((theight / 2, twidth), u'{}/{}'.format(num+1, 4), fill="white", font=font)

    # https://www.bilibili.com/read/cv10342533
    #targetimg = targetimg.convert("CMYK")
    targetpath = rootdir+ ("kz\\rst.%d.jpg" % num)
    writefile(targetpath, "")
    osremove(targetpath)
    targetimg.save(targetpath, "jpeg")
    print("save", targetimg.mode)

if __name__ == "__main__":
    for idx in range(int(total/subnum)):
        mainsplit(r"E:\kSource\blog\kaoyu\现杀现烤 _ _br__重庆烤鱼·猪肚鸡\\",
                  r"现杀现烤 _ _br__重庆烤鱼·猪肚鸡_%d.png.cmyk.jpg", idx)
