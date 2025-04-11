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
        if not fname.endswith(ftype) or fpath.find("Engine_CADF_Samples_SampleImages_") != -1:
            fdata = readfile(fpath)
            fpath = os.path.splitext(fpath)[0]+"."+ftype
            osremove(fpath)
            fpath = fpath.replace("Engine_CADF_Samples_SampleImages_", "")
            writefile(fpath, fdata)

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
