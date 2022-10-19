#encoding=utf8
#!/usr/bin/env python3
import socket
import os
import stat
from urllib.parse import unquote

from threading import Thread

# 换行符
NEWLINE = "\r\n"

# 读取文本
def get_file_contents(file_name):
    #with open(file_name, "r") as f:
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
        self.sock.listen(128)

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
        data = client_sock.recv(4096)
        req = data.decode("utf-8")

        response = self.process_response(req)
        client_sock.send(response)

        # clean up
        client_sock.shutdown(1)
        client_sock.close()

    def process_response(self, request):
        formatted_data = request.strip().split(NEWLINE)
        request_words = formatted_data[0].split()

        if len(request_words) == 0:
            return

        requested_file = request_words[1][1:]
        if request_words[0] == "GET":
            return self.get_request(requested_file, formatted_data)
        if request_words[0] == "POST":
            return self.post_request(requested_file, formatted_data)
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

    # TODO: Write the response to a GET request
    def get_request(self, requested_file, data):

        if (not os.path.exists(requested_file)):
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
    def post_request(self, requested_file, data):

        builder = ResponseBuilder()
        builder.set_status("200", "OK")
        builder.add_header("Connection", "close")
        builder.add_header("Content-Type", MIME_TYPES["html"])
        builder.set_content(get_file_contents("MyForm.html"))
        return builder.build()

    """
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

if __name__ == "__main__":
    HTTPServer()
