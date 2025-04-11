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

INSTALL = "install" in sys.argv

def checkimg(xfile):

    try:
        img = Image.open(xfile)
    except Exception as ex:
        print(ex)
        try:
            import cv2
            tempfile = os.path.join("tempdir", "tempfile.jpg")
            copyfile(xfile, tempfile)
            img = cv2.imread(tempfile, 1) # BGR
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        except Exception as ey:
            print(ey)
            print("错误", xfile)
            osremove(xfile) # 解析错误
            return False

    width, height = img.size
    if width / height < 1/3 or height / width < 1/3 or width * height < 150 * 150:
        print(img.size, xfile)
        print("太小", xfile)
        img.close()
        osremove(xfile) # 图片太小
        return False

    ratio = 1.0
    while width * height * ratio * ratio > 256 * 256:
        ratio *= 0.99
    if ratio == 1.0 and img.mode == "RGB":
        #print("跳过", xfile)
        return True

    width = round(width * ratio * 0.99)
    height = round(height * ratio * 0.99)
    try:
        img = img.resize((width, height))
    except OSError: # image file is truncated (39 bytes not processed)
        print(img.size, xfile)
        print("错误", xfile)
        img.close()
        osremove(xfile) # 图片错误
        return False

    if img.mode != "RGB":
        img = img.convert("RGB")

    img.save(xfile)
    print(img.size, xfile)
    print("存储", xfile)
    return True

def copyimg(xfile, yfile):

    if os.path.exists(yfile):
        return
    mydir = os.path.split(yfile)[0]
    if not os.path.exists(mydir):
        os.makedirs(mydir)

    try:
        img = Image.open(xfile)
    except Exception as ex:
        print(ex)
        try:
            import cv2
            tempfile = os.path.join("tempdir", "tempfile.jpg")
            copyfile(xfile, tempfile)
            img = cv2.imread(tempfile, 1) # BGR
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        except Exception as ey:
            print(ey)
            return

    print(img.size, xfile)
    #img.save(yfile)
    width, height = img.size
    if width * height < 200 * 200:
        print("IGNORE", xfile)
        return

    ratio = 1.0
    while width * height * ratio * ratio > 256 * 256:
        ratio *= 0.99
    width = round(width * ratio)
    height = round(height * ratio)
    try:
        img = img.resize((width, height))
    except OSError: # image file is truncated (39 bytes not processed)
        return
    if img.mode != "RGB":
        img = img.convert("RGB")

    img.save(yfile)
    print(img.size, yfile)

