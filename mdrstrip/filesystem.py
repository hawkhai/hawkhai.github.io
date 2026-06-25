#encoding=utf8
"""Directory checks, large-file guards, and review-js maintenance."""
from .runtime import *
from .config import readFileIgnoreList

def onCheckDirectory(rootdir, basename=None):
    if rootdir in G_CHECKTINUE_SET.keys():
        return G_CHECKTINUE_SET[rootdir]
    curdir = rootdir
    for i in range(10):
        imgnocheck = os.path.join(curdir, "imgnocheck.txt")
        if os.path.exists(imgnocheck):
            G_CHECKTINUE_SET[rootdir] = False
            return False
        # 已经到 git 根目录了。
        if os.path.exists(os.path.join(curdir, ".git")):
            break
        curdir = os.path.split(curdir)[0]
    G_CHECKTINUE_SET[rootdir] = True
    return True

def checkFileSize(fpath, fname, ftype):
    # 原图不存在了，要移除缩略图。
    if fname.endswith(THUMBNAIL):
        srcimg = fpath[:-len(THUMBNAIL)]
        if not os.path.exists(srcimg):
            osremove(fpath)
            return

    if not onCheckDirectory(os.path.split(fpath)[0]):
        return

    invdir = isInvisibleDir(fpath)
    mdrstripBigfile = os.path.join("invisible" if invdir else ".", "config/large-files.txt")
    fmd5 = getFileSrcMd5z(fpath, mycache=MYCACHE, assertx=False) # checkFileSize

    igbigfiles = readFileIgnoreList(mdrstripBigfile)
    if not (fmd5 in igbigfiles) and not (fpath in igbigfiles):
        size = os.path.getsize(fpath) / 1024.0 / 1000.0 # 1000 KB
        if size >= 1.0:
            print(getFileSrcMd5z(fpath, mycache=MYCACHE, assertx=False), "#", fpath, "#", "%.1f MB"%size)

            if ftype in ("gif",) and IS_WINDOWS:
                from pythonx import pygrab
                pygrab.gifbuildwebp(fpath)

            if not IGNOREERR and fpath.find(os.sep+"_site"+os.sep) == -1: # 规避 _site 文件夹
                openTextFile(mdrstripBigfile)
                assert False, "大文件最好不要入库..."

def findPostMdFile(rootdir, fnamek):
    fpathk = fnamek
    def mainfile(fpath, fname, ftype):
        if fname == fnamek:
            nonlocal fpathk
            assert fpathk == fnamek # 没有被赋值过。
            fpathk = fpath
    searchdir(rootdir, mainfile) # findPostMdFile
    return fpathk

def checkReviewJS(jsdir, rootdir):
    def mainfile(fpath, fname, ftype):
        assert fname.endswith(".md.js"), fname
        jsfile = os.path.relpath(fpath, jsdir)
        mdfile = jsfile[:-len(".js")]
        if mdfile.startswith("blogs"+os.sep):
            mdfile = findPostMdFile("_posts", mdfile.split(os.sep)[-1])
            mdfile = os.path.relpath(mdfile, rootdir)
        mdfile = os.path.join(rootdir, mdfile)
        if not os.path.exists(mdfile):
            osremove(fpath)
        elif OPENRESENT:
            jsdata = readfile(fpath, True).strip() # document.write("2021-12-06: review");
            jsy, jsm, jsd = refindall("[0-9]+", jsdata)[:3]
            today = datetime.date.today()
            jsday = datetime.date(int(jsy), int(jsm), int(jsd))
            xday = today - jsday
            print(type(xday), xday, xday.days)
            if xday.days <= (30 if OPENRESENTx else 15):
                openTextFile(mdfile)
    searchdir(jsdir, mainfile) # checkReviewJS
