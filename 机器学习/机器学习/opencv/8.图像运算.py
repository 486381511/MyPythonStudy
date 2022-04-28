import cv2
import numpy as np


def mask():
    # 掩模，也叫掩码，mask
    # 医生做手术，盖白布，留白

    mask = np.ones((150,150,3),np.uint8)
    mask[50:100,20:80,:] = 255
    cv2.imshow('mask1',mask)
    mask[:,:,:] = 255
    mask[50:100,20:80,:] = 0
    cv2.imshow('mask2',mask)
    cv2.waitKey()
    cv2.destroyAllWindows()


def add():
    # 一般是不会让两张图像数组用"+"相加的，而是通过add()方法
    # dst = cv2.add(src1,src2,mask,dtype)
    # 后面两个参数默认即可
    # 要注意的是当相加的值大于255时，取255（原因）
    src1 = cv2.imread('zophie.jpg')
    src2 = cv2.imread('zophie.jpg')
    dst = cv2.add(src1,src2)
    cv2.imshow('add',dst)
    cv2.waitKey()


def bitwise():
    # 图像的位运算
    # 像素可以用十进制表示，十进制转化为二进制
    # opencv提供的方法
    # cv2.bitwise_and()       # 按位与
    # cv2.bitwise_or()        # 按位或
    # cv2.bitwise_not()       # 按位取反
    # cv2.bitwise_xor()       # 按位异或

    # dst = cv2.bitwise_and(src1,src2,mask)
    # 如果某像素与纯白像素做与运算，结果仍是某像素原值
    # 如果某像素与纯黑像素做与运算，结果仍是纯黑像素

    img = cv2.imread('zophie.jpg')
    print(img.shape)
    src2 = np.zeros(img.shape,np.uint8)
    src2[400:800,:,:] =255
    print(src2)
    cv2.imshow('src',src2)
    dst = cv2.bitwise_and(img,src2)
    cv2.imshow('and',dst)

    dst1 = cv2.bitwise_or(img,src2)
    # 按位或运算，纯黑为某像素，纯白还是纯白
    cv2.imshow('or',dst1)

    dst2 = cv2.bitwise_not(img)
    # 按位取反运算，呈现与原图颜色完全相反
    cv2.imshow('not',dst2)

    dst3 = cv2.bitwise_xor(img,src2)
    # 按位异或运算，白色区域的原图像取反，黑色区域的原图像不变
    cv2.imshow('xor',dst3)
    cv2.waitKey()
    cv2.destroyAllWindows()


def addWeighted():
    # 加权和（多次曝光）
    # dst = cv2.addWeighted(src1,alpha,src2,beta,gamma)
    # alpha 第一幅图的权重
    # beta 第二幅图的权重
    # gamma 越大越亮，越小越暗

    src1 = cv2.imread('zophie.jpg')
    rows,colmns,channel = src1.shape
    src2 = cv2.imread('mn.jpg')
    src2 = cv2.resize(src2,(colmns,rows))
    dst = cv2.addWeighted(src1,0.7,src2,0.4,0)
    cv2.imshow('addWeighted',dst)
    cv2.waitKey()




# add()
# bitwise()
addWeighted()
