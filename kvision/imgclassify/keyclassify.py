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
from pythonx.iciba import getChinese

import pythonx.chatgpt.chatchat as cc

REASK = "reask" in sys.argv

def ask_xunfei(app_id, api_secret, api_key, content, reask=False):

    localcache = os.path.join("tempdir", "xunfei", "xunfei", getMd5(content, "utf8") + ".txt")
    if os.path.exists(localcache) and not reask:
        print("READCACHE", localcache)
        return readfileJson(localcache, "utf8")

    config = {
        "xunfei": {
            "app_id": app_id,
            "api_secret": api_secret,
            "api_key": api_key,
        }
    }
    localfile = os.path.join("tempdir", "chatchat", "xunfei.json")
    writefileJson(localfile, config)
    completion = cc.xunfei.Completion(localfile)
    json = {
        "header": {
            "app_id": completion.jdata['app_id'],
        },
        "parameter": {
            "chat": {
                "domain": 'generalv2',
            }
        },
        "payload": {
            "message": {
                "text": [
                    {"role": "user", "content": content}
                ]
            }
        }
    }
    r = completion.create(json, stream=True)
    print(r)
    writefileJson(localcache, r, "utf8")
    return r

def ask_baidu(api_key, secret_key, content, reask=False):

    localcache = os.path.join("tempdir", "baidu", "wenxin", getMd5(content, "utf8") + ".txt")
    if os.path.exists(localcache) and not reask:
        print("READCACHE", localcache)
        return readfileJson(localcache, "utf8")

    config = {
        "baidu": {
            "api_key": api_key,
            "secret_key": secret_key,
        }
    }
    localfile = os.path.join("tempdir", "chatchat", "baidu.json")
    writefileJson(localfile, config)
    completion = cc.baidu.Completion(localfile)
    payload = {
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ]
    }
    r = completion.create(payload)
    print(r)
    writefileJson(localcache, r, "utf8")
    return r

def ask_baidux(content, reask=False):
    api_key = "NvFu5TZ6teBl0BsBY5UfHBnT"
    secret_key = "0Gvc3mTSNChzqWfTyL23hs9YtG1wVIvo"

    fjson = ask_baidu(api_key, secret_key, content, reask)
    result = fjson["result"]

    return result

def ask_xunfeix(content, reask=False):
    app_id = "8ed9a00f"
    api_secret = "YjE0YjFlNDY1MDRkOTBkNjVlMDBhN2Rm"
    api_key = "edbe50b9cc30cc8a96098f12b05b628f"

    result = ask_xunfei(app_id, api_secret, api_key, content, reask)
    return result

def check_result(result):
    regex = "动物|动漫|建筑|食物|日常用品|室内|夜景|人物|植物|风景|文本|交通工具|不确定"
    li = re.findall(regex, result, re.IGNORECASE)
    li = list(set(li))
    li.sort()
    #print(li)
    if len(li) <= 0:
        return False
    if len(li) == 1 and li[0] != "不确定":
        return li[0]
    if len(li) == 2 and "不确定" in li:
        for i in li:
            if i != "不确定": return i
    return False

def ask(key):

    content = r"""我定义了一些图片分类
“动物”、“动漫”、“建筑”、“食物”、“日常用品”、“室内”、“夜景”、“人物”、“植物”、“风景”、“文本”、“交通工具”，
请问 “{}” 分到哪个类别最合理？如果不确定，请回答不确定，控制在十个字以内。""".format(key)

    result_baidu = ""
    for i in range(2):
        result = ask_baidux(content, reask=i>0)
        result_baidu = check_result(result)
        if result_baidu:
            colorPrint("result_baidu", result_baidu)
            break

    result_xunfei = ""
    for i in range(2):
        result = ask_xunfeix(content, reask=i>0)
        result_xunfei = check_result(result)
        if result_xunfei:
            colorPrint("result_xunfei", result_xunfei)
            break

    return result_baidu, result_xunfei

@CWD_DIR_RUN(os.path.split(os.path.abspath(__file__))[0])
def main():
    result_baidu, result_xunfei = ask("girl")

    keysfile = r"Improving-Loss-Function-for-Deep-CNN-based-AIA\datasets\Corel-5k\corel5k_vocabulary.txt"
    keys = readfile(keysfile, True, "utf8").split("\n")
    keys = [i.strip() for i in keys if i.strip()]
    for i in range(len(keys)):

        key = keys[i].split(":")[0].split("->")[0]
        type = keys[i].split(":")[1].split("->")[0] if keys[i].find(":") != -1 else ""
        name = keys[i].split("->")[1] if keys[i].find("->") != -1 else ""
        if not name:
            name = getChinese(key)

        if not type:
            result_baidu, result_xunfei = ask(key)
            if result_baidu and result_baidu == result_xunfei:
                type = result_baidu
                colorPrint("ASK", key, result_baidu)

        keys[i] = "{}:{}->{}".format(key, type, name)
        writefile(keysfile, "\r\n".join(keys)+"\r\n", "utf8")

if __name__ == "__main__":
    main()
