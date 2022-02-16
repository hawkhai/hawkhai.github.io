#encoding=utf8
import sys
import re, os, sys
sys.path.append("../")
import datetime, time
from pythonx.funclib import *
from pythonx.pelib import mydllfunc

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from socketserver import ThreadingMixIn
import threading
import ssl

import urllib.parse
import headfmt
from urllib.parse import quote, unquote

data = {'result': 'this is a test'}
HOST = ('localhost', 8888)

def getPostInfo(path): # "/favicon.ico"
    result = urllib.parse.urlsplit("http://test"+path)
    print("path", "--", result.path)
    return parseRootReq(path, result, result.path)

def findPostMdFile(rootdir, fnamek):
    fpathk = fnamek
    def mainfile(fpath, fname, ftype):
        if ftype != "md": return
        if fname == fnamek:
            nonlocal fpathk
            assert fpathk == fnamek # 没有被赋值过。
            fpathk = fpath
    searchdir(rootdir, mainfile)
    return fpathk

def parseRootReq(path, result, action):
    querysrc = urllib.parse.parse_qsl(result.query)
    query = dict(querysrc)
    href = query["href"] if "href" in query.keys() else None
    if not href:
        return None
    result = urllib.parse.urlparse(unquote(href))
    if result.scheme:   print("scheme", "--", result.scheme)
    if result.netloc:   print("netloc", "--", result.netloc)
    if result.path:     print("path", "--", result.path)
    if result.params:   print("params", "--", result.params)
    if result.query:    print("query", "--", result.query)
    if result.fragment: print("fragment", "--", result.fragment)

    path = result.path
    # /blog/invisible/video/fastvc-plan
    localjs = os.path.join("assets", "configjs", path.split("/blog/", 1)[1]+".cfg.js")
    localmd = path.split("/blog/", 1)[1] + ".md"

    blog = re.findall("^/blog/blog/([0-9]{4})/([0-9]{2})/([0-9]{2})/(.*)", path)
    if blog:
        blog = blog[0] # 如果有，只会有一个。
        print(blog)
        fnamek = "{}-{}-{}-{}.md".format(*blog)
        localmd = findPostMdFile("_posts", fnamek)
        localmd = os.path.relpath(localmd, ".")

    if path.startswith("/blog/invisible/"):
        localjs = os.path.join("invisible", "configjs", path.split("/invisible/", 1)[1]+".cfg.js")
    if not os.path.exists(localjs):
        pass#writefile(localjs, "")

    assert os.path.exists(localmd), (localmd, path)
    localmd = localmd.replace("/", "\\")
    kjson = headfmt.parseHeadKeyValue(localmd, None, "md")
    kjson["categories"] = [] if not kjson["categories"] else json.loads(kjson["categories"])
    kjson["tags"] = [] if not kjson["tags"] else json.loads(kjson["tags"])

    headnote = readfileJson("config/headnote.txt", "utf8")
    if action == "/":
        return parseReqAction(localjs, localmd, kjson, query, headnote, href)
    if action == "/chgcat":
        return parseReqActionChgCate(localjs, localmd, kjson, querysrc, headnote, href)
    if action == "/chgtag":
        return parseReqActionChgTag(localjs, localmd, kjson, querysrc, headnote, href)
    if action == "/tagctrl":
        return parseReqActionTagCtrl(localjs, localmd, kjson, query, headnote, href)

def headkv_jsonsumps(li):
    temp = jsondumps(li, False, 0)
    temp = " ".join(temp.split())
    if temp.startswith("[ "): temp = "["+temp[2:]
    if temp.endswith(" ]"): temp = temp[:-2]+"]"
    return temp

def parseReqActionChgCate(localjs, localmd, kjson, querysrc, headnote, href):
    kjson["chgcat"] = querysrc
    li = []
    for k, v in querysrc:
        if k == "mycate":
            li.append(v)
    headfmt.mainxkeyfile(localmd, None, "md", setkv={"categories": headkv_jsonsumps(li)})
    return kjson

def parseReqActionChgTag(localjs, localmd, kjson, querysrc, headnote, href):
    kjson["chgtag"] = querysrc
    li = []
    for k, v in querysrc:
        if k == "mytag":
            li.append(v)
    headfmt.mainxkeyfile(localmd, None, "md", setkv={"tags": headkv_jsonsumps(li)})
    return kjson

