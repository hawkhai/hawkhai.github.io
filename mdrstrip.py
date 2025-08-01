#encoding=utf8
import re, os, sys
sys.path.append("../")
import datetime, time
import traceback
from urllib.parse import unquote
from coderstrip import *
from pythonx.funclib import *
from pythonx.kangxi import TranslateKangXi
from pythonx.pelib import getLuckFileMd5, get_local_ipinfo

__file__   = os.path.abspath(__file__)
if __name__ == "__main__":
    CACHEFILE = os.path.join("tempdir", "mycache", os.path.split(__file__)[-1], 'cache.db')
    print("CACHEFILE", CACHEFILE)
    MYCACHE = LocalLimitedDict(CACHEFILE, max_size=10000)
else:
    MYCACHE = None

from PIL import Image
# AttributeError: module 'PIL.Image' has no attribute 'Resampling'
PIL_IMAGE_SAMPLE = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.ANTIALIAS

# Paranoid text spacing in Python
# https://github.com/vinta/pangu.py

OPENFILE   = "openfile" in sys.argv
AUTOFORMAT = "format" in sys.argv
REBUILD    = "rebuild" in sys.argv
COPYRES    = "copyres" in sys.argv
CLEARIMG   = "clearimg" in sys.argv
IGNOREERR  = "ignoreerr" in sys.argv
OPENRESENT = "openresent" in sys.argv or "openresentx" in sys.argv
OPENRESENTx = "openresentx" in sys.argv
NETFAKE    = "netfake" in sys.argv
DEBUG = "debug" in sys.argv

# 名称，域名正则。
LINKTAGARRAY = (("bili",     "bilibili.com"),
                ("zhihu",    "zhihu.com"),
                ("cnblogs",  "cnblogs.com"),
                ("csdn",     "csdn.net"),
                ("github",   "github.com|github.io"),
                ("jianshu",  "jianshu.com"),
                ("wiki",     "wikipedia.org"),
                ("weixin",   "weixin.qq.com"),
                ("keqq",     "ke.qq.com"),
                ("scriptol", "scriptol.com"),
                ("khronos",  "khronos.org"),
                ("gluon",    "gluon.ai"),
               )

SPACEBACKFILE_TAIL = ".spaceback.json"
NEWLINE_CHAR = "\r\n" if IS_WINDOWS else "\n"
PAUSE_CMD = "pause" if IS_WINDOWS else "read -p 'Press [Enter] key to continue...'"

def getLinkTagSrc(name):
    return "{% include relref_"+name+".html %}"

def isHostIgnoreStat(hostk):
    for name, host in LINKTAGARRAY:
        if refindall("^({})$".format(host), hostk):
            return True
        if refindall("\\.({})$".format(host), hostk):
            return True
    for host in ("sunocean.life", "hawkhai.com",):
        if refindall("^({})$".format(host), hostk):
            return True
        if refindall("\\.({})$".format(host), hostk):
            return True
    return False

G_CACHE_IGLIST = {}
def readfileIglist(fpath):

    hash = "{},{},{}".format(getMd5(fpath), os.path.getsize(fpath), os.path.getmtime(fpath))
    if hash in G_CACHE_IGLIST:
        return G_CACHE_IGLIST[hash]

    li = readfile(fpath, True, "utf8").split("\n")
    li = [i.strip().split(" #")[0].strip() for i in li if i.strip().split(" #")[0].strip()]
    li = [i.strip().split("# ")[0].strip() for i in li if i.strip().split("# ")[0].strip()]
    if not IGNOREERR:
        assert li, fpath

    G_CACHE_IGLIST[hash] = li
    return li

# copyfrom E:\kSource\blog\checkcache.py
G_CHECKPAGE = []
def checkpage(fdata):
    if not G_CHECKPAGE:
        itag0 = bytesToString("ERR_CONNECTION_TIMED_OUT".encode("utf8"))
        itag1 = bytesToString("无法访问此网站".encode("utf8"))
        itag2 = bytesToString('<div class="Qrcode-title">扫码登录</div>'.encode("utf8")) # 知乎的问题
        itag3 = bytesToString('未注册手机验证后自动登录，注册即代表同意'.encode("utf8")) # 知乎的问题
        itag4 = bytesToString("其他登录方式".encode("utf8"))
        itag5 = bytesToString("其他方式登录".encode("utf8"))
        itag6 = bytesToString('name="passport_iframe" src="https://passport.csdn.net/account/login?'.encode("utf8"))
        itag7 = bytesToString('www.zhihu.com/api/v3/account/api/login/qrcode/'.encode("utf8"))
        # 垃圾广告。动力广告
        itag8 = bytesToString('pp.chuzushijian.cn'.encode("utf8"))
        itag9 = bytesToString('动力广告'.encode("utf8"))

        itag10 = bytesToString('<title>404 Not Found</title>'.encode("utf8"))
        itag11 = bytesToString('<title>隐私设置错误</title>'.encode("utf8"))
        itag12 = bytesToString('网站在更新其安全设置期间可能会经常显示警告。此问题应该很快就会得到改进。'.encode("utf8"))
        itag13 = bytesToString('<h1>您的连接不是私密连接</h1>'.encode("utf8"))
        itag14 = bytesToString('出现此问题的原因可能是配置有误或您的连接被拦截了。'.encode("utf8"))

        G_CHECKPAGE.extend((itag0, itag1, itag2, itag3, itag4, itag5, itag6, itag7, itag8, itag9,
                            itag10, itag11, itag12, itag13, itag14))

    for itag in G_CHECKPAGE:
        if fdata.find(itag) != -1:
            return itag
    return None

