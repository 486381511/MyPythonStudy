import numpy as np
import cv2

# 使得图像轮廓更加鲜明，更容易被计算机识别

# 流程：把图像色彩空间转化为灰度空间，再进行阈值处理
# openCV提供了threshold()方法用于图像进行阈值处理
# retval,dst = cv2.threshold(src,thresh,maxval,type)
# thresh: 阈值
# maxval：阈值处理采用的最大值
# type：阈值处理的类型
        # cv2.THRESH_BINARY             二值化阅值处理
        # cv2.THRESH_BINARY_INV         反二值化阀值处理
        # cv2.THRESH_TOZERO             低于阀值零处理
        # cv2.THRESH_TOZERO_INV         超出阈值零处理
        # cv2.THRESH_TRUNC              截断阈值处理
# retval：处理时采用的阈值


# 二值化处理
# 进行二值化处理时，每一个像素都会与阈值进行比较，将大于阈值的像素值变为最大值，小于或等于阈值的像素值变为0
img = cv2.imread('zophie.jpg',0)    # 将图像读取成灰度图像
t1,dst1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow('snow',dst1)
print(t1)   # 就是阈值
cv2.waitKey()

# 反二值化处理
# 进行反二值化处理时，每一个像素都会与阈值进行比较，将大于阈值的像素值变为0，小于或等于阈值的像素值变为最大值
t2,dst2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow('snow',dst2)
print(t2)   # 就是阈值
cv2.waitKey()



# 零处理
# 零处理会将某一个范围内的像素值变为0，并允许范围之外的像素值保留原值。
# 零处理包括低于阈值0处理和高于阈值零处理

# 低于阈值零处理
# 低于阈值的像素值变为0，高的保持不变
t3,dst3 = cv2.threshold(img,130,255,cv2.THRESH_TOZERO)  # 低于阈值零处理上最大阈值没用
cv2.imshow('snow',dst3)
print(t3)   # 就是阈值
cv2.waitKey()

# 超出阈值零处理
# 超出阈值的像素值变为0，低于的保持不变
t4,dst4 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)  # 超出阈值零处理上最大阈值没用
cv2.imshow('snow',dst4)
print(t4)   # 就是阈值
cv2.waitKey()



# 截断处理
# 截断处理也叫截断阈值处理，该处理将图像中大于阈值的像素值变为和阈值一样的值，小于阈值保持不变
t5,dst5 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC)  # 截断阈值零处理上最大阈值没用
cv2.imshow('snow',dst5)
print(t5)   # 就是阈值
cv2.waitKey()



# 自适应处理
# 图像中不同区域使用不同阈值，把这种改进阈值处理技术称为自适应阈值处理
# 处理明暗不均图像，获得更加简单的图像效果
# !!!传入图要为灰度图像
# dst = cv2.adaptiveThreshold(src,maxValue,adaptiveMethod,thresholdType,blockSize,C)
# src：被处理图像，该图像要是灰度图像
# maxValue：阈值处理采用的最大值
# adaptiveMethod：自适应阈值的计算方法
           # cv2.ADAPTIVE_THRESH_MEAN_C             对一个正方形区域内的所有像素平均加权
           # cv2.ADAPTIVE_THRESH_GAUSSIAN_C         高斯函数.....
# thresholdType：阈值处理类型，要为二值化处理，或者是反二值化处理
# blockSize：一个正方形区域的大小，5值的是5*5区域
# C：常数
img2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)
cv2.imshow('snow',img2)
cv2.waitKey()



# 电脑自己找阈值
# Ostu方法
# 前面都是自己找阈值，ostu()方法可以让电脑自己计算出阈值
# ostu 方法基本与threshold一样

# retval,dst = cv2.threshold(src,thresh,maxval,type)
# thresh要设置为0
# type 再加上一个阈值处理类型，原cv2.类型 + cv2.THRESH_OTSU







