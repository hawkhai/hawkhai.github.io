#encoding=utf8
import os, re, sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from lib import kalgorithm

def main():
    inputfile = r"./input_images/phase2/phase2_broken.jpg"
    imgsrc = kalgorithm.imgRead(inputfile)

    # 均值滤波器
    meanFilterOutput=r"./output_images/phase2/phase2_broken_mean_filter.jpg"
    img = kalgorithm.meanFilter(imgsrc.copy(), ksize=5)
    kalgorithm.imgSave(meanFilterOutput, img)

    # 中值滤波
    medianFilterOutput=r"./output_images/phase2/phase2_broken_median_filter.jpg"
    img = kalgorithm.medianFilter(imgsrc.copy(), ksize=5)
    kalgorithm.imgSave(medianFilterOutput, img)

    # 高斯滤波
    gaussianFilterOutput=r"./output_images/phase2/phase2_broken_gaussian_filter.jpg"
    img = kalgorithm.gaussianFilter(imgsrc.copy(), ksize=5)
    kalgorithm.imgSave(gaussianFilterOutput, img)

if __name__ == "__main__":
    main()