def backupUrlContent(fpath, md5src, url):
    for urlz in readfileIglist("config/mdrstrip_url_ignore_ends.txt"):
        if url.endswith(urlz):
            return

    if not IGNOREERR:
        assert not url.endswith(".exe"), url
        assert not url.endswith(".zip"), url

    # 有可能挂掉的网站，都稍微做一下备份。
    fname = os.path.split(fpath)[-1]

    urligstarts = readfileIglist("config/mdrstrip_url_ignore_starts.txt")
    urligstarts.extend(readfileIglist("invisible/config/mdrstrip_url_ignore_starts.txt"))
    for urlz in urligstarts:
        if url.startswith(urlz):
            return
        if "[{}]{}".format(fname, url).startswith(urlz):
            return

    print(fpath, url)
    chrome = True # 可能有 js 代码，所以必须都用 Chrome 进行缓存
    chromeDialog = False
    for urlz in readfileIglist("config/mdrstrip_url_chrome_dialog.txt"):
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
    if chrome and urlhostsrc in readfileIglist("config/mdrstrip_host_jekyll.txt"):
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
    if not url in readfileIglist("config/mdrstrip_url_ignore.txt"):
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
    igbigfiles = readfileIglist(mdrstripBigfile)
    if not fmd5 in igbigfiles and not flocal in igbigfiles:
        if len(fdata) >= 1024*1000*1 and not IGNOREERR:
            print(getFileSrcMd5z(flocal, mycache=MYCACHE, assertx=False), "#", flocal, "#", "%.1f MB"%(len(fdata) / 1024 / 1024))
            assert False, (len(fdata) / 1024.0 / 1000.0, url, flocal)

    remote = buildlocal(".html" if mdxfile else ttype).replace("\\", "/")
    touchSnapCache(urlmd5, flocal)

    # protocol :// hostname[:port] / path / [:parameters][?query]#fragment
    remotename = url.split("?")[0].split("#")[0].split("/")[-1]
    ignorenamefile = "config/mdrstrip_url_ignore_nametype.txt"
    if remotename in readfileIglist(ignorenamefile):
        return remote

    # 外链类型 断言...
    if not remote.split(".")[-1] in ("pdf", "html", "git", "php", "c", "phtml", "cpp", "cxx", "htm", "shtm", "xml",
                                     "ipynb", "py", "asp", "shtml", "aspx", "xhtml", "txt", "mspx", "sh",):
        print(fpath, url)
        openTextFile(ignorenamefile)
        assert False, remote
    return remote

G_IMG_TAGED = set() # 图片资源等。
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

    fakeimgfiles = readfileIglist("config/mdrstrip_fake_image_files.txt")

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
        fakeimgfiles = readfileIglist("config/mdrstrip_fake_image_files.txt")
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

G_HOSTSET = {}
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

    iglist = readfileIglist("config/mdrstrip_url_quote.txt")
    iglist.extend(readfileIglist("invisible/config/mdrstrip_url_quote.txt"))

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

# 语法高亮的 tag 检查。
def loadRougifyList():
    ROUGIFY_LIST_FILE = "config/rougify_list_json.txt"
    ROUGIFY_LIST = readfileJson(ROUGIFY_LIST_FILE)
    if not ROUGIFY_LIST:
        ROUGIFY_LIST_SRC = readfile("config/rougify_list.txt", True)
        ROUGIFY_LIST = refindall("\n([^\\s:]+):", ROUGIFY_LIST_SRC, re.MULTILINE)
        ROUGIFY_LIST2 = refindall("\\[\\s*aliases\\s*:(.*?)\\]", ROUGIFY_LIST_SRC)
        for temp in ROUGIFY_LIST2:
            temp = temp.strip().split(",")
            for itemp in temp:
                itemp = itemp.strip()
                if not itemp: continue
                ROUGIFY_LIST.append(itemp)
        assert len(ROUGIFY_LIST) == 366, len(ROUGIFY_LIST)
        writefileJson(ROUGIFY_LIST_FILE, ROUGIFY_LIST)
        for i in ROUGIFY_LIST:
            assert refindall("^([0-9a-z_#+-]+)$", i, re.IGNORECASE), i
    return ROUGIFY_LIST

