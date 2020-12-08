#encoding=utf8
import re, os, sys
sys.path.append("../")
from pythonx.funclib import *

OPENFILE = "openfile" in sys.argv
AUTOFORMAT = "format" in sys.argv
REBUILD = "rebuild" in sys.argv

# 在西歐、北歐及東歐國家常用的字母，帶變音符，和一般英文字母不同。
DIACRITIC = """
À Á Â Ã Ä Å Æ Ā Ă Ą
Ç Ć Ĉ Ċ
Ð Ď Đ
È É Ê Ë Ē Ė Ę Ě Ə
Ĝ Ġ Ģ
Ĥ Ħ
Ì Í Î Ï Ī Į Ĳ
Ĵ
Ķ
Ļ Ł
Ñ Ń Ņ Ň
Ò Ó Ô Õ Ö Ø Ő Œ
Ŕ Ř
ẞ Ś Ŝ Ş Š Ș Þ
Ţ Ť Ț
Ù Ú Û Ü Ū Ŭ Ů Ű Ų
Ŵ
Ý Ŷ
Ÿ Ź Ż Ž
à á â ã ä å æ ā ă ą
ç ć ĉ ċ
ð ď đ
è é ê ë ē ė ę ě ə
ĝ ġ ģ
ĥ ħ
ì í î ï ī į ĳ
ĵ
ķ
ļ ł
ñ ń ņ ň
ò ó ô õ ö ø ő œ
ŕ ř
ß ś ŝ ş š ș þ
ţ ť ț
ù ú û ü ū ŭ ů ű ų
ŵ
ý ŷ
ÿ ź ż ž"""
DIACRITIC = "[{}]".format("".join(DIACRITIC.split()))

linktagli = (("{% include relref_bili.html %}]",     "bilibili]",    "bilibili"),
             ("{% include relref_zhihu.html %}]",    "zhihu]",       "zhihu"),)

mdkeylist = """
categories
tags
location
comments
toclistyle
layout
visibility
mermaid
title
mathjax
glslcanvas
permalink
toc""".split()

def getLeftSpaceCount(line):
    line = line[:]
    assert not line.startswith("\t"), line
    count = 0
    while line and line[0] == " ":
        line = line[1:]
        count += 1
    return count

def calcType(ttype, url):
    url = url.split("?")[0].split("#")[0]
    url = url.split("/")[-1].strip()
    if not url: return ttype
    secli = url.split(".")
    if len(secli) <= 1: return ttype
    if not secli[-1]: return ttype
    return "."+secli[-1].lower()

def backupUrlContent(fpath, url):
    for file in ("/qt-creator-opensource-windows-x86-4.13.2.exe",
                 "/qt-opensource-windows-x86-5.14.1.exe",
                 "/qt-opensource-windows-x86-5.14.2.exe",
                 "/d2l-zh.zip",
                 "/mingw-get-setup.exe",
                ):
        if url.endswith(file):
            return
    assert not url.endswith(".exe"), url
    assert not url.endswith(".zip"), url
    # 有可能挂掉的网站，都稍微做一下备份。
    for host in ("https://pypi.tuna.tsinghua.edu.cn/", "https://apache-mxnet.s3.cn-north-1.amazonaws.com.cn/",
                 "https://www.bilibili.com/",
                 "http://doc.qt.nokia.com/",
                 "http://www.cuteqt.com/", "http://ogre3d.cn/",
                 "http://en.wikipedia.org/", "https://msdn.microsoft.com/",
                 "http://tcbuglist.rdev.kingsoft.net/", "https://ml00cz5fm4.feishu.cn/",
                ):
        if url.startswith(host):
            return

    print(fpath, url)
    chrome = False
    for host in ("https://blog.walterlv.com/",
                 "https://betterexplained.com/",
                 "https://opencv-python-tutroals.readthedocs.io/",
                 "https://stackoom.com/",
                 "https://www.freesion.com/",
                 "https://www.jianshu.com/",
                 "https://rubyinstaller.org/",
                 "https://www.anaconda.com/",
                 "https://bbs.pediy.com/",
                 "http://developer.nvidia.com/",
                ):
        if url.startswith(host):
            chrome = True
    mdname = os.path.split(fpath)[-1]
    uhost = url.split("//")[1].split("/")[0]
    umd5 = getmd5(url)
    ttype = ".html"
    local = os.path.join("backup", mdname, uhost, umd5 + ttype)
    ttype = calcType(ttype, url)
    slocal = os.path.join("backup", mdname, uhost, umd5[:8] + ttype)
    if os.path.exists(local):
        os.rename(local, slocal)
    fdata = netgetCacheLocal(url, timeout=60*60*24*1000, chrome=chrome, local=slocal)
    remote = "{}/{}/{}/{}".format("backup", mdname, uhost, umd5[:8] + ttype)
    return remote

