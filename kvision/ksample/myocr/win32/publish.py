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

def checkpe(rootdir, x64):
    for _dir in os.listdir(rootdir):
        _path = os.path.join(rootdir, _dir)
        if not isPeFile(_path):
            continue
        
        if isPe64(_path):
            if x64:
                os.remove(_path)
            else:
                print("x64", _path)
        else:
            if not x64:
                os.remove(_path)
            else:
                print("x86", _path)

def pecheck():
    checkpe(r"ocrdemo-debug\fastocr", False)
    checkpe(r"ocrdemo-debug\fastocr\x64", True)
    checkpe(r"ocrdemo-debug", True)
    checkpe(r"ocrdemo-release\fastocr", False)
    checkpe(r"ocrdemo-release\fastocr\x64", True)
    checkpe(r"ocrdemo-release", True)
    
def main(debug, x64=False):

    # kdump.dll & kdump64.dll
    QTDIR = r"D:\Qt\5.15.0\msvc2019\\"
    DUBADIR = r"D:\program files (x86)\kingsoft\kingsoft antivirus\\"

    binlist32 = [
        [r"OcrLibTestd.exe", r"OcrLibTestd.exe"],
        [r"x64\OcrLibTest64d.exe", r"OcrLibTest64d.exe"],
        
        [r"pdfocrd.exe", r"fastocr\\pdfocrd.exe"],
        [r"pdfocrsdkd.dll", r"fastocr\\pdfocrsdkd.dll"],
        [r"kpipe.dll", r"fastocr\\kpipe.dll"],
        [r"x64\pdfocr64d.exe", r"fastocr\\x64\\pdfocr64d.exe"],
        [r"x64\pdfocrsdk64d.dll", r"fastocr\\x64\\pdfocrsdk64d.dll"],
        [r"x64\kpipe64.dll", r"fastocr\\x64\\kpipe64.dll"],
        [r"pdfaihelperd.exe", r"fastocr\\pdfaihelperd.exe"],
        
        [r"pdfocrd.dll", r"fastocr\\pdfocrd.dll"],
        [r"x64\pdfocr64d.dll", r"fastocr\\x64\\pdfocr64d.dll"],

        #[DUBADIR+r"kdump.dll", r"fastocr\\kdump.dll"],
        #[DUBADIR+r"kdump64.dll", r"fastocr\\kdump64.dll"],

        #[QTDIR+r"bin\Qt5Cored.dll",     "fastocr\\Qt5Cored.dll"],
        #[QTDIR+r"bin\Qt5Guid.dll",      "fastocr\\Qt5Guid.dll"],
        #[QTDIR+r"bin\Qt5Widgetsd.dll",  "fastocr\\Qt5Widgetsd.dll"],
        #[QTDIR+r"plugins\platforms\qwindowsd.dll",          "fastocr\\plugins\\platforms\\qwindowsd.dll"],
        #[QTDIR+r"plugins\styles\qwindowsvistastyled.dll",   "fastocr\\plugins\\styles\\qwindowsvistastyled.dll"],

    ] if debug else [

        [r"OcrLibTest.exe", r"OcrLibTest.exe"],
        [r"x64\OcrLibTest64.exe", r"OcrLibTest64.exe"],
        
        [r"pdfocr.exe", r"fastocr\\pdfocr.exe"],
        [r"pdfocrsdk.dll", r"fastocr\\pdfocrsdk.dll"],
        [r"kpipe.dll", r"fastocr\\kpipe.dll"],
        [r"pdfaihelper.exe", r"fastocr\\pdfaihelper.exe"],

        [r"x64\pdfocr64.exe", r"fastocr\\x64\\pdfocr64.exe"],
        [r"x64\pdfocrsdk64.dll", r"fastocr\\x64\\pdfocrsdk64.dll"],
        [r"x64\kpipe64.dll", r"fastocr\\x64\\kpipe64.dll"],
        
        #[DUBADIR+r"kdump.dll", r"fastocr\\kdump.dll"],
        #[DUBADIR+r"kdump64.dll", r"fastocr\\kdump64.dll"],
        
        #[QTDIR+r"bin\Qt5Core.dll",      "fastocr\\Qt5Core.dll"],
        #[QTDIR+r"bin\Qt5Gui.dll",       "fastocr\\Qt5Gui.dll"],
        #[QTDIR+r"bin\Qt5Widgets.dll",   "fastocr\\Qt5Widgets.dll"],
        #[QTDIR+r"plugins\platforms\qwindows.dll",           "fastocr\\plugins\\platforms\\qwindows.dll"],
        #[QTDIR+r"plugins\styles\qwindowsvistastyle.dll",    "fastocr\\plugins\\styles\\qwindowsvistastyle.dll"],
    ]

    binlist64 = [
    ] if debug else [
    ]
    
    binlist32.extend([

        [r"..\3rdsdk\onnxruntime-win-x86-1.11.1\lib\onnxruntime.dll", r"fastocr\\onnxruntime.dll"],
        [r"..\3rdsdk\onnxruntime-win-x86-1.11.1\lib\onnxruntime_providers_shared.dll", r"fastocr\\onnxruntime_providers_shared.dll"],

        [r"..\3rdsdk\onnxruntime-win-x64-1.11.1\lib\onnxruntime.dll", r"fastocr\\x64\\onnxruntime.dll"],
        [r"..\3rdsdk\onnxruntime-win-x64-1.11.1\lib\onnxruntime_providers_shared.dll", r"fastocr\\x64\\onnxruntime_providers_shared.dll"],

        [r"..\core\build-win-vs2019-x86\Release\concrt140.dll", "fastocr\\concrt140.dll",],
        [r"..\core\build-win-vs2019-x86\Release\msvcp140.dll", "fastocr\\msvcp140.dll",],
        [r"..\core\build-win-vs2019-x86\Release\msvcp140_1.dll", "fastocr\\msvcp140_1.dll",],
        [r"..\core\build-win-vs2019-x86\Release\msvcp140_2.dll", "fastocr\\msvcp140_2.dll",],
        [r"..\core\build-win-vs2019-x86\Release\msvcp140_atomic_wait.dll", "fastocr\\msvcp140_atomic_wait.dll",],
        [r"..\core\build-win-vs2019-x86\Release\msvcp140_codecvt_ids.dll", "fastocr\\msvcp140_codecvt_ids.dll",],
        [r"..\core\build-win-vs2019-x86\Release\vcamp140.dll", "fastocr\\vcamp140.dll",],
        [r"..\core\build-win-vs2019-x86\Release\vccorlib140.dll", "fastocr\\vccorlib140.dll",],
        [r"..\core\build-win-vs2019-x86\Release\vcomp140.dll", "fastocr\\vcomp140.dll",],
        [r"..\core\build-win-vs2019-x86\Release\vcruntime140.dll", "fastocr\\vcruntime140.dll",],
    
        [r"..\x64\Release\concrt140.dll", "fastocr\\x64\\concrt140.dll",],
        [r"..\x64\Release\msvcp140.dll", "fastocr\\x64\\msvcp140.dll",],
        [r"..\x64\Release\msvcp140_1.dll", "fastocr\\x64\\msvcp140_1.dll",],
        [r"..\x64\Release\msvcp140_2.dll", "fastocr\\x64\\msvcp140_2.dll",],
        [r"..\x64\Release\msvcp140_atomic_wait.dll", "fastocr\\x64\\msvcp140_atomic_wait.dll",],
        [r"..\x64\Release\msvcp140_codecvt_ids.dll", "fastocr\\x64\\msvcp140_codecvt_ids.dll",],
        [r"..\x64\Release\vcamp140.dll", "fastocr\\x64\\vcamp140.dll",],
        [r"..\x64\Release\vccorlib140.dll", "fastocr\\x64\\vccorlib140.dll",],
        [r"..\x64\Release\vcomp140.dll", "fastocr\\x64\\vcomp140.dll",],
        [r"..\x64\Release\vcruntime140.dll", "fastocr\\x64\\vcruntime140.dll",],
        [r"..\x64\Release\vcruntime140_1.dll", "fastocr\\x64\\vcruntime140_1.dll",],
    
        #[r"models\cls_v2.dat", "fastocr\\models\\pdfocr\\cls_v2.dat",],
        #[r"models\det_v4.dat", "fastocr\\models\\pdfocr\\det_v4.dat",],
        #[r"models\keys_v1.dat", "fastocr\\models\\pdfocr\\keys_v1.dat",],
        #[r"models\rec_v4.dat", "fastocr\\models\\pdfocr\\rec_v4.dat",],
        [r"models\fastocr.kmod", "fastocr\\models\\fastocr.kmod",],
        [r"font\ikeymap.json", "fastocr\\font\\ikeymap.json",],
    
        [r"imgtest.jpg", r"test.jpg"],
        [r"..\include\pdfocr.h", r"pdfocr.h"],
        [r"..\test\src\maintest.cpp", r"maintest.cpp"],
        
        #[r"dist\drawtest.exe", r"drawtest.exe"],
        #[r"dist\drawtest.exe", r"fastocr\\drawtest.exe"],
        #[r"dist\drawtest.exe", r"fastocr\\x64\\drawtest.exe"],
        [r"字体识别使用文档.pdf", r"字体识别使用文档.pdf"],
        [r"imgtest1.png", r"test2.png"],
    ])
    
    binlist32.extend(binlist64)
    binlist64 = binlist32[:]
    
    for img in os.listdir("font"):
        if not img.split(".")[-1] in ("png",):
            continue
        ipath = os.path.join("font", img)
        #binlist32.append([ipath, "fastocr\\"+ipath])
        #binlist64.append([ipath, "fastocr\\"+ipath])

    for api in os.listdir("x86"):
        if not api.split(".")[-1].lower() in ("dll",):
            continue
        if not api.lower().startswith("api-ms-"):
            continue
        ipath = os.path.join("x86", api)
        binlist32.append([ipath, "fastocr\\"+api.lower()])
        binlist64.append([ipath, "fastocr\\"+api.lower()])

    for api in os.listdir("x64"):
        if not api.split(".")[-1].lower() in ("dll",):
            continue
        if not api.lower().startswith("api-ms-"):
            continue
        ipath = os.path.join("x64", api)
        binlist32.append([ipath, "fastocr\\x64\\"+api.lower()])
        binlist64.append([ipath, "fastocr\\x64\\"+api.lower()])

    if x64:
        zipfile = "ocrdemo-debug64.zip" if debug else "ocrdemo-release64.zip"
        gzipflist(zipfile, binlist64)
        datalist = [y.replace("\\\\", "\\") for x, y in binlist64]
        datalist.sort()
        writefile(zipfile+".txt", "\r\n".join(datalist), "utf8")
        for x, y in binlist64:
            assert os.path.exists(x)
            if isPeFile(x) and not x.split("\\")[-1] in (
                    "drawtest.exe", "pdfocrsdk.dll", "kpipe.dll",
                    "pdfocrsdkd.dll",):
                assert True or isPe64(x), x
            copyfile(x, os.path.join("ocrdemo-debug64" if debug else "ocrdemo-release64", y))
    else:
        zipfile = "ocrdemo-debug.zip" if debug else "ocrdemo-release.zip"
        gzipflist(zipfile, binlist32)
        datalist = [y.replace("\\\\", "\\") for x, y in binlist32]
        datalist.sort()
        writefile(zipfile+".txt", "\r\n".join(datalist), "utf8")
        for x, y in binlist32:
            assert os.path.exists(x)
            if isPeFile(x) and not x.split("\\")[-1] in (
                    "drawtest.exe", "pdfocrsdk64.dll", "kpipe64.dll",
                    "pdfocrsdk64d.dll",):
                assert True or isPe32(x), x
            copyfile(x, os.path.join("ocrdemo-debug" if debug else "ocrdemo-release", y))

if __name__ == "__main__":
    if "debug" in sys.argv:
        main(True)
    if "release" in sys.argv:
        main(False)
    if "debug64" in sys.argv:
        main(True, True)
    if "release64" in sys.argv:
        main(False, True)
    
    if "check" in sys.argv:
        pecheck()
    
    print("ok")