G_CNCHAR = []
G_CSCHAR = [] # 中文符号集合
G_ENCHAR = []
G_TYPESET = set()
G_MDKEYSET = set()
SNAPSHOT_HTML = "<font class='ref_snapshot'>参考资料快照</font>"
REVIEW_REGEX  = "^<p class='reviewtip'><script type='text/javascript' src='{% include relrefx?.html url=\".*?\" %}'></script></p>$"
REVIEW_FORMAT = "<p class='reviewtip'><script type='text/javascript' src='{%% include relref.html url=\"/%s.js\" %%}'></script></p>"
REVIEW_LINE   = "<hr class='reviewline'/>"
REVIEW_JS_PATH = "%s.js"
ROUGIFY_LIST = loadRougifyList()

def removeRefs(fpath, lines):
    lineCount = len(lines)
    headIndex = -1
    for index in range(lineCount):
        i = lineCount-1 - index
        if not lines[i] or not lines[i].strip():
            continue
        if refindall("^- \\[{}\\]\\({}\\)$".format(".*?", ".*?"), lines[i]): # \\[[0-9]+\\]
            continue
        if lines[i] == SNAPSHOT_HTML:
            headIndex = i
            break
        break

    if headIndex != -1:
        assert lines[headIndex-1] == "" or refindall(REVIEW_REGEX, lines[headIndex-1]), "%r"%lines[headIndex-1]
        if lines[headIndex-2] in ("-----", REVIEW_LINE): #, "%r"%lines[headIndex-2]
            assert lines[headIndex-3] == "", "%r"%lines[headIndex-3]
            lines = lines[:headIndex-3]
        else: # 没有 REVIEW_REGEX 的情况。
            if lines[headIndex-2] == "": #, "%r"%lines[headIndex-2]
                lines = lines[:headIndex-2]
            else:
                lines = lines[:headIndex-1]
    else:
        while lines and (lines[-1] in ("", "-----", REVIEW_LINE) or
                refindall(REVIEW_REGEX, lines[-1])):
            lines = lines[:-1]
    return lines

def appendRefs(fpath, md5src, lines, imgthumb, mdconfig):
    reflist = []

    for index, line in enumerate(lines):
        ireflist, line = collectHost(fpath, md5src, line, imgthumb)
        lines[index] = line
        if ireflist:
            reflist.extend(ireflist)

    invdir = isInvisibleDir(fpath)
    fpath = os.path.relpath(fpath, ".")
    frelgit = fpath
    if os.path.exists(fpath+".tempd"): # 存在加密版本。
        frelgit = fpath+".tempd"

    def getDateStr(frelgit):
        # 获取 md 文件的最后修改时间。
        cmdx = 'git log -n 1 --pretty=format:"%ad" --date=short -- "{}"'.format(frelgit)
        if invdir:
            cmdx = 'cd {} & git log -n 1 --pretty=format:"%ad" --date=short -- "{}"'.format(*frelgit.split(os.sep, 1))
        if invdir and IS_MACOS:
            cmdx = 'cd {} && git log -n 1 --pretty=format:"%ad" --date=short -- "{}" && cd ..'.format(*frelgit.split(os.sep, 1))

        try:
            datestr = popenCmd(cmdx)
            datestr = bytesToString(datestr)
        except FileNotFoundError: # [Errno 2] No such file or directory: 'cd invisible && git log -n 1 --pretty=format:"%ad" --date=short -- "ncnn/onnxruntime-for-win7/README_EN.md" && cd ..'
            datestr = None
        if not datestr:
            datestr = datetime.datetime.now().date()
        return datestr

    if fpath.startswith("_posts"+os.sep):
        fpath = os.path.join("blogs", fpath.split(os.sep)[-1])
    if invdir:
        fpath = "invisible"+os.sep+"reviewjs"+os.sep+ fpath[len("invisible"+os.sep):]
    else:
        fpath = "assets"+os.sep+"reviewjs"+os.sep + fpath

    reviewjs = REVIEW_JS_PATH % (fpath)
    fcode = readfile(reviewjs, True)
    fcheck = refindall("[0-9a-f]{32}", fcode)
    if fcheck and md5src == fcheck[0]:
        pass
    else:
        fcode = """document.write("%s: review"); // md5src=%s%s""" % (
                getDateStr(frelgit), md5src, NEWLINE_CHAR)
        writefile(reviewjs, fcode)
    review = REVIEW_FORMAT % (fpath.replace("\\", "/"))
    assert refindall(REVIEW_REGEX, review), review

    if "sortrefs: true" in lines:
        reflist = sorted(reflist, key=lambda x: x[1], reverse=False)

    if reflist:
        lines.append("")
        lines.append("")
        if mdconfig:
            lines.append(REVIEW_LINE)
            lines.append(review)
        lines.append(SNAPSHOT_HTML)
        lines.append("")
        lines.append("")
        urlset = set()
        count = 0
        for url, remote in reflist:
            if url in urlset: continue
            urlset.add(url)
            count = count + 1
            if mdconfig:
                remote = "{% " + ("include relrefx.html url=\"/%s\"" % (remote,)) + " %}"
                lines.append("- [{}]({})".format(url, remote)) # count
            else:
                lines.append("- [{}]({})".format(url, url)) # count
        lines.append("")
    else:
        if mdconfig:
            lines.append("")
            lines.append("")
            lines.append(REVIEW_LINE)
            lines.append(review)
            lines.append("")
    return lines

