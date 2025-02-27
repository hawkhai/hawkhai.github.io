#encoding=utf8
import re, os, sys
sys.path.append("../")
from pythonx.funclib import *
from pythonx.pelib import mydllfunc, get_local_ipinfo

GIT_URL = 'url: "https://blog.hawkhai.com"'
GIT_URLx = 'urlx: "https://blog.hawkhai.com"'
GIT_BASEURL = 'baseurl: ""'
SUN_URL = 'url: "https://sunocean.life"'
SUN_URLx = 'urlx: "https://sunocean.life"'
SUN_BASEURL = 'baseurl: "/blog"'
JEKYLL = "bundle exec jekyll serve --watch --host 0.0.0.0"

def readfile(fpath):
    fin = open(fpath, "rb")
    fdata = fin.read()
    fin.close()
    return bytesToString(fdata)

def writefile(fpath, fdata):
    fout = open(fpath, "wb")
    fout.write(stringToBytes(fdata))
    fout.close()

def bytesToString(bytes, encoding="ISO8859-1"):
    return bytes.decode(encoding)

def stringToBytes(str, encoding="ISO8859-1"):
    return str.encode(encoding)

def checkbackup():
    print(LINE_SEP_SHORT)
    print("检查备份文件...")
    htmlist = os.listdir("backup")
    htmlist = [md[:-3]+".html" for md in htmlist if md.endswith(".md")]
    htmlist.sort()
    idxdata = "[htmlist]"
    for md in htmlist:
        idxdata += "\n" + md + "=1"
    writefile("backup/htmlist.ini", idxdata)

def checksite():
    print(LINE_SEP_SHORT)
    print("检查 _site 文件夹...")
    def sitefile(fpath, fname, ftype):
        if ftype in ("py",):
            return
        fdata = readfile(fpath)
        # http://localhost:4000/blog/
        if fdata.find("localhost:4000") != -1 and fname not in ("blog.js",
                "mdserv.py.bak", "opencv-4.1.2.html", "feed.xml",
                "rdevblog.py.bak", "rdevblog.py",):
            print("警告", "localhost:4000")
            openTextFile(fpath)
            #assert False, fpath
    searchdir("_site", sitefile, ignorelist=["_site",])

def checkgitline(fpath, tag, until):
    lines = readfileLines(fpath)
    for line in lines:
        if line.find(until) != -1:
            return
        if line.find(tag) != -1:
            assert False, fpath
    assert False, fpath

def checkgit():
    print(LINE_SEP_SHORT)
    print("检查 git 是否存在误入...")
    ymlfile = "tempdir/_config.yml.txt"
    gemfile = "tempdir/Gemfile.lock.txt"
    if not os.path.exists("tempdir"):
        os.makedirs("tempdir")
    os.system("git log -p _config.yml  > {}".format(ymlfile,))
    os.system("git log -p Gemfile.lock > {}".format(gemfile,))

    #checkgitline(ymlfile, "sunocean.life", "0d86ec78b65c032162ea43fe8abb13d79288ec3f")
    #checkgitline(gemfile, "wdm", "0d86ec78b65c032162ea43fe8abb13d79288ec3f")

def modifyconfig():
    print(LINE_SEP_SHORT)
    currentfile = os.path.abspath(__file__)
    configfile = os.path.join(os.path.split(currentfile)[0], "_config.yml")
    print("修改配置文件", configfile)

    config = readfile(configfile)
    config = config.replace(GIT_URL, SUN_URL)
    config = config.replace(GIT_URLx, SUN_URLx)
    config = config.replace(GIT_BASEURL, SUN_BASEURL)
    writefile(configfile, config)

    assert config.find(SUN_URL) != -1, SUN_URL
    assert config.find(SUN_URLx) != -1, SUN_URLx
    assert config.find(SUN_BASEURL) != -1, SUN_BASEURL

def mainjekyll():
    checkbackup()
    checksite()
    checkgit()
    modifyconfig()
    retv = os.system(JEKYLL)
    return retv

if __name__ == "__main__":
    if IS_WINDOWS:
        result = get_local_ipinfo()
        copyfile("Gemfile-win", "Gemfile")
        copyfile("Gemfile-win.lock", "Gemfile.lock")
    else:
        result = None
        copyfile("Gemfile-mac", "Gemfile")
        copyfile("Gemfile-mac.lock", "Gemfile.lock")
    osremove("assets\\localhost.js")
    ipaddrx = result
    if ipaddrx and len(ipaddrx) == 1:
        result = ipaddrx[0]
        writefile("assets\\localhost.js", "var localhostip = '" + result + "';\r\n")
    print(result)
    if IS_MACOS:
        while True:
            try: # ^Z to Stopped
                print("mainjekyll", mainjekyll())
            except:
                traceback.print_exc()
    else:
        mainjekyll()
