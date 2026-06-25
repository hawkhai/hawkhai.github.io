#encoding=utf8
"""Configuration readers and small shared helpers for mdrstrip."""
from .runtime import *

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

def readFileIgnoreList(fpath):

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

def mergeSpaceFixJson(spacefixjson, extra):
    if not extra:
        return spacefixjson

    for key, value in extra.items():
        if key == "regex":
            if key not in spacefixjson:
                spacefixjson[key] = {}
            spacefixjson[key].update(value)
            continue
        spacefixjson[key] = value
    return spacefixjson

def loadSpaceFixJson():
    spacefixjson = {}
    for fpath in ("config/mdrstrip.spacefix.json", "invisible/config/mdrstrip.spacefix.json"):
        if os.path.exists(fpath):
            mergeSpaceFixJson(spacefixjson, readfileJson(fpath, "utf8"))
    return spacefixjson

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
