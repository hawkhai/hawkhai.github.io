#encoding=utf8
import cv2
import numpy as np

def thresholdBinarization(img, th=128):
    img[img < th] = 0
    img[img >= th] = 255
    return img

# Otsu Binarization
# 大津二值化算法（Otsu's Method）
def thresholdOtsuBinarization(img, retx=False):
    max_sigma = 0
    max_t = 0
    out = img.copy()
    H, W = img.shape

    # determine threshold
    for _t in range(1, 256):
        v0 = out[np.where(out < _t)]
        m0 = np.mean(v0) if len(v0) > 0 else 0.
        w0 = len(v0) / (H * W)
        v1 = out[np.where(out >= _t)]
        m1 = np.mean(v1) if len(v1) > 0 else 0.
        w1 = len(v1) / (H * W)
        sigma = w0 * w1 * ((m0 - m1) ** 2)
        if sigma > max_sigma:
            max_sigma = sigma
            max_t = _t

    # Binarization
    # print("threshold >>", max_t)
    th = max_t
    out[out < th] = 0
    out[out >= th] = 255
    if retx:
        return out, max_t
    return out
