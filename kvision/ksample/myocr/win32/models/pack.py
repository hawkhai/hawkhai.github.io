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

def main():
    flist = [
        "cls_v2.dat",
        "det_v4.dat",
        "keys_v1.dat",
        "rec_v4.dat",
    ]
    fout = "fastocr.kmod"
    
    writefile(fout, "FASTOCR.KMOD")
    fjson = {
    }
    total = 0
    for f in flist:
        fdata = readfile(f)
        while os.path.getsize(fout) % 4:
            appendfile(fout, b"\x00")
        fjson[f] = [os.path.getsize(fout), len(fdata)]
        size = len(fdata)
        strbin = bytesToString(fdata)
        rstbin = ""
        
        magicx = 0x97
        magicy = 0x97
    
        for i in range(size):
            assert ord(strbin[i]) >= 0 and ord(strbin[i]) <= 255
            rstbin += chr(ord(strbin[i]) ^ magicx)
            magicx = (magicx + ord(strbin[i])) % 256

        appendfile(fout, rstbin)

        for i in range(size):
            assert ord(rstbin[i]) >= 0 and ord(rstbin[i]) <= 255
            assert strbin[i] == chr(ord(rstbin[i]) ^ magicy)
            magicy = (magicy + ord(strbin[i])) % 256
            
        assert magicx == magicy
        fjson[f].append(magicy) # 校验码
    
    appendfile(fout, fout+"="*10)
    strbin = json.dumps(fjson)
    
    size = len(strbin)
    rstbin = ""
    magicx = 0x97
    magicy = 0x97
    for i in range(size):
        assert ord(strbin[i]) >= 0 and ord(strbin[i]) <= 255
        rstbin += chr(ord(strbin[i]) ^ magicx)
        magicx = (magicx + ord(strbin[i])) % 256

    for i in range(size):
        assert ord(rstbin[i]) >= 0 and ord(rstbin[i]) <= 255
        assert strbin[i] == chr(ord(rstbin[i]) ^ magicy)
        magicy = (magicy + ord(strbin[i])) % 256

    rstbin += chr(magicx)

    appendfile(fout, rstbin)
    print(strbin, magicx)
    print(getFileMd5(fout))

if __name__ == "__main__":
    main()
    print("ok")
