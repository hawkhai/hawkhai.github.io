#encoding=utf8
import sys
import re, os, sys
sys.path.append("../")
import datetime, time
from pythonx.funclib import *

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

import urllib.parse
import headfmt

data = {'result': 'this is a test'}
HOST = ('localhost', 8888)

def getPostInfo(path): # "/favicon.ico"
    result = urllib.parse.urlsplit("http://test"+path)
    query = dict(urllib.parse.parse_qsl(result.query))
    href = query["href"] if "href" in query.keys() else None
    if not href:
        return None
    result = urllib.parse.urlparse(href)
    #print(result.scheme)
    #print(result.netloc)
    #print(result.path)
    #print(result.params)
    #print(result.query)
    #print(result.fragment)

    path = result.path
    # /blog/invisible/video/fastvc-plan
    localjs = os.path.join("assets", "configjs", path.split("/blog/", 1)[1]+".cfg.js")
    localmd = path.split("/blog/", 1)[1] + ".md"
    if path.startswith("/blog/invisible/"):
        localjs = os.path.join("invisible", "configjs", path.split("/invisible/", 1)[1]+".cfg.js")
    if not os.path.exists(localjs):
        writefile(localjs, "")

    assert os.path.exists(localmd), localmd
    kjson = headfmt.parseHeadKeyValue(localmd, None, "md")
    kjson["categories"] = [] if not kjson["categories"] else json.loads(kjson["categories"])
    kjson["tags"] = [] if not kjson["tags"] else json.loads(kjson["tags"])

    headnote = readfileJson("headnote.txt", "utf8")
    mycate = kjson["categories"]
    allcate = headnote["categories"]
    mytag = kjson["tags"]
    alltag = headnote["tags"]

    # http://c.biancheng.net/view/7588.html
    htmlcate = '<fieldset><form action="http://localhost:8888/chgcat?" method="get" name="chgcat">分类：\r\n'
    for cate in allcate:
        htmlcate += '<nobr><input type="radio" name="mycate" value="%(value)s" id="%(id)s" %(checked)s>\
                                <label for="%(id)s">%(value)s</label>&nbsp;&nbsp;</nobr>\r\n' % {
            "value": cate, "id": cate,
            "checked": 'checked="checked"' if cate in mycate else ""
        }
    htmlcate += '<input type="submit" name="submit" value="提交"></form></fieldset><br/>'
    kjson["htmlcate"] = htmlcate

    # http://c.biancheng.net/view/7597.html
    htmltag = '<fieldset><form action="http://localhost:8888/chgtag?" method="get" name="chgtag">标签：\r\n'
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
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:4000')
        self.end_headers()

        if self.path == "/favicon.ico":
            self.wfile.write(readfile("favicon.ico"))
            return

        print(self.path)
        pinfo = getPostInfo(self.path)

        headnote = readfileJson("headnote.txt", "utf8")
        self.wfile.write(json.dumps({
            "headnote": headnote,
            "pinfo": pinfo,
        }).encode())

if __name__ == '__main__':
    server = HTTPServer(HOST, Resquest)
    print("Starting server, listen at: %s:%s" % HOST)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