def parseReqActionTagCtrl(localjs, localmd, kjson, query, headnote, href):
    gkvconfig = readfileJson("config/headnote.json", "utf8")
    value = not not int(query["taged"])
    gkvconfig[localmd]["taged"] = value
    mdtagfile = (localmd+".tag").replace(".md.tag", ".mdtag").replace("-", "")
    if value:
        osremove(mdtagfile)
    else:
        writefile(mdtagfile, "")
    #writefileJson("config/headnote.json", gkvconfig)

def parseReqAction(localjs, localmd, kjson, query, headnote, href):
    mycate = kjson["categories"]
    allcate = headnote["categories"]
    mytag = kjson["tags"]
    alltag = headnote["tags"]

    gkvconfig = readfileJson("config/headnote.json", "utf8")
    config = gkvconfig[localmd] if localmd in gkvconfig.keys() else { "taged": False, }
    kjson["config"] = config

    tagctrl = '<form action="http://localhost:8888/tagctrl" method="get" name="chgcat">\r\n'
    tagctrl += '<input type="hidden" name="href" value="%s">' % quote(href)
    tagctrl += '<input type="hidden" name="taged" value="%d">' % (1 if not config["taged"] else 0)
    tagctrl += '<input type="submit" name="submit" value="%s"></form><br/>' % ("关闭" if not config["taged"] else "修改")
    kjson["tagctrl"] = tagctrl

    # http://c.biancheng.net/view/7588.html
    htmlcate = '<fieldset><form action="http://localhost:8888/chgcat" method="get" name="chgcat">分类：\r\n'
    htmlcate += '<input type="hidden" name="href" value="%s">' % quote(href)
    for cate in allcate:
        htmlcate += '<nobr><input type="radio" name="mycate" value="%(value)s" id="%(id)s" %(checked)s>\
                                <label for="%(id)s">%(value)s</label>&nbsp;&nbsp;</nobr>\r\n' % {
            "value": cate, "id": cate,
            "checked": 'checked="checked"' if cate in mycate else ""
        }
    htmlcate += '<input type="submit" name="submit" value="提交"></form></fieldset><br/>'
    kjson["htmlcate"] = htmlcate

    # http://c.biancheng.net/view/7597.html
    htmltag = '<fieldset><form action="http://localhost:8888/chgtag" method="get" name="chgtag">标签：\r\n'
    htmltag += '<input type="hidden" name="href" value="%s">' % quote(href)
    for tag in alltag:
        htmltag += '<nobr><input type="checkbox" name="mytag" value="%(value)s" id="%(id)s" %(checked)s>\
                        <label for="%(id)s">%(value)s</label>&nbsp;&nbsp;</nobr>\r\n' % {
            "value": tag, "id": tag,
            "checked": 'checked="checked"' if tag in mytag else ""
        }
    htmltag += '<input type="submit" name="submit" value="提交"></form></fieldset><br/>'
    kjson["htmltag"] = htmltag
    return kjson

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')

        CrossOrigin = False
        result = mydllfunc("getipaddr", {"minorVer": 2, "majorVer": 2,})
        if result["ret"] == 0:
            result = result["result"]
            result = result["result"]
            result = [i for i in result if not re.findall("^[0-9]+\\.[0-9]+\\.[0-9]+\\.1$", i)]
            for ip in result:
                self.send_header('Access-Control-Allow-Origin', 'http://{}:4000'.format(ip))
                CrossOrigin = True
        if not CrossOrigin:
            self.send_header('Access-Control-Allow-Origin', 'http://localhost:4000')

        self.end_headers()

        if self.path == "/favicon.ico":
            self.wfile.write(readfile("favicon.ico"))
            return

        print(self.path)
        pinfo = getPostInfo(self.path)

        headnote = readfileJson("config/headnote.txt", "utf8")
        self.wfile.write(json.dumps({
            "headnote": headnote,
            "pinfo": pinfo,
        }).encode())

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

if __name__ == '__main__':
    server = ThreadingSimpleServer(HOST, Resquest)
    print("Starting server, listen at: %s:%s" % HOST)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
    print("Server stopped.")
