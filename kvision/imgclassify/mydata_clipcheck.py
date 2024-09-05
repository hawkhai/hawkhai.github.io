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

def test():
    from torchvision.datasets import CIFAR100

    # Download the dataset
    cifar100 = CIFAR100(root=dlrootdir, download=True, train=False)

    # Prepare the inputs
    image, class_id = cifar100[3637]
    print(type(image), class_id)
    image_input = preprocess(image).unsqueeze(0).to(device)
    text_inputs = torch.cat([clip.tokenize(f"a image of {c}") for c in cifar100.classes]).to(device)

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

def getMaxKV(retmap, retsecond=False):

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
    if retsecond:
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
    text_inputs = torch.cat([clip.tokenize(f"a image of {c}") for c in classes]).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(min(TOPK_COUNT, len(classes)))

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

"""
输入数据结构调整：
image -- 图片
classes -- 是一个字典，比如：{
    "type1": ["anime", "cartoon"],
    "type2": ["animal"],
}
需要找出 image 和 哪个 class 最接近，而每个 type 包含的关键字列表，要取最接近图片的那个。
"""
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

def cateclip2(image, classes):
    # 对图像进行预处理
    image_input = preprocess(image).unsqueeze(0).to(device)
    
    # 存储每个 type 对应的最大相似度值
    type_max_probs = {}
    
    # 遍历字典中的每个 type
    for type_key, keywords in classes.items():
        # 生成对应的文本描述
        texts = [f"a {keyword} image" for keyword in keywords]
        text_tokens = torch.cat([clip.tokenize(text) for text in texts]).to(device)
        
        # 计算图像和文本的特征
        with torch.no_grad():
            image_features = model.encode_image(image_input)
            text_features = model.encode_text(text_tokens)
            assert image_features.size()[0] == 1, image_features.size()
            assert text_features.size()[0] == len(keywords), text_features.size()
            
            # 归一化特征
            image_features /= image_features.norm(dim=-1, keepdim=True)
            text_features /= text_features.norm(dim=-1, keepdim=True)
            
            # 计算图像和文本的相似度
            similarity = (100.0 * image_features @ text_features.T) #.softmax(dim=-1)
            
            # 提取相似度分数
            similarity_scores = similarity[0].cpu().numpy()
            #print(similarity_scores)
            
            type_max_probs[type_key] = np.max(similarity_scores)
    
    # 转换为 tensor 以便使用 softmax
    type_keys = list(type_max_probs.keys())
    type_values = np.array(list(type_max_probs.values()))
    
    if type_values.size > 0:
        # 使用 softmax 进行归一化
        softmax_probs = F.softmax(torch.tensor(type_values, dtype=torch.float32), dim=0).numpy()
        normalized_probs = dict(zip(type_keys, softmax_probs))
    else:
        # 如果没有有效的相似度值，返回所有值为 0
        normalized_probs = {key: 0 for key in type_max_probs.keys()}
    
    #print(type_max_probs)
    #print(normalized_probs)
    return getMaxKV(normalized_probs), normalized_probs

