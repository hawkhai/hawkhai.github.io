#encoding=utf8
import sys
import re, os, sys
sys.path.append("../")
import datetime, time
from pythonx.funclib import *

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result': 'this is a test'}
host = ('localhost', 8888)

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
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
