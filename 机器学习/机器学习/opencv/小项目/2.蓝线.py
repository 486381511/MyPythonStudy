import cv2
import numpy as np

# 加载摄像头对象
video = cv2.VideoCapture(1,cv2.CAP_DSHOW)

# 定义一个i变量，后面用来确定蓝线的位置
i=0

# 蓝线的形状是3通道宽5高480
lineBlue = np.zeros([480,5,3])
# 第一个通道所有数都是255
# 记住BGR(255,0,0)就是蓝色
lineBlue[:,:,0]=255

# 先定义一个左照片，高480，宽640，通道数为3，先不用管，后面再用
rightImg = np.zeros([480,640,3],dtype=np.uint8)
# 定义一个名叫snow的图像，同上
snow = np.zeros([480,640,3],dtype=np.uint8)
# 定义一个名叫blue的图像，同上
blue = np.zeros([480,640,3],dtype=np.uint8)
# cv2.waitKey()

# video对象的isOpend()方法，调取摄像头成功就返回True，否则False
while video.isOpened():
    # video对象大胆read()方法，读取摄像头的图像
    # 返回两个值，读取摄像头的图像，成功就返回第一个参数True，否则False
    # 第二个参数就是摄像头读取的照片
    recth,img = video.read()
    # 左照片的高不变，宽是5 （i+5-i）
    #
    rightImg[0:480,i:i+5] = img[0:480,i:i+5]
    snow[0:480,i:i+5] = rightImg[0:480,i:i+5]
    snow[0:480,i+5:640] = img[0:480,i+5:640]
    blue = snow.copy()
    blue[0:480,i:i+5] = lineBlue
    # print(blue)
    cv2.imshow('snow',blue)
    i = i+5
    key = cv2.waitKey(60)
    if i >= 640:
        break

print('成型图像')
cv2.imshow('snow',snow)
cv2.waitKey()