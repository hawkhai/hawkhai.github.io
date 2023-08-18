#encoding=utf8
import re, os, sys
import cv2
from PIL import Image

curfiledir = os.path.split(os.path.abspath(__file__))[0]
pythonxdir = r"E:\kSource"
if not sys.path or pythonxdir not in sys.path: # for pythonx
    sys.path.insert(0, pythonxdir)
    sys.path.insert(0, os.path.join(pythonxdir, "pythonx"))
from pythonx.funclib import *

import tarfile
import time
from functools import wraps
from copy import deepcopy

# Use Aspose.Cells for Python via Java
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import *

# https://blog.aspose.com/cells/convert-excel-to-image-in-python/#Convert-Excel-to-SVG-in-Python
def xlsx2svgf(xlsxfile, svgfile):
    # load the Excel workbook
    workbook = Workbook(xlsxfile)

    # create image options
    imgOptions = ImageOrPrintOptions()
    imgOptions.setSaveFormat(SaveFormat.SVG)

    # get sheet count
    sheetCount = workbook.getWorksheets().getCount()

    # loop through the sheets
    sheet = workbook.getWorksheets().get(0)
        
    # convert each sheet to SVG
    sr = SheetRender(sheet, imgOptions)
    #for j in range(0, sr.getPageCount()):
    sr.toImage(0, svgfile)

def myxlsx2svg(rootdir):
        
    def mainfile(fpath, fname, ftype):
        if not ftype in ("xlsx"):
            return
        print(fpath)
        xlsx2svgf(fpath, fpath+".svg")

    searchdir(rootdir, mainfile)

if __name__ == "__main__":
    rootdir = r"E:\kSource\blog\kvision\ksample\mytable"
    myxlsx2svg(rootdir)
    print("ok")
