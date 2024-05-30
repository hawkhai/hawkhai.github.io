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
import urllib.parse

def main():
    urls = readfileLines("urls.txt")
    for url in urls:
        if not url.startswith("https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&"):
            continue
        print(url)
        try:
            fjson = netgetJsonCache(url, unssl=True)
            # {"ret":-6,"errmsg":"unknown error","home_page_list":[]}
            assert fjson["ret"] == 0, fjson
        except json.decoder.JSONDecodeError as ex: # Expecting value: line 1 column 1 (char 0)
            print(ex)
            raise ex
        time.sleep(5)

def procdata(page, pagemap):

    testfile = os.path.join("tempdir", "wechatdl", "jsondata.txt")
    writefile(testfile, page)
    #openTextFile(testfile)

    page = json.loads(page)
    itemlist = page["list"]
    for item in itemlist:
        app_msg_ext_info = item["app_msg_ext_info"]
        comm_msg_info = item["comm_msg_info"]

        idx = comm_msg_info["id"]
        datetime = comm_msg_info["datetime"]

        title = app_msg_ext_info["title"]
        content_url = app_msg_ext_info["content_url"]
        cover = app_msg_ext_info["cover"]
        if not content_url: continue
        print(idx, bytesToString(stringToBytes(title), "utf8"))

        pagemap[idx] = {
            "title": title,
            "url": content_url,
            "cover": cover,
            "idx": idx,
            "datetime": datetime,
        }

def genhtml(pagemap):
    keys = pagemap.keys()
    mdpage = ""
    index = 0
    for key in keys:
        value = pagemap[key]
        title = value["title"].replace("&nbsp;", " ").replace("|", "\\|")
        url = value["url"].replace("&amp;", "&").replace("&amp;", "&")
        cover = value["cover"]
        idx = value["idx"]
        datetime = value["datetime"]
        index = index + 1
        datetime = formatTimeStamp(datetime).split()[0]
        mdpage += "{}. {} [{} weixin]({})\r\n".format(index, datetime, title, url)

    # http://localhost:4000/blog/source/wechatdl/wechatdl
    localfile = "wechatdl.md"
    writefile(localfile, mdpage)
    openTextFile(localfile)

def main2():
    lidata = readfileJson("UntitledSession.chlsj")
    pagemap = {}
    for data in lidata:
        host = data["host"]
        if not host in ("mp.weixin.qq.com",): continue
        path = data["path"]
        if not path in ("/mp/profile_ext",): continue
        query = data["query"]
        response = data["response"]

        mimeType = response["mimeType"]
        if query.startswith("action=getmsg&__biz="):
            assert mimeType == "application/json", mimeType
            text = response["body"]["text"]

            page = json.loads(text)
            assert page["ret"] == 0
            msglist = page["general_msg_list"]

            procdata(msglist, pagemap)

        if query.startswith("action=home&__biz="):
            assert mimeType == "text/html", mimeType
            text = response["body"]["text"]

            page = re.findall("var msgList = (.*?)[\r\n]", text)[0].strip()
            assert page.startswith("'") and page.endswith("';")
            msglist = urllib.parse.unquote(page[1:-2]).replace("&quot;", "\"")

            procdata(msglist, pagemap)

    genhtml(pagemap)
    print(len(pagemap))
    return pagemap

if __name__ == "__main__":
    main2()
