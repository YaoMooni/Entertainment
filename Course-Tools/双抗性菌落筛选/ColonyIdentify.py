import cv2
import numpy as np
from PIL import Image


# 读取图像
img = Image.open(r'E:\学习\03四川大学\2-5大二下\7-1微生物学实验\环境中微生物的筛选与检测\fig\A2.jpg')

# 将图像转换为灰度图
if img is not None:
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    # 继续处理灰度图
    cv2.imwrite('gray_image.jpg', gray)

else:
    print("无法读取图像文件")


# # 使用 Canny 边缘检测算法检测边缘
# edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# # 使用霍夫变换检测直线
# lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

# # 绘制直线
# for line in lines:
#     rho, theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a * rho
#     y0 = b * rho
#     x1 = int(x0 + 1000 * (-b))
#     y1 = int(y0 + 1000 * (a))
#     x2 = int(x0 - 1000 * (-b))
#     y2 = int(y0 - 1000 * (a))
#     cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# # 显示结果
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 获取图像尺寸
h, w = gray.shape

# 计算每个格子的尺寸,并留出一些空白距离
cell_size = min(h, w) // 6
cell_spacing = cell_size // 6
cells = [gray[y+cell_spacing:y+cell_size-cell_spacing, x+cell_spacing:x+cell_size-cell_spacing] for y in range(0, h, cell_size) for x in range(0, w, cell_size)]

# 遍历每个格子,检测是否有小球
for i, cell in enumerate(cells):
    # 使用二值化和轮廓检测来检测小球
    thresh_val = 120  # 调整这个值来控制颜色误差的容忍度
    _, thresh = cv2.threshold(cell, thresh_val, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        # 打印有小球的格子坐标
        row, col = i // 6, i % 6
        print(f"格子坐标: ({row}, {col})")