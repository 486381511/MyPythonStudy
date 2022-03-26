import numpy as np
import cv2

# 尽量保存原图像信息的情况下，去除掉图像内的噪声，降低细节层次信息等一系列的过程叫图像的平滑处理
# 实现图像平滑处理的常用工具就是滤波器

# 均值滤波器，中值滤波器，高斯滤波器，双边滤波器

# 以一个像素位核心，其周围像素可以组成一个n行n列的矩阵
# 这样的矩阵结构在滤波器操作中被称为’滤波核‘（奇数）

def blur():
    # 均值滤波器
    # dst = cv2.blur(src,ksize,anchor,borderType)
    # ksize 滤波核大小，格式位（高，宽），建议使用n*n奇数边长
    # 滤波核越大，处理后图像越模糊
    # 后面值为默认就好
    src = cv2.imread('zophie.jpg')
    dst = cv2.blur(src,(2,2))
    cv2.imshow('blur',dst)
    cv2.waitKey()


def medianBlur():
    # 中值滤波器
    src = cv2.imread('zophie.jpg')
    # 这次是滤波器的边长，且只能为奇数
    dst = cv2.medianBlur(src,3)
    cv2.imshow('medianblur',dst)
    cv2.waitKey()


def GaussionBlur():
    # 高斯滤波器
    # 高斯模糊
    # 权重计算
    src = cv2.imread('zophie.jpg')
    # 滤波核是奇数！
    # dst = cv2.GaussianBlur(src,ksize,sigmaX,sigmaY,borderType)
    # 不知道算卷积核就填0
    dst = cv2.GaussianBlur(src,(31,31),0,0)
    cv2.imshow('GaussionBlur',dst)
    cv2.waitKey()

def bilateralFilter():
    # 双边滤波器
    pass

# blur()
# medianBlur()
GaussionBlur()
cv2.destroyAllWindows()