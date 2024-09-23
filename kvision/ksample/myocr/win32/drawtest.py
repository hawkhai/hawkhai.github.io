#encoding=utf8
import re, os, sys
reldirx, _lidir = "", []
while not _lidir and len(reldirx) <= 100:
    reldirx += "../"
    checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
    _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
    if _lidir: reldirx = _lidir[0]
sys.path.append(reldirx)
if not os.getcwd() in sys.path: # fix linux 软连接的 bug
    sys.path.append(os.getcwd())
import time
from pythonx.funclib import *
from pythonx.pelib import *
from PIL import Image, ImageDraw, ImageFont

from fontTools import ttLib, ttx

def extract_font_name(filepath, ttf=None, langID_expected=[2052, 3076, 1028, 1033, 2057]):
    if ttf is None:
        ttf = ttLib.TTFont(filepath)
    font_family_name, font_style_name = "", ""
    font_name_dict = {}
    for n in ttf['name'].names:
        if n.platformID != 3 or (n.langID not in langID_expected):
            continue
        if n.nameID != 1 and n.nameID != 2:
            continue
        if n.langID not in font_name_dict:
            font_name_dict[n.langID] = {}
        font_name_dict[n.langID][n.nameID] = str(n)
    for langID in langID_expected:
        if langID not in font_name_dict:
            continue
        font_family_name = font_name_dict[langID][1] if 1 in font_name_dict[langID] else ""
        font_style_name = font_name_dict[langID][2] if 2 in font_name_dict[langID] else ""
        break
    return font_family_name, font_style_name
        
def extract_ttc2ttf(ttc_path, ttf_dir, name_prefix=""):
    """
    extract ttf files from ttc and save to files.
    using windows font name and language prefer chinese.
    reference: [NameRecord](https://docs.microsoft.com/en-us/typography/opentype/spec/name)
        Platform IDs :
            3 = Windows, 1 = Macintosh
        Windows language IDs:
            Chinese	People’s Republic of China	0804
            Chinese	Hong Kong S.A.R.	0C04
            Chinese	Macao S.A.R.	1404
            Chinese	Singapore	1004
            Chinese	Taiwan	0404
        Name IDS:
            1. The name the user sees. Times New Roman
            2. The name of the style. Bold
    """
    ttx_type = ttx.guessFileType(ttc_path)
    if ttx_type.lower() != "ttc":
        raise TypeError("expect ttc got {}".format(ttx_type))
    ttc = ttLib.TTCollection(ttc_path)
    for ttf in ttc:
        font_family_name, font_style_name = extract_font_name(None, ttf=ttf)
        if font_family_name:
            ttf.save("{}/{}{}{}.ttf".format(ttf_dir, name_prefix, font_family_name, "_{}".format(font_style_name) if len(font_style_name) > 0 else ""))
        else:
            raise LookupError("has no name")