def createCnFile():
    page = b""
    ordch = 0x4e00
    count = 0
    while ordch <= 0x9fa5:
        ch = chr(ordch)
        ordch += 1
        page += ch.encode("utf8")
        count += 1
        if count % 50 == 0:
            page += b"\r\n"
    tempfile = tempfile = os.path.join("tempdir", "tempfile.txt")
    writefile(tempfile, page)
    openTextFile(tempfile)
#createCnFile()

g_hostset = {}
def collectHost(fpath, line):

    reflist = []

    linesrc = line[:]
    xline = line[:]
    for tak, src, name in linktagli:
        xline = xline.replace(tak, src)
    #li = re.findall("<.*?>", xline)
    #for tx in li:
    #    line = line.replace(tx, "")

    regex = r"""(
                    (https?)://
                        ([a-z0-9\.-]+\.[a-z]{2,6})
                        (:[0-9]{1,4})?
                    (/[a-z0-9\&%_\./~–-]*)?
                    (\?[a-z0-9\&%_\./~=:-]*)?
                    (#[a-z0-9\&%_\./~=:-]*)?
                )"""

    regex = "".join(regex.split())
    li = re.findall(regex, line, re.IGNORECASE)
    if not li: return
    for tx in li:
        url = tx[0]
        host = tx[2]
        checkz = line.split(url)
        for xline in checkz[1:]:
            checkli = ["", ")", "]", ">", " ", "*"]
            if url in ("https://msdl.microsoft.com/download/symbols",):
                checkli.append(";")
            if xline[:2] in ("{{",):
                continue
            if not xline[:1] in checkli:
                print(line)
                print(url)
                assert False, checkz
        assert not url.endswith("."), path +" "+ url
        remote = backupUrlContent(fpath, url)
        if remote:
            reflist.append([url, remote])
        if not host in g_hostset:
            g_hostset[host] = 0
        g_hostset[host] += 1

    for tak, src, name in linktagli:
        # 视频要特别标注域名。
        li1 = re.findall(name+".com", xline)
        li2 = re.findall(name+"\\]", xline)
        if len(li1) == len(li2):
            continue
        print(xline)
        print(li1)
        print(li2)
        assert False, linesrc
    return reflist

g_cnchar = []
g_cschar = []
g_enchar = []
g_tpset = set()
g_mdkeyset = set()
FONT_REF_SNAP = "<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>"
def removeRefs(fpath, lines):
    lineCount = len(lines)
    headIndex = -1
    for index in range(lineCount):
        i = lineCount-1 - index
        if not lines[i] or not lines[i].strip():
            continue
        if re.findall("^- \\[[0-9]+\\] \\[{}\\]\\({}\\)$".format(".*?", ".*?"), lines[i]):
            continue
        if lines[i] == FONT_REF_SNAP:
            headIndex = i
            break
        break

    if headIndex != -1:
        assert lines[headIndex-1] == "", "%r"%lines[headIndex-1]
        assert lines[headIndex-2] == "-----", "%r"%lines[headIndex-2]
        assert lines[headIndex-3] == "", "%r"%lines[headIndex-3]
        lines = lines[:headIndex-3]
    return lines

