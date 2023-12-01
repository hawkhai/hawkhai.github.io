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

import requests
import base64

# https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjhhu
# https://ai.baidu.com/ai-doc/IMAGERECOGNITION/Xk3bcxe21
def getToken():
    client_id = "vgOXhG8fcMllloKbXndlLiG5"
    client_secret = "10HcwskzFSu5bwc44UQPqXjRR3GkrM13"
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    fjson = json.loads(response.text)
    print(jsondumps(fjson))
    return fjson["access_token"]

def reqfile(access_token, imgfile, logfile):

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    # 二进制方式打开图片文件
    f = open(imgfile, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        fjson = response.json()
        print(jsondumps(fjson, ascii=False))
        writefile(logfile, jsondumps(fjson, ascii=False), "utf8")
    assert response

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main():

    access_token = getToken()

    def mainfile(fpath, fname, ftype):

        if ftype in ("txt", "json"):
            return
        assert ftype in ("png", "jpg", "jpeg"), ftype

        ipath = os.path.relpath(fpath, ".")
        logfile = os.path.join("logdata", "baidu", ipath + ".json")
        logfile2 = os.path.join("logdata", "baidu", os.path.splitext(ipath)[0] + ".json")
        if os.path.exists(logfile):
            os.rename(logfile, logfile2)
        logfile = logfile2

        from pythonx import lockfile
        with lockfile.lock(fpath, 10):

            if os.path.exists(logfile):
                fjson = readfileJson(logfile, "utf8")
                #writefile(logfile, jsondumps(fjson, ascii=False), "utf8")
                # "error_code": 18,
                # "error_msg": "Open api qps request limit reached"
                if "error_code" in fjson:
                    pass
                elif fjson["result_num"] and "result" in fjson and fjson["result"]:
                    return

            # 为并发准备的，默认不支持并发。
            #fjson = {"result_num":5}
            #writefile(logfile, jsondumps(fjson, ascii=False), "utf8")

        print(fpath)
        reqfile(access_token, fpath, logfile)

    assert sys.argv[-1] in os.listdir("dataset") or sys.argv[-1] == ".", sys.argv
    searchdir(os.path.join("dataset", sys.argv[-1]), mainfile)

if __name__ == "__main__":
    main()
