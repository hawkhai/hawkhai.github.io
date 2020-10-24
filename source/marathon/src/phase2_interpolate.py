#encoding=utf8
import os, re, sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from lib import kalgorithm

# 最近邻
def nnInterpolateProc(imgsrc, imgdst, scale):
    img = kalgorithm.nnInterpolate(imgsrc, scale, scale)
    kalgorithm.imgSave(imgdst, img)

# 双线性二次插值
def blInterpolateProc(imgsrc, imgdst, scale):
    img = kalgorithm.blInterpolate(imgsrc, scale, scale)
    kalgorithm.imgSave(imgdst, img)

# 双线性三次插值
def bcInterpolateProc(imgsrc, imgdst, scale):
    img = kalgorithm.bcInterpolate(imgsrc, scale, scale)
    kalgorithm.imgSave(imgdst, img)

# 插值算法
def main():
    inputfile = r"./input_images/phase2/phase2_broken.jpg"
    imgsrc = kalgorithm.imgRead(inputfile, True)

    # 最近邻
    nnInterpolateOutPath = r"./output_images/phase2/phase2_broken_nn.jpg"
    nnInterpolateProc(imgsrc.copy(), nnInterpolateOutPath, 3)
    nnInterpolateProc(imgsrc.copy(), nnInterpolateOutPath+".png", 3)

    # 双线性二次插值
    blInterpolateOutPath = r"./output_images/phase2/phase2_broken_bl.jpg"
    blInterpolateProc(imgsrc.copy(), blInterpolateOutPath, 2)

    # 双线性三次插值
    bcInterpolateOutPath = r"./output_images/phase2/phase2_broken_bc.jpg"
    bcInterpolateProc(imgsrc.copy(), bcInterpolateOutPath, 2)

if __name__ == "__main__":
    main()