def mainfile(fpath, fname, ftype, fdepth=0):

    if fpath.endswith(SPACEBACKFILE_TAIL):
        fjson = readfileJson(fpath, "utf8")
        writefileJson(fpath, fjson, ascii=False, encoding="utf8")
        return

    iglist = readfileIglist("config/mdrstrip_file_ignore.txt")
    if fname in iglist:
        return

    fpathsrc, fnamesrc, ftypesrc = fpath, fname, ftype
    checkfilesize(fpath, fname, ftype)

    ftype = ftype.lower()
    errcnt = 0

    warnCnEnSpace    = ftype in ("md", "php", "html", "htm", "vsh", "fsh",) # 英文中文空符检查
    warnTitleSpace   = ftype in ("md",) # 标题前后空行检查
    warnIndentSpace  = ftype in ("md", "php", "scss", "vsh", "fsh",) # 缩进检查
    isMdFile         = ftype in ("md",)
    isSrcFile        = ftype in ("md", "php", "html", "htm", "js", "css", "scss", "svg", "py", "vsh", "fsh",)
    keepStripFile    = ftype in ("svg",) or fname in ("gitsrc.html",) or refindall("^relref[a-z_]*\\.html$", fname)
    keepFileTypeList = ("rar", "zip", "pdf", "doc", "mp4",) # 中英文间隔，容易造成失误的列表。

    if fpath.find(os.sep+"winfinder"+os.sep) != -1:
        isSrcFile = isSrcFile or ftype in ("h", "cpp", "cxx", "rc", "c",)

    if not isSrcFile:
        if fpath.find(os.sep+"_site"+os.sep) != -1: # 必须在 _site 文件夹?
            G_TYPESET.add(ftype)
        return

    mdconfig = {}
    if isMdFile:
        # 收集 Jekyll 头定义 key 集合。
        fdata = readfile(fpath, True).strip()
        if fdata.startswith("---"):
            kvlist = fdata.split("---")[1].strip().split("\n")
            for kv in kvlist:
                kv = kv.strip()
                key, value = kv.split(":", 1)
                key = key.strip()
                value = value.strip()
                G_MDKEYSET.add(key)
                mdconfig[key] = value

    if fpath.find(os.sep+"_site"+os.sep) != -1: # _site 文件夹
        return

    def linerstrip(line):
        if isMdFile:
            for name, host in LINKTAGARRAY:
                tak = getLinkTagSrc(name)
                # 移除多余空格
                line = line.replace("  "+tak+"]", tak+"]")
                line = line.replace(" "+tak+"]", tak+"]")
                # 格式化。
                line = line.replace(tak+"]", " "+tak+"]")
                line = line.replace(name+"]", tak+"]")
                line = line.replace("[ "+tak+"]", "["+name+" "+tak+"]")
            line = line.replace(" ——", "——").replace(" ——", "——")
            line = line.replace("—— ", "——").replace("—— ", "——")
            line = line.replace("——", " —— ")
        return line.rstrip()

    print(fpath)
    if IS_MACOS or IS_LINUX:
        fdata = readfile(fpath)
        fdata = fdata.replace(b"\r\n", b"\n").replace(b"\r", b"\n").replace(b"\n", b"\r\n")
        writefile(fpath, fdata)
    md5src = getFileMd5(fpath, mycache=MYCACHE, assertx=False) # mainfile
    try:
        lines = readfileLines(fpath, False, False, "utf8")
    except Exception as ex:
        openTextFile(fpath)
        raise ex
    lines = removeRefs(fpath, lines)
    lines = [linerstrip(line) for line in lines]
    lines.append("")
    lines.append("")
    while len(lines) >= 2 and not lines[-1] and not lines[-2]:
        lines = lines[:-1]
    while len(lines) >= 1 and not lines[0]:
        lines = lines[1:]

    if keepStripFile:
        while len(lines) >= 1 and not lines[-1]:
            lines = lines[:-1]

    if isMdFile:

        imgthumb = True
        lineCount = 0
        for line in lines:
            if line.strip() == "---":
                lineCount = lineCount + 1
                if lineCount >= 2: break
            if "".join(line.strip().lower().split()) == "imgthumb:false":
                imgthumb = False
                break
            # 避免格式化的文件。
            if "".join(line.strip().lower().split()) == "codeformat:false":
                return

        try:
            lines = appendRefs(fpath, md5src, lines, imgthumb, mdconfig)
        except AssertionError as ex:
            if fdepth >= 5:
                raise ex
            openTextFile(fpath)
            traceback.print_exc()
            print("断言错误 {}".format(ex,))
            os.system(PAUSE_CMD)
            return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

    # .spaceback.json
    spacebackfile = (os.path.splitext(fpath)[0] + SPACEBACKFILE_TAIL)
    spacebackjson = {}
    if not os.path.exists(spacebackfile):
        spacebackfile = os.path.join(os.path.split(fpath)[0], "k"+os.path.splitext(fname)[0]+SPACEBACKFILE_TAIL)
    if os.path.exists(spacebackfile):
        spacebackjson = readfileJson(spacebackfile, "utf8")

    codestate = False
    chartstate = False
    for index, line in enumerate(lines):

        for kftype in keepFileTypeList:
            line = line.replace(" ."+kftype, "."+kftype)
            lines[index] = line

        if isMdFile and line.count("**") >= 2 and line.count("**") % 2 == 0 and line.count("***") == 0 and not codestate:
            dotlines = line.split("**")
            newline = ""
            for idx, dot in enumerate(dotlines):
                if idx % 2 == 1:
                    if not newline.strip():
                        newline = newline + "**" + dot.strip() + "** "
                    else:
                        newline = newline.rstrip() + " **" + dot.strip() + "** "
                else:
                    if idx >= 2:
                        newline += dot.lstrip()
                    else:
                        newline += dot
            newline = newline.rstrip()
            line = newline
            lines[index] = line

        line = line.replace("````", "```").replace("````", "```")
        linxCount = line.count("`")
        if isMdFile and linxCount >= 2 and linxCount % 2 == 0:
            newline = ""
            linxCount = 0
            for idx, ch in enumerate(line):
                if ch == '`':
                    linxCount = linxCount + 1
                    if linxCount % 2 == 1:
                        if newline and not newline.endswith(" "):
                            if not newline.endswith("："):
                                newline += " "
                            newline += "`"
                        else:
                            if newline.endswith("： "):
                                newline = newline[:-1]
                            newline += "`"
                    else:
                        newline += "`"
                        if idx+1 < len(line) and line[idx+1] != " ":
                            newline += " "
                else:
                    newline += ch
            line = newline
            lines[index] = line

        preline = lines[index - 1] if index > 0 else ""
        nextline = lines[index + 1] if index < len(lines)-1 else ""

        # ```java
        # {% highlight ruby %}
        # https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers
        li1 = refindall("```\\s*([0-9a-z_#+-]+)", line, re.IGNORECASE)
        li2 = refindall("\\{%\\s*highlight\\s*([0-9a-z_#+-]+)", line, re.IGNORECASE)
        li1.extend(li2)
        for i in li1:
            if not i in ROUGIFY_LIST:
                openTextFile(fpath)
                print("代码语言无法识别 {}:{} \"{}\"".format(fpath, index+1, i))
                os.system(PAUSE_CMD)
                return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

        tagregex = "^\\s*[#]+\\s"
        prelinetag = refindall(tagregex, preline)
        nextlinetag = refindall(tagregex, nextline)
        if warnTitleSpace and not codestate:
            tagregexk = "^\\s*[#]+\\s{2,}" # md 文件标题后接的空格 只能是一个。
            if refindall(tagregexk, preline):
                openTextFile(fpath)
                assert False, preline

        if refindall("^\\s*[*-]+\\s", line):
            idtcnt = 2 # 如果在列表里面，缩进检查 2 个为单位。
        else:
            idtcnt = 4

        cnsign  = "‘’“”" # 中文符号
        cnregex = "\u4e00-\u9fa5" # 中文汉字
        # 统计出现的字符。
        for ch in line:
            ordch = ord(ch)
            regch = "\\u%04x"%(ordch)
            if ordch <= 0x7F or isDiacritic(ch):
                G_ENCHAR.append(ch) # 英文
                continue
            if ordch >= 0x4e00 and ordch <= 0x9fa5:
                if cnregex.find(regch) == -1:
                    cnregex += regch # 中文汉字
                if G_CNCHAR.count(ch) == 0:
                    G_CNCHAR.append(ch)
            else:
                if cnsign.find(regch) == -1:
                    cnsign += regch # 中文符号
                if G_CSCHAR.count(ch) == 0:
                    G_CSCHAR.append(ch)
        cnregexc = cnregex[:]
        cnregex += cnsign # 中文汉字符号都来起。

        # 1.不间断空格\u00A0,主要用在office中,让一个单词在结尾处不会换行显示,快捷键ctrl+shift+space;
        # 2.半角空格(英文符号)\u0020,代码中常用的;
        # 3.全角空格(中文符号)\u3000,中文文章中使用;
        # 不能出现全角的空格。
        # utf8：20 c2a0 e38080 "\xa0"
        if line.find("\u00A0") != -1 and line.find("\u3000") != -1 and not fname in ("glslEditor.min.js",):
            print("xspace", fpath, line)
            errcnt += 1

        #liw = refindall("[{}]+".format(cnregex,), line, re.IGNORECASE)
        #lia = refindall("[^{}]+".format(cnregex,), line, re.IGNORECASE)

        linec = line
        for itmp in refindall("\\$\\$.*?\\$\\$", line): # 忽略数学公式
            linec = linec.replace(itmp, " ") # "$$$$")
        for itmp in refindall("“.*?”", line): # 忽略双引号
            linec = linec.replace(itmp, " ") # "“”")
        for itmp in refindall("`.*?`", line): # 忽略代码部分
            linec = linec.replace(itmp, " ") # "“”")

        # 忽略特殊的 tag 标记。
        for itmp in ('"WEB前端"',):
            linec = linec.replace(itmp, "\"\"")

        # 图片 caption 不校验空格。
        linec = linec.replace('caption="', 'caption=" ')
        linec = linec.replace('caption2="', 'caption2=" ')
        linec = linec.replace('title="', 'title=" ')

        lix1 = refindall("[{}][^{} *]".format(cnregex, cnregex), linec, re.IGNORECASE)
        lix2 = refindall("[^{} *][{}]".format(cnregex, cnregex), linec, re.IGNORECASE)
        lix = []
        lix.extend(lix1)
        lix.extend(lix2)

        cnsignregex = "[{}]".format(cnsign)
        for ix in lix:
            cx, cy = ix
            # 其中一个是中文符号。
            if refindall(cnsignregex, cy) or refindall(cnsignregex, cx):
                continue
            if cy in "-<]~" or cx in "->[~":
                continue

            if chartstate:
                continue

            if cx in ("\"", "[") and (" "+line).count(" "+ix) == 1:
                continue
            if cy in ("\"", "]", ",") and (line+" ").count(ix+" ") == 1:
                continue

            if cx in ("(", ) and (" \\"+line).count(" \\"+ix) == 1:
                continue
            if cy in ("\\", ) and (line+") ").count(ix+") ") == 1:
                continue

            if cx in ("\"",) and ("["+line).count("["+ix) == 1:
                continue
            if cy in ("\"",) and ((line+"]").count(ix+"]") == 1 or (line+",").count(ix+",") == 1):
                continue

            tagcontinue = False
            for kftype in keepFileTypeList:
                if cy in (".",) and (line.count(ix+kftype) == 1):
                    tagcontinue = True
            if tagcontinue: continue

            if not warnCnEnSpace:
                continue

            if codestate:
                if cy in "\":" or cx in "\":":
                    continue

                if line.startswith("print ("):
                    continue

            print("[%d]"%(index+1), ix, cx, cy, "\t", line)
            errcnt += 1
            if AUTOFORMAT:
                line = line.replace(ix, cx+" "+cy)
                lines[index] = line

        # 检查中文问本里面不应该出现的英文符号。
        if isMdFile:
            lixyx = refindall("[{}] [,()] [{}]".format(cnregex, cnregex), linec, re.IGNORECASE)
            lixyx.extend(refindall("[{}] [,()]$".format(cnregex), linec, re.IGNORECASE))
            lixyx.extend(refindall("[{}][,;] [{}]".format(cnregexc, cnregexc), linec, re.IGNORECASE))
            if lixyx:
                openTextFile(fpath)
                print(lixyx)
                print("中文符号问题 {}:{} \"{}\"".format(fpath, index+1, linec))
                os.system(PAUSE_CMD)
                return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

        fxline = "".join(line.split())
        if fxline.startswith("<divclass=\"mermaid\"") and not chartstate:
            chartstate = True
        if fxline.startswith("</div>") and chartstate:
            chartstate = False

        if fxline.startswith("{%highlight"):
            codestate = True
            continue
        if fxline.startswith("{%endhighlight%}"):
            codestate = False
            continue

        if fxline.startswith("```") and not codestate:
            codestate = True
            continue
        if fxline.startswith("```") and codestate:
            codestate = False
            continue

        # 代码规范问题，需要有空格。
        if isMdFile and (line.lower().replace("endif", "x").find("if(") != -1 or line.lower().find("while(") != -1):
            openTextFile(fpath)
            print("'if(' & 'while(' 问题 {}:{} \"{}\"".format(fpath, index+1, line))
            os.system(PAUSE_CMD)
            return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

        if codestate:
            continue

        if warnTitleSpace and (prelinetag or nextlinetag):
            if line:
                openTextFile(fpath)
                print("标题前后空行问题 {}:{} \"{}\"".format(fpath, index+1, line))
                os.system(PAUSE_CMD)
                return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

        countspace = getLeftSpaceCount(line if warnIndentSpace else line.replace("\t", " "*4))
        if countspace > 12 or countspace % idtcnt == 0 or countspace in (3,):
            pass # ok
        elif warnIndentSpace:
            openTextFile(fpath)
            print("空格缩进问题 {}:{} \"{}\"".format(fpath, index+1, line))
            os.system(PAUSE_CMD)
            return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

    assert not codestate # 断言代码片段闭合。

    page = NEWLINE_CHAR.join(lines)
    while page.find(NEWLINE_CHAR * 3) != -1:
        page = page.replace(NEWLINE_CHAR * 3, NEWLINE_CHAR * 2)

    page = page.replace(NEWLINE_CHAR+REVIEW_LINE, NEWLINE_CHAR*3+REVIEW_LINE)
    codereg = "\\{\\%\\s*highlight.*?\\{\\%\\s*endhighlight\\s*\\%\\}"
    codeli1 = refindall(codereg, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)

    coderegz = "```.*?```"
    codeli1z = refindall(coderegz, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)

    if warnTitleSpace:
        page = page.replace(NEWLINE_CHAR*2+"### ", NEWLINE_CHAR*3+"### ")
        page = page.replace(NEWLINE_CHAR*2+"## ",  NEWLINE_CHAR*3+"## ")
        page = page.replace(NEWLINE_CHAR*2+"# ",   NEWLINE_CHAR*3+"# ")

    # 代码里面的替换要还原。
    codeli2 = refindall(codereg, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)
    for i in range(len(codeli1)):
        page = page.replace(codeli2[i], codeli1[i])
    # 代码里面的替换要还原。
    codeli2z = refindall(coderegz, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)
    for i in range(len(codeli1z)):
        page = page.replace(codeli2z[i], codeli1z[i])

    # 移除康熙编码，会造成乱码。
    if not fname in ("2021-03-14-Equivalent-Unified-Ideograph.md",):
        page = TranslateKangXi(page)

    def spacebackreg(regkey, regmap, page):
        li = re.findall(regkey, page)
        if not li: return page
        for i in li:
            ix = i
            for ik in regmap.keys():
                ix = ix.replace(ik, regmap[ik])
            page = page.replace(i, ix)
        return page
    for spacebackkey in spacebackjson.keys():
        spacebackvalue = spacebackjson[spacebackkey]
        if spacebackkey == "regex":
            for regkey in spacebackvalue.keys():
                regmap = spacebackvalue[regkey] # 字典
                page = spacebackreg(regkey, regmap, page)
            continue
        page = page.replace(spacebackkey, spacebackvalue)

    # 时间过长，如果被手工改了，这里会形成覆盖。
    md5src2 = getLuckFileMd5(fpath, md5src)
    if md5src2 == md5src:
        if not writefile(fpath, page.encode("utf8")):
            return 0
        return errcnt

    print("文本中途被改过了。{}".format(fpath,))
    os.system(PAUSE_CMD)
    return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

