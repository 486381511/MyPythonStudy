import numpy as np
import cv2


# 把图像的轮廓提取出来

# contours,hierarvhy = cv2.findContours(image,mode,method)
# image：被检测的图像，必须是8位单通道二值图像，如果原始图像是色彩图像，必须转化为灰度图像，并经过二值化处理
# mode：轮廓的检索模式
    # cv2.RETR_EXTERNAL         只检测外轮廓
    # cv2.RETR_LIST             检测所有轮廓，但不建立层次关系
    # cv2.RETR_CCOMP            检测所有轮廓，并建立两级层次关系
    # cv2.RETR_TREE             检测所有轮廓，并建立树状结构的层次关系
# method：检测轮廓时使用的方法
    # cv2.CHAIN_APPROX_NONE           储存轮廓上的所有点
    # cv2.CHAIN_APPROX_SIMPLE         只保存水平，垂直或对角线轮廓的端点
    # cv2.CHAIN_APPROX_TC89_L1        Ten-Chinl 近似算法的一种
    # cv2.CHAIN_APPROX_TC89_KCOS      Ten-Chinl 近似算法的一种

# contours：检测出的所有轮廓，list类型，每一个元素都是某个轮廓的像素坐标数组。
# hierarchy：轮廓之间的层次关系。
# 通过findContours()方法找到图像轮廓后，为了方便开发人员观测，最好能把轮廓画出来
# 于是OpenCV提供了drawContours()方法用来绘制这些轮廓


# image = cv2.drawContours(image, contours, contourIdx, color, thickness, lineTypee, hierarchy, maxLevel, offse)
# 参数说明：
# 　image：被绘制轮廓的原始图像，可以是多通道图像
# 　contours：findContours()方法得出的轮廓列表
# 　contourIdx：绘制轮廓的索引，如果为-1则绘制所有轮廓
# 　color：绘制颜色，使用BGR格式
# 　thickness：可选参数，画笔的粗细程度，如果该值为-1则绘制实心轮廓
# 　lineTypee：可选参数，绘制轮廓的线型
# 　hierarchy：可选参数，findContours()方法得出的层次关系

src = cv2.imread('mn.jpg')
BWSrc = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
t1,dst1 = cv2.threshold(BWSrc,166,255,cv2.THRESH_BINARY)
cv2.imshow('src',dst1)
cv2.waitKey()
contours,hierarvhy = cv2.findContours(dst1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
src = cv2.drawContours(src, contours, -1, (0,0,255), 3)
cv2.imshow('src',src)
cv2.waitKey()



# 轮廓拟合
# 拟合是指将平面上的一系列点，用一条光滑的曲线连接起来
# 轮廓的拟合就是将凹凸不平的轮廓用平整的几何图形体现出来

# 矩形包围框
# 矩形包围框是指图像轮廓的最小矩形边界
# OpenCV提供的boundingRect()方法可以自动计算轮廓最小矩形边界的坐标、宽和高

# retval = cv2.boundingRect (array)
# array：轮廓数组
# 返回值说明：
# retval：元组类型，包含4个整数值
# 分别是最小矩形包围框的：
# 左上角顶点的横坐标、左上角顶点的纵坐标、矩形的宽和高
# 所以也可以写成x, y, w, h = cv2.boundingRect (array)的形式



# 圆形包围框
# 圆形包围框与矩形包围框一样，是图像轮廓的最小圆形边界
# OpenCV提供的minEnclosingCircle ()方法可以自动计算轮廓最小圆形边界的圆心和半径

# center,radius = cv2.minEnclosingCircle(points)

# points：轮廓数组
# center：元组类型，包含2个浮点值，是最小圆形包围框圆形的横坐标和纵坐标
# radius：浮点类型，最小圆形包围框的半径



# 凸包
# 之前介绍了矩形包围框和圆形包围框
# 这2种包围框虽然已经逼近了图形的边缘
# 但这种包围框为了保持几何形状，与图形的真实轮廓贴合度较差
# 如果能找出图形最外层的端点，将这些端点连接起来，就可以围出一个包围图形的最小包围框
# 这种包围框叫凸包

# OpenCV提供的convexHull()方法可以自动找出轮廓的凸包

# hull = cv2.convexHull(points, clockwise, returnPoints)

# points：轮廓数组。
# clockwise：可选参数，布尔类型。当该值为True时，凸包中的点按顺时针排列，为False时按逆时针排列。
# returnPoints：可选参数，布尔类型。当该值为True时返回点坐标，为False时返回点索引。默认值为True。
# hull：凸包的点阵数组。



# 霍夫变换
# 霍夫变换是一种特征检测，通过算法识别图像的特征，从而判断图像中的特殊形状，例如直线和圆。本节将介绍如何检测图像中的直线和圆

# 直线检测

# 圆环检测

# 看书