def appendRefs(fpath, lines):
    reflist = []

    for index, line in enumerate(lines):
        ireflist = collectHost(fpath, line)
        if ireflist:
            reflist.extend(ireflist)

    if reflist:
        lines.append("")
        lines.append("-----")
        lines.append("")
        lines.append(FONT_REF_SNAP)
        lines.append("")
        lines.append("")
        urlset = set()
        count = 0
        for url, remote in reflist:
            if url in urlset: continue
            urlset.add(url)
            count = count + 1
            from urllib.parse import unquote
            remote = "{% " + ("include relref.html url=\"/%s\"" % (remote,)) + " %}"
            lines.append("- [{}] [{}]({})".format(count, url, remote))
        lines.append("")
    return lines

def mainfile(fpath, fname, ftype):

    ftype = ftype.lower()
    errcnt = 0

    warnCnEnSpace    = ftype in ("md", "php", "html", "htm",) # 英文中文空符检查
    warnTitleSpace   = ftype in ("md",) # 标题前后空行检查
    warnIndentSpace  = ftype in ("md", "php",) # 缩进检查
    isMdFile         = ftype in ("md",)
    isSrcFile        = ftype in ("md", "py", "php", "html", "htm", "js",)

    if not isSrcFile:
        if fpath.find("\\_site\\") != -1:
            g_tpset.add(ftype)
        return

    if isMdFile:
        fdata = readfile(fpath, True).strip()
        if fdata.startswith("---"):
            kvlist = fdata.split("---")[1].strip().split("\n")
            for kv in kvlist:
                kv = kv.strip()
                key, value = kv.split(":", 1)
                key = key.strip()
                value = value.strip()
                g_mdkeyset.add(key)

    if fpath.find("\\_site\\") != -1:
        return

    def linerstrip(line):
        if isMdFile:
            for tak, src, name in linktagli:
                # 移除多余空格
                line = line.replace("  "+tak, tak)
                line = line.replace(" "+tak, tak)
                # 格式化。
                line = line.replace(tak, " "+tak)
                line = line.replace(src, tak)
                line = line.replace("[ "+tak, "["+name+" "+tak)
            line = line.replace(" ——", "——").replace(" ——", "——")
            line = line.replace("—— ", "——").replace("—— ", "——")
            line = line.replace("——", " —— ")
        return line.rstrip()

    print(fpath)
    lines = readfileLines(fpath, False, False, "utf8")
    lines = removeRefs(fpath, lines)
    lines = [linerstrip(line) for line in lines]
    lines.append("")
    lines.append("")
    while len(lines) >= 2 and not lines[-1] and not lines[-2]:
        lines = lines[:-1]
    while len(lines) >= 1 and not lines[0]:
        lines = lines[1:]

    if fname in ("relref.html", "relref_bili.html", "relref_zhihu.html",):
        while len(lines) >= 1 and not lines[-1]:
            lines = lines[:-1]

    if isMdFile:
        lines = appendRefs(fpath, lines)

    codestate = False
    chartstate = False
    for index, line in enumerate(lines):

        preline = lines[index - 1] if index > 0 else ""
        nextline = lines[index + 1] if index < len(lines)-1 else ""

        tagregex = "^\\s*[#]+ "
        tagregexk = "^\\s*[#]+\\s{2,}"
        prelinetag = re.findall(tagregex, preline)
        nextlinetag = re.findall(tagregex, nextline)
        if warnTitleSpace:
            assert not re.findall(tagregexk, preline), preline

        if re.findall("^\\s*[*-]+ ", line):
            idtcnt = 2
        else:
            idtcnt = 4

        cnsign  = "‘’“”"
        cnregex = "\u4e00-\u9fa5"

        for ch in line:
            ordch = ord(ch)
            regch = "\\u%04x"%(ordch)
            if ordch <= 0x7F or re.findall(DIACRITIC, ch):
                g_enchar.append(ch)
                continue
            if ordch >= 0x4e00 and ordch <= 0x9fa5:
                if cnregex.find(regch) == -1:
                    cnregex += regch
                if g_cnchar.count(ch) == 0:
                    g_cnchar.append(ch)
            else:
                if cnsign.find(regch) == -1:
                    cnsign += regch
                if g_cschar.count(ch) == 0:
                    g_cschar.append(ch)
        cnregex += cnsign

        if line.find("\xa0") != -1 and not fname in ("glslEditor.min.js",):
            print("xspace", fpath, line)
            errcnt += 1

        #liw = re.findall("[{}]+".format(cnregex,), line, re.IGNORECASE)
        #lia = re.findall("[^{}]+".format(cnregex,), line, re.IGNORECASE)

        linec = line
        for itmp in re.findall("\\$\\$.*?\\$\\$", line): # 忽略数学公式
            linec = linec.replace(itmp, "$$$$")
        for itmp in re.findall("“.*?”", line): # 忽略双引号
            linec = linec.replace(itmp, "“”")

        lix1 = re.findall("[{}][^{} *]".format(cnregex, cnregex), linec, re.IGNORECASE)
        lix2 = re.findall("[^{} *][{}]".format(cnregex, cnregex), linec, re.IGNORECASE)
        lix = []
        lix.extend(lix1)
        lix.extend(lix2)

        cnsignregex = "[{}]".format(cnsign)
        for ix in lix:
            cx, cy = ix
            if re.findall(cnsignregex, cy) or re.findall(cnsignregex, cx):
                continue
            if cy in "-<]" or cx in "->[":
                continue

            if chartstate:
                continue

            if cx in ("\"", "[") and (" "+line).count(" "+ix) == 1:
                continue
            if cy in ("\"", "]", ",") and (line+" ").count(ix+" ") == 1:
                continue

            if cx in ("(", ) and (" \\"+line).count(" \\"+ix) == 1:
                continue
            if cy in ("\\", ) and (line+") ").count(ix+") ") == 1:
                continue

            if cx in ("\"",) and ("["+line).count("["+ix) == 1:
                continue
            if cy in ("\"",) and ((line+"]").count(ix+"]") == 1 or (line+",").count(ix+",") == 1):
                continue

            if cy in (".") and (line.count(ix+"rar") == 1 or line.count(ix+"zip") == 1):
                continue

            if not warnCnEnSpace:
                continue

            if codestate:
                if cy in "\":" or cx in "\":":
                    continue

                if line.startswith("print ("):
                    continue

            print("[%d]"%(index+1), ix, cx, cy, "\t", line)
            errcnt += 1
            if AUTOFORMAT:
                line = line.replace(ix, cx+" "+cy)
                lines[index] = line

        fxline = "".join(line.split())
        if fxline.startswith("<divclass=\"mermaid\"") and not chartstate:
            chartstate = True
        if fxline.startswith("</div>") and chartstate:
            chartstate = False

        if fxline.startswith("{%highlight"):
            codestate = True
            continue
        if fxline.startswith("{%endhighlight%}"):
            codestate = False
            continue

        if fxline.startswith("```") and not codestate:
            codestate = True
            continue
        if fxline.startswith("```") and codestate:
            codestate = False
            continue

        if codestate:
            continue

        if warnTitleSpace and (prelinetag or nextlinetag):
            if line:
                openTextFile(fpath)
                assert False, "{}:{} {}".format(fpath, index+1, line)

        countspace = getLeftSpaceCount(line if warnIndentSpace else line.replace("\t", " "*4))
        if countspace > 12 or countspace % idtcnt == 0:
            pass # ok
        elif warnIndentSpace:
            openTextFile(fpath)
            assert False, "{}:{} \"{}\"".format(fpath, index+1, line)

    page = "\r\n".join(lines)
    while page.find("\r\n" * 3) != -1:
        page = page.replace("\r\n" * 3, "\r\n" * 2)

    codereg = "\\{\\%\\s*highlight.*?\\{\\%\\s*endhighlight\\s*\\%\\}"
    codeli1 = re.findall(codereg, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)

    coderegz = "```.*?```"
    codeli1z = re.findall(coderegz, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)

    if warnTitleSpace:
        page = page.replace("\r\n"*2+"### ", "\r\n"*3+"### ")
        page = page.replace("\r\n"*2+"## ",  "\r\n"*3+"## ")
        page = page.replace("\r\n"*2+"# ",   "\r\n"*3+"# ")

    codeli2 = re.findall(codereg, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)
    for i in range(len(codeli1)):
        page = page.replace(codeli2[i], codeli1[i])

    codeli2z = re.findall(coderegz, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)
    for i in range(len(codeli1z)):
        page = page.replace(codeli2z[i], codeli1z[i])

    writefile(fpath, page.encode("utf8"))
    return errcnt

