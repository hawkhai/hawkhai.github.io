#encoding=utf8
#!/usr/bin/env python3
import socket
import os
import stat
from urllib.parse import unquote

import json
from urllib import parse
from threading import Thread
import time

import re, os, sys
sys.path.append("../")
from pythonx.funclib import *
from pythonx.pelib import mydllfunc

# 换行符
NEWLINE = "\r\n"
MAX_FILE_SIZE = 100 * 1024 * 1024 # 100MB

# 读取文本
def get_file_contents(file_name):
    #with open(file_name, "r") as f:
    if not os.path.exists(file_name):
        file_name = os.path.join(getPythonxDir(), "..", file_name)
    with open(file_name, "rb") as f:
        return f.read()

# 读取二进制
def get_file_binary_contents(file_name):
    with open(file_name, "rb") as f:
        return f.read()

# 是否有访问权限
def has_permission_other(file_name):
    stmode = os.stat(file_name).st_mode
    return (getattr(stat, "S_IROTH") & stmode) > 0

# 二进制读取的文件类型
BINARY_TYPE_FILES = set(["jpg", "jpeg", "mp3", "png", "html", "js", "css", "ico"])
TEXT_MIME_TYPE = "text/plain"
JSON_MIME_TYPE = "application/json"
# MIME 映射表
MIME_TYPES = {
    "html": "text/html",
    "css": "text/css",
    "js": "text/javascript",
    "mp3": "audio/mpeg",
    "png": "image/png",
    "jpg": "image/jpg",
    "jpeg": "image/jpeg",
    "ico": "image/ico",
}

# 是否需要二进制返回。
def should_return_binary(file_extension):
    return file_extension in BINARY_TYPE_FILES

# 获取文件 MIME 类型，否则都采用 TEXT_MIME_TYPE
def get_file_mime_type(file_extension):
    mime_type = MIME_TYPES[file_extension] if file_extension in MIME_TYPES.keys() else None
    return mime_type if mime_type is not None else TEXT_MIME_TYPE

