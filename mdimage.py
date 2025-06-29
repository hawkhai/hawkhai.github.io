#encoding=utf8
import sys
import re, os, sys
sys.path.append("../")
import datetime, time
from pythonx.funclib import *

AUTOFORMAT = "format" in sys.argv
NEWLINE_CHAR = "\r\n" if IS_WINDOWS else "\n"
DEBUG = "debug" in sys.argv

def mainfilew(fpath, fname, ftype):
    if not ftype in ("md",): return
    fdata = readfile(fpath, True)
    fdatabak = fdata[:]

    z0 = bytesToString(b"\xef\xbc\x90")
    zA = bytesToString(b"\xef\xbc\xa1")

    li = fdata.split(NEWLINE_CHAR)
    li2 = []
    first = True
    for line in li:
        result = refindall("^({})\\s+({})$".format("[^ ]+\\.(?:png|jpg|jpeg|webp|gif|jfif|webm)", "[0-9.]+"), line)
        if result:
            result = result[0]
            if first:
                print(fpath)
                first = False
            img, idx = result
            line = r"""{{% include image.html url="/images/{}" relocate="{}" %}}""".format(img, idx)
            if idx == "0":
                line = r"""{{% include image.html url="/images/{}" %}}""".format(img,)
            print("\t"*1, result, line)
            imgfile = "./images/"+img
            assert os.path.exists(imgfile), imgfile
            if refindall("^IMG_[0-9a-f]{32}\\.", img):
                print("极光图片", imgfile)
                from PIL import Image
                img = Image.open(imgfile)
                width, height = img.size
                img = img.resize((width, height), Image.ANTIALIAS)
                img.save(imgfile)
            li2.append(line)
        else:
            result = refindall("\\xef\\xbc[\\x90-\\x99\\xa1-\\xba]", line)
            if result:
                if first:
                    print(fpath)
                    first = False
                print("\t"*1, result, line)
                for ch in result:
                    chtail = ch[-1]
                    if 0x90 <= ord(chtail) <= 0x99:
                        target = "%d"%(ord(chtail)-0x90)
                        print(bytesToString(stringToBytes(ch), "utf8"), target)
                        line = line.replace(ch, target)
                    elif 0xa1 <= ord(chtail) <= 0xba:
                        target = "%c"%(ord('A')+ord(chtail)-0xa1)
                        print(bytesToString(stringToBytes(ch), "utf8"), target)
                        line = line.replace(ch, target)
                    else:
                        assert False, ch
                li2.append(line)
            else:
                li2.append(line)

    fdata = NEWLINE_CHAR.join(li2)

    if fdata != fdatabak and AUTOFORMAT:
        print("writefile", fpath)
        writefile(fpath, fdata)

def main():
    print(parsePythonCmdx(__file__))
    searchdir(".", mainfilew, ignorelist=(
        "backup", "d2l-zh", "mathjax", "tempdir", "msgboard",
        "Debug", "Release", ".vs", "openglcpp", "opengl-3rd", "opengles3-book", "opengles-book-samples",
        "UserDataSpider", "docs.gl", "ml-notes", "table-transformer", "pdfdata", "imgclassify", "ksample",
        "node_modules",
        ), reverse=True)

if __name__ == "__main__":
    print(sys.argv)
    import cProfile
    if len(sys.argv) >= 2 and os.path.isdir(sys.argv[1]):
        workdir = sys.argv[1]
        @CWD_DIR_RUN(workdir)
        def maingo():
            cProfile.run("main()") if DEBUG else main()
        maingo()
    else:
        cProfile.run("main()") if DEBUG else main()
    print(parsePythonCmdx(__file__))
