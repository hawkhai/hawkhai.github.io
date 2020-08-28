#encoding=utf8
import re, os, sys

GIT_URL = 'url: "https://blog.hawkhai.com"'
GIT_BASEURL = 'baseurl: ""'
SUN_URL = 'url: "https://sunocean.life"'
SUN_BASEURL = 'baseurl: "/blog"'
JEKYLL = "bundle exec jekyll serve --host localhost"

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

def mainjekyll():
    currentfile = os.path.abspath(__file__)
    configfile = os.path.join(os.path.split(currentfile)[0], "_config.yml")
    print(configfile)

    config = readfile(configfile)
    config = config.replace(GIT_URL, SUN_URL)
    config = config.replace(GIT_BASEURL, SUN_BASEURL)
    writefile(configfile, config)

    assert config.find(SUN_URL) != -1, SUN_URL
    assert config.find(SUN_BASEURL) != -1, SUN_BASEURL
    os.system(JEKYLL)

if __name__ == "__main__":
    mainjekyll()
