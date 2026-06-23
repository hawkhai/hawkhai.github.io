#encoding=utf8
"""Per-file formatting and content validation for mdrstrip."""
from .runtime import *
from .config import getLinkTagSrc, loadRougifyList, readFileIgnoreList
from .filesystem import checkFileSize
from .references import appendRefs, removeRefs

ROUGIFY_LIST = loadRougifyList()

def mainfile(fpath, fname, ftype, fdepth=0):

    if fpath.endswith(SPACEBACKFILE_TAIL):
        fjson = readfileJson(fpath, "utf8")
        writefileJson(fpath, fjson, ascii=False, encoding="utf8")
        return

    iglist = readFileIgnoreList("config/mdrstrip_file_ignore.txt")
    if fname in iglist:
        return

    fpathsrc, fnamesrc, ftypesrc = fpath, fname, ftype
    checkFileSize(fpath, fname, ftype)

    ftype = ftype.lower()
    errcnt = 0

    warnCnEnSpace    = ftype in ("md", "php", "html", "htm", "vsh", "fsh",) # 英文中文空符检查
    warnTitleSpace   = ftype in ("md",) # 标题前后空行检查
    warnIndentSpace  = ftype in ("md", "php", "scss", "vsh", "fsh",) # 缩进检查
    isMdFile         = ftype in ("md",)
    isSrcFile        = ftype in ("md", "php", "html", "htm", "js", "css", "scss", "svg", "py", "vsh", "fsh",)
    keepStripFile    = ftype in ("svg",) or fname in ("gitsrc.html",) or refindall("^relref[a-z_]*\\.html$", fname)
    keepFileTypeList = ("rar", "zip", "pdf", "doc", "mp4",) # 中英文间隔，容易造成失误的列表。

    if fpath.find(os.sep+"winfinder"+os.sep) != -1:
        isSrcFile = isSrcFile or ftype in ("h", "cpp", "cxx", "rc", "c",)

    if not isSrcFile:
        if fpath.find(os.sep+"_site"+os.sep) != -1: # 必须在 _site 文件夹?
            G_TYPESET.add(ftype)
        return

    mdconfig = {}
    if isMdFile:
        # 收集 Jekyll 头定义 key 集合。
        fdata = readfile(fpath, True).strip()
        if fdata.startswith("---"):
            kvlist = fdata.split("---")[1].strip().split("\n")
            for kv in kvlist:
                kv = kv.strip()
                key, value = kv.split(":", 1)
                key = key.strip()
                value = value.strip()
                G_MDKEYSET.add(key)
                mdconfig[key] = value

    if fpath.find(os.sep+"_site"+os.sep) != -1: # _site 文件夹
        return

    def lineRstrip(line):
        if isMdFile:
            for name, host in LINKTAGARRAY:
                tak = getLinkTagSrc(name)
                # 移除多余空格
                line = line.replace("  "+tak+"]", tak+"]")
                line = line.replace(" "+tak+"]", tak+"]")
                # 格式化。
                line = line.replace(tak+"]", " "+tak+"]")
                line = line.replace(name+"]", tak+"]")
                line = line.replace("[ "+tak+"]", "["+name+" "+tak+"]")
            line = line.replace(" ——", "——").replace(" ——", "——")
            line = line.replace("—— ", "——").replace("—— ", "——")
            line = line.replace("——", " —— ")
        return line.rstrip()

    print(fpath)
    if IS_MACOS or IS_LINUX:
        fdata = readfile(fpath)
        fdata = fdata.replace(b"\r\n", b"\n").replace(b"\r", b"\n").replace(b"\n", b"\r\n")
        writefile(fpath, fdata)
    md5src = getFileMd5(fpath, mycache=MYCACHE, assertx=False) # mainfile
    try:
        lines = readfileLines(fpath, False, False, "utf8")
    except UnicodeDecodeError as ex:
        print("跳过非 UTF-8 文件: {} byte={} pos={} reason={}".format(
            fpath, hex(ex.object[ex.start]), ex.start, ex.reason))
        return 0
    except Exception as ex:
        openTextFile(fpath)
        raise ex
    lines = removeRefs(fpath, lines)
    lines = [lineRstrip(line) for line in lines]
    lines.append("")
    lines.append("")
    while len(lines) >= 2 and not lines[-1] and not lines[-2]:
        lines = lines[:-1]
    while len(lines) >= 1 and not lines[0]:
        lines = lines[1:]

    if keepStripFile:
        while len(lines) >= 1 and not lines[-1]:
            lines = lines[:-1]

    if isMdFile:

        imgthumb = True
        lineCount = 0
        for line in lines:
            if line.strip() == "---":
                lineCount = lineCount + 1
                if lineCount >= 2: break
            if "".join(line.strip().lower().split()) == "imgthumb:false":
                imgthumb = False
                break
            # 避免格式化的文件。
            if "".join(line.strip().lower().split()) == "codeformat:false":
                return

        try:
            lines = appendRefs(fpath, md5src, lines, imgthumb, mdconfig)
        except AssertionError as ex:
            if fdepth >= 5:
                raise ex
            openTextFile(fpath)
            traceback.print_exc()
            print("断言错误 {}".format(ex,))
            os.system(PAUSE_CMD)
            return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

    # .spaceback.json
    spacebackfile = (os.path.splitext(fpath)[0] + SPACEBACKFILE_TAIL)
    spacebackjson = {}
    if not os.path.exists(spacebackfile):
        spacebackfile = os.path.join(os.path.split(fpath)[0], "k"+os.path.splitext(fname)[0]+SPACEBACKFILE_TAIL)
    if os.path.exists(spacebackfile):
        spacebackjson = readfileJson(spacebackfile, "utf8")

    spacebackjson["粤 ICP 备 17134686 号"] = "粤ICP备17134686号"

    codestate = False
    chartstate = False
    frontmatter = False
    frontmatter_count = 0
    for index, line in enumerate(lines):

        if isMdFile and line.strip() == "---":
            frontmatter_count += 1
            if frontmatter_count == 1:
                frontmatter = True
            elif frontmatter_count == 2:
                frontmatter = False

        for kftype in keepFileTypeList:
            line = line.replace(" ."+kftype, "."+kftype)
            lines[index] = line

        if isMdFile and line.count("**") >= 2 and line.count("**") % 2 == 0 and line.count("***") == 0 and not codestate:
            dotlines = line.split("**")
            newline = ""
            for idx, dot in enumerate(dotlines):
                if idx % 2 == 1:
                    if not newline.strip():
                        newline = newline + "**" + dot.strip() + "** "
                    else:
                        newline = newline.rstrip() + " **" + dot.strip() + "** "
                else:
                    if idx >= 2:
                        newline += dot.lstrip()
                    else:
                        newline += dot
            newline = newline.rstrip()
            line = newline
            lines[index] = line

        line = line.replace("````", "```").replace("````", "```")
        linxCount = line.count("`")
        if isMdFile and linxCount >= 2 and linxCount % 2 == 0:
            newline = ""
            linxCount = 0
            for idx, ch in enumerate(line):
                if ch == '`':
                    linxCount = linxCount + 1
                    if linxCount % 2 == 1:
                        if newline and not newline.endswith(" "):
                            if not newline.endswith("："):
                                newline += " "
                            newline += "`"
                        else:
                            if newline.endswith("： "):
                                newline = newline[:-1]
                            newline += "`"
                    else:
                        newline += "`"
                        if idx+1 < len(line) and line[idx+1] != " ":
                            newline += " "
                else:
                    newline += ch
            line = newline
            lines[index] = line

        preline = lines[index - 1] if index > 0 else ""
        nextline = lines[index + 1] if index < len(lines)-1 else ""

        # ```java
        # {% highlight ruby %}
        # https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers
        li1 = refindall("```\\s*([0-9a-z_#+-]+)", line, re.IGNORECASE)
        li2 = refindall("\\{%\\s*highlight\\s*([0-9a-z_#+-]+)", line, re.IGNORECASE)
        li1.extend(li2)
        for i in li1:
            if not i in ROUGIFY_LIST:
                openTextFile(fpath)
                print("代码语言无法识别 {}:{} \"{}\"".format(fpath, index+1, i))
                os.system(PAUSE_CMD)
                return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

        tagregex = "^\\s*[#]+\\s"
        prelinetag = refindall(tagregex, preline)
        nextlinetag = refindall(tagregex, nextline)
        if warnTitleSpace and not codestate:
            tagregexk = "^\\s*[#]+\\s{2,}" # md 文件标题后接的空格 只能是一个。
            if refindall(tagregexk, preline):
                openTextFile(fpath)
                assert False, preline

        if refindall("^\\s*[*-]+\\s", line):
            idtcnt = 2 # 如果在列表里面，缩进检查 2 个为单位。
        else:
            idtcnt = 4

        cnsign  = "‘’“”" # 中文符号
        cnregex = "\u4e00-\u9fa5" # 中文汉字
        # 统计出现的字符。
        for ch in line:
            ordch = ord(ch)
            regch = "\\u%04x"%(ordch)
            if ordch <= 0x7F or isDiacritic(ch):
                G_ENCHAR.append(ch) # 英文
                continue
            if ordch >= 0x4e00 and ordch <= 0x9fa5:
                if cnregex.find(regch) == -1:
                    cnregex += regch # 中文汉字
                if G_CNCHAR.count(ch) == 0:
                    G_CNCHAR.append(ch)
            else:
                if cnsign.find(regch) == -1:
                    cnsign += regch # 中文符号
                if G_CSCHAR.count(ch) == 0:
                    G_CSCHAR.append(ch)
        cnregexc = cnregex[:]
        cnregex += cnsign # 中文汉字符号都来起。

        # 1.不间断空格\u00A0,主要用在office中,让一个单词在结尾处不会换行显示,快捷键ctrl+shift+space;
        # 2.半角空格(英文符号)\u0020,代码中常用的;
        # 3.全角空格(中文符号)\u3000,中文文章中使用;
        # 不能出现全角的空格。
        # utf8：20 c2a0 e38080 "\xa0"
        if line.find("\u00A0") != -1 and line.find("\u3000") != -1 and not fname in ("glslEditor.min.js",):
            print("xspace", fpath, line)
            errcnt += 1

        #liw = refindall("[{}]+".format(cnregex,), line, re.IGNORECASE)
        #lia = refindall("[^{}]+".format(cnregex,), line, re.IGNORECASE)

        linec = line
        for itmp in refindall("\\$\\$.*?\\$\\$", line): # 忽略数学公式
            linec = linec.replace(itmp, " ") # "$$$$")
        for itmp in refindall("“.*?”", line): # 忽略双引号
            linec = linec.replace(itmp, " ") # "“”")
        for itmp in refindall("`.*?`", line): # 忽略代码部分
            linec = linec.replace(itmp, " ") # "“”")

        # 忽略特殊的 tag 标记。
        for itmp in ('"WEB前端"',):
            linec = linec.replace(itmp, "\"\"")

        # 图片 caption 不校验空格。
        linec = linec.replace('caption="', 'caption=" ')
        linec = linec.replace('caption2="', 'caption2=" ')
        linec = linec.replace('title="', 'title=" ')

        lix1 = refindall("[{}][^{} *]".format(cnregex, cnregex), linec, re.IGNORECASE)
        lix2 = refindall("[^{} *][{}]".format(cnregex, cnregex), linec, re.IGNORECASE)
        lix = []
        lix.extend(lix1)
        lix.extend(lix2)

        cnsignregex = "[{}]".format(cnsign)
        for ix in lix:
            cx, cy = ix
            # 其中一个是中文符号。
            if refindall(cnsignregex, cy) or refindall(cnsignregex, cx):
                continue
            if cy in "-<]~" or cx in "->[~":
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

            tagcontinue = False
            for kftype in keepFileTypeList:
                if cy in (".",) and (line.count(ix+kftype) == 1):
                    tagcontinue = True
            if tagcontinue: continue

            if not warnCnEnSpace:
                continue

            if codestate:
                if cy in "\":" or cx in "\":":
                    continue

                if line.startswith("print ("):
                    continue

            print("[%d]"%(index+1), ix, cx, cy, "\t", line)
            errcnt += 1
            if AUTOFORMAT and not frontmatter:
                line = line.replace(ix, cx+" "+cy)
                lines[index] = line

        # 检查中文问本里面不应该出现的英文符号。
        if isMdFile:
            lixyx = refindall("[{}] [,()] [{}]".format(cnregex, cnregex), linec, re.IGNORECASE)
            lixyx.extend(refindall("[{}] [,()]$".format(cnregex), linec, re.IGNORECASE))
            lixyx.extend(refindall("[{}][,;] [{}]".format(cnregexc, cnregexc), linec, re.IGNORECASE))
            if lixyx:
                openTextFile(fpath)
                print(lixyx)
                print("中文符号问题 {}:{} \"{}\"".format(fpath, index+1, linec))
                os.system(PAUSE_CMD)
                return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

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

        # 代码规范问题，需要有空格。
        if isMdFile and (line.lower().replace("endif", "x").find("if(") != -1 or line.lower().find("while(") != -1):
            openTextFile(fpath)
            print("'if(' & 'while(' 问题 {}:{} \"{}\"".format(fpath, index+1, line))
            os.system(PAUSE_CMD)
            return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

        if codestate:
            continue

        if warnTitleSpace and (prelinetag or nextlinetag):
            if line:
                openTextFile(fpath)
                print("标题前后空行问题 {}:{} \"{}\"".format(fpath, index+1, line))
                os.system(PAUSE_CMD)
                return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

        countspace = getLeftSpaceCount(line if warnIndentSpace else line.replace("\t", " "*4))
        if countspace > 12 or countspace % idtcnt == 0 or countspace in (3,):
            pass # ok
        elif warnIndentSpace:
            openTextFile(fpath)
            print("空格缩进问题 {}:{} \"{}\"".format(fpath, index+1, line))
            os.system(PAUSE_CMD)
            return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

    assert not codestate # 断言代码片段闭合。

    page = NEWLINE_CHAR.join(lines)
    while page.find(NEWLINE_CHAR * 3) != -1:
        page = page.replace(NEWLINE_CHAR * 3, NEWLINE_CHAR * 2)

    page = page.replace(NEWLINE_CHAR+REVIEW_LINE, NEWLINE_CHAR*3+REVIEW_LINE)
    codereg = "\\{\\%\\s*highlight.*?\\{\\%\\s*endhighlight\\s*\\%\\}"
    codeli1 = refindall(codereg, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)

    coderegz = "```.*?```"
    codeli1z = refindall(coderegz, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)

    if warnTitleSpace:
        page = page.replace(NEWLINE_CHAR*2+"### ", NEWLINE_CHAR*3+"### ")
        page = page.replace(NEWLINE_CHAR*2+"## ",  NEWLINE_CHAR*3+"## ")
        page = page.replace(NEWLINE_CHAR*2+"# ",   NEWLINE_CHAR*3+"# ")

    # 代码里面的替换要还原。
    codeli2 = refindall(codereg, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)
    for i in range(len(codeli1)):
        page = page.replace(codeli2[i], codeli1[i])
    # 代码里面的替换要还原。
    codeli2z = refindall(coderegz, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)
    for i in range(len(codeli1z)):
        page = page.replace(codeli2z[i], codeli1z[i])

    # 移除康熙编码，会造成乱码。
    if not fname in ("2021-03-14-Equivalent-Unified-Ideograph.md",):
        page = TranslateKangXi(page)

    def spaceBackReg(regkey, regmap, page):
        li = re.findall(regkey, page)
        if not li: return page
        for i in li:
            ix = i
            for ik in regmap.keys():
                ix = ix.replace(ik, regmap[ik])
            page = page.replace(i, ix)
        return page
    for spacebackkey in spacebackjson.keys():
        spacebackvalue = spacebackjson[spacebackkey]
        if spacebackkey == "regex":
            for regkey in spacebackvalue.keys():
                regmap = spacebackvalue[regkey] # 字典
                page = spaceBackReg(regkey, regmap, page)
            continue
        page = page.replace(spacebackkey, spacebackvalue)

    # 时间过长，如果被手工改了，这里会形成覆盖。
    md5src2 = getLuckFileMd5(fpath, md5src)
    if md5src2 == md5src:
        if not writefile(fpath, page.encode("utf8")):
            return 0
        return errcnt

    print("文本中途被改过了。{}".format(fpath,))
    os.system(PAUSE_CMD)
    return mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

def viewchar(lichar, xfile, xmin, xmax):
    li = list(set("".join(lichar)))
    li.sort()
    page = ""
    minv, maxv = 1024, 0
    for index, tchar in enumerate(li):
        page += tchar
        if (index + 1) % 50 == 0:
            page += NEWLINE_CHAR
        if isDiacritic(tchar):
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
