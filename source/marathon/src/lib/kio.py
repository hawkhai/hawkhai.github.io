#encoding=utf8
import cv2
import numpy as np
from matplotlib import pyplot as plt

def imgRead(fpath, float=False):
    img = cv2.imread(fpath)
    if float:
        return img.astype(np.float32)
    return img

def imgSave(fpath, img):
    print("Image Save\r\n", fpath)
    cv2.imwrite(fpath, img)
    return fpath

def imgShow(img, title="result"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def pltHistAndImage(img, title="result"):
    plt.figure(num=title)
    plt.subplot(121)
    plt.hist(img.ravel(), 256)
    plt.subplot(122)
    b,g,r = cv2.split(img)
    img = cv2.merge([r,g,b])
    plt.imshow(img)
    plt.show()
