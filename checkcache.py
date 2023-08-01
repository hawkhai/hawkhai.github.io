#encoding=utf8
import re, os, sys
reldirx, _lidir = "", []
while not _lidir and len(reldirx) <= 100:
    reldirx += "../"
    checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
    _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
    if _lidir: reldirx = _lidir[0]
sys.path.append(reldirx)
from pythonx.funclib import *

REMOVE = "remove" in sys.argv

def needcheck(fpath, fname, ftype):
    for sign in r""".zhihu.com
                    .jianshu.com
                    .csdn.net""".split():
        if fpath.find(sign) != -1:
            return True
    return False

def checkpage(fdata):
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

    for itag in (itag0, itag1, itag2, itag3, itag4, itag5, itag6, itag7, itag8, itag9):
        if fdata.find(itag) != -1:
            return itag
    return None

def maincheck(fpath, fname, ftype):

    if not needcheck(fpath, fname, ftype):
        return

    fdata = readfile(fpath, True)
    result = checkpage(fdata)
    if result:
        print("无法访问此网站", fpath, result)
        if REMOVE:
            osremove(fpath)

def formatbigfiles(fpath):
    fpage = readfile(fpath, True, "utf8")
    lines = fpage.replace("\r\n", "\n").split("\n")
    rootdir = os.path.split(fpath)[0]
    def myfunc(tmp):
        tmpli = tmp.split("#")
        if len(tmpli) >= 3:
            localdir = os.path.join(rootdir, "..")
            local = os.path.join(localdir, tmpli[1].strip())
            pathz = os.path.relpath(local, localdir)
            if not os.path.exists(local):
                print("not os.path.exists", pathz)
            tmpli[1] = " %s " % pathz
            tmp = "#".join(tmpli)
        return " ".join(tmp.split())
    lines = [myfunc(line) for line in lines if line.strip()]
    def mycmp(tmp):
        if not tmp.strip(): return tmp.strip()
        if len(tmp.split(" # ")) > 1:
            return tmp.split(" # ")[1]
        return tmp.strip()
    lines.sort(key=mycmp)
    #print(lines)
    writefile(fpath, "\r\n".join(lines)+"\r\n", "utf8")

if __name__ == "__main__":
    searchdir(".", maincheck, ignorelist=("_site",))
    formatbigfiles(r"config\\mdrstrip_bigfiles.txt")
    formatbigfiles(r"invisible\\config\\mdrstrip_bigfiles.txt")