def cateclip_cn2(image, classes):
    # 对图片进行预处理
    image = preprocess(image).unsqueeze(0).to(device)
    
    # 存储每个 type 对应的最大相似度值
    type_max_probs = {}
    
    # 遍历字典中的每个 type
    for type_key, keywords in classes.items():
        # 生成对应的文本描述
        texts = [f"一张 {keyword} 图片" for keyword in keywords]
        text_tokens = cn_clip.tokenize(texts).to(device)
        
        # 计算图像和文本的特征
        with torch.no_grad():
            image_features = model_cn.encode_image(image)
            text_features = model_cn.encode_text(text_tokens)
            assert image_features.size()[0] == 1, image_features.size()
            assert text_features.size()[0] == len(keywords), text_features.size()

            # 归一化特征
            image_features /= image_features.norm(dim=-1, keepdim=True)
            text_features /= text_features.norm(dim=-1, keepdim=True)
            
            # 计算图像和文本的相似度
            similarity = (100.0 * image_features @ text_features.T) #.softmax(dim=-1)
            
            # 提取相似度分数
            similarity_scores = similarity[0].cpu().numpy()
            #print(similarity_scores)
            
            type_max_probs[type_key] = np.max(similarity_scores)
            continue
            
            # 计算图像和文本的相似度
            logits_per_image, _ = model_cn.get_similarity(image_features, text_features)
            
            # 计算每个文本描述的概率
            probs = logits_per_image.softmax(dim=-1).cpu().numpy()
            
            # 对于每个 type，计算最大概率
            max_prob = np.max(probs)
            
            # 存储当前 type 对应的最大概率
            type_max_probs[type_key] = max_prob
    
    # 转换为 tensor 以便使用 softmax
    type_keys = list(type_max_probs.keys())
    type_values = np.array(list(type_max_probs.values()))
    
    if type_values.size > 0:
        # 使用 softmax 进行归一化
        softmax_probs = F.softmax(torch.tensor(type_values, dtype=torch.float32), dim=0).numpy()
        normalized_probs = dict(zip(type_keys, softmax_probs))
    else:
        # 如果没有有效的相似度值，返回所有值为 0
        normalized_probs = {key: 0 for key in type_max_probs.keys()}
    
    #print(type_max_probs)
    #print(normalized_probs)
    return getMaxKV(normalized_probs), normalized_probs

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main(dataset):
    classes = {
        "animal": ["animal", "mammal", "bird", "reptile", "fish", "insect", "wildlife"],
        "cartoon": ["anime", "cartoon", "animated series", "manga", "comic", "illustration"],
        "building": ["building", "architecture", "urban elements", "skyscraper", "structure", "historical building"],
        "food": ["food", "dish", "meal", "cuisine", "snack", "ingredient", "beverage"],
        "goods": ["goods", "everyday objects", "products", "merchandise", "items", "commodities"],
        "nightscape": ["nightscape", "night view", "night scene", "nighttime", "city lights", "starlight"],
        "people": ["people", "person", "portrait", "group", "individual", "human"],
        "plant": ["plant", "flower", "tree", "shrub", "leaf", "vegetation"],
        "landscape": ["scenery", "natural landscape", "view", "terrain", "outdoor", "nature", "countryside"],
        "text": ["text", "scanned document", "written content", "letter", "page", "manuscript"],
        "vehicle": ["vehicle", "transportation", "car", "bike", "bus", "train", "airplane", "boat"],
        "abstract": ["art", "abstract", "conceptual", "modern art", "non-representational", "expressionism"],
    }
    classes_cn = {
        "animal": ["动物", "哺乳动物", "鸟类", "爬行动物", "鱼类", "昆虫", "野生动物"],
        "cartoon": ["动漫", "卡通", "动画片", "漫画", "插画", "动画系列"],
        "building": ["建筑", "建筑物", "城市元素", "摩天大楼", "结构", "历史建筑"],
        "food": ["食物", "菜肴", "餐点", "美食", "小吃", "原料", "饮料"],
        "goods": ["日常物品", "商品", "产品", "商品", "货物", "物品"],
        "nightscape": ["夜景", "夜晚风景", "夜间场景", "城市灯光", "星光", "夜景摄影"],
        "people": ["人物", "人", "肖像", "人群", "个人", "人类"],
        "plant": ["植物", "花卉", "树木", "灌木", "叶子", "绿植"],
        "landscape": ["风景", "自然风光", "景色", "地形", "户外", "自然", "乡村"],
        "text": ["文本", "扫描件", "书写内容", "信件", "页面", "手稿"],
        "vehicle": ["交通工具", "车辆", "汽车", "自行车", "公交车", "火车", "飞机", "船只"],
        "abstract": ["抽象", "艺术", "概念艺术", "现代艺术", "非具象", "表现主义"],
    }

    def mainfile(fpath, fname, ftype):
        ifile = fpath # os.path.join(subdir, idir)
        if ftype in ("txt", "json", "log", "pt", "", "py"):
            return
        if ftype not in ("jpg", "jpeg", "png", "bmp",):
            assert False, ftype
            return

        print("***" * 30)
        colorPrint(ifile)
        image = Image.open(ifile)
        # 需要两步分类，避免分类之间的重叠问题。
        """cartoon/text/abstract
people/animal/food/plant
landscape/nightscape/building/vehicle
goods"""
        def classification(catefunc, image, classes):
            classe_ids = [c.split(":")[-1].strip() for c in classes]
            classes = [c.split(":")[0].strip() for c in classes]
            classmap = {}
            for idx in range(len(classe_ids)):
                classmap[classe_ids[idx]] = classes[idx]

            supclasz = [
                f'{classmap["cartoon"]} or {classmap["text"]}:1',
                f'not {classmap["cartoon"]} and not {classmap["text"]}:2',
            ]
            (idx12, idv12), retmap12 = catefunc(image, supclasz)
            print(supclasz)
            print(retmap12)
            subclasz = [
                f'{classmap["cartoon"]}:cartoon',
                f'{classmap["text"]}:text',
                f'{classmap["abstract"]}:abstract',
            ]
            (idxA, idvA), retmapA = catefunc(image, subclasz)
            print(subclasz)
            print(retmapA)

            supclasz = [
                f'{classmap["people"]} or {classmap["animal"]} or {classmap["food"]} or {classmap["plant"]}:3',
                f'not {classmap["people"]} and not {classmap["animal"]} and not {classmap["food"]} and not {classmap["plant"]}:4',
            ]
            (idx34, idv34), retmap34 = catefunc(image, supclasz)
            print(supclasz)
            print(retmap34)
            subclasz = [
                f'{classmap["people"]}:people',
                f'{classmap["animal"]}:animal',
                f'{classmap["food"]}:food',
                f'{classmap["plant"]}:plant',
            ]
            (idxB, idvB), retmapB = catefunc(image, subclasz)
            print(subclasz)
            print(retmapB)

            supclasz = [
                f'{classmap["landscape"]} or {classmap["nightscape"]} or {classmap["building"]} or {classmap["vehicle"]}:5',
                f'not {classmap["landscape"]} and not {classmap["nightscape"]} and not {classmap["building"]} and not {classmap["vehicle"]}:6',
            ]
            (idx56, idv56), retmap56 = catefunc(image, supclasz)
            print(supclasz)
            print(retmap56)
            subclasz = [
                f'{classmap["landscape"]}:landscape',
                f'{classmap["nightscape"]}:nightscape',
                f'{classmap["building"]}:building',
                f'{classmap["vehicle"]}:vehicle',
            ]
            (idxC, idvC), retmapC = catefunc(image, subclasz)
            print(subclasz)
            print(retmapC)

            supclasz = [
                f'{classmap["goods"]}:7',
                f'not {classmap["goods"]}:8',
            ]
            (idx78, idv78), retmap78 = catefunc(image, supclasz)
            print(supclasz)
            print(retmap78)

            retmap = {
                 "cartoon": retmap12["1"] * retmapA["cartoon"],
                 "text": retmap12["1"] * retmapA["text"],
                 "abstract": retmap12["1"] * retmapA["abstract"],
                 "people": retmap12["2"] * retmap34["3"] * retmapB["people"],
                 "animal": retmap12["2"] * retmap34["3"] * retmapB["animal"],
                 "food": retmap12["2"] * retmap34["3"] * retmapB["food"],
                 "plant": retmap12["2"] * retmap34["3"] * retmapB["plant"],
                 "landscape": retmap12["2"] * retmap34["4"] * retmap56["5"] * retmapC["landscape"],
                 "nightscape": retmap12["2"] * retmap34["4"] * retmap56["5"] * retmapC["nightscape"],
                 "building": retmap12["2"] * retmap34["4"] * retmap56["5"] * retmapC["building"],
                 "vehicle": retmap12["2"] * retmap34["4"] * retmap56["5"] * retmapC["vehicle"],
                 "goods": retmap12["2"] * retmap34["4"] * retmap56["6"] * retmap78["7"],    
                 "unknow": retmap12["2"] * retmap34["4"] * retmap56["6"] * retmap78["8"],    
            }
            maxid, maxv = -1, -1
            for key in retmap.keys():
                val = retmap[key]
                if val > maxv:
                    maxv = val
                    maxid = key
            print(retmap)
            return [maxid, maxv], retmap

        def classification2(catefunc, image, classes):
            retv = catefunc(image, classes)
            return retv

        (idx1, idv1), retmap1 = classification2(cateclip2, image, classes)
        colorPrint(idx1, idv1)
        (idx2, idv2), retmap2 = classification2(cateclip_cn2, image, classes_cn)
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

        if not flag and not DATAX: # 没有答案就算了。
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
    if DEBUG:
        for argv in sys.argv:
            if not os.path.isfile(argv):
                continue
            main(argv)
    elif DATAX:
        main("datax")
    else:
        main("mydata/dataset")
    print("ok")