def viewchar(lichar, xfile, xmin, xmax):
    li = list(set("".join(lichar)))
    li.sort()
    page = ""
    minv, maxv = 1024, 0
    for index, tchar in enumerate(li):
        page += tchar
        if (index + 1) % 50 == 0:
            page += NEWLINE_CHAR
        if isDiacritic(tchar):
            continue
        minv = min(minv, ord(tchar))
        maxv = max(maxv, ord(tchar))
    tempfile = os.path.join("tempdir", xfile)
    writefile(tempfile, page.encode("utf8"))

    if OPENFILE:
        openTextFile(tempfile)
    print(minv, maxv)
    print([("%04x"%ord(k), k) for k in li[:5]]),
    print([("%04x"%ord(k), k) for k in li[-5:]])
    assert xmin <= minv and maxv <= xmax

def mainfilew(fpath, fname, ftype):

    #if fname not in ("layout.md", "README.md"):
    #    return

    if not REBUILD and checklog(__file__, fpath):
        # print("cached", fpath)
        return 0

    if "only" in sys.argv:
        if not fname in sys.argv:
            return 0

    removelog(__file__, fpath)
    errcnt = mainfile(fpath, fname, ftype)
    if errcnt == 0:
        savelog(__file__, fpath)
    return errcnt

G_CHECKTINUE_SET = {}