def viewchar(lichar, xfile, xmin, xmax):
    li = list(set("".join(lichar)))
    li.sort()
    page = ""
    minv, maxv = 1024, 0
    for index, tchar in enumerate(li):
        page += tchar
        if (index + 1) % 50 == 0:
            page += "\r\n"
        if re.findall(DIACRITIC, tchar):
            continue
        minv = min(minv, ord(tchar))
        maxv = max(maxv, ord(tchar))
    tempfile = os.path.join("tempdir", xfile)
    writefile(tempfile, page.encode("utf8"))

    if OPENFILE:
        openTextFile(tempfile)
    print(minv, maxv)
    print([("%04x"%ord(k), k) for k in li[:5]]),
    print([("%04x"%ord(k), k) for k in li[-5:]])
    assert xmin <= minv and maxv <= xmax

def checklog(fpath1, fpath2):
    localfile = os.path.join("tempdir", getFileMd5(fpath1), getFileMd5(fpath2))
    return os.path.exists(localfile)

def savelog(fpath1, fpath2):
    localfile = os.path.join("tempdir", getFileMd5(fpath1), getFileMd5(fpath2))
    copyfile(fpath2, localfile)

def removelog(fpath1, fpath2):
    localfile = os.path.join("tempdir", getFileMd5(fpath1), getFileMd5(fpath2))
    if os.path.exists(localfile):
        os.remove(localfile)

