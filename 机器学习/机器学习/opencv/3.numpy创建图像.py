import cv2
import numpy

# 创建一个100行，200列（即使宽200，高100）的数组
img = numpy.zeros((100, 200))
cv2.imshow(winname='Snow', mat=img)
cv2.waitKey(1000)

img2 = numpy.ones((100, 200)) * 255
cv2.imshow('Snow', img2)
cv2.waitKey(1000)

# 黑中带白
img[25:76, 50:151] = 255
cv2.imshow('Snow', img)
cv2.waitKey(1000)

# 创建黑白相间的图像
img = numpy.zeros((100, 200))
for i in range(0, 200, 50):
    # 全部组，每次隔开20列
    img[:, i:i + 20] = 255
cv2.imshow('Snow', img)
cv2.waitKey(1000)





# 创建彩色图像
# 以上实例都是使用二维数组表示的黑白图像
# 而当显示生活中丰富多彩的颜色需要引进光谱三基色的概念时，就无法使用二维数组来表示
# 而要用到三维数组来表示。
# BGR 蓝绿红

# 创建三维数组
# 创建好表示纯黑图像的三维数组后，复制出三个副本
# 三个副本分别修改最后一个索引代表的元素值
# 根据BGR的顺序，索引0表示蓝，索引1表示绿，索引2表示红
width = 600
height = 600
# 创建指定宽高，3通道，像素值都为0的图像
img = numpy.zeros((height,width,3))
blue = img.copy()
# 第一通道是255，还有两个通道依旧是0
blue[:,:,0] = 255
green = img.copy()
green[:,:,2] = 255
red = img.copy()
red[:,:,2] = 255
cv2.imshow('Snow',blue)
cv2.waitKey(500)
cv2.imshow('Snow',green)
cv2.waitKey(50)
cv2.imshow('Snow',red)
cv2.waitKey(500)




# 创建随机图像
# 每一个像素都是随机生成的
# 雪花点图像
width = 600
height = 600
# 单通道
# 3通道    三个通道值都是随机的
# 不知道为什么数据类型要uint8
img = numpy.random.randint(0,256,size=[height,width,3],dtype=numpy.uint8)
cv2.imshow('Snow',img)
cv2.waitKey()



# 图像拼接
# 水平拼接方法hstack()与竖直拼接方法vstack()
n1 = numpy.array([1,2,3])
n2 = numpy.array([4,5,6])

n3 = numpy.hstack((n1,n2))
n4 = numpy.vstack((n1,n2))

print(n3)
print(n4)