gfontflag = False
mytestfile = readfile("mytestfile.txt", True, "gbk").strip()
print("mytestfile", mytestfile)
def mainfile(fpath, fname, ftype):
    if not ftype in ("json",):
        return
    if not fname.endswith("_test.json"):
        return
    
    if isPythonExe():
        if fname.find(mytestfile) == -1 and not "all" in sys.argv:
            return
    elif "filter" in sys.argv:
        isok = False
        for argv in sys.argv:
            if argv.startswith("filter="):
                argv = argv[len("filter="):]
                if argv and fname.find(argv) != -1:
                    isok = True
        if not isok:
            return
    
    print(fpath)
    fjson = readfileJson(fpath, "utf8")
    fmask = fpath.replace("_test.json", "_mask.png")
    fsrc  = fpath.replace("_test.json", "_src.jpg")
    fbgfile = fpath.replace("_test.json", "_rst.png")
    
    foutput1 = fpath.replace("_test.json", "_rst1.png")
    foutput2 = fpath.replace("_test.json", "_rst2.png")
    foutput3 = fpath.replace("_test.json", "_rst3.png")
    
    fontMap = fjson["fontMap"]
    global gfontflag
    if not gfontflag:
        gfontflag = True
        for font in fjson["fontMap"]:
            continue
            file = font["file"]
            name = font["name"]
            style = font["style"]
            winfontfile = os.path.join(r"C:\Windows\Fonts", file)
            localfontfile = os.path.join(r"Fonts", file)
            # "msyhl_微软雅黑 Light_Regular.ttf",
            winttcfile = os.path.join(r"C:\Windows\Fonts", file.split("_")[0]+".ttc")
            localttcfile = os.path.join(r"Fonts", file.split("_")[0]+".ttc")
            
            if os.path.exists(localfontfile):
                print("EXISTS", localfontfile)
            elif os.path.exists(winfontfile):
                copyfile(winfontfile, localfontfile)
                
            else: # ttc
                if len(file.split("_")) == 3:
                    if os.path.exists(winttcfile):
                        copyfile(winttcfile, localttcfile)
                        extract_ttc2ttf(localttcfile, r"Fonts", name_prefix=file.split("_")[0]+"_")
                        
                    elif not os.path.exists(localttcfile):
                        print("ERROR", localttcfile)
                        
                elif not os.path.exists(localfontfile):
                    print("ERROR", winfontfile)
    
    for fsrc, fdst, fbox, drawRotate in (
                    (fsrc, foutput1, True, False), 
                    (fbgfile, foutput3, False, False), 
                    (fbgfile, foutput2, False, True)):
    
        if os.path.exists(fdst) and "all" in sys.argv:
            continue
    
        img = Image.open(fsrc)
        if img.mode != "RGB":
            img = img.convert("RGB")
        
        textBlocks = fjson["textBlocks"]
        textBoxes = fjson["textBoxes"]
        assert len(textBlocks) == len(textBoxes), (len(textBlocks), len(textBoxes))

        if not "background" in fjson.keys():
            continue
        print(fjson.keys(), fpath)
        print(fjson["background"])
        width = fjson["background"]["width"]
        height = fjson["background"]["height"]
        img = img.resize((width, height))
        draw = ImageDraw.Draw(img)

        index = -1
        for textBlock in textBlocks:
            index += 1
            textBox = textBoxes[index]
            textBoxColor = textBox["color"]
            textBoxFont = textBox["fontlist"] # list
            textLineSize = textBox["contentSize"] # width / height 参考的图片宽高
            rotation = textBox["rotation"]
            assert type(rotation) != type(None), fpath
            
            currentColor = textBoxColor["colorBGR"] # BGR
            textcolor = "#%02x%02x%02x" % (currentColor[2], currentColor[1], currentColor[0])
            # "file" / "name" / "style"
            fontok = textBoxFont and textBoxFont[0]["score"] >= 0.01
            fontScore = ("%.2f"%textBoxFont[0]["score"]) if fontok else ""
            fontidx = textBoxFont[0]["idx"] if fontok else 0
            currentFontFile = fontMap[textBoxFont[0]["idx"]] if fontok else \
                              fontMap[0] # "simsun_新宋体_常规.ttf",
            debug_bold = currentFontFile["debug_bold"]
            debug_italic = currentFontFile["debug_italic"]
            currentFontFile = os.path.join("C:\\Windows\\Fonts", currentFontFile["debug_file"])

            boxPoint = textBlock["boxPoint"]
            x1, y1, x2, y2, x3, y3, x4, y4 = boxPoint
            
            xmin = min(x1, x2, x3, x4)
            xmax = max(x1, x2, x3, x4)
            ymin = min(y1, y2, y3, y4)
            ymax = max(y1, y2, y3, y4)
            #textLineSize = xmax - xmin, ymax - ymin
            
            points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x1, y1)]
            color = (255, 0, 0) # RGB 格式的红色
            if fbox: # 绘制多边形边框
                #draw.polygon(points, outline=color)
                draw.line(points[0:2], fill=(255, 0, 0))
                draw.line(points[1:3], fill=(0, 255, 0))
                draw.line(points[2:4], fill=(0, 0, 255))
                draw.line(points[3:5], fill=(0, 0, 0))
                #draw.line(points, outline=color)
            #draw.rectangle([(xmin, ymin), (xmax, ymax)])
        
            text = textBlock["text"]
            fontsize = min(*textLineSize)
            if not text: continue
            if fontsize < 7: # 最小 7 像素。
                fontsize = 7 # 默认
            
            font = ImageFont.truetype(currentFontFile, fontsize)
            # 返回一个四元组 (x0, y0, x1, y1)，表示文本框的左上角和右下角坐标。
            textsize = draw.textbbox((0, 0), text, font=font)
            textsize = textsize[2]-textsize[0], textsize[3]-textsize[1]
            while textsize[0] > textLineSize[0] or textsize[1] > textLineSize[1]:
                fontsize -= 1
                font = ImageFont.truetype(currentFontFile, fontsize)
                # 返回一个四元组 (x0, y0, x1, y1)，表示文本框的左上角和右下角坐标。
                textsize = draw.textbbox((0, 0), text, font=font) # textsize
                textsize = textsize[2]-textsize[0], textsize[3]-textsize[1]
                if fontsize <= 7: break
                
            x = (xmax + xmin) / 2 - textsize[0] / 2
            y = (ymax + ymin) / 2 + textsize[1] / 2
            #textcolor = "#000000"
            
            #img = img.rotate(rotation / 3.14159265 * 180)
            #draw = ImageDraw.Draw(img)
            # https://github.com/python-pillow/Pillow/issues/5738
            if drawRotate:
                text = "R%.0f %s %s"%(rotation / 3.14159265 * 180,
                        fontScore, fontMap[fontidx]["name"])
            if not fbox:
                # https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
                if debug_bold:
                    if debug_italic:
                        draw.text((x, y-textsize[1]), " ".join(text.split()), fill=textcolor, font=font,
                                  stroke_width=round(1/35*fontsize), angle=15)
                    else:
                        draw.text((x, y-textsize[1]), " ".join(text.split()), fill=textcolor, font=font,
                                  stroke_width=round(1/35*fontsize))
                else:
                    if debug_italic:
                        draw.text((x, y-textsize[1]), " ".join(text.split()), fill=textcolor, font=font,
                                  angle=15)
                    else:
                        draw.text((x, y-textsize[1]), " ".join(text.split()), fill=textcolor, font=font)
            #img = img.rotate(-rotation / 3.14159265 * 180)
            #draw = ImageDraw.Draw(img)

        print(fdst)
        img.save(fdst)

def main(rootdir):
    searchdir(rootdir, mainfile)

if __name__ == "__main__":
    main(r"3_result")
    main(r"2_result")
    main(r"1_result")
    main(r"result")
    print("ok")