def oncheckdirectory(rootdir, basename=None):
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

def checkfilesize(fpath, fname, ftype):
    # 原图不存在了，要移除缩略图。
    if fname.endswith(THUMBNAIL):
        srcimg = fpath[:-len(THUMBNAIL)]
        if not os.path.exists(srcimg):
            osremove(fpath)
            return

    if not oncheckdirectory(os.path.split(fpath)[0]):
        return

    invdir = isInvisibleDir(fpath)
    mdrstripBigfile = os.path.join("invisible" if invdir else ".", "config/mdrstrip_bigfiles.txt")
    fmd5 = getFileSrcMd5z(fpath, mycache=MYCACHE, assertx=False) # checkfilesize

    igbigfiles = readfileIglist(mdrstripBigfile)
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

def mainw():
    print(parsePythonCmdx(__file__))
    timea = time.time()
    main()
    removedirTimeout("tempdir")
    cleardirEmpty("tempdir")
    timeb = time.time()
    print("Total Time =", timeb - timea)

def main():
    buildSnapCache("backup")
    buildSnapCache("invisible"+os.sep+"backup")
    if REBUILD or OPENRESENT:
        checkReviewJS("assets"+os.sep+"reviewjs", ".")
        checkReviewJS("invisible"+os.sep+"reviewjs", "invisible")
    if CLEARIMG:
        tidyupImgCollect("assets"+os.sep+"images")
        tidyupImgCollect("invisible"+os.sep+"images")

    igdirs = readfileIglist("config/mdrstrip_dir_ignore.txt")

    CHECK_IGNORE_LIST = [
        "backup", "tempdir", "_site",
        "Debug", "Release", ".vs", "opengl-3rd", "opengles3-book", "opengles-book-samples",
        "UserDataSpider", "docs.gl", "ml-notes", "ksample", "dataset", "pdfdata", "imgclassify", "ksample",
        "node_modules",
        ]
    CHECK_IGNORE_LIST.extend(igdirs)
    searchdir(".", checkfilesize, ignorelist=CHECK_IGNORE_LIST, onDirectory=oncheckdirectory)
    searchdir("backup", checkfilesize, ignorelist=CHECK_IGNORE_LIST, onDirectory=oncheckdirectory)
    searchdir("invisible"+os.sep+"backup", checkfilesize, ignorelist=CHECK_IGNORE_LIST, onDirectory=oncheckdirectory)

    MAINW_IGNORE_LIST = [
        "backup", "tempdir",
        "Debug", "Release", ".vs", "opengl-3rd", "opengles3-book", "opengles-book-samples",
        "UserDataSpider", "docs.gl", "ml-notes", "ksample", "dataset", "pdfdata", "imgclassify", "ksample",
        "openglcpp", "d2l-zh", "mathjax", "msgboard",
        "node_modules",
        ]
    MAINW_IGNORE_LIST.extend(igdirs)
    searchdir(".", mainfilew, ignorelist=MAINW_IGNORE_LIST, reverse=True)
    if REBUILD:
        clearSnapCache()
        cleardirEmpty("images")
        cleardirEmpty("source")
        tidyupImgClear()

    global G_CSCHAR
    global G_TYPESET

    viewchar(G_CNCHAR, "cnfile.txt", 0x80, 0x7FFFFFFF)
    viewchar(G_CSCHAR, "csfile.txt", 0x80, 0x7FFFFFFF)
    viewchar(G_ENCHAR, "enfile.txt", 0x0,  0x7F)

    print(LINE_SEP_SHORT)
    G_CSCHAR = list(set(G_CSCHAR))
    G_CSCHAR.sort()
    print("".join(G_CSCHAR))
    imgset  = ("jpeg", "jpg", "png", "gif", "bmp", "jfif")
    fontset = ("eot", "ttf", "woff", "svg", "woff2", )
    codeset = ("cc", "js", "txt", "xml", "css", "mk", "lock", "zip", "makefile", "scss",)
    G_TYPESET -= set(imgset)
    G_TYPESET -= set(fontset)
    G_TYPESET -= set(codeset)
    print(G_TYPESET)
    print(G_MDKEYSET)

    hostlist = sorted(G_HOSTSET.items(), key=lambda x: x[1], reverse=True)
    print(hostlist)
    for hostx in hostlist[:10]:
        print(hostx)

if __name__ == "__main__":
    print(sys.argv)
    import cProfile
    if len(sys.argv) >= 2 and os.path.isdir(sys.argv[1]):
        workdir = sys.argv[1]
        @CWD_DIR_RUN(workdir)
        def maingo():
            cProfile.run("mainw()") if DEBUG else mainw()
        maingo()
    else:
        cProfile.run("mainw()") if DEBUG else mainw()
        os.system(r"cd invisible & {} tempd.py encrypt".format(getPythonExe(),))
    if MYCACHE: MYCACHE.del_impl()
    del MYCACHE
    print(parsePythonCmdx(__file__))