def mainfilew(fpath, fname, ftype):
    if checklog(__file__, fpath) and not REBUILD:
        # print("cached", fpath)
        return 0
    removelog(__file__, fpath)
    errcnt = mainfile(fpath, fname, ftype)
    if errcnt == 0:
        savelog(__file__, fpath)
    return errcnt

def main():
    print(parsePythonCmdx(__file__))
    removedirTimeout("tempdir")
    clearemptydir("tempdir")
    searchdir(".", mainfilew, ignorelistMore=(
        "backup", "d2l-zh", "mathjax", "tempdir", "msgboard",
        "Debug", "Release", ".vs", "openglcpp", "opengl-3rd",))
    global g_cschar
    global g_tpset

    viewchar(g_cnchar, "cnfile.txt", 0x80, 0x7FFFFFFF)
    viewchar(g_cschar, "csfile.txt", 0x80, 0x7FFFFFFF)
    viewchar(g_enchar, "enfile.txt", 0x0,  0x7F)

    print(LINE_SEP_SHORT)
    g_cschar = list(set(g_cschar))
    g_cschar.sort()
    print("".join(g_cschar))
    imgset  = ("jpeg", "jpg", "png", "gif", )
    fontset = ("eot", "ttf", "woff", "svg", "woff2", )
    codeset = ("cc", "js", "txt", "xml", "css", "mk", "lock", "zip", "makefile", )
    g_tpset -= set(imgset)
    g_tpset -= set(fontset)
    g_tpset -= set(codeset)
    print(g_tpset)
    print(g_mdkeyset)

    hostlist = sorted(g_hostset.items(), key=lambda x: x[1], reverse=True)
    print(hostlist)
    for hostx in hostlist[:10]:
        print(hostx)

if __name__ == "__main__":
    main()
