import numpy as np
import cv2
import time

# 绘制图形和文字
# OpenCV提供了许多绘制图形的方法
# 包括绘制线段的line()方法、绘制矩形的rectangle()方法、
# 绘制圆形的circle()方法、绘制多边形的polylines()方法和绘制文字的putText()方法。
# 本章将依次对上述各个方法进行讲解，并使用上述方法绘制相应的图形


def line():
    # 线段的绘制
    # img =cv2.line(img,pt1,pt2,color,thickness)
    # img：画布、pt1：线段的起点坐标、pt2：线段的终点坐标
    # color：颜色、thickness：宽度
    # 线条颜色是RGB格式的，例如红色(255,0,0)
    # 但在openCV中，RGB图像的通道顺序被转换为BGR
    # 因此红色是(0,0,255)

    canvas = np.zeros((600,300,3),np.uint8)
    canvas = cv2.line(canvas, (50, 120), (250, 120), (255, 0, 0), 10)
    canvas = cv2.line(canvas, (150, 30), (150, 230), (255, 0, 0), 10)
    canvas = cv2.line(canvas, (150, 120), (50, 200), (255, 0, 0), 10)
    canvas = cv2.line(canvas, (150, 120), (250, 200), (255, 0, 0), 10)
    canvas = cv2.line(canvas, (50, 230), (250, 230), (255, 0, 0), 10)
    canvas = cv2.line(canvas, (250, 230), (150, 300), (255, 0, 0), 10)
    canvas = cv2.line(canvas, (150, 300), (150, 400), (255, 0, 0), 10)
    canvas = cv2.line(canvas, (150, 400), (120, 350), (255, 0, 0), 10)
    canvas = cv2.line(canvas, (50, 300), (250, 300), (255, 0, 0), 10)
    cv2.imshow('snow',canvas)
    cv2.waitKey()


def rectangle():
    # 矩形绘制
    # img = cv2.rectangle(img,pt1,pt2,color,thickness)
    # pt1 左上角坐标，pt2 右下角坐标
    # thickness为负数时为填充
    canvas = np.zeros((600, 300, 3), np.uint8)
    color = (0,0,255)
    cv2.rectangle(img=canvas,pt1=(50,50),pt2=(250,550),color=color,thickness=10)
    cv2.imshow('snow',canvas)
    cv2.waitKey()


def circle():
    # img = cv2.circle(img,center,radius,color,thickness)
    # center为圆心坐标
    # radius为半径
    img = np.ones((500,500,3),np.uint8)
    cv2.circle(img,(250,250),100,(255,0,0),10)
    cv2.imshow('snow',img)
    cv2.waitKey()


def polyline():
    # 多边形的绘制
    # img = cv2.polylines(img,pts,isClosed,color,thickness)
    # pts是多边形各个点的坐标
    # isClosed为True就是封闭
    img = np.zeros((600,600,3),np.uint8)
    pts = np.array([[120,25],[45,544],[343,34],[34,6]])
    cv2.polylines(img,[pts],True,(255,0,0),10)
    cv2.imshow('snow',img)
    cv2.waitKey()

def putText():
    # openCV提供的绘制文字的方法
    # img = cv2.putText(img,text,org,fontFace,fontScale,color,thickness,lineType,bottomLeftOrigin)
    # text 绘制内容
    # org 文字在画布中的左下角坐标
    # fontFace 文字样式，可选参数
    # fontScale 字体大小
    # color 绘制文字时的线条的颜色
    # thickness 字体的宽度
    # lineType 线型，由4和8两个值，默认为8
    # bottomLeftOrigin 绘制文字时的方向，有True和False两个值，开启即使镜像模式
    img = np.zeros((600,600,3),np.uint8)
    text = 'Hello World!'
    cv2.putText(img,text,(50,300),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,0,0),10)
    cv2.imshow('snow',img)
    cv2.waitKey()


def boll():
    # 小球动画
    # 难
    width,height = 600,600  # 画面的宽高
    r = 20  # 圆半径
    x = r+20   # 圆心横坐标起始坐标  x=40
    y = r+100   # 圆心纵坐标起始坐标 y=120
    x_offer = y_offer = 4   # 每一帧的移动速度

    while cv2.waitKey(1) == -1:
        if x>width-r or x<r:
            x_offer += -1
        if y>height-r or y<r:
            y_offer += -1
        x += x_offer
        y += y_offer
        img = np.ones((width,height,3),np.uint8)*255
        cv2.circle(img,(x,y),r,(0,0,0),-1)
        cv2.imshow('snow',img)
        time.sleep(1/120)
    cv2.destroyAllWindows()




# line()
# rectangle()
# circle()
# polyline()
# putText()
boll()










