from operator import index

import numpy as np
import cv2

def VideoCapture_JieShao():
    # 视频处理
    # OPenCV不仅能够处理图像，还能够处理视频
    # 视频是由大量的图像构成的
    # 这些图像以固定的时间间隔从视频中获取
    # 这样就能够使用图像处理的方法对这些图像进行处理，进而达到处理视频的目的
    # 要处理视频，需要先对视频进行读取、显示和保存等相关操作
    # OpenCV提供了VideoCapture类和VideoWrite类的相关方法

    # 读取并显示摄像头视频
    # VideoWrite类及其相关方法
    capture = cv2.VideoCapture(0)
    # capture要打开的摄像头    index摄像头的设备索引
    # index为0时表示打开第一个摄像头，笔记本自带
    # index为时表示打开第二个摄像头，笔记本外设
    retval = capture.isOpened()
    # retval：isOpened()方法的返回值，摄像头初始化成功则返回True，否则False
    print(retval)

    # 摄像头初始化成功后，可以从摄像头中读取帧，VideoCapture类提供了read()方法
    retval,image = capture.read()

    # 成功从摄像头中读取帧后,retval返回True，否则False
    # image：帧

    # 不需要摄像头要关闭
    capture.release()

def VideoCapture_Use():
    # cv2.CAP_DSHOW     解除警告
    capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while (capture.isOpened()):
        retval,image = capture.read()
        cv2.imshow('image', image)
        key = cv2.waitKey(1)       # 按下空格跳出循环
        if key == 32:
            break
    capture.release()
    cv2.destroyAllWindows()


def readVideo():
    # video = cv2.VideoCapture(filename)
    video = cv2.VideoCapture('D:\\ceshi\\sucai.mp4')
    while (video.isOpened()):
        retval,img = video.read()
        cv2.imshow('img',img)
        key = cv2.waitKey(40)
        if key == 32:
            break


def VideoWrite():
    # 暂时不用，看书
    pass

# 还有一些不常用方法看书

VideoCapture_Use()
# readVideo()







