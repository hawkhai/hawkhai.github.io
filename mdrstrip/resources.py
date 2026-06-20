#encoding=utf8
"""URL snapshot backup and local image resource handling."""
from .runtime import *
from .config import checkpage, getLinkTagSrc, isHostIgnoreStat, readFileIgnoreList

def backupUrlContent(fpath, md5src, url):
    for urlz in readFileIgnoreList("config/mdrstrip_url_ignore_ends.txt"):
        if url.endswith(urlz):
            return

    if not IGNOREERR:
        assert not url.endswith(".exe"), url
        assert not url.endswith(".zip"), url

    # 有可能挂掉的网站，都稍微做一下备份。
    fname = os.path.split(fpath)[-1]

    urligstarts = readFileIgnoreList("config/mdrstrip_url_ignore_starts.txt")
    urligstarts.extend(readFileIgnoreList("invisible/config/mdrstrip_url_ignore_starts.txt"))
    for urlz in urligstarts:
        if url.startswith(urlz):
            return
        if "[{}]{}".format(fname, url).startswith(urlz):
            return

    print(fpath, url)
    chrome = True # 可能有 js 代码，所以必须都用 Chrome 进行缓存
    chromeDialog = False
    for urlz in readFileIgnoreList("config/mdrstrip_url_chrome_dialog.txt"):
        if url.startswith(urlz):
            chromeDialog = True
    mdname = os.path.split(fpath)[-1]
    urlhostsrc = calcHost(url)
    urlhostdir = urlhostsrc.replace(":", "/")
    urlmd5 = getMd5(url)[:8]
    invdir = isInvisibleDir(fpath)

    if mdname in ("wechatdl.md",):
        return

    ttype = ".html"
    ttype = calcType(ttype, url.split(urlhostsrc)[1])
    if ttype.endswith(".md"): # 不能是这个，否则会被 Jekyll 自动格式化。
        ttype = ".html"
    if ttype in (".action",):
        ttype = ".html"

    if ttype.endswith(".pdf"): # pdf 下载
        chrome = False

    def buildlocal(ftype):
        flocal = os.path.join("backup", mdname, urlhostdir, urlmd5 + ftype)
        if invdir:
            flocal = os.path.join("invisible", flocal)
        return flocal

    mdxfile = False
    flocal = buildlocal(ttype)
    if chrome and urlhostsrc in readFileIgnoreList("config/mdrstrip_host_jekyll.txt"):
        mdxfile = True
        ttype = ".md" # 借用 Jekyll 格式化
        newlocal = buildlocal(ttype)
        if os.path.exists(flocal):
            os.rename(flocal, newlocal)
        flocal = newlocal
        ttype = ".html" # 太多了，严重影响速度，改回 html。
        newlocal = buildlocal(ttype)
        if os.path.exists(flocal):
            os.rename(flocal, newlocal)
        flocal = newlocal

    shotpath = flocal + SELENIUM
    fdata = querySnapCache(urlmd5)
    if fdata:
        writefile(flocal, fdata)
        fdatalocal = True
    else:
        if NETFAKE:
            fdata = b""
        else:
            fdata = netgetCacheLocal(url, cacheTimeout=60*60*24*1000, chrome=chrome, local=flocal, shotpath=shotpath, chromeDialog=chromeDialog)
        fdatalocal = False

    idata = bytesToString(fdata)
    if not url in readFileIgnoreList("config/mdrstrip_url_ignore.txt"):
        result = checkpage(idata)
        if result:
            print("无法访问此网站", fpath, url, result)
            if not fdatalocal: os.system(PAUSE_CMD)
            removeSnapCache(urlmd5)
            osremove(flocal)
            osremove(shotpath)
            return backupUrlContent(fpath, md5src, url)

    def addmdhead(fdata):
        xtime = formatTimeStamp(time.time())
        xurl = url
        fdata = """---
title : %(title)s
---

* TIME: %(time)s
* URL: <%(url)s>

-----

""" % { "time": xtime, "url": xurl, "title": "自动快照存档", } + fdata
        return fdata

    def ismdhead(fdata):
        return fdata and fdata.startswith("---")

    def html2md(fdata):
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        fdata = h.handle(fdata)
        return fdata.replace("{{", "{ {").replace("}}", "} }")

    # html 过大，自动切换到 mdfile
    if len(fdata) >= 1024*1000*1 and fdata.lower().find(b"<body") != -1 and fdata.lower().find(b"<html") != -1:
        mdxfile = True

    if mdxfile:
        fdata = bytesToString(fdata, "utf8")
        if fdata.lower().find("<body") != -1 and fdata.lower().find("<html") != -1:
            fdata = html2md(fdata)
            fdata = addmdhead(fdata)
            if not NETFAKE:
                writefile(flocal, fdata, "utf8")
        elif not ismdhead(fdata):
            fdata = addmdhead(fdata)
            if not NETFAKE:
                writefile(flocal, fdata, "utf8")

        if urlhostsrc == "www.shadertoy.com":
            li = refindall(r"""\r?\n\r?\n[0-9]+\r?\n\r?\n    \r?\n    \r?\n    """, fdata)
            for i in li: fdata = fdata.replace(i, NEWLINE_CHAR+"    ")
            if not NETFAKE:
                writefile(flocal, fdata, "utf8")

    fmd5 = getFileSrcMd5z(flocal, mycache=MYCACHE, assertx=False) # 大文件，错误已经铸成，改不了了。
    invdir2 = isInvisibleDir(flocal) # invdir = isInvisibleDir(fpath)
    mdrstripBigfile = os.path.join("invisible" if invdir2 else ".", "config/mdrstrip_bigfiles.txt")
    igbigfiles = readFileIgnoreList(mdrstripBigfile)
    if not fmd5 in igbigfiles and not flocal in igbigfiles:
        if len(fdata) >= 1024*1000*1 and not IGNOREERR:
            print(getFileSrcMd5z(flocal, mycache=MYCACHE, assertx=False), "#", flocal, "#", "%.1f MB"%(len(fdata) / 1024 / 1024))
            assert False, (len(fdata) / 1024.0 / 1000.0, url, flocal)

    remote = buildlocal(".html" if mdxfile else ttype).replace("\\", "/")
    touchSnapCache(urlmd5, flocal)

    # protocol :// hostname[:port] / path / [:parameters][?query]#fragment
    remotename = url.split("?")[0].split("#")[0].split("/")[-1]
    ignorenamefile = "config/mdrstrip_url_ignore_nametype.txt"
    if remotename in readFileIgnoreList(ignorenamefile):
        return remote

    # 外链类型 断言...
    if not remote.split(".")[-1] in ("pdf", "html", "git", "php", "c", "phtml", "cpp", "cxx", "htm", "shtm", "xml",
                                     "ipynb", "py", "asp", "shtml", "aspx", "xhtml", "txt", "mspx", "sh",):
        print(fpath, url)
        #openTextFile(ignorenamefile)
        #assert False, remote
    return remote

