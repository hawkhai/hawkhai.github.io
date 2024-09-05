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

QUICK = "quick" in sys.argv
DEBUG = "debug" in sys.argv
INSTALL = "install" in sys.argv
DATAX = "datax" in sys.argv
TOPK_COUNT = 11

# 官网推荐的 'ViT-B/32'
# ViT-L/14 35.9M 1.71GB
# ViT-B/32 21.6M 605MB
# ViT-B/16 17.6M 598MB
# C:\Users\hawkhai\.cache\clip\ViT-L-14.pt 910MB
# C:\Users\hawkhai\.cache\clip\ViT-B-32.pt 345MB
DEVAULTV_CLIP   = ('ViT-B/32', "ViT-L/14") # 345MB / 910MB
# 官网推荐的 "ViT-B-16"
# ViT-L-14 28.4K 1.63GB
# ViT-B-16 19.9K 753MB
# D:\kSource\blog\kvision\imgclassify\clip_cn_vit-l-14.pt 1587MB
# D:\kSource\blog\kvision\imgclassify\clip_cn_vit-b-16.pt 735MB
DEVAULTV_CNCLIP = ('ViT-B-16', "ViT-L-14") # 735MB / 1587MB

# https://github.com/openai/clip
# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load(DEVAULTV_CLIP[0 if QUICK else 1], device)

# https://github.com/OFA-Sys/Chinese-CLIP
import cn_clip.clip as cn_clip
from cn_clip.clip import load_from_name, available_models
print("Available models:", available_models())
# Available models: ['ViT-B-16', 'ViT-L-14', 'ViT-L-14-336', 'ViT-H-14', 'RN50']

# os.path.expanduser("~/.cache")
dlrootdir = os.path.split(os.path.abspath(__file__))[0]
model_cn, preprocess_cn = load_from_name(DEVAULTV_CNCLIP[0 if QUICK else 1], device=device, download_root=dlrootdir)
model_cn.eval()

def test():
    from torchvision.datasets import CIFAR100

    # Download the dataset
    cifar100 = CIFAR100(root=dlrootdir, download=True, train=False)

    # Prepare the inputs
    image, class_id = cifar100[3637]
    print(type(image), class_id)
    image_input = preprocess(image).unsqueeze(0).to(device)
    text_inputs = torch.cat([clip.tokenize(f"a image of a {c}") for c in cifar100.classes]).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(TOPK_COUNT)

    # Print the result
    #print("\nTop predictions:\n")
    for value, index in zip(values, indices):
        print(f"{cifar100.classes[index]:>16s}: {100 * value.item():.2f}%")

def getMaxKV(retmap, retdb=False):

    keys = [k for k in retmap.keys()]
    #assert len(keys) in (5, 12), keys
    keys.sort()
    vals = [retmap[k] for k in keys]

    if DEBUG:
        print("===" * 30)
        for key in keys:
            print("%8s"%key, "-"*int(retmap[key]*100), "%.8f"%retmap[key])

    valsk = vals[:]
    valsk.sort()
    valsk = valsk[::-1]
    if retdb:
        return keys[vals.index(valsk[0])], valsk[0], keys[vals.index(valsk[1])], valsk[1]
    return keys[vals.index(valsk[0])], valsk[0]

def mergeTest(retmap1, retmap2):
    assert len(retmap1) == len(retmap2)
    retmap = {}
    for key in retmap1.keys():
        retmap[key] = (retmap1[key] + retmap2[key]) / 2
    colorPrint("mergeTest", color="yellow")
    # 合并后，第一名 >= 0.5，第二名 < 0.4
    return getMaxKV(retmap, True)

# Download the dataset
#cifar100 = CIFAR100(root=os.path.expanduser("~/.cache"), download=True, train=False)
def cateclip(image, classes):
    # Prepare the inputs
    #image, class_id = cifar100[3637]
    image_input = preprocess(image).unsqueeze(0).to(device)

    classe_ids = [c.split(":")[-1].strip() for c in classes]
    classes = [c.split(":")[0].strip() for c in classes]
    #print(classe_ids)
    #print(classes)
    text_inputs = torch.cat([clip.tokenize(f"a image of a {c}") for c in classes]).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(TOPK_COUNT)

    # Print the result
    #print("\nTop predictions:\n")
    retmap = {}
    for value, index in zip(values, indices):
        #print(f"{classes[index]:>16s}: {100 * value.item():.2f}%")
        #return classe_ids[index], value.item()
        if not classe_ids[index] in retmap:
            retmap[classe_ids[index]] = 0
        retmap[classe_ids[index]] += value.item()

    return getMaxKV(retmap), retmap

