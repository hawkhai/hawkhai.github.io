#encoding=utf8
import sys
import re, os, sys
sys.path.append("../")
import datetime, time
from pythonx.funclib import *

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

import urllib.parse

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
    local = os.path.join("assets", "configjs", path.split("/blog/", 1)[1]+".cfg.js")
    if path.startswith("/blog/invisible/"):
        local = os.path.join("invisible", "configjs", path.split("/invisible/", 1)[1]+".cfg.js")
    if not os.path.exists(local):
        writefile(local, "")

    return result

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

        headnote = readfileJson("headnote.txt")
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
