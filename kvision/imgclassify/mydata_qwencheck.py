#encoding=utf8
import re, os, sys
for reldirx, _lidir in (
        (os.path.dirname(os.path.abspath(__file__)), []), # 这个先，规避加载漏洞。
        (os.path.dirname(os.path.abspath(".")), [])):
    while not _lidir and len(reldirx) > 3: # 3 应该所有平台都问题不大。
        reldirx = os.path.dirname(reldirx) # 只尝试 funclib.py，funclib.pyc 存在版本。
        _checkfunc = lambda idir: os.path.exists(os.path.join(reldirx, idir, "pythonx", "funclib.py"))
        _lidir = [os.path.join(reldirx, idir) for idir in os.listdir(reldirx) if _checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
        del _checkfunc
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del _lidir # reldirx 可以继续使用
from pythonx.funclib import *

import base64
import requests
import time

# https://help.aliyun.com/zh/dashscope/developer-reference/vl-plus-quick-start
QWEN_KEY = os.getenv("DASHSCOPE_API_KEY")
while not QWEN_KEY or len(QWEN_KEY) != 35:
    QWEN_KEY = input("请输入 QWEN_KEY：")

QWEN_PLUS_VERSION = "plus" in sys.argv

# G:\work\pythonx\decode\pyenv\Python312\python.exe G:\work\pythonx\chatgpt\qwen_test.py
QWEN_ROLE = "你是一个图片分类器，对给定图片进行分类。"
QWEN_PROMPT = """
给定图片分类：
1. 人物 people or human
2. 动物 animal
3. 植物 plant
4. 风景 scenery or landscape
5. 建筑 building or architecture
6. 交通工具 vehicle or transportation
7. 食物 food
8. 日常物品 goods or Everyday Objects
9. 文本或扫描件 text or scanned document
10. 动漫或卡通 anime or cartoon
11. 夜景 nightscape
12. 抽象或艺术 art or abstract

请用一个唯一的数字作答。
"""

g_count = 0
g_time = 0
g_countpd = 0
g_timepd = 0

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def build_image(image_path):
    # Getting the base64 string
    base64_image = encode_image(image_path)
    fname = os.path.basename(image_path)

    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {QWEN_KEY}",
      "api-key": QWEN_KEY,
    }

    payload = {
      "model": "qwen-vl-max-0809",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "text": QWEN_ROLE
            },
            {
              "text": QWEN_PROMPT
            },
            {
              # https://aliyun.sunocean.life/test/images/14c4bec3d0c47caba3789f662d3471a.jpg
              "image": f"https://aliyun.sunocean.life/test/images/{fname}"
            }
          ]
        }
      ],
      "max_tokens": 10240 # 默认是 1024
    }
    return headers, payload

def post_cache(fpath, headers, payload):
    localkey = getMd5(jsondumps([headers, payload]).replace(os.linesep, "\r\n")) + getFileMd5(fpath)

    #print(localkey, getMd5(localkey))
    localkey = getMd5(localkey)
    localfile = os.path.join(TEMPDIR, "postCache", localkey + ".json")
    localfile2 = os.path.join(TEMPDIR, "postCache", payload["model"], localkey + ".json")

    if IS_LINUX:
        localfile = os.path.join("/home/yqh/code/pythonx/chatgpt", "postCache", localkey + ".json")
        localfile2 = os.path.join("/home/yqh/code/pythonx/chatgpt", "postCache", payload["model"], localkey + ".json")

    if os.path.exists(localfile) and not os.path.exists(localfile2):
        localdir2 = os.path.dirname(localfile2)
        if not os.path.exists(localdir2): os.makedirs(localdir2)
        os.rename(localfile, localfile2)
    localfile = localfile2
    print(localfile)

    global g_count
    global g_time

    fjson = readfileJson(localfile, "utf8")
    if fjson and "status_code" in fjson and fjson["status_code"] == 200:

        ctime = float(readfile(localfile+".txt", True, "utf8"))

        g_count += 1
        g_time += ctime
        colorPrint("DASHSCOPE", g_count, g_time, g_time / g_count)

        calcfile = os.path.join("tempdir", "mycalc",
                "%04d_%s"%(int(round(ctime)), os.path.basename(fpath)))
        copyfile(fpath, calcfile)
        return localkey, fjson

    modifyFileTimeCur(localfile)
    removedirTimeout(os.path.dirname(localfile), baseCount=3000)

    if IS_LINUX:
        assert False, fpath

    # Send request
    try:
        #response = requests.post(QWEN_ENDPOINT, headers=headers, json=payload)
        #response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

        from http import HTTPStatus
        import dashscope

        atime = time.time()

        response = dashscope.MultiModalConversation.call(model=payload["model"],
                                                         messages=payload["messages"])
        # The response status_code is HTTPStatus.OK indicate success,
        # otherwise indicate request is failed, you can get error code
        # and message from code and message.
        if response.status_code == HTTPStatus.OK:
            print(response)
        else:
            print(response.code)  # The error code.
            print(response.message)  # The error message.
            raise response

        btime = time.time()
        writefile(localfile+".txt", str(btime-atime), "utf8")

        g_count += 1
        g_time += btime - atime
        colorPrint("DASHSCOPE", g_count, g_time, g_time / g_count)

        writefile(localfile, str(response), "utf8")
        return localkey, json.loads(str(response))

    except Exception as ex:
        # Error code: 400, with error text
        # {"error":{"code":"1301","message":"系统检测到输入或生成内容可能包含不安全或敏感内容，请您避免输入易产生敏感内容的提示语，感谢您的配合。"}}
        # print(dir(ex.response), ex.response)
        fjson = ex.response # status_code

        if fjson["error"]["code"] != "1301":
            raise ex

        writefile(localfile, jsondumps(fjson), "utf8")
        return localkey, fjson

    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

def request_qwen(image_path):
    headers, payload = build_image(image_path)
    localkey, fjson = post_cache(image_path, headers, payload)
    print(jsondumps(fjson))
    return localkey, fjson

# G:\work\pythonx\decode\pyenv\Python312\python.exe G:\work\pythonx\chatgpt\qwen_test.py
@CUR_DIR_RUN(__file__)
def main():

    def mainfile(fpath, fname, ftype):

        localkey, fjson = request_qwen(fpath)
    
        # qwen_format(fjson["output"]["choices"][0]["message"]["content"][0]["text"])), "utf8")
        # qwen_format(fjson["output"]["choices"][0]["message"]["content"][0]["text"])
        # {"error":{"code":"1301","message":"系统检测到输入或生成内容可能包含不安全或敏感内容，请您避免输入易产生敏感内容的提示语，感谢您的配合。"}}
        # if "error" not in fjson else fjson["error"]["message"])

    

if __name__ == "__main__":
    main()
    print("ok")
