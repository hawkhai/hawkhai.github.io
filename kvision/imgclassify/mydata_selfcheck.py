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

import sys, os
sys.path.append("/home/yqh/code/pythonx/fastai/image_classification")
sys.path.append("/home/yqh/code/pythonx/fastai/image_classification/demo")

QUICK = "quick" in sys.argv
DEBUG = "debug" in sys.argv
DATAX = "datax" in sys.argv # 强行分类
INSTALL = not DATAX # "install" in sys.argv
TOPK_COUNT = 11

def mergeTest(fpath):
    from app import classify_imagefile, classify_score
    if INSTALL:
        retraw = False # 相当于发布版本，准确度优先，否则要删除的数据就太多了。
    elif DATAX:
        retraw = True # 谨慎移除数据，删一点少一点。
    else: # Review
        retraw = True # 直接返回原始数据，否则就 Review 太多了。
    retv, maxid, maxv = classify_imagefile(fpath, retraw=retraw)
    return retv, maxid, maxv, classify_score

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main(dataset):

    def mainfile(fpath, fname, ftype):
        ifile = fpath # os.path.join(subdir, idir)
        if ftype in ("txt", "json", "log", "pt",):
            return

        print("***" * 30)
        colorPrint(ifile)
        image = Image.open(ifile)

        retv, maxid, maxv, classify_score = mergeTest(ifile)

        if INSTALL:

            fmd5 = getFileMd5(ifile)[:16]
            rad = int(fmd5, 16) % 100

            if rad < 20:
                targetfile = os.path.join("tempset", "val", maxid, fmd5+fname)
            else:
                targetfile = os.path.join("tempset", "train", maxid, fmd5+fname)
            targetfile = targetfile.replace(fmd5*2, fmd5)
            fdir = os.path.dirname(targetfile)
            if not os.path.exists(fdir):
                os.makedirs(fdir)

            # OSError: cannot write mode RGBA as JPEG
            try:
                copyfile(ifile, targetfile)#image.save(targetfile)
            except OSError: # cannot write mode RGBA as JPEG
                copyfile(ifile, targetfile)
            assert os.path.exists(targetfile), targetfile
            if not DEBUG:
                image.close()
                osremove(ifile)

        else: # Review
            mytype = os.path.split(os.path.split(fpath)[0])[-1]
            assert mytype in [c.split(":")[-1].strip() for c in classify_score.keys()], mytype
            if maxid == mytype: # 如果相等，就不要再 Review 了。
                return

            ifile = os.path.abspath(ifile)
            assert ifile.find("imgclassify") != -1, ifile
            if DATAX:
                targetfile = ifile.replace("imgclassify", "imgclassifx_self")
            else:
                targetfile = ifile.replace("imgclassify", "imgclassifz_self")

            copyfile(ifile, targetfile)
            assert os.path.exists(targetfile), targetfile
            if not DEBUG:
                image.close()
                osremove(ifile)

    searchdir(dataset, mainfile)

# 还需要移除相似图片。
if __name__ == "__main__":
    #test()
    if DATAX:
        main("datax")
    else:
        main("mydata/dataset")
    print("ok")
