import cv2
import numpy as np

# 模板匹配是一种最原始、最基本的识别方法
# 在原图找特定的图像的位置（适用于简单的场景！！！）

# openCV提供了matchTemplate()
# result = cv2.matchTemplate(image,templ,method,mask)
# templ 模板图像，尺寸要小于或等于原图
# method 匹配方法，参数值
# cv2.TM_SQDIFF           平方差匹配，越匹配，计算值越小
# cv2.TM_CCORR_NORMED     标准差匹配，同上
# cv2.TM_CCORR            相关匹配，值越大越匹配
# cv2.TM_CCORR_NORMED     标准相关匹配，同上
# cv2.TM_CCOEFF           相关系数匹配
# cv2.TM_CCOEFF_NORMED    标准相关系数匹配

# result说明：如果原图W、H，模板图像w、h，result就是一个W-w+1列，H-h+1行的32位浮点数数组


# 单模板匹配
# matchTemplate()方法的计算结果是一个二维数组，openCV提供了一个minMaxLoc()方法来解析这个数组
# minValue,maxValue,minLoc,maxLoc = cv2.minMaxLoc(src,mask)
# src：matchTemperature()计算出来的数组,方法不一样计算要的结果不一样
# minValue：数组的最小值
# maxValue：数组的最大值
# minLoc：最小值的坐标（x，y）
# maxLoc：最大值的坐标（x，y）

src1 = cv2.imread('mn.jpg')
src2 = cv2.imread('mntou.jpg')
height,width,c = src2.shape
results = cv2.matchTemplate(src1,src2,cv2.TM_SQDIFF_NORMED) # 标准平方差
minValue,maxValue,minLoc,maxLoc = cv2.minMaxLoc(results)
print(results)
resultPoint1 = minLoc
resultPoint2 = (resultPoint1[0]+width,resultPoint1[1]+height)
cv2.rectangle(src1,resultPoint1,resultPoint2,(0,0,255),5)
cv2.imshow('muban',src1)
cv2.waitKey()






