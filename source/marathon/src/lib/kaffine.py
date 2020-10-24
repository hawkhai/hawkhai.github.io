#encoding=utf8
import cv2
import numpy as np

# Affine
# a b tx
# c d ty
# 0 0 1
# 仿射变换（Afine Transformations）
def affine(img, a, b, c, d, tx, ty):
    H, W, C = img.shape
    imgsrc = img

    # temporary image
    img = np.zeros((H+2, W+2, C), dtype=np.float32)
    img[1:H+1, 1:W+1] = imgsrc

    # get new image shape
    H_new = np.round(H * d).astype(np.int)
    W_new = np.round(W * a).astype(np.int)
    out = np.zeros((H_new+1, W_new+1, C), dtype=np.float32)

    # get position of new image
    x_new = np.tile(np.arange(W_new), (H_new, 1))
    y_new = np.arange(H_new).repeat(W_new).reshape(H_new, -1)

    # get position of original image by affine
    adbc = a * d - b * c
    x = np.round((d * x_new  - b * y_new) / adbc).astype(np.int) - tx + 1
    y = np.round((-c * x_new + a * y_new) / adbc).astype(np.int) - ty + 1

    x = np.minimum(np.maximum(x, 0), W+1).astype(np.int)
    y = np.minimum(np.maximum(y, 0), H+1).astype(np.int)

    # assgin pixcel to new image
    out[y_new, x_new] = img[y, x]

    out = out[:H_new, :W_new]
    out = out.astype(np.uint8)

    return out

# cos(theta) -sin(theta)
# sin(theta) cos(theta)
def affineRotation(img, theta):
    a = np.cos(theta)
    b = -np.sin(theta)
    c = np.sin(theta)
    d = np.cos(theta)
    return affineCenter(img, a=a, b=b, c=c, d=d, tx=0, ty=0)

# 假如发生旋转，要居中旋转。
# a b tx
# c d ty
# 0 0 1
# 仿射变换（Afine Transformations）
def affineCenter(img, a, b, c, d, tx, ty):
    H, W, C = img.shape
    imgsrc = img

    img = np.zeros((H+2, W+2, C), dtype=np.float32)
    img[1:H+1, 1:W+1] = imgsrc

    newH = np.round(H).astype(np.int)
    newW = np.round(W).astype(np.int)
    out = np.zeros((newH, newW, C), dtype=np.float32)

    newx = np.tile(np.arange(newW), (newH, 1)) # [[0 1 2] [0 1 2]]
    newy = np.arange(newH).repeat(newW).reshape(newH, -1) # [[0 0 0] [1 1 1]]

    adbc = a * d - b * c
    x = np.round((d * newx - b * newy) / adbc).astype(np.int) - tx + 1
    y = np.round((-c * newx + a * newy) / adbc).astype(np.int) - ty + 1

    dcx = (x.max() + x.min()) // 2 - W // 2
    dcy = (y.max() + y.min()) // 2 - H // 2

    x -= dcx
    y -= dcy

    x = np.clip(x, 0, W + 1)
    y = np.clip(y, 0, H + 1)

    out[newy, newx] = img[y, x]
    out = out.astype(np.uint8)
    return out