class HTTPServer:
    def __init__(self, host="localhost", port=9001, directory="."):

        if host == "localhost":
            ipaddr = mydllfunc("getipaddr", {"minorVer": 2, "majorVer": 2,})
            if ipaddr and ipaddr["ret"] == 0:
                ipaddr = ipaddr["result"]
                ipaddr = ipaddr["result"]
                # ['192.168.110.1', '192.168.245.1', '192.168.0.102']
                ipaddr = [i for i in ipaddr if not re.findall("^[0-9]+\\.[0-9]+\\.[0-9]+\\.1$", i)]
                if ipaddr and len(ipaddr) == 1:
                    host = ipaddr[0] # 换算成 IP。

        assert host != "localhost", "host 不能是 'localhost'!!"

        print(f"Server started. Listening at http://{host}:{port}/")
        self.host = host
        self.port = port
        self.working_dir = directory

        self.setup_socket()
        self.accept()

        self.teardown_socket()

    def setup_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(128) # 允许队列的等待长度。

    def teardown_socket(self):
        if self.sock is not None:
            self.sock.shutdown()
            self.sock.close()

    def accept(self):
        while True:
            (client, address) = self.sock.accept()
            th = Thread(target=self.accept_request, args=(client, address))
            th.start()

    def accept_request(self, client_sock, client_addr):
        req = ""
        while req.find(NEWLINE * 2) == -1:
            req += bytesToString(client_sock.recv(1))

        print("***" * 50)
        print(req)

        # https://www.runoob.com/python/python-socket.html
        response = self.process_response(req, client_sock)
        client_sock.send(response)

        # clean up
        client_sock.shutdown(1)
        client_sock.close()

    def process_response(self, request, client_sock):
        formatted_data = request.strip().split(NEWLINE)
        request_words = formatted_data[0].split()

        # GET /?listdir=kvision/2Original HTTP/1.1
        if len(request_words) == 0:
            return

        requested_file = request_words[1]
        if requested_file.startswith("/"):
            requested_file = requested_file[1:]

        if request_words[0] == "GET":
            return self.get_request(requested_file, formatted_data)
        if request_words[0] == "POST":
            return self.post_request(requested_file, formatted_data, client_sock)
        return self.method_not_allowed()

    # The response to a HEADER request
    def head_request(self, requested_file, data):
        if not os.path.exists(requested_file):
            response = NOT_FOUND
        elif not has_permission_other(requested_file):
            response = FORBIDDEN
        else:
            response = OK

        return response.encode('utf-8')

    def api_listdir(self, rootdir):
        ignorelist = (".gitignore",)
        logdir = r"kvision/ksample/1Unshaded"
        if not os.path.exists(logdir):
            logdir = r"ksample/1Unshaded"
        if not os.path.exists(rootdir):
            rootdir = r"ksample" + rootdir.split("ksample", 1)[-1]
        return [{"fname": os.path.join(rootdir, i).replace("\\", "/"),
                 "fsize": os.path.getsize(os.path.join(rootdir, i)),
                 "classifyShadowType": int(iniRead(os.path.join(logdir, i+".log"), "log", "classifyShadowType", defaultValue="-99997")),
                 "classifyCode": int(iniRead(os.path.join(logdir, i+".log"), "log", "code", defaultValue="-99997")),
                } for i in listSortNumName(os.listdir(rootdir)) if not i in ignorelist]

    def api_listlog(self):
        logdir = r"kvision/ksample/1Unshaded"
        if not os.path.exists(logdir):
            logdir = r"ksample/1Unshaded"
        return [{"fname": i.replace("\\", "/"),
                 "fsize": os.path.getsize(os.path.join(logdir, i)),
                 "classifyShadowType": int(iniRead(os.path.join(logdir, i), "log", "classifyShadowType", defaultValue="-99997")),
                 "classifyCode": int(iniRead(os.path.join(logdir, i), "log", "code", defaultValue="-99997")),
                } for i in listSortNumName(os.listdir(logdir)) if i.endswith(".log")]

    # listdir=kvision/2Original
    def get_request_api(self, requested_file, data):
        argvs = parse.parse_qs(requested_file)
        print("GET_REQUEST_API", argvs)

        builder = ResponseBuilder()

        if "listlog" in argvs.keys():
            builder.set_content(jsondumps(self.api_listlog()))
        elif "listdir" in argvs.keys():
            builder.set_content(jsondumps(self.api_listdir(argvs["listdir"][0])))
        else:
            return self.response_ok()

        builder.set_status("200", "OK")
        builder.add_header("Connection", "close")
        builder.add_header("Content-Type", JSON_MIME_TYPE)
        return builder.build()

    def post_request_upload(self, requested_file, data, client_sock):
        argvs = parse.parse_qs(requested_file)
        # Content-Length: 653306
        contentlength = MAX_FILE_SIZE # 实在太多可能造成客户端超时错误。
        for idata in data:
            if idata.startswith("Content-Length"):
                contentlength = int(idata.split(":")[-1].strip())

        print("POST_REQUEST_UPLOAD", contentlength, argvs)
        assert contentlength != MAX_FILE_SIZE, contentlength
        atime = time.time()
        # 如果约定的长度没有达到，就会超时，直到客户端断开。
        fdata = client_sock.recv(contentlength, socket.MSG_WAITALL)
        print("POST_REQUEST_UPLOAD", len(fdata), "time=%.4fs" % (time.time()-atime), "--", getCurrentTimeStr())
        # 这里断言完整，要么不写，要么就是完整的。
        assert len(fdata) == contentlength, (len(fdata), contentlength, argvs)

        # POST upimage=kvision/4Enhance/60.jpg.guide.png HTTP/1.1
        if "upimage" in argvs.keys():

            fpath = argvs["upimage"][0]
            writefile(fpath, fdata)

            builder = ResponseBuilder()
            builder.set_content(jsondumps({
                "fpath": fpath,
                "size": len(fdata),
            }))

            builder.set_status("200", "OK")
            builder.add_header("Connection", "close")
            builder.add_header("Content-Type", JSON_MIME_TYPE)
            return builder.build()
        return self.response_ok()

    # TODO: Write the response to a GET request
    # ?listdir=kvision/2Original
    def get_request(self, requested_file, data):

        if not os.path.exists(requested_file):
            blog_requested_file = os.path.join("..", requested_file)
            if os.path.exists(blog_requested_file):
                requested_file = blog_requested_file

        if (not os.path.exists(requested_file)):
            if requested_file.startswith("?"):
                return self.get_request_api(requested_file[1:], data)
            return self.resource_not_found()
        elif (not has_permission_other(requested_file)):
            return self.resource_forbidden()
        else:
            builder = ResponseBuilder()

            if (should_return_binary(requested_file.split(".")[-1])):
                builder.set_content(get_file_binary_contents(requested_file))
            else:
                builder.set_content(get_file_contents(requested_file))

            builder.set_status("200", "OK")
            builder.add_header("Connection", "close")
            builder.add_header("Content-Type", get_file_mime_type(requested_file.split(".")[-1]))
            return builder.build()

    # TODO: Write the response to a POST request
    def post_request(self, requested_file, data, client_sock):

        # POST ?upimage=kvision/4Enhance/60.jpg.guide.png HTTP/1.1
        if requested_file.startswith("?"):
            return self.post_request_upload(requested_file[1:], data, client_sock)

        return self.response_ok()

    def response_ok(self):
        builder = ResponseBuilder()
        builder.set_status("200", "OK")
        builder.add_header("Connection", "close")
        builder.add_header("Content-Type", MIME_TYPES["html"])
        builder.set_content(b"ok")
        return builder.build()

    """
        `urllib.parse.unquote`
        https://github.com/ruijun-ni/CS4131-Internet-Programming/blob/main/hw4/myServer.py
    """
    def method_not_allowed(self):
        builder = ResponseBuilder()
        builder.set_status("405", "METHOD NOT ALLOWED")
        allowed = ", ".join(["GET", "POST"])
        builder.add_header("Allow", allowed)
        builder.add_header("Connection", "close")
        return builder.build()

    # TODO: Make a function that handles not found error
    def resource_not_found(self):
        builder = ResponseBuilder()
        builder.set_status("404", "NOT FOUND")
        builder.add_header("Connection", "close")
        builder.add_header("Content-Type", MIME_TYPES["html"])
        builder.set_content(get_file_contents("httpserv/404.html"))
        return builder.build()

    # TODO: Make a function that handles forbidden error
    def resource_forbidden(self):
        builder = ResponseBuilder()
        builder.set_status("403", "FORBIDDEN")
        builder.add_header("Connection", "close")
        builder.add_header("Content-Type", MIME_TYPES["html"])
        builder.set_content(get_file_contents("httpserv/403.html"))
        return builder.build()

