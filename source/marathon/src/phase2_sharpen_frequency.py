#encoding=utf8
import cv2
import numpy as np
from lib import kalgorithm

#
# phase 2
# 图像锐化
# 频域算法
#
def main():
    inputfile = r"./input_images/phase2/phase2_broken.jpg"
    outputfile = r"./output_images/phase2/phase2_sharpen_frequency_gaussian.jpg"
    img = cv2.imread(inputfile)
    newimg = kalgorithm.gaussianHighFrequencyFilterImage(img)
    kalgorithm.imgSave(outputfile, newimg)

if __name__ == "__main__":
    main()
