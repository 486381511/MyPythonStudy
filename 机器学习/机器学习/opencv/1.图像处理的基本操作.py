import cv2
import numpy as np


# OpenCV提供了用于读取图像的imread()方法
# imread(filename= ,flags= )
# imread()方法中filename是图片路径，flags有两个参数，1与0，1是有颜色，0是无色
image = cv2.imread(filename='C:\\Users\\yi\\PycharmProjects\\pythonProject\\zophie.jpg',flags=1)
print(image)
# 输出的数字是图像的部分像素值，有关像素和像素值的内容


# 相对于上面密密麻麻的数字，OpenCV提供了
# imshow()、waitKey()方法和destroyAllWindows()方法用于展示图像
# imshow(winname,mat)    winname:显示图像的窗口名称，mat:要显示的图像
cv2.imshow(winname='Snow',mat=image)


# waitKey()方法用于等待用户按下键盘上按键的时间。当用户按下键盘上任意的按键时
# 将会执行waitKey()方法，并且获取waitKey()方法的返回值
# retval:与被按下的按键对应的ASCII码
# delay:等待用户按下键盘上按键的时间，单位为毫秒(ms)，当delay值为负数，空，0时表示无限时间等待
retval = cv2.waitKey(delay=2000)


# destroyAllWindows()方法用于关闭所有正在显示图像的窗口
cv2.destroyAllWindows()


# 保存图像
# imwrite(filename= ,img)
cv2.imwrite(filename='C:\\Users\\yi\\PycharmProjects\\pythonProject\\ziyaun\\10000.jpg',img=image)



# 获取图像属性
# 在处理图像的过程中，经常需要获取图像的大小，类型等图像属性
# 为此，OpenCV提供了shape、size和dtype三个常用的属性
# shape:  如果是彩色图像，那么就获取的是一个包含图像的水平像素、垂直像素和通道数的数组）
# 即（垂直像素、水平像素、通道数）;
# 如果是灰度图像，那么获取的是一个包含图像的水平像素和垂直像素的数组，即为（垂直像素，水平像素）
# 说明：垂直像素指定是垂直方向上的像素，水平像素指的是水平方向上的像素
# size：获取的是图像包含的像素的个数，其值为“水平像素*垂直像素*通道数”,灰度图像的通道数为1.
# dtype：获取的是图像的数据类型

print('shape:',image.shape)
print('size:',image.size)
print('dtype：',image.dtype)