class ResponseBuilder:
    def __init__(self):
        self.headers = []
        self.status = None
        self.content = None

    def add_header(self, headerKey, headerValue):
        """ Adds a new header to the response """
        self.headers.append(f"{headerKey}: {headerValue}")

    def set_status(self, statusCode, statusMessage):
        """ Sets the status of the response """
        self.status = f"HTTP/1.1 {statusCode} {statusMessage}"

    def set_content(self, content):
        """ Sets `self.content` to the bytes of the content """
        if isinstance(content, (bytes, bytearray)):
            self.content = content
        else:
            self.content = content.encode("utf-8")

    # TODO Complete the build function
    def build(self):

        response = self.status
        response += NEWLINE
        for i in self.headers:
            response += i
        response += NEWLINE
        response += NEWLINE
        response = response.encode("utf-8")
        response += self.content

        return response

# mklink /J 2Original E:\kpdf\pdfreader_image\fastpdf-turbo\image\imagetest\testdata\jpg
# http://localhost:9001/?listdir=kvision/2Original
if __name__ == "__main__":
    try:
        if re.findall("^[0-9.]+$", sys.argv[-1]):
            HTTPServer(sys.argv[-1])
        else:
            HTTPServer()
    except:

        traceback.print_exc()
        print("实在抱歉，程序出错了。^_^")
        os.system("pause")