def tidyupImgClear():
    for key in G_IMG_TAGED:
        osremove(key)

def tidyupImgCollect(rootdir):
    def mainfile(fpath, fname, ftype):
        if fname.endswith(THUMBNAIL):
            if not os.path.exists(fpath[:-len(THUMBNAIL)]):
                osremove(fpath)
        else:
            G_IMG_TAGED.add(os.path.relpath(fpath, ".").lower())
    searchdir(rootdir, mainfile) # tidyupImgCollect

# 本地图片缓存路径。
def tidyupImg(imglocal, fpath, line, imgthumb=True):

    fakeimgfiles = readFileIgnoreList("config/mdrstrip_fake_image_files.txt")

    if imglocal in fakeimgfiles:
        return line

    imgdir, imgfname = os.path.split(imglocal)
    imgnocopy = os.path.join(imgdir, "imgnocopy.txt")
    if imgfname.find(".") == -1:
        imgfname = imgfname + ".jpg"
    imgtype = imgfname.split(".")[-1].lower()
    if imgtype == "mp4":
        ffmpegConvert(imglocal)

    if not COPYRES:
        assert os.path.exists(imglocal), fpath +"  "+ imglocal
        return line
    invdir = isInvisibleDir(fpath)
    fname = os.path.split(fpath)[-1]
    if fname.lower().endswith(".md"):
        fname = fname[:-3]
    if refindall("^[0-9]{4}-[0-9]{2}-[0-9]{2}-", fname):
        fname = fname[:10].replace("-", "")[-6:]+"-"+fname[11:]
    if len(fname) > 32:
        fname = fname[:30]+"~"+getMd5(fname)[:2]

    tpath = os.path.join("assets", "images", fname.lower(), imgfname) #.lower() 不能转小写，因为服务器是大小写敏感的。
    if invdir:
        tpath = os.path.join("invisible", "images", fname.lower(), imgfname) #.lower() 不能转小写，因为服务器是大小写敏感的。
    if os.path.exists(imgnocopy):
        tpath = imglocal

    if not os.path.exists(imglocal) and os.path.exists(tpath): # 貌似已经剪切过去了。
        copyfile(tpath, imglocal)
    count = 0
    while not os.path.exists(imglocal):
        if os.path.exists(imgnocopy):
            return line
        print("文件不存在", imglocal, os.path.abspath(imglocal))
        if not imgthumb: # 特殊图片，不用检测。
            return line
        count = count + 1
        if count >= 3:
            assert False, "重试次数过多..."
        os.system(PAUSE_CMD)
        fakeimgfiles = readFileIgnoreList("config/mdrstrip_fake_image_files.txt")
        if imglocal in fakeimgfiles:
            return line

    iscopy = copyfile(imglocal, tpath) # 是否图片挪窝了。
    imglocalnail = imglocal + THUMBNAIL
    tpathnail = tpath + THUMBNAIL
    isnailcopy = False
    if os.path.exists(imglocalnail):
        isnailcopy = copyfile(imglocalnail, tpathnail) # 是否缩略图挪窝了。

    if os.path.abspath(imglocal) != os.path.abspath(tpath):
        G_IMG_TAGED.add(os.path.relpath(imglocal, ".").lower())
    if os.path.relpath(tpath, ".").lower() in G_IMG_TAGED:
        G_IMG_TAGED.remove(os.path.relpath(tpath, ".").lower())

    # 同样大小的小图片先占位... lazyload
    thumbPath = tpath + THUMBNAIL
    from PIL import Image

    # 1. 明确指出不需要缩略图的情况。
    if not imgthumb:
        osremove(thumbPath)

    # 2. 创建缩略图。
    elif not os.path.exists(thumbPath) and imgtype in ("png", "jpg", "gif", "jpeg", "webp", "bmp", "jfif",):
        try:
            img = Image.open(tpath)
        except RuntimeError as ex: # could not create decoder object
            print("Image.open RuntimeError", tpath)
            raise ex
        width, height = img.size
        widthctrl = 64
        if width > widthctrl:
            try:
                # DeprecationWarning: ANTIALIAS is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.LANCZOS instead.
                imgtmp = img.resize((widthctrl, round(widthctrl*height/width)), PIL_IMAGE_SAMPLE)
                img = imgtmp.convert("RGB")
            except OSError as ex: # broken data stream when reading image file
                print("Image.resize OSError", tpath)
                raise ex
            # DeprecationWarning: ANTIALIAS is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.LANCZOS instead.
            img = img.resize((width, height), PIL_IMAGE_SAMPLE) # 恢复到原来大小，便于客户端排版。

            from PIL import ImageFont, ImageDraw # 导入模块
            draw = ImageDraw.Draw(img, "RGBA") # 修改图片
            font = ImageFont.truetype(r"assets/logos/方正楷体_GB2312.ttf", size = 20)
            draw.rectangle(((0, 0), (width, 40)), fill=(0,0,0,127))
            draw.text((10, 10), u'图片加载中, 请稍候....', fill="#ffffff", font=font)
            #img.show()
            #exit(0)

        # 小于 100K...
        img = img.convert("RGB") #.convert("L")
        img.save(thumbPath)
        appendfile(thumbPath, getFileMd5(tpath, mycache=MYCACHE, assertx=False))

    # 3. 无法创建缩略图（矢量图）。
    elif not os.path.exists(thumbPath) and imgtype in ("svg",):
        osremove(thumbPath)

    # 4. 检查缩略图。
    elif os.path.exists(thumbPath):

        srcmd5 = readfileLast(thumbPath, True, size=32)
        if getLuckFileMd5(tpath, srcmd5) != srcmd5: # 原图变化了。
            osremove(thumbPath)
            return tidyupImg(imglocal, fpath, line, imgthumb=imgthumb)

        #img = Image.open(tpath)
        #width, height = img.size
        #try:
        #    img = Image.open(thumbPath)
        #except RuntimeError as ex: # could not create decoder object
        #    print("Image.open RuntimeError", thumbPath)
        #    osremove(thumbPath)
        #    return tidyupImg(imglocal, fpath, line) # 存在问题，重新创建。

        #if img.size != (width, height): # 尺寸不对，重新创建。
        #    img.close()
        #    osremove(thumbPath)
        #    return tidyupImg(imglocal, fpath, line)

    imgtype = imgfname.split(".")[-1].lower()
    if not imgtype in ("pdf", "png", "jpg", "gif", "jpeg", "webp", "mp4", "zip", "bmp", "svg", "jfif", "webm", "avif",):
        print(imglocal, fpath, line)
        assert False, imglocal

    if iscopy: osremove(imglocal)
    if isnailcopy: osremove(imglocalnail)
    return line.replace(imglocal, tpath.replace("\\", "/"))

