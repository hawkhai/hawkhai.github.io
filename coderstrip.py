#encoding=utf8
import re, os, sys
sys.path.append("../")
from pythonx.funclib import *

# 在西歐、北歐及東歐國家常用的字母，帶變音符，和一般英文字母不同。
DIACRITIC = """
À Á Â Ã Ä Å Æ Ā Ă Ą
Ç Ć Ĉ Ċ
Ð Ď Đ
È É Ê Ë Ē Ė Ę Ě Ə
Ĝ Ġ Ģ
Ĥ Ħ
Ì Í Î Ï Ī Į Ĳ
Ĵ
Ķ
Ļ Ł
Ñ Ń Ņ Ň
Ò Ó Ô Õ Ö Ø Ő Œ
Ŕ Ř
ẞ Ś Ŝ Ş Š Ș Þ
Ţ Ť Ț
Ù Ú Û Ü Ū Ŭ Ů Ű Ų
Ŵ
Ý Ŷ
Ÿ Ź Ż Ž
à á â ã ä å æ ā ă ą
ç ć ĉ ċ
ð ď đ
è é ê ë ē ė ę ě ə
ĝ ġ ģ
ĥ ħ
ì í î ï ī į ĳ
ĵ
ķ
ļ ł
ñ ń ņ ň
ò ó ô õ ö ø ő œ
ŕ ř
ß ś ŝ ş š ș þ
ţ ť ț
ù ú û ü ū ŭ ů ű ų
ŵ
ý ŷ
ÿ ź ż ž"""
DIACRITIC = "[{}]".format("".join(DIACRITIC.split()))

THUMBNAIL = ".thumbnail.webp"
SELENIUM  = ".selenium.png"

def isDiacritic(tchar):
    return re.findall(DIACRITIC, tchar)

def createCnFile():
    page = b""
    ordch = 0x4e00
    count = 0
    while ordch <= 0x9fa5:
        ch = chr(ordch)
        ordch += 1
        page += ch.encode("utf8")
        count += 1
        if count % 50 == 0:
            page += b"\r\n"
    tempfile = os.path.join("tempdir", "tempfile.txt")
    writefile(tempfile, page)
    openTextFile(tempfile)
#createCnFile()

def getLeftSpaceCount(line):
    line = line[:]
    assert not line.startswith("\t"), line
    count = 0
    while line and line[0] == " ":
        line = line[1:]
        count += 1
    return count

def calcType(ttype, url):
    url = url.split("?")[0].split("#")[0]
    url = url.split("/")[-1].strip()
    if not url: return ttype
    secli = url.split(".")
    if len(secli) <= 1: return ttype
    if not secli[-1]: return ttype
    return "."+secli[-1].lower()

def calcHost(url):
    url = url.split("?")[0].split("#")[0]
    return url.split("//")[1].split("/")[0]

def checklog(fpath1, fpath2):
    localfile = os.path.join("tempdir", getFileMd5(fpath1), getFileMd5(fpath2))
    return os.path.exists(localfile)

def savelog(fpath1, fpath2):
    localfile = os.path.join("tempdir", getFileMd5(fpath1), getFileMd5(fpath2))
    copyfile(fpath2, localfile)

def removelog(fpath1, fpath2):
    localfile = os.path.join("tempdir", getFileMd5(fpath1), getFileMd5(fpath2))
    if os.path.exists(localfile):
        os.remove(localfile)

G_SNAPCACHE = {}
G_UNTOUCHED = {}
# 收集所有缓存快照。
def buildSnapCache(rootdir):
    rootdir = os.path.normpath(rootdir)
    def mainfile(fpath, fname, ftype):
        fpath = os.path.normpath(fpath)
        if not re.findall("^[0-9a-f]{8}\\.", fname, re.IGNORECASE):
            return
        if fname.find(SELENIUM) != -1:
            return
        key = fname[:8]
        if not key in G_SNAPCACHE.keys():
            G_SNAPCACHE[key] = []
        G_SNAPCACHE[key].append(fpath)
        if not key in G_UNTOUCHED.keys():
            G_UNTOUCHED[key] = []
        G_UNTOUCHED[key].append(fpath)
    searchdir(rootdir, mainfile)

# 出现过的移除标记。
def touchSnapCache(umd5, flocal):
    if umd5 in G_UNTOUCHED.keys() and flocal in G_UNTOUCHED[umd5]:
        G_UNTOUCHED[umd5] = [i for i in G_UNTOUCHED[umd5] if i != flocal]

# 查询可能的缓存路径。
def querySnapCache(umd5):
    if umd5 in G_SNAPCACHE.keys() and G_SNAPCACHE[umd5]:
        return readfile(G_SNAPCACHE[umd5][0])
    return None

# 移除指定缓存快照。
def removeSnapCache(umd5):
    if umd5 in G_SNAPCACHE.keys() and G_SNAPCACHE[umd5]:
        return osremove(G_SNAPCACHE[umd5][0])
    return None

# 清理那些剩余的缓存快照。
def clearSnapCache():
    print("ClearSnapCache", len(G_UNTOUCHED))
    for umd5 in G_UNTOUCHED.keys():
        for x in G_UNTOUCHED[umd5]:
            osremove(x)

def ffmpegConvert(fpath):
    if fpath.endswith(".264.mp4"): return
    tpath = fpath + ".264.mp4"
    if os.path.exists(tpath): return
    ffmpeg = r"C:\Program Files\ImageMagick-6.9.11-Q16-HDRI\ffmpeg.exe"
    cmdx = r"""
    "{}" -y -i "{}" -r 30000/1001
    -b:a 2M -bt 4M -vcodec libx264 -pass 1
    -coder 0 -bf 0 -flags -loop -wpredp 0
    -an "{}"
    """.format(ffmpeg, fpath, tpath)
    cmdx = " ".join(cmdx.split()).strip()
    ossystem(cmdx)

def isInvisibleDir(fpath):
    fpath = os.path.abspath(fpath).lower()
    invisible = os.path.abspath("invisible").lower()+"\\"
    invdir = fpath.startswith(invisible)
    # .\_site\invisible\
    siteinvisible = os.path.abspath(r"_site\invisible").lower()+"\\"
    invdir = invdir or fpath.startswith(siteinvisible)
    return invdir
