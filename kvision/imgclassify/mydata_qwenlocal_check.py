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
if not os.getcwd() in sys.path: # fix linux 软连接的 bug
    sys.path.append(os.getcwd())
import time
from pythonx.funclib import *
from pythonx.pelib import *
from PIL import Image, ImageDraw, ImageFont

import os
import clip
import torch
#from torchvision.datasets import CIFAR100
import cv2
from PIL import Image
import numpy as np
import torch.nn.functional as F

QUICK = "quick" in sys.argv
DEBUG = "debug" in sys.argv
INSTALL = "install" in sys.argv
FORCE_CATE = "force" in sys.argv # 强行分类
TOPK_COUNT = 11

from mydata_Qwen2_VL_7B import run_example

"""
动漫或卡通:cartoon/文本或扫描件:text/抽象或艺术:art or abstract
风景:landscape/夜景:nightscape/建筑:building/交通工具:vehicle
人物:people/动物:animal/食物:food/植物:plant
日常物品:goods

cartoon/text/abstract
landscape/nightscape/building/vehicle
people/animal/food/plant
goods
"""

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main(dataset):

    def mainfile(fpath, fname, ftype):
        ifile = fpath # os.path.join(subdir, idir)
        if ftype in ("txt", "json", "log", "pt", "", "py"):
            return
        if ftype not in ("jpg", "jpeg", "png", "bmp",):
            assert False, ftype
            return

        print("***" * 30)
        colorPrint(ifile)

        def classification2():

            input_img = ifile
            text_input = r"""你是一个图片分类器。根据定义的图片分类及其提示词列表，请问这张图片属于哪个分类？{
    "animal": ["动物", "哺乳动物", "鸟类", "爬行动物", "鱼类", "昆虫", "野生动物", "宠物"],
    "cartoon": ["动漫", "卡通", "动画系列", "漫画", "日本漫画"], # animation
    "building": ["建筑", "建筑学", "摩天大楼", "历史建筑", "办公楼"], # architecture
    "food": ["食物", "菜肴", "餐点", "美食", "小吃", "饮料", "甜点"],
    "goods": ["商品", "产品", "货物", "消费品", "日常用品", "电视机", "电脑"], # products
    "nightscape": ["夜景", "城市灯光", "星空"],
    "people": ["人物", "肖像", "人类"],
    "plant": ["植物", "花卉", "树木", "灌木", "叶子", "植被", "灌木丛"],
    "landscape": ["风景", "自然景观", "地形", "乡村风光", "山脉", "湖泊", "海滩", "森林"], # nature
    "text": ["文本", "扫描件", "书写内容", "手稿", "屏幕截图"],
    "vehicle": ["车辆", "汽车", "自行车", "公交车", "火车", "飞机", "船", "摩托车"],
    "abstract": ["抽象艺术", "概念艺术", "现代艺术", "非具象艺术", "表现主义", "超现实主义", "极简主义"],
}"""
            model_selector = "Qwen/Qwen2-VL-7B-Instruct"
            output_text = run_example(input_img, text_input, model_selector)
            print(output_text)
            li = re.findall("animal|cartoon|building|food|goods|nightscape|people|plant|landscape|text|vehicle|abstract", output_text)
            if not li or len(li) != 1:
                return "notsure", 1.0, "notsure", 0.0
            return li[0], 1.0, "notsure", 0.0

        idx1, idv1, idx2, idv2 = classification2()
        colorPrint(idx1, idv1, idx2, idv2)

        if idv1 == "notsure":
            if not FORCE_CATE: # 没有答案就算了。
                return
            else:
                pass # 如果是 datax 就强制分类。

        if INSTALL:

            fmd5 = getFileMd5(ifile)[:16]
            rad = int(fmd5, 16) % 100

            if rad < 20:
                targetfile = os.path.join("mydata", "tempset", "val", idx1, fmd5+"_"+fname)
            else:
                targetfile = os.path.join("mydata", "tempset", "train", idx1, fmd5+"_"+fname)
            targetfile = targetfile.replace(fmd5*2, fmd5)
            fdir = os.path.dirname(targetfile)
            if not os.path.exists(fdir):
                os.makedirs(fdir)

            # OSError: cannot write mode RGBA as JPEG
            try:
                copyfile(ifile, targetfile)#image.save(targetfile)
            except OSError: # cannot write mode RGBA as JPEG
                copyfile(ifile, targetfile)
            print(targetfile)
            assert os.path.exists(targetfile), targetfile
            if not DEBUG:
                osremove(ifile)

        else: # Review
            mytype = os.path.split(os.path.split(fpath)[0])[-1]
            assert mytype in [c.split(":")[-1].strip() for c in classes] or mytype == "notsure", mytype
            if idx1 == mytype: # 如果相等，就不要再 Review 了。
                return

            ifile = os.path.abspath(ifile)
            assert ifile.find("imgclassify") != -1, ifile
            if FORCE_CATE:
                targetfile = ifile.replace("imgclassify", "imgclassifx_qwenlocal_force")
            else:
                targetfile = ifile.replace("imgclassify", "imgclassifz_qwenlocal_review")

            copyfile(ifile, targetfile)
            assert os.path.exists(targetfile), targetfile
            if not DEBUG:
                osremove(ifile)

    searchdir(dataset, mainfile)

# 还需要移除相似图片。
if __name__ == "__main__":
    #test()
    if DEBUG:
        for argv in sys.argv:
            if not os.path.isfile(argv):
                continue
            main(argv)
    elif FORCE_CATE:
        main("mydata/val")
        main("mydata/train")
        main("mydata/tempset")
    else:
        main("mydata/dataset")
    print("ok")
