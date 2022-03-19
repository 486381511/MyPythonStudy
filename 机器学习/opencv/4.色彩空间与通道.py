import numpy as np
import cv2


# 色彩空间
# GRAY色彩空间与HSV色彩空间

# GRAY色彩空间
# 1.什么是GRAY色彩空间
# GRAY色彩空间通常指的是灰度图像，灰度图像是一种每个像素都是黑到白
# 被处理为256个灰度级别的单色图像，这256个灰度级别分别用区间[0,255]中的数值表示

# 2.从BGR色彩空间转换到GRAY色彩空间
# cv2.cvtColor(src,code)方法，src转换前的初始化图像，code:色彩空间转换码
# BGR转换到GRAY,code通常用cv2.COLOR_BGR2GRAY
image = cv2.imread(filename='C:\\Users\\yi\\PycharmProjects\\pythonProject\\zophie.jpg',flags=1)
dst = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Snow',image)
cv2.waitKey(2000)
cv2.imshow('Snow',dst)
cv2.waitKey(2000)


# HSV色彩空间
# 1.什么是HSV色彩空间
# BGR色彩空间是基于三基色而言的，红绿蓝
# HSV色彩空间是基于色调、饱和度和亮度而言的

# 1.1 色调（H）是指光的颜色，例如彩虹中的红橙黄绿青蓝紫分别表示不同的色调
# 在openCV中，色调在区间[0,180]内取值
# 例如，表示红色、黄色、绿色、蓝色的色调值分别为0，30，60，120

# 1.2 饱和度（S）是指色彩的深浅
# 在openCV中，饱和度在区间[0,255]内取值，当饱和度为0时，图像变为灰度图像

# 1.3 亮度（V）是指光的明暗
# 与饱和度相同，在openCV中，亮度在[0,255]内取值
# 亮度值越大，图像越亮；当亮度值为0时，图像呈纯黑白


# 2.从BGR色彩空间转换到HSV色彩空间
# 还是cv2.cvtColor(src,code)方法,转换码cv2.COLOR_BGR2HSV
image = cv2.imread(filename='C:\\Users\\yi\\PycharmProjects\\pythonProject\\zophie.jpg',flags=1)
HsvImage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('Snow',HsvImage)
cv2.waitKey()




# 通道

# 1.拆分通道
# 为了拆分图像中的通道，openCV提供了split()方法

# 1.1拆分一幅BGR图像中的通道
# b,g,r = cv2.split(bgr_image)
# b:B通道图像，g:G通道图像，r:R通道图像，bgr_image:一幅BGR图像
bgr_image = cv2.imread(filename='C:\\Users\\yi\\PycharmProjects\\pythonProject\\zophie.jpg',flags=1)
b,g,r = cv2.split(bgr_image)
cv2.imshow('Snow',b)
cv2.waitKey()
cv2.imshow('Snow',g)
cv2.waitKey()
cv2.imshow('Snow',r)
cv2.waitKey()
cv2.destroyAllWindows()

# 三幅灰度图像为什么？
# 原因是当程序执行到cv2.imshow('Snow',b)时
# 原图像B、G、R三个通道的值都会被修改为B通道图像的值，即(b,b,b)
# 对于BGR图像，只要B、G、R三个通道的值都相同，就可以得到灰度图像


# 1.2拆分一幅HSV图像中的通道
# 把BGR色彩空间图像转化为HSV图像，再拆分
hsv_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_image)
cv2.imshow('h',h)
cv2.waitKey()
cv2.imshow('s',s)
cv2.waitKey()
cv2.imshow('v',v)
cv2.waitKey()
cv2.destroyAllWindows()



# 合并通道
#（拆分通道的逆过程）
# 使用openCV的merge()方法

# 当使用merge方法合并BGR通道时，按B到G到R的顺序合并通道
bgr = cv2.merge([b,g,r])
# 合并HSV也差不多
hsv = cv2.merge([h,s,v])
cv2.imshow('bgr',bgr)
cv2.imshow('hsv',hsv)
cv2.waitKey()
cv2.destroyAllWindows()



# 综合运用拆分通道和合并通道
# 在HSV色彩空间图像中，保持两个通道不变，改变一个通道
# 只把H通道的值调整为180

# 思路： BGR转换为HSV，拆分通道，改变一个通道，合并所有通道，转换为BGR
bgr_image = cv2.imread(filename='C:\\Users\\yi\\PycharmProjects\\pythonProject\\zophie.jpg',flags=1)
hsv_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_image)
s[:,:] = 55
chanceHsvImage = cv2.merge([h,s,v])
cv2.imshow('Snow',chanceHsvImage)
cv2.waitKey()
chanceBgrImage = cv2.cvtColor(chanceHsvImage,cv2.COLOR_HSV2BGR)
cv2.imshow('Snow',chanceBgrImage)
cv2.waitKey()
cv2.destroyAllWindows()



# alpha通道
# GRBA(BGRA)
bgr_image = cv2.imread(filename='C:\\Users\\yi\\PycharmProjects\\pythonProject\\zophie.jpg',flags=1)
rgba = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2BGRA)
b,g,r,a = cv2.split(rgba)
a[:,:] = 0
rgbaIm = cv2.merge([b,g,r,a])
cv2.imshow('Snow',rgbaIm)
cv2.waitKey()
cv2.destroyAllWindows()





















