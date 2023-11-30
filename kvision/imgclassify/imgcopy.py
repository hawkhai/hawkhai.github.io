#encoding=utf8
import re, os, sys
for reldirx, _lidir in (("./", []), (os.path.split(__file__)[0]+"/", [])):
    while not _lidir and len(reldirx) <= 100:
        reldirx += "../"
        checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx)
from pythonx.funclib import *

from PIL import Image

def copyimg(xfile, yfile):
    try:
        img = Image.open(xfile)
    except Exception as ex:
        print(ex)
        try:
            import cv2
            tempfile = os.path.join("tempdir", "tempfile.jpg")
            copyfile(xfile, tempfile)
            img = cv2.imread(tempfile, 1)
            color_coverted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(color_coverted)
        except Exception as ey:
            print(ey)
            return
     
    print(img.size, xfile)
    #img.save(yfile)
    width, height = img.size
    if width * height < 200 * 200:
        print("small", xfile)
        return
    
    ratio = 1.0
    while width * height * ratio * ratio > 256 * 256:
        ratio *= 0.99
    width = round(width * ratio)
    height = round(height * ratio)
    img = img.resize((width, height))
    if img.mode != "RGB":
        img = img.convert("RGB")

    img.save(yfile)
    print(img.size, yfile)

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir2(srcdir, dstdir):
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
        md5 = getFileMd5(xfile)[:7] # copydir2

        mydir = os.path.join(dstdir, "cadb_"+subdir)
        yfile = os.path.join(mydir, md5+"."+ftype)
        yfile2 = os.path.join(mydir, "cadb_"+md5+"."+ftype)
        if os.path.exists(yfile):
            os.rename(yfile, yfile2)
            return
        yfile = yfile2

        if os.path.exists(yfile):
            return
        if not os.path.exists(mydir):
            os.makedirs(mydir)

        copyimg(xfile, yfile)

    searchdir(srcdir, mainfile)
    print(srcdir)
    print(statx)
    print()

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir(srcdir, dstdir):
    statx = {}
    def mainfile(fpath, fname, ftype):
        if not ftype in statx:
            statx[ftype] = 0
        statx[ftype] = statx[ftype] + 1

        ifile = os.path.relpath(fpath, srcdir)
        assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
        xfile = os.path.join(srcdir, ifile)
        md5 = getFileMd5(xfile)[:7] # copydir

        yfile = os.path.join(dstdir, md5+"."+ftype)
        yfile2 = os.path.join(dstdir, "pp_"+md5+"."+ftype)
        if os.path.exists(yfile):
            os.rename(yfile, yfile2)
            return
        yfile = yfile2

        if os.path.exists(yfile):
            return
        if not os.path.exists(dstdir):
            os.makedirs(dstdir)

        copyimg(xfile, yfile)

    searchdir(srcdir, mainfile)
    print(srcdir)
    print(statx)
    print()

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir5():
    rootdir = r"D:\BaiduNetdiskDownload"

    def copydir4z(xdir, ydir):
        if not ydir: return

        xdir = os.path.join(rootdir, xdir)
        ydir = os.path.join(r"dataset", ydir)
        assert os.path.exists(ydir), ydir

        def mainfile(fpath, fname, ftype):
            print(fpath)
            if not ftype:
                ftype = "jpg"
                
            li = re.findall("u=([0-9]+,[0-9]+)&", fname)
            if not li: return
            assert len(li) == 1, li
            md5 = li[0]

            ifile = os.path.relpath(fpath, xdir)
            assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
            xfile = os.path.join(xdir, ifile)
            md5 = getmd5(md5)[:7] # copydir5

            yfile = os.path.join(ydir, "baidu_"+md5+"."+ftype)

            if os.path.exists(yfile):
                print("EXISTS", yfile)
                return
            copyimg(xfile, yfile)

        searchdir(xdir, mainfile)

    copydir4z(r"动漫_百度图片搜索_files", "anime")
    copydir4z(r"卡通_百度图片搜索_files", "anime")
    copydir4z(r"anime 日本_百度图片搜索_files", "anime")
    
    copydir4z(r"夜景_百度图片搜索_files", "night")
    
    copydir4z(r"物品图片 真实_百度图片搜索_files", "goods")
    copydir4z(r"室内_百度图片搜索_files", "indoor")
    
    copydir4z(r"文字文本_百度图片搜索_files", "text")
    
    # ...
    copydir4z(r"小物件 真实_百度图片搜索_files", "goods")
    copydir4z(r"建筑_百度图片搜索_files", "building")
    copydir4z(r"交通工具 真实_百度图片搜索_files", "vehicle")
    copydir4z(r"扫描件_百度图片搜索_files", "text")
    copydir4z(r"商品 真实图片_百度图片搜索_files", "goods")
    
    copydir4z(r"植物_百度图片搜索_files", "plant")

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir4():
    rootdir = r"D:\worktemp\Corel5K\真正的Corel5k数据集(带标注,训练与测试集)"

    def copydir4z(xdir, ydir):
        if not ydir: return

        xdir = os.path.join(rootdir, xdir)
        ydir = os.path.join(r"dataset", ydir)
        assert os.path.exists(ydir), ydir

        def mainfile(fpath, fname, ftype):

            ifile = os.path.relpath(fpath, xdir)
            assert ifile.find("\\") == -1 and ifile.find("/") == -1, ifile
            xfile = os.path.join(xdir, ifile)
            md5 = getFileMd5(xfile)[:7] # copydir4

            yfile = os.path.join(ydir, "corel5k_"+md5+"."+ftype)

            if os.path.exists(yfile):
                return
            copyimg(xfile, yfile)

        searchdir(xdir, mainfile)

    copydir4z(r"13000", "plant") # 花卉
    copydir4z(r"41000", "animal") # 动物
    copydir4z(r"119000", "building") # 建筑
    copydir4z(r"143000", "scenery") # 风景
    copydir4z(r"152000", "plant") # 植物
    copydir4z(r"189000", "people") # 人物
    copydir4z(r"231000", "scenery") # 风景

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def copydir3():
    xlist1 = readfileLines(r"album94479\onehot_train.txt")
    xlist2 = readfileLines(r"album94479\onehot_test.txt")
    xlist3 = readfileLines(r"album94479\onehot_valid.txt")

    def copydirx(xlist):
        labels = r"""Vehicle:vehicle
Sky:scenery
Food:food
Person:people
Building:architecture
Animal:animal
Cartoons:anime
Certificate:text
Electronic:text
Screenshot:text
BankCard:text
Mountain:scenery
Sea:scenery
Bill:text
Selfie:people
Night:night
Aircraft:vehicle
Flower:plant
Child:people
Ship:vehicle""".split()
        for line in xlist:
            name, tags = line.split()
            print(name, tags)
            tags = tags.strip().split(",")
            assert len(tags) == len(labels), name

            imgfile = os.path.join(r"D:\BaiduNetdiskDownload\album\album\img", name)
            assert os.path.exists(imgfile), imgfile

            checktag = [labels[i].split(":")[-1] for i in range(len(tags)) if tags[i] != "0"]
            if len(checktag) != 1: continue

            for i in range(len(tags)):
                if tags[i] == "0":
                    continue

                subdir = labels[i].split(":")[-1]

                xfile = imgfile
                ftype = os.path.splitext(xfile)[-1].lower()
                md5 = getFileMd5(xfile)[:7] # copydir3

                mydir = os.path.join(r"dataset", "pp2_"+subdir)
                yfile = os.path.join(mydir, "pp2_"+md5+ftype)

                if os.path.exists(yfile):
                    continue
                if not os.path.exists(mydir):
                    os.makedirs(mydir)

                copyimg(xfile, yfile)

    copydirx(xlist1)
    copydirx(xlist2)
    copydirx(xlist3)

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def checkimg(rootdir):
    fnamez = {}
    def mainfile(fpath, fname, ftype):
        if ftype in ("txt", "json"):
            return

        fnamec = fname.split(".")[0].split("_", 1)[1]
        if fnamec in fnamez:
            print("REMOVE REP", fnamez[fnamec], fpath)
            os.remove(fpath)
            return
        fnamez[fnamec] = fpath

        img = Image.open(fpath)
        width, height = img.size
        if width / height < 1/3 or height / width < 1/3 or width * height < 150 * 150:
            img.close()
            os.remove(fpath)
            print("REMOVE", (width, height), fpath)

    searchdir(rootdir, mainfile)

def main():
    if False:
        copydir(r"D:\BaiduNetdiskDownload\dataset\animals",   r"dataset\animal")
        copydir(r"D:\BaiduNetdiskDownload\dataset\food",      r"dataset\food")
        copydir(r"D:\BaiduNetdiskDownload\dataset\people",    r"dataset\people")
        copydir(r"D:\BaiduNetdiskDownload\dataset\scenery",   r"dataset\scenery")
        copydir(r"D:\BaiduNetdiskDownload\dataset\text",      r"dataset\text")

    # pp
    if False:
        copydir2(r"D:\BaiduNetdiskDownload\CADB_Dataset\images", r"dataset")

    # pp2
    # https://aistudio.baidu.com/datasetdetail/94479/
    if False:
        copydir3()

    # Corel5K
    if False:
        copydir4()

    # 百度网页
    if True:
        copydir5()

    print("ok")
    checkimg(r"dataset")

if __name__ == "__main__":
    main()