def luckcopy(rootdir, targetdir, clasz, pname):
    #for fname in os.listdir(rootdir):
    def mainfile(fpath, fname, ftype):
        #fpath = os.path.join(rootdir, fname)

        fmd5 = getFileMd5(fpath)[:16]
        rad = int(fmd5, 16) % 100

        if rad < 20:
            targetfile = os.path.join(targetdir, "mydata", "val", clasz, pname+fname)
        else:
            targetfile = os.path.join(targetdir, "mydata", "train", clasz, pname+fname)

        print(targetfile)
        copyimg(fpath, targetfile)
        osremove(fpath)

    searchdir(rootdir, mainfile)

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main2():

    luckcopy("mydata/tempset/animal", ".", "animal", "")
    luckcopy("mydata/tempset/goods", ".", "goods", "")
    luckcopy("mydata/tempset/plant", ".", "plant", "")
    luckcopy("mydata/tempset/vehicle", ".", "vehicle", "")
    return

    # https://www.kaggle.com/datasets/noobyogi0100/shoe-dataset
    luckcopy(r"D:\分类数据\archive_shoeTypeClassifierDataset\shoeTypeClassifierDataset\validation", r"E:\kSource\blog\kvision\imgclassify",
             "goods", "shoeTypeClassifierDataset_")

    luckcopy(r"D:\分类数据\Vechicles", r"E:\kSource\blog\kvision\imgclassify",
             "vehicle", "PaddleClas_Vechicles_")
    luckcopy(r"D:\分类数据\FashionProductImageSmall", r"E:\kSource\blog\kvision\imgclassify",
             "goods", "PaddleClas_goods_")
    return

    # 李宏毅 2023 年春的 homework3 数据集
    rootdir = r"D:\分类数据\food-11\valid"
    targetdir = r"E:\kSource\blog\kvision\imgclassify"
    luckcopy(rootdir, targetdir, "food", "food-11_")

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir_CADB(srcdir, dstdir):
    statx = {}
    config = readfileJson("scene_categories.json")
    def mainfile(fpath, fname, ftype):

        subdir = config[fname]
        if not subdir in statx:
            statx[subdir] = 0
        statx[subdir] = statx[subdir] + 1

        ifile = os.path.relpath(fpath, srcdir)
        assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
        xfile = os.path.join(srcdir, ifile)
        md5 = getFileMd5(xfile)[:16] # copydir_CADB

        mydir = os.path.join(dstdir, "cadb_"+subdir)
        yfile = os.path.join(mydir, "cadb_"+md5+"."+ftype)

        copyimg(xfile, yfile)

    searchdir(srcdir, mainfile)
    print(srcdir)
    print(statx)
    print()

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir(srcdir, dstdir):

    def mainfile(fpath, fname, ftype):

        ifile = os.path.relpath(fpath, srcdir)
        assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
        xfile = os.path.join(srcdir, ifile)
        md5 = getFileMd5(xfile)[:16] # copydir pp_ 智慧相册数据

        yfile = os.path.join(dstdir, "pp_"+md5+"."+ftype)

        copyimg(xfile, yfile)

    searchdir(srcdir, mainfile)
    print(srcdir)
    print()

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir_baidu():
    rootdir = r"E:\kSource\blog\kvision\imgclassify\mydata"

    def copydirkz(xdir, ydir, prekey="baidu", dirname=False):
        if not ydir: return

        srcdir = os.path.join(rootdir, xdir)
        dstdir = os.path.join(r"E:\kSource\blog\kvision\imgclassify\mydata", "tempset", ydir)
        if not os.path.exists(dstdir):
            os.makedirs(dstdir)

        def mainfile(fpath, fname, ftype):
            print(fpath)
            if not ftype:
                ftype = "jpg"

            li = re.findall("u=([0-9]+,[0-9]+)&", fname)
            #if not li: return
            #assert len(li) == 1, li
            #imgid = li[0]

            ifile = os.path.relpath(fpath, srcdir)
            #assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
            xfile = os.path.join(srcdir, ifile)
            md5 = getFileMd5(fpath)[:16] # copydir_baidu

            # dirname
            idirname = os.path.basename(os.path.dirname(fpath))
            if dirname:
                yfile = os.path.join(dstdir, prekey+"_"+idirname+"_"+os.path.splitext(fname)[0]+"."+ftype)
            else:
                yfile = os.path.join(dstdir, prekey+"_"+md5+"."+ftype)

            print(yfile)
            copyimg(xfile, yfile)

        print(os.path.exists(srcdir), srcdir)
        searchdir(srcdir, mainfile)
        cleardirEmpty(dstdir)

    if False:
        rootdir = r"D:\分类数据\VOCtrainval_11-May-2012.tar\VOCdevkit\VOC2012\ImageSets\Main"
        for itxt in os.listdir(rootdir):
            txtfile = os.path.join(rootdir, itxt)
            if not os.path.isfile(txtfile) or itxt.find("trainval") == -1:
                continue
            txtlines = readfileLines(txtfile)
            print(txtfile)
            for txtline in txtlines:
                #print(txtline)
                img = txtline.split()[0]
                if txtline.split()[-1] == "-1":
                    continue
                #assert idx == "-1", txtline
                imgfile = "D:\分类数据\VOCtrainval_11-May-2012.tar\VOCdevkit\VOC2012\JPEGImages\{}.jpg".format(img)
                if not os.path.exists(imgfile):
                    print(imgfile)
                else:
                    targetd = os.path.splitext(txtfile)[0]
                    targetf = os.path.join(targetd, "VOCtrainval_11-May-2012_{}_{}.jpg".format(itxt.split("_trainval.txt")[0], img))
                    copyimg(imgfile, targetf)

    copydirkz(r"D:\分类数据\OfficeHomeDataset_10072016\Real World", "goods", "OfficeHomeDataset_10072016", True)
    copydirkz(r"D:\分类数据\archive_animals\animals\animals", "animal", "90_Different_Animals", True)
    return

    copydirkz(r"E:\kSource\blog\kvision\imgclassify\mydata\63页Png，速通高等数学！_files", "text")
    copydirkz(r"D:\BaiduNetdiskDownload\M6Doc_test\test2017", "text")

    copydirkz(r"日常物品_百度图片搜索_files", "goods")
    copydirkz(r"日常用品_百度图片搜索_files", "goods")

    copydirkz(r"动漫_百度图片搜索_files", "cartoon")
    copydirkz(r"卡通_百度图片搜索_files", "cartoon")
    copydirkz(r"anime 日本_百度图片搜索_files", "cartoon")

    copydirkz(r"夜景_百度图片搜索_files", "nightscape")

    copydirkz(r"物品图片 真实_百度图片搜索_files", "goods")
    copydirkz(r"商品 真实图片_百度图片搜索_files", "goods")
    copydirkz(r"小物件 真实_百度图片搜索_files", "goods")

    copydirkz(r"室内_百度图片搜索_files", "indoor")

    copydirkz(r"文字文本_百度图片搜索_files", "text")
    copydirkz(r"扫描件_百度图片搜索_files", "text")

    copydirkz(r"建筑_百度图片搜索_files", "building")

    copydirkz(r"交通工具 真实_百度图片搜索_files", "vehicle")

    copydirkz(r"植物_百度图片搜索_files", "plant")

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir_vehicle():
    rootdir = r"D:\worktemp\vehicle\vehicle"

    def copydirkz(srcdir, ydir):
        if not ydir: return

        dstdir = os.path.join(r"dataset", ydir)
        assert os.path.exists(dstdir), dstdir

        def mainfile(fpath, fname, ftype):

            ifile = os.path.relpath(fpath, srcdir)
            #assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
            xfile = os.path.join(srcdir, ifile)
            md5 = getFileMd5(xfile)[:16] # copydir_vehicle

            yfile = os.path.join(dstdir, "vehicle_"+md5+"."+ftype)

            copyimg(xfile, yfile)

        searchdir(srcdir, mainfile)

    copydirkz(rootdir, "vehicle")

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir_corel5k():
    rootdir = r"D:\worktemp\Corel5K\真正的Corel5k数据集(带标注,训练与测试集)"

    def copydirkz(xdir, ydir):
        if not ydir: return

        xdir = os.path.join(rootdir, xdir)
        ydir = os.path.join(r"dataset", ydir)
        assert os.path.exists(ydir), ydir

        def mainfile(fpath, fname, ftype):

            ifile = os.path.relpath(fpath, xdir)
            assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
            xfile = os.path.join(xdir, ifile)
            md5 = getFileMd5(xfile)[:16] # copydir_corel5k

            yfile = os.path.join(ydir, "corel5k_"+md5+"."+ftype)

            if os.path.exists(yfile):
                return
            copyimg(xfile, yfile)

        searchdir(xdir, mainfile)

    copydirkz(r"13000", "plant") # 花卉
    copydirkz(r"41000", "animal") # 动物
    copydirkz(r"119000", "building") # 建筑
    copydirkz(r"143000", "landscape") # 风景
    copydirkz(r"152000", "plant") # 植物
    copydirkz(r"189000", "people") # 人物
    copydirkz(r"231000", "landscape") # 风景

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir_album():
    xlist1 = readfileLines(r"baidu94479\onehot_train.txt")
    xlist2 = readfileLines(r"baidu94479\onehot_test.txt")
    xlist3 = readfileLines(r"baidu94479\onehot_valid.txt")

    def copydirx(xlist):
        labels = r"""Vehicle:vehicle
Sky:landscape
Food:food
Person:people
Building:building
Animal:animal
Cartoons:cartoon
Certificate:text
Electronic:text
Screenshot:text
BankCard:text
Mountain:landscape
Sea:landscape
Bill:text
Selfie:people
Night:nightscape
Aircraft:vehicle
Flower:plant
Child:people
Ship:vehicle""".split()
        for line in xlist:
            name, tags = line.split()
            print(name, tags)
            tags = tags.strip().split(",")
            assert len(tags) == len(labels), name

            imgfile = os.path.join(r"E:\BaiduNetdiskDownload\album\album\img", name)
            assert os.path.exists(imgfile), imgfile

            tagcount = len(tags)
            checktag = [labels[i].split(":")[-1] for i in range(tagcount) if tags[i] != "0"]
            checktag = list(set(checktag))
            if len(checktag) != 1:
                continue

            for i in range(tagcount):
                if tags[i] == "0":
                    continue

                subdir = labels[i].split(":")[-1]

                xfile = imgfile
                ftype = os.path.splitext(xfile)[-1].lower()
                md5 = getFileMd5(xfile)[:16] # copydir_album

                mydir = os.path.join(r"dataset", subdir)
                yfile = os.path.join(mydir, "pp2_"+md5+ftype)

                copyimg(xfile, yfile)

    copydirx(xlist1)
    copydirx(xlist2)
    copydirx(xlist3)

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def checkimg_baidu(rootdir):
    fnamez = {}
    def mainfile(fpath, fname, ftype):
        if ftype in ("txt", "json"):
            return

        fnamec = fname.split(".")[0].split("_", 1)[1]
        if fnamec in fnamez:
            print("REMOVE REP", fnamez[fnamec], fpath)
            os.remove(fpath) # 重复
            return
        fnamez[fnamec] = fpath

        img = Image.open(fpath)
        width, height = img.size
        if width / height < 1/3 or height / width < 1/3 or width * height < 150 * 150:
            img.close()
            os.remove(fpath) # 太小
            print("REMOVE", (width, height), fpath)

    searchdir(rootdir, mainfile)

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main():
    # pp
    # https://aistudio.baidu.com/datasetdetail/110303
    if False:
        copydir(r"D:\BaiduNetdiskDownload\dataset\animals",   r"dataset\animal")
        copydir(r"D:\BaiduNetdiskDownload\dataset\food",      r"dataset\food")
        copydir(r"D:\BaiduNetdiskDownload\dataset\people",    r"dataset\people")
        copydir(r"D:\BaiduNetdiskDownload\dataset\scenery",   r"dataset\landscape")
        copydir(r"D:\BaiduNetdiskDownload\dataset\text",      r"dataset\text")

    # CADB
    # https://github.com/bcmi/Image-Composition-Assessment-Dataset-CADB
    if False:
        copydir_CADB(r"D:\BaiduNetdiskDownload\CADB_Dataset\images", r"dataset")

    # pp2
    # https://aistudio.baidu.com/datasetdetail/94479/
    if False:
        copydir_album()

    # Corel5K - github
    if False:
        copydir_corel5k()

    # 百度网页
    if False:
        copydir_baidu()

    # D:\worktemp\vehicle\vehicle
    # https://aistudio.baidu.com/datasetdetail/125181
    if False:
        copydir_vehicle()

    print("ok")
    checkimg_baidu(r"dataset")

if __name__ == "__main__":
    if INSTALL:
        main2()
    else:
        copydir_baidu()
    print("ok")
