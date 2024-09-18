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
FORCE_CATE = "force" in sys.argv # 强行分类
INSTALL = not FORCE_CATE # "install" in sys.argv
TOPK_COUNT = NUM_CLASSES

# https://blog.csdn.net/qq_40243750/article/details/125545964
# https://blog.csdn.net/juluwangriyue/article/details/118082260
import tensorflow as tf

# 加载 TFLite 模型
interpreter = tf.lite.Interpreter(model_path="mydata/exp/aimodel/pic_recommend_local_pc/pic_recommend_model.tflite")
interpreter.allocate_tensors()

# 获取输入和输出张量的详细信息
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 定义预处理函数
def preprocess_image(image_path, input_shape):
    img = Image.open(image_path).convert("RGB").resize((input_shape[1], input_shape[2]))
    img = np.array(img).astype(np.float32)  # 模型要求浮点32类型
    img = img / 255.0  # 归一化至 [0, 1]
    img = np.expand_dims(img, axis=0)  # 增加 batch 维度
    return img

# 进行推理
def run_inference(image_path):
    # 加载和预处理图片
    input_shape = input_details[0]['shape']
    img = preprocess_image(image_path, input_shape)

    # 设置模型输入
    interpreter.set_tensor(input_details[0]['index'], img)

    # 执行推理
    interpreter.invoke()

    # 获取输出数据
    output_data = interpreter.get_tensor(output_details[0]['index'])

    return output_data

# 调用推理函数，打印输出
def print_output(output):
    #output = run_inference(image_path)

    categories = r"""animal
text
people
landscape
other
cartoon""".split()

    # 获取分类及其对应概率
    retv = {}
    for i, score in enumerate(output[0]):
        #print(f"{categories[i]}: {score:.4f}")
        retv[categories[i]] = float(score)

    # 找出概率最大的类别
    predicted_index = np.argmax(output[0])
    predicted_category = categories[predicted_index]
    confidence = output[0][predicted_index]

    print(f"\nPredicted category: {predicted_category} (confidence: {confidence:.4f})")
    return retv, predicted_category, float(confidence)


def mergeTest(fpath):
    from app import classify_imagefile
    if INSTALL:
        retraw = False # 相当于发布版本，准确度优先，否则要删除的数据就太多了。
    elif FORCE_CATE:
        retraw = True # 谨慎移除数据，删一点少一点。
    else: # Review
        retraw = True # 直接返回原始数据，否则就 Review 太多了。
    #retv, maxid, maxv = classify_imagefile(fpath, retraw=retraw)

    # 调用推理函数，打印输出
    output = run_inference(fpath)
    retv, maxid, maxv = print_output(output)

    return retv, maxid, maxv

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main(dataset):

    def mainfile(fpath, fname, ftype):
        ifile = fpath # os.path.join(subdir, idir)
        if ftype in ("txt", "json", "log", "pt",):
            return

        print("***" * 30)
        colorPrint(ifile)
        image = Image.open(ifile)

        retv, maxid, maxv = mergeTest(ifile)

        if INSTALL:

            fmd5 = getFileMd5(ifile)[:16]
            rad = int(fmd5, 16) % 100

            if rad < 20:
                targetfile = os.path.join("mydata", "tempset", "val", maxid, fmd5+"_"+fname)
            else:
                targetfile = os.path.join("mydata", "tempset", "train", maxid, fmd5+"_"+fname)
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
            assert mytype in "animal|text|people|landscape|other|cartoon".split("|"), mytype
            if maxv < 0.80:
                maxid = "notsure"
            if maxid == mytype: # 如果相等，就不要再 Review 了。
                return

            ifile = os.path.abspath(ifile)
            assert ifile.find("imgclassify") != -1, ifile
            if FORCE_CATE:
                targetfile = ifile.replace("imgclassify", "imgclassifx_self_force")
            else:
                targetfile = ifile.replace("imgclassify", "imgclassifz_self_review")

            copyfile(ifile, targetfile)
            assert os.path.exists(targetfile), targetfile
            if not DEBUG:
                image.close()
                osremove(ifile)

    searchdir(dataset, mainfile)

# 还需要移除相似图片。
if __name__ == "__main__":
    #test()
    if FORCE_CATE:
        main("mydatax")
    else:
        main("mydata/dataset")
    print("ok")
