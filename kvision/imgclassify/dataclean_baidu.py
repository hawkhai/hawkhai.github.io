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
