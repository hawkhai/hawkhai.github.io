#encoding=utf8
import re, os, sys
for reldirx, _lidir in (
        (os.path.dirname(os.path.abspath(__file__)), []), # 这个先，规避加载漏洞。
        (os.path.dirname(os.path.abspath(".")), [])):
    while not _lidir and len(reldirx) > 3: # 3 应该所有平台都问题不大。
        reldirx = os.path.dirname(reldirx) # 只尝试 funclib.py，funclib.pyc 存在版本。
        _checkfunc = lambda idir: os.path.exists(os.path.join(reldirx, idir, "pythonx", "funclib.py"))
        _lidir = [os.path.join(reldirx, idir) for idir in os.listdir(reldirx) if _checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
        del _checkfunc
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del _lidir # reldirx 可以继续使用
from pythonx.funclib import *
from PIL import Image
import cv2

# 最终 png 文件能控制在 5 MB 左右。
def resize_image(image, output_image_path, size=(1754, 1754)): # 1241 x 1754
    #with Image.open(input_image_path) as image:
    
    # 获取原始图片的宽度和高度
    width, height = image.size
    
    # 检查是否需要调整大小
    if width > size[0] or height > size[1]:
        # 计算新的尺寸以保持原始宽高比
        if width > height:
            new_width = size[0]
            new_height = int(height * (new_width / width))
        else:
            new_height = size[1]
            new_width = int(width * (new_height / height))
        
        # 使用高质量的重采样滤波器调整图片大小
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
    
        # 保存调整后的图片
        image.save(output_image_path)

def main(rootdir):
    print("ROOTDIR", rootdir)

    def mainfile(fpath, fname, ftype, depth):
        try:
            assert ftype not in ("webp", "jfif",)
            img = Image.open(fpath)
            if img.size[0] * img.size[1] > 1241 * 1754:
                resize_image(img, fpath)
                print(fpath)
            return
        except Exception as ex:
            print(ex, fpath)
            
        tmpfile = "tempfile.png"
        copyfile(fpath, tmpfile)
        try:
            image = cv2.imread(tmpfile)
        except Exception as ex:
            print(ex, fpath)
            return
        
        if type(image) == type(None) or not image.any():
            return
        
        cv2.imwrite(tmpfile, image)
        copyfile(tmpfile, os.path.splitext(fpath)[0]+".png")
        colorPrint(fpath)
        osremove(fpath)
        osremove(tmpfile)

    searchdir(rootdir, mainfile, numnamesort=False)

if __name__ == "__main__":
    #main(os.path.dirname(os.path.abspath(__file__)))
    main(r"E:\kSource\blog\kvision\ksample\dewarp")
    main(r"E:\kSource\blog\kvision\ksample\testimg")
    main(r"E:\kSource\blog\kvision\ksample\myocr")
    print("ok")
