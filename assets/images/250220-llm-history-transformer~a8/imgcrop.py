import cv2
import numpy as np

def is_mostly_white(pixel_values, threshold):
    """ 判断是否大部分是白色（允许一定噪点） """
    return np.count_nonzero(pixel_values <= 250) <= threshold

def find_top_white_line(gray):
    """寻找最上方的主要白色横线索引（允许2.5%噪点）"""
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    width = gray.shape[1]
    threshold = int(width * 0.025)  # 允许的噪点数量

    for y in range(20, gray.shape[0]):  # 从上往下遍历
        if is_mostly_white(gray[y, :], threshold):
            continue
        return y  # 找到非白色区域
    return 0  # 没找到，返回0

def find_bottom_white_line(gray):
    """寻找最下方的主要白色横线索引（允许2.5%噪点）"""
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    width = gray.shape[1]
    threshold = int(width * 0.025)  # 允许的噪点数量

    for y in range(gray.shape[0] - 1, -1, -1):  # 从下往上遍历
        if is_mostly_white(gray[y, :], threshold):
            continue
        return y
    return gray.shape[0]

def find_left_white_line(gray):
    """寻找最左侧的主要白色竖线索引（允许2.5%噪点）"""
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height = gray.shape[0]
    threshold = int(height * 0.025)  # 允许的噪点数量

    for x in range(gray.shape[1]):  # 从左往右遍历
        if is_mostly_white(gray[:, x], threshold):
            continue
        return x
    return 0

def find_right_white_line(gray):
    """寻找最右侧的主要白色竖线索引（允许2.5%噪点）"""
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height = gray.shape[0]
    threshold = int(height * 0.025)  # 允许的噪点数量

    for x in range(gray.shape[1] - 1, -1, -1):  # 从右往左遍历
        if is_mostly_white(gray[:, x], threshold):
            continue
        return x
    return gray.shape[1]

def crop_white_borders(image_path, output_path):
    """读取图片，去除上下左右的白色边界，并保存"""
    image = cv2.imread(image_path)

    top = find_top_white_line(image)
    bottom = find_bottom_white_line(image)
    left = find_left_white_line(image)
    right = find_right_white_line(image)

    # 进行裁剪
    cropped_image = image[top:bottom, left:right]

    # 保存裁剪后的图片
    cv2.imwrite(output_path, cropped_image)
    print(f"裁剪完成，结果保存在: {output_path}")

def auto_crop(image_path, output_path):
    # 读取图片
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 进行二值化（白色背景通常高亮）
    _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    #cv2.imwrite("temp.png", binary)

    top = find_top_white_line(binary)
    bottom = find_bottom_white_line(binary)

    # 进行裁剪
    cropped_image = image[top:bottom, :]

    binary = binary[top:bottom, :]
    left = find_left_white_line(binary)
    right = find_right_white_line(binary)

    cropped_image = image[top:bottom, left:right]

    # 保存裁剪后的图片
    cv2.imwrite(output_path, cropped_image)
    print(f"裁剪完成，结果保存在: {output_path}")

# 示例调用
#auto_crop("20250304003933.png", "20250304003933.png")
#auto_crop("20250304003942.png", "20250304003942.png")
#auto_crop("20250304003905.png", "20250304003905.png")
#auto_crop("20250304003923.png", "20250304003923.png")
