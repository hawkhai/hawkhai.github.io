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
