#encoding=utf8
import cv2
import numpy as np

# function: BGR -> RGB
def bgr2rgb(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    # RGB := BGR
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b
    return img

# Gray scale - return unit8
def rgb2gray(img, bgr=False):
    r = img[:, :, 2 if bgr else 0].copy().astype(np.float)
    g = img[:, :, 1].copy().astype(np.float)
    b = img[:, :, 0 if bgr else 2].copy().astype(np.float)
    # Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)
    return out

def bgr2gray(img):
    return rgb2gray(img, True)

# Grayscale
def bgr2grayFloat(img):
    # Grayscale
    gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
    return gray

# BGR -> HSV
def bgr2hsv(img):
    img = img.copy() / 255.

    hsv = np.zeros_like(img, dtype=np.float32)

    # get max and min
    max_v = np.max(img, axis=2).copy()
    min_v = np.min(img, axis=2).copy()
    min_arg = np.argmin(img, axis=2)

    # H
    hsv[..., 0][np.where(max_v == min_v)] = 0
    ## if min == B
    ind = np.where(min_arg == 0)
    hsv[..., 0][ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60
    ## if min == R
    ind = np.where(min_arg == 2)
    hsv[..., 0][ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
    ## if min == G
    ind = np.where(min_arg == 1)
    hsv[..., 0][ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300

    # S
    hsv[..., 1] = max_v.copy() - min_v.copy()

    # V
    hsv[..., 2] = max_v.copy()

    return hsv

def hsv2bgr(hsv, img):
    img = img.copy() / 255.

    # get max and min
    max_v = np.max(img, axis=2).copy()
    min_v = np.min(img, axis=2).copy()

    out = np.zeros_like(img)

    H = hsv[..., 0]
    S = hsv[..., 1]
    V = hsv[..., 2]

    C = S
    H_ = H / 60.
    X = C * (1 - np.abs(H_ % 2 - 1))
    Z = np.zeros_like(H)

    vals = [[Z,X,C], [Z,C,X], [X,C,Z], [C,X,Z], [C,Z,X], [X,Z,C]]

    for i in range(6):
        ind = np.where((i <= H_) & (H_ < (i + 1)))
        out[..., 0][ind] = (V - C)[ind] + vals[i][0][ind]
        out[..., 1][ind] = (V - C)[ind] + vals[i][1][ind]
        out[..., 2][ind] = (V - C)[ind] + vals[i][2][ind]

    out[np.where(max_v == min_v)] = 0
    out = np.clip(out, 0, 1)
    out = (out * 255).astype(np.uint8)

    return out

# hsvInverseHue
def hsvTransposeHue(hsv):
    # Transpose Hue
    hsv[..., 0] = (hsv[..., 0] + 180) % 360
    return hsv

# Decrease color
def decreaseColor(img):
    out = img.copy()
    out = out // 64 * 64 + 32
    return out

# make mask
# 像这样通过使用黑白二值图像将对应于黑色部分的原始图像的像素改变为黑色的操作被称为掩膜。
def getBlueMask255(hsv):
    mask = np.zeros_like(hsv[..., 0])
    #mask[np.where((hsv > 180) & (hsv[0] < 260))] = 255
    mask[np.logical_and((hsv[..., 0] > 180), (hsv[..., 0] < 260))] = 255
    return mask

# masking
def doMasking(img, mask):
    mask = 1 - mask
    out = img.copy()
    # mask [h, w] -> [h, w, channel]
    mask = np.tile(mask, [3, 1, 1]).transpose([1, 2, 0])
    out *= mask

    return out

# make mask
def getBlueMask1(hsv):
    mask = np.zeros_like(hsv[..., 0])
    # mask[np.where((hsv > 180) & (hsv[0] < 260))] = 255
    mask[np.logical_and((hsv[..., 0] > 180), (hsv[..., 0] < 260))] = 1
    return mask
