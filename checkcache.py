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

def formatbigfiles(fpath, md5hub, mycache=None):
    fpage = readfile(fpath, True, "utf8")
    lines = fpage.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    rootdir = os.path.split(fpath)[0]
    def myfunc(tmp):

        if not tmp.strip(): return tmp.strip()
        # 要么是注释，要么就是规则。
        assert tmp.startswith("# ") or re.findall("^[0-9a-f]{32} # .*? # ([0-9.]+) MB$", tmp), tmp

        tmpli = tmp.split("#")
        if len(tmpli) >= 3:
            srcmd5, srcpath, srcsize = tmpli
            srcmd5, srcpath, srcsize = srcmd5.strip(), srcpath.strip(), srcsize.strip()
            if srcmd5 in md5hub:
                srcpath = md5hub[srcmd5]
            elif os.path.exists(srcpath):
                srcmd5 = getFileSrcMd5z(srcpath, mycache=mycache)
            else:
                return None # 文件已经不存在了。

            pathz = os.path.relpath(srcpath, ".")
            if not os.path.exists(pathz):
                print("warning>", pathz)
            else:
                srcsize = "%.1f MB" % (os.path.getsize(pathz)/1024/1024)
            srcpath = pathz

            tmp = " # ".join([srcmd5, srcpath, srcsize])
        return " ".join(tmp.split())
    lines = [myfunc(line) for line in lines if line.strip() and myfunc(line)]
    def mycmp(tmp):
        if not tmp.strip():
            return tmp.strip()
        if len(tmp.split(" # ")) > 1:
            return tmp.split(" # ")[1]
        return tmp.strip()
    lines.sort(key=mycmp)
    #print(lines)
    writefile(fpath, "\r\n".join(lines)+"\r\n", "utf8")

if __name__ == "__main__":
    searchdir(".", maincheck, ignorelist=("_site",))
    md5hubfile = os.path.join("tempdir", "md5hub.txt")
    md5hub = readfileJson(md5hubfile)
    if not md5hub: md5hub = {}
    def mainmd5file(fpath, fname, ftype):
        fmd5 = getFileSrcMd5z(fpath, mycache=None)
        if not fmd5 in md5hub:
            md5hub[fmd5] = fpath
    if not md5hub:
        searchdir(".", mainmd5file, ignorelist=("_site",))
        writefileJson(md5hubfile, md5hub)
    #print(md5hub)
    formatbigfiles(r"config\\mdrstrip_bigfiles.txt", md5hub)
    formatbigfiles(r"invisible\\config\\mdrstrip_bigfiles.txt", md5hub)