def cateclip_cn(image, classes):

    classe_ids = [c.split(":")[-1].strip() for c in classes]
    classes = [c.split(":")[0].strip() for c in classes]

    #print(classe_ids)
    #print(classes)
    image = preprocess(image).unsqueeze(0).to(device)
    text = cn_clip.tokenize([f"一张 {c} 图片" for c in classes]).to(device)

    with torch.no_grad():
        image_features = model_cn.encode_image(image)
        text_features = model_cn.encode_text(text)
        # 对特征进行归一化，请使用归一化后的图文特征用于下游任务
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        logits_per_image, logits_per_text = model_cn.get_similarity(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    # 创建一个 numpy 数组
    float_array = np.array(probs[0])
    # 找到最大值
    max_value = np.max(float_array)
    # 找到最大值的索引
    max_index = np.argmax(float_array)
    #print("Label probs:", probs)  # [[1.268734e-03 5.436878e-02 6.795761e-04 9.436829e-01]]
    #return classe_ids[max_index], max_value
    retmap = {}
    for index, value in enumerate(probs[0]):
        if not classe_ids[index] in retmap:
            retmap[classe_ids[index]] = 0
        retmap[classe_ids[index]] += value

    return getMaxKV(retmap), retmap

# 自然界（如动物、植物）
# 人造环境（如建筑、交通工具）
# 日常生活中的各种物品和场景（如食物、日常物品、夜景、人物、风景）
# 特定的图像类型（如动漫/卡通、文本/扫描件）
#城市元素 (Urban Elements)
#抽象或艺术 (Art or Abstract)
@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main(dataset):
    classes = r"""
animal
anime or cartoon:cartoon
building or architecture or Urban Elements:building
food
goods or Everyday Objects:goods
nightscape:nightscape
people or person:people
plant
scenery or Natural landscape:landscape
text or scanned document:text
vehicle or transportation:vehicle
    """.strip().split("\n")
    classes = [i.strip() for i in classes]
    classes_cn = r"""
动物:animal
动漫或卡通:cartoon
建筑:building
食物:food
日常物品:goods
夜景:nightscape
人物:people
植物:plant
风景:landscape
文本或扫描件:text
交通工具:vehicle
    """.strip().split("\n")
    classes_cn = [i.strip() for i in classes_cn]

    def mainfile(fpath, fname, ftype):
        ifile = fpath # os.path.join(subdir, idir)
        if ftype in ("txt", "json", "log", "pt",):
            return

        print("***" * 30)
        colorPrint(ifile)
        image = Image.open(ifile)
        (idx1, idv1), retmap1 = cateclip(image, classes)
        colorPrint(idx1, idv1)
        (idx2, idv2), retmap2 = cateclip_cn(image, classes_cn)
        colorPrint(idx2, idv2)

        flag = False
        # 分类和分类之间存在重叠，所以 0.4 就可以了。
        if idx1 == idx2 and idv1 >= 0.4 and idv2 >= 0.4:
            flag = True

        idx1, idv1, idx2, idv2 = mergeTest(retmap1, retmap2)
        colorPrint(idx1, idv1, idx2, idv2)
        # 均值 0.5，差距控制在 0.2，有一定把握才行。
        if idv1 >= 0.5 and idv2 < idv1 - 0.2:
            flag = True

        if not flag: # 没有答案就算了。
            return

        if INSTALL:

            fmd5 = getFileMd5(ifile)[:16]
            rad = int(fmd5, 16) % 100

            if rad < 20:
                targetfile = os.path.join("tempset", "val", idx1, fmd5+fname)
            else:
                targetfile = os.path.join("tempset", "train", idx1, fmd5+fname)
            fdir = os.path.dirname(targetfile)
            if not os.path.exists(fdir):
                os.makedirs(fdir)

            # OSError: cannot write mode RGBA as JPEG
            try:
                image.save(targetfile)
            except OSError: # cannot write mode RGBA as JPEG
                copyfile(ifile, targetfile)
            assert os.path.exists(targetfile), targetfile
            if not DEBUG:
                image.close()
                osremove(ifile)

        else: # Review
            mytype = os.path.split(os.path.split(fpath)[0])[-1]
            assert mytype in [c.split(":")[-1].strip() for c in classes], mytype
            if idx1 == mytype: # 如果相等，就不要再 Review 了。
                return

            ifile = os.path.abspath(ifile)
            assert ifile.find("imgclassify") != -1, ifile
            if DATAX:
                targetfile = ifile.replace("imgclassify", "imgclassifx_clip")
            else:
                targetfile = ifile.replace("imgclassify", "imgclassifz")

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