def collectHost(fpath, md5src, line, imgthumb):

    reflist = []
    linesrc = line[:]

    regex = "(?:\"/(.*?)\")|(?:'/(.*?)')"
    li = refindall(regex, line)
    for imglocal in li:
        imglocal = "".join(imglocal)
        if imglocal.endswith("/"):
            continue
        if len(imglocal) <= 2:
            continue

        kignore = False
        for src in ("/player.bilibili.com/",
                    "source/", "blog/", "source/shader/", "assets/glslEditor-0.0.20/",
                    "images/photo.jpg",):
            if imglocal.startswith(src):
                kignore = True
        if kignore: continue

        if os.path.isdir(imglocal):
            continue

        line = tidyupImg(imglocal, fpath, line, imgthumb=imgthumb)

    regex = r"""(
                    (https?)://
                        ([a-z0-9\.-]+\.[a-z]{2,8})
                        (:[0-9]{1,4})?
                    (/[a-z0-9\&%_\./~=+:@–-]*)?
                    (\?[a-z0-9\&%_\./~=+:\[\]-]*)?
                    (#[a-z0-9\&%_\./~=:?-]*)?
                )"""

    regex = "".join(regex.split())
    li = refindall(regex, line, re.IGNORECASE)
    if not li: return reflist, line

    iglist = readFileIgnoreList("config/mdrstrip_url_quote.txt")
    iglist.extend(readFileIgnoreList("invisible/config/mdrstrip_url_quote.txt"))

    for tx in li:
        url = tx[0]
        host = tx[2]
        checkz = line.split(url)
        for iline in checkz[1:]: # 检查网址的后继标记。
            checkli = ["", ")", "]", ">", " ", "*", "$"]
            for urlz in iglist:
                if url.startswith(urlz) and urlz:
                    checkli.append(";")
                    checkli.append("\"")
                    checkli.append("\'")
                    checkli.append("\\")
                    checkli.append("`")
            if iline[:2] in ("{{",):
                continue
            if not iline[:1] in checkli:
                print(line)
                print(url)
                assert False, (url, checkz)
        assert not url.endswith("."), fpath +" "+ url
        remote = backupUrlContent(fpath, md5src, url)
        if remote:
            reflist.append([url, remote])

        if isHostIgnoreStat(host):
            continue
        if not host in G_HOSTSET:
            G_HOSTSET[host] = 0
        G_HOSTSET[host] += 1

    xline = line[:]
    for name, host in LINKTAGARRAY:
        tak = getLinkTagSrc(name)
        xline = xline.replace(tak+"]", name+"]")
    li = refindall("<.*?>", xline)
    for tx in li:
        xline = xline.replace(tx, "")
    for name, host in LINKTAGARRAY:
        # 视频要特别标注域名。
        li1 = refindall(host, xline, re.IGNORECASE)
        li2 = refindall(name+"\\]", xline, re.IGNORECASE)
        if len(li1) == len(li2):
            continue
        if xline.find("[")==-1 and xline.find("<")==-1 and xline.find("(")==-1:
            continue
        print(xline)
        print(li1)
        print(li2)
        openTextFile(fpath)
        assert False, linesrc
    return reflist, line
