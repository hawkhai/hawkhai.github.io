import cv2
import numpy as np

def rectify_ppt_by_color(image_path, output_path="ppt_rectified.png", debug_mask="mask.png"):
    img = cv2.imread(image_path)
    orig = img.copy()

    # ---- Step 1: 在RGB颜色空间定义范围 ----
    # 目标颜色1: (215,191,191) 和 目标颜色2: (216,188,185)
    target_rgb1 = np.array([191, 191, 215])  # BGR转RGB
    target_rgb2 = np.array([185, 188, 216])  # BGR转RGB
    
    print(f"目标颜色1 RGB: {target_rgb1}")
    print(f"目标颜色2 RGB: {target_rgb2}")
    
    # 计算RGB范围，确保都能包含
    tolerance = 40  # RGB容差 (扩大范围)
    r_min = min(target_rgb1[0], target_rgb2[0]) - tolerance
    r_max = max(target_rgb1[0], target_rgb2[0]) + tolerance
    g_min = min(target_rgb1[1], target_rgb2[1]) - tolerance
    g_max = max(target_rgb1[1], target_rgb2[1]) + tolerance
    b_min = min(target_rgb1[2], target_rgb2[2]) - tolerance
    b_max = max(target_rgb1[2], target_rgb2[2]) + tolerance
    
    # BGR格式的范围
    lower = np.array([max(0, b_min), max(0, g_min), max(0, r_min)])
    upper = np.array([min(255, b_max), min(255, g_max), min(255, r_max)])
    
    print(f"BGR范围: lower={lower}, upper={upper}")

    mask = cv2.inRange(img, lower, upper)

    # ---- Step 3: 连通区域分析和过滤 ----
    # 先进行基本的形态学操作去除噪声
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)  # 去除小噪点
    
    # 连通组件分析
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
    
    # 计算总面积
    total_area = mask.shape[0] * mask.shape[1]
    min_area_threshold = total_area * 0.1  # 10% 阈值
    
    print(f"检测到 {num_labels-1} 个连通区域")
    
    # 创建新的mask，只保留大于10%的区域
    filtered_mask = np.zeros_like(mask)
    valid_regions = 0
    
    for i in range(1, num_labels):  # 跳过背景(label=0)
        area = stats[i, cv2.CC_STAT_AREA]
        area_ratio = area / total_area
        print(f"区域 {i}: 面积 {area} 像素 ({area_ratio:.2%})")
        
        if area >= min_area_threshold:
            filtered_mask[labels == i] = 255
            valid_regions += 1
            print(f"  ✅ 保留区域 {i}")
        else:
            print(f"  ❌ 移除区域 {i} (小于10%)")
    
    print(f"保留了 {valid_regions} 个有效区域")
    mask = filtered_mask
    
    # ---- Step 4: 去除毛刺 ----
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)  # 填充小洞
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)   # 去除毛刺

    # ---- 计算核心内容区域面积占比 ----
    total_pixels = img.shape[0] * img.shape[1]
    core_pixels = cv2.countNonZero(mask)
    core_area_ratio = core_pixels / total_pixels
    
    print(f"📊 图像总像素: {total_pixels}")
    print(f"📊 核心内容像素: {core_pixels}")
    print(f"📊 核心内容面积占比: {core_area_ratio:.2%}")
    
    if core_area_ratio > 0.4:
        print("✅ 核心内容面积超过 40%，继续处理...")
        # 保存调试用的 mask
        cv2.imwrite(debug_mask, mask)
        print(f"🟡 mask 已输出到 {debug_mask}")
    else:
        print(f"❌ 核心内容面积仅为 {core_area_ratio:.2%}，未达到 40% 阈值")
        # 仍然保存 mask 用于调试
        cv2.imwrite(debug_mask, mask)
        print(f"🟡 调试用 mask 已保存到 {debug_mask}")
        return None

    # ---- Step 4: 找轮廓 ----
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        raise Exception("未检测到 PPT 背景区域")

    # 取最大轮廓
    c = max(cnts, key=cv2.contourArea)

    # 尝试拟合矩形
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    pts = np.int0(box).astype("float32")

    # ---- Step 5: 四点排序 ----
    rect_pts = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect_pts[0] = pts[np.argmin(s)]  # 左上
    rect_pts[2] = pts[np.argmax(s)]  # 右下

    diff = np.diff(pts, axis=1)
    rect_pts[1] = pts[np.argmin(diff)]  # 右上
    rect_pts[3] = pts[np.argmax(diff)]  # 左下

    (tl, tr, br, bl) = rect_pts
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = int(max(widthA, widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = int(max(heightA, heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # ---- Step 6: 透视变换 ----
    M = cv2.getPerspectiveTransform(rect_pts, dst)
    warp = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))

    cv2.imwrite(output_path, warp)
    print(f"✅ 已保存矫正后的 PPT 到 {output_path}")
    print(f"🟡 调试用 mask 已保存到 {debug_mask}")

if __name__ == "__main__":
    rectify_ppt_by_color("640llm.png", "ppt_rectified.png", "mask.png")
