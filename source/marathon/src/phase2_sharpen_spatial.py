#encoding=utf8
import os, re, sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from lib import kalgorithm

#
# phase 2
# 图像锐化
# 空域算法
#
#图像锐化
def main():
    inputfile  = r"./input_images/phase2/phase2_broken.jpg"
    imgsrc = kalgorithm.imgRead(inputfile)

    outputfile  = r"./output_images/phase2/phase2_broken_sharpen_spatial.jpg"
    img = kalgorithm.sharpenImage3d(imgsrc.copy())
    kalgorithm.imgSave(outputfile, img)

if __name__ == "__main__":
    main()
