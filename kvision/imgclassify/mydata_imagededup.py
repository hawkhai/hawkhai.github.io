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

import requests
import base64
from imgcopy_baidu import *

import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np
import faiss
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def extract_features(image_path, model, transform):
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        features = model(image).cpu().numpy().flatten()
    return features

def batch_extract_features(image_paths, model, transform, batch_size=32):
    features_list = []
    for i in range(0, len(image_paths), batch_size):
        batch_paths = image_paths[i:i + batch_size]
        images = [transform(Image.open(p).convert('RGB')).unsqueeze(0) for p in batch_paths]
        images = torch.cat(images).to(device)

        with torch.no_grad():
            batch_features = model(images).cpu().numpy()
            features_list.extend(batch_features)

    return np.array(features_list)

def faiss_topk_search(features_list, top_k=5):
    features_list = np.array(features_list).astype('float32')
    index = faiss.IndexFlatL2(features_list.shape[1])  # 使用L2距离，构建索引
    index.add(features_list)  # 将特征向量添加到索引中

    D, I = index.search(features_list, top_k + 1)  # 搜索最相似的Top-K个向量

    neighbors = []
    for i, (distances, indices) in enumerate(zip(D, I)):
        similar_indices = [(ind, dist) for ind, dist in zip(indices[1:], distances[1:]) if ind != i]
        neighbors.append(similar_indices)

    return neighbors

def find_duplicates(image_dir, model, transform, threshold=0.98):
    features_list = []
    image_paths = []

    for image_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_name)
        features = extract_features(image_path, model, transform)
        features_list.append(features)
        image_paths.append(image_path)

    # 计算所有图像特征之间的余弦相似度
    similarities = cosine_similarity(features_list)

    # 识别相似度高于阈值的图片对
    duplicates = set()
    for i in range(len(similarities)):
        for j in range(i + 1, len(similarities)):
            if similarities[i][j] > threshold:
                if i < ind:
                    duplicates.add((image_paths[i], image_paths[ind]))
                elif i > ind:
                    duplicates.add((image_paths[ind], image_paths[i]))

    return duplicates

def find_duplicates_with_faiss(image_dir, model, transform, top_k=5, similarity_threshold=0.98):

    image_paths = []
    def mainfile(fpath, fname, ftype):
        if ftype in ("jpg", "jpeg", "webp", "png", "bmp"):
            image_paths.append(fpath)
    for i in image_dir:
        searchdir(i, mainfile)

    features_list = batch_extract_features(image_paths, model, transform)

    # 使用Faiss进行Top-K搜索
    neighbors = faiss_topk_search(features_list, top_k=top_k)

    duplicates = set()
    for i, similar_imgs in enumerate(neighbors):
        for ind, dist in similar_imgs:
            if dist < (1 - similarity_threshold):  # 距离越小，越相似
                if i < ind:
                    duplicates.add((image_paths[i], image_paths[ind]))
                elif i > ind:
                    duplicates.add((image_paths[ind], image_paths[i]))

    return duplicates

def remove_duplicates(duplicates):
    for img1, img2 in duplicates:
        if os.path.exists(img1):
            copyfile(img1, img2.replace("imgclassify", "imgclassifz")+".jpg")

        if os.path.exists(img2):
            copyfile(img2, img2.replace("imgclassify", "imgclassifz"))
            os.remove(img2)
        print(f"Removed: {img2}")

# https://github.com/idealo/imagededup
# https://github.com/idealo/imagededup/blob/master/examples/Finding_duplicates.ipynb

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main():

    r"""
ShuffleNetV2 0.5x
模型大小: 约 4.8 MB
Top-1 准确率: 57.7%

ShuffleNetV2 1.0x
模型大小: 7.4 MB
Top-1 准确率: 69.4%

ShuffleNetV2 1.5x
模型大小: 12.0 MB
Top-1 准确率: 73.2%

ShuffleNetV2 2.0x
模型大小: 21.8 MB
Top-1 准确率: 75.3%
    """
    model = models.shufflenet_v2_x2_0(pretrained=True).to(device)
    model.fc = torch.nn.Identity()  # 移除分类层
    model.eval()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    image_directory = [
        r"E:\kSource\blog\kvision\imgclassify\mydata\val",
        r"E:\kSource\blog\kvision\imgclassify\mydata\train",
        r"E:\kSource\blog\kvision\imgclassify\mydata\dataset",
        r"E:\kSource\blog\kvision\imgclassify\mydata\valset",
    ] if IS_WINDOWS else [
        r"/home/yqh/code/blog/kvision/imgclassify/mydata/val",
        r"/home/yqh/code/blog/kvision/imgclassify/mydata/train",
        r"/home/yqh/code/blog/kvision/imgclassify/mydata/dataset",
        r"/home/yqh/code/blog/kvision/imgclassify/mydata/valset",
    ]
    duplicates = find_duplicates_with_faiss(image_directory, model, transform,
                        top_k=5, similarity_threshold=0.98)
    remove_duplicates(duplicates)
    cleardirEmpty(r"/home/yqh/code/blog/kvision/imgclassify")

if __name__ == "__main__":
    main()
