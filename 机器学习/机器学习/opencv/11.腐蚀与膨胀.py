import numpy as np
import cv2

def erode():
    # 腐蚀
    # dst = cv2.erode(src,kernel,anchor,iterations,borderType,borderValue)
    # kernel        腐蚀使用的核
    # 后面全部默认
    # 腐蚀用的核，行列数越大，计算效果越粗糙，行列数越小，计算效果越精细
    k = np.ones((5,5),np.uint8)
    src = cv2.imread('zophie.jpg')
    dst = cv2.erode(src,k)
    cv2.imshow('erode',dst)
    cv2.waitKey()

def dilate():
    # 膨胀
    # dst = cv2.dilate(src,kernel,anchor,iterations,borderType,borderValue)
    # kernel        膨胀使用的核
    # 后面全部默认
    # 膨胀用的核，行列数越大，计算效果越粗糙，行列数越小，计算效果越精细
    k = np.ones((5,5),np.uint8)
    src = cv2.imread('zophie.jpg')
    dst = cv2.dilate(src,k)
    cv2.imshow('dilate',dst)
    cv2.waitKey()


# 开运算：先腐蚀再膨胀
# 闭运算：先膨胀再腐蚀


def XingTaiXue():
    # dst = cv2.morphologyEx(src,op,kernel)
    # op：操作类型，参数：
    # cv2.MORPH_ERODE             腐蚀
    # cv2.MORPH_DILATE            膨胀
    # cv2.MORPH_OPEN              开运算：先腐蚀再膨胀
    # cv2.MORPH_CLOSE             闭运算：先膨胀再腐蚀
    # cv2.MORPH_GRADIENT          梯度运算，膨胀图减腐蚀图
    # cv2.MORPH_TOPHAT            顶帽运算，原始图减开运算图
    # cv2.MORPH_BLACKHAT          黑帽运算，闭运算图减原始图
    # 详细看书
    pass

erode()
dilate()










