import cv2
import numpy as np

# 像素是图像的最小单元。每一幅图像都是由M行N列的像素组成的，其中每一个像素都储存一个像素值。
# 以灰度图像为例，计算机通常把灰度图像的像素处理为256个灰度级别
# 256个灰度级别分别使用区间[0,255]中的整数数值表示。
# 其中，“0”表示纯黑色；“255”表示纯白色


# 获取指定区域的BGR值
image = cv2.imread('C:\\Users\\yi\\PycharmProjects\\pythonProject\\zophie.jpg')
px = image[100,100]
print(px)

p1 = image[100,100,0]   # B的值
p2 = image[100,100,1]   # G的值
p3 = image[100,100,2]   # R的值
print(p1,p2,p3)


# 修改像素的BGR值
# px = image[100,100]，修改了这里像素值
px = [200,200,200]


# 修改一个区域的像素值
for i in range(100,500):
    for j in range(50,620):
        image[i,j] =[55,125,255]
cv2.imshow(winname='snow',mat=image)
cv2.waitKey(0)





