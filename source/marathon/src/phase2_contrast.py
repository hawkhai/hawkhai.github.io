#encoding=utf8
import os, re, sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from lib import kalgorithm

def main():
    inputfile  = r"./input_images/phase2/phase2_broken.jpg"
    imgsrc = kalgorithm.imgRead(inputfile)
    kalgorithm.pltHistAndImage(imgsrc.astype(np.uint8), "phase2_broken.Original")

    img = kalgorithm.histEqualization(imgsrc.copy())
    outfile  = r"./output_images/phase2/phase2_broken_hist_equalization.jpg"
    kalgorithm.imgSave(outfile, img)
    kalgorithm.pltHistAndImage(img, "phase2_broken.histEqualization")

    img = kalgorithm.histManipulation(imgsrc.copy())
    outfile  = r"./output_images/phase2/phase2_broken_hist_manipulation.jpg"
    kalgorithm.imgSave(outfile, img)
    kalgorithm.pltHistAndImage(img, "phase2_broken.histManipulation")

if __name__ == "__main__":
    main()
