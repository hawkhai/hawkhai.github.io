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

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load('ViT-B/32', device)

import cn_clip.clip as cn_clip
from cn_clip.clip import load_from_name, available_models
print("Available models:", available_models())  
# Available models: ['ViT-B-16', 'ViT-L-14', 'ViT-L-14-336', 'ViT-H-14', 'RN50']

model_cn, preprocess_cn = load_from_name("ViT-B-16", device=device, download_root='./')
model_cn.eval()

def test():
    from torchvision.datasets import CIFAR100

    # Download the dataset
    cifar100 = CIFAR100(root=os.path.expanduser("~/.cache"), download=True, train=False)

    # Prepare the inputs
    image, class_id = cifar100[3637]
    print(type(image), class_id)
    image_input = preprocess(image).unsqueeze(0).to(device)
    text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in cifar100.classes]).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(5)

    # Print the result
    #print("\nTop predictions:\n")
    for value, index in zip(values, indices):
        print(f"{cifar100.classes[index]:>16s}: {100 * value.item():.2f}%")

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
    text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in classes]).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(5)

    # Print the result
    #print("\nTop predictions:\n")
    for value, index in zip(values, indices):
        print(f"{classes[index]:>16s}: {100 * value.item():.2f}%")
        return classe_ids[index], value.item()

def cateclip_cn(image, classes):

    classe_ids = [c.split(":")[-1].strip() for c in classes]
    classes = [c.split(":")[0].strip() for c in classes]

    #print(classe_ids)
    #print(classes)
    image = preprocess(image).unsqueeze(0).to(device)
    text = cn_clip.tokenize([f"一张 {c} 照片" for c in classes]).to(device)

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
    return classe_ids[max_index], max_value

def main(dataset):
    classes = r"""
animal
anime
cartoon:anime
building
architecture:building
food
goods
product:goods
indoor
night view:night
people
figure:people
plant
scenery
landscape:scenery
text
scanned document:text
vehicle
transportation:vehicle
    """.strip().split("\n")
    classes = [i.strip() for i in classes]
    classes_cn = r"""
动物:animal
动漫:anime
卡通:anime
建筑:building
食物:food
商品:goods
室内:indoor
夜景:night
人物:people
植物:plant
风景:scenery
文本:text
扫描件:text
交通工具:vehicle
    """.strip().split("\n")
    classes_cn = [i.strip() for i in classes_cn]
    for dir in os.listdir(dataset):
        subdir = os.path.join(dataset, dir)
        if not os.path.isdir(subdir):
            continue
        for idir in os.listdir(subdir):
            ifile = os.path.join(subdir, idir)
            if ifile.endswith(".txt"):
                continue
            
            print("***" * 30)
            print(ifile)
            image = Image.open(ifile)
            idx1, idv1 = cateclip(image, classes)
            idx2, idv2 = cateclip_cn(image, classes_cn)
            #break
            if idx1 != idx2:
                continue
            if idv1 < 0.5 or idv2 < 0.5:
                continue

            fmd5 = getFileMd5(ifile)[:5]
            rad = int(fmd5, 16) % 100
            
            if rad < 20:
                targetfile = os.path.join("mydata", "val", idx1, fmd5+".jpg")
            else:
                targetfile = os.path.join("mydata", "train", idx1, fmd5+".jpg")
            fdir = os.path.dirname(targetfile)
            if not os.path.exists(fdir):
                os.makedirs(fdir)
            image.save(targetfile)
            osremove(ifile)

# 还需要移除相似图片。
if __name__ == "__main__":
    #test()
    main("dataset")
    main("valset")
    print("ok")
