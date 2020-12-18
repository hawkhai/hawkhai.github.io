#encoding=utf8
import re, os, sys
sys.path.append("../../")
from funclib import *

def mainfile(fpath, fname, ftype):
    pass

def maincheck(rootdir):
    searchdir(rootdir, mainfile)

if __name__ == "__main__":
    maincheck(".")
