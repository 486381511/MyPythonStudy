import cv2
import numpy as np

# 几何变换是指改变图像的几何结构，例如大小、角度和形状等
# 让图像呈现出缩放、翻转、映射和透视效果

def resize():
    # 缩放
    # dst = cv2.resize(src,dsize,fx,fy,interpolation)
    # src：原始图像
    # dsize：输出图像的大小，格式为（宽、高），单位为像素
    # fx：可选参数，水平方向的缩放比例
    # fy：可选参数，垂直方向的缩放比例
    # interpolation：可选参数，缩放的插值方式，补充像素
    # dst：缩放后图像
    img = cv2.imread('C:\\Users\\yi\\PycharmProjects\\pythonProject\\zophie.jpg',1)
    dst1 = cv2.resize(img,(100,100))    # 按照宽100像素，高100像素的大小进行缩小
    dst2 = cv2.resize(img,(1800,1800))  # 同上，放大
    # cv2.imshow('snow',img)
    # cv2.waitKey()
    cv2.imshow('snow',dst1)
    cv2.waitKey()
    # cv2.imshow('snow',dst2)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # fx与fy参数实现放缩
    # 使用fx与fy参数时，dsize值要为none
    # 新图像的宽度 = fx * 原图像宽度
    # 新图像的高度 = fy * 原图像高度
    dst3 = cv2.resize(img,dsize=None,fx=2,fy=2)    # x与y都放大两倍
    cv2.imshow('snow',dst3)
    cv2.waitKey()


def flip():
    # 旋转(x,y,xy转)
    # dst = cv2.flip(src,flipCode)
    # src：原始图像、flipCod：反转类型、dst：反转后图像
    # flip: 0(沿x轴翻转)  正数（沿y轴翻转）  负数（同时xy）
    img = cv2.imread('zophie.jpg')
    # flipCode为0沿x轴翻转
    dst = cv2.flip(img,flipCode=0)
    cv2.imshow('snow',dst)
    cv2.waitKey()
    # flipCode为正数沿y轴翻转
    dst2 = cv2.flip(img, flipCode=1)
    cv2.imshow('snow', dst2)
    cv2.waitKey()
    # flipCode为负数沿x与y轴翻转
    dst3 = cv2.flip(img, flipCode=-1)
    cv2.imshow('snow', dst3)
    cv2.waitKey()
    cv2.destroyAllWindows()


def warpAffine():
    # 仿射变换
    # 包含平移、旋转和倾斜
    # dst = cv2.warpAffine(src,M,dsize,flags,borderMode,borderValue)
    # M：一个2行3列的矩阵，根据此矩阵的值变换原图中的像素的位置
    # dsize：输出图像的大小
    # flags：插值
    # 后面两个默认

    # M也被叫作仿射矩阵，实际上就是一个2*3的列表
    # M=[[a,b,c],[d,e,f]]

    # 图像做何种仿射变换取决于M的值
    # 新x = 原x*a + 原y*b + c
    # 新y = 原x*d + 原y*e + f

    # M矩阵中数字采用32位浮点格式
    M = np.zeros((2,3),np.float32)

    # ？具体赋值
    M = np.float32([[1,2,3],[4,5,6]])

    # 平移（所有像素移动）
    # M = [[1,0,水平移动距离],[0,1,垂直移动距离]]
    img = cv2.imread('zophie.jpg')
    rows = len(img)     # img的行数
    cols = len(img[0])   # img的列数
    M = np.float32([[1,0,200],[0,1,200]])
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow('snow',dst)
    cv2.waitKey()

    # 旋转
    # 让图像旋转也是通过M矩阵实现的，但得出这个矩阵需要做很复杂的运算
    # 于是OpenCV提供了getRotationMatrix2D()
    # 方法自动计算旋转图像的M矩阵
    # M = cv2.getRotationMatrix2D(center, angle, scale)
    # center: 旋转中心点坐标
    # angle： 旋转的角度  正顺负逆
    # scale： 比例，浮点类型
    img = cv2.imread('zophie.jpg')
    rows = len(img)  # img的行数
    cols = len(img[0])  # img的列数
    M = cv2.getRotationMatrix2D((500,500),30,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow('snow',dst)
    cv2.waitKey()

    # 倾斜
    # OpenCV需要定位图像的3个点来计算倾斜效果
    # 这3个点分别是“左上角”点A、“右上角”点B和“左下角”点C
    # OpenCV会根据这3个点的位置变化来计算其他像素的位置变化
    # 因为要保证图像的“平直性”和“平行性”，所以不需要“右下角”的点做第4个参数
    # 右下角这个点的位置根据A、B、C 3点的变化自动计算得出。

    # 让图像倾斜也是需要通过M矩阵实现的，但得出这个矩阵需要做很复杂的运算
    # 于是OpenCV提供了getAffineTransform()方法来自动计算倾斜图像的M矩阵

    # M = cv2.getAffineTransform(src,dst)
    # src：原图3个点坐标，格式位3行2列的32位浮点数列表
    # dst：倾斜图像的3个点坐标，格式与src一样

    img = cv2.imread('zophie.jpg')
    rows = len(img)  # img的行数
    cols = len(img[0])  # img的列数
    p1 = np.zeros((3,2),np.float32)  # 32位浮点类型空列表，原图3个点
    p1[0] = [0,0]   # 左上角点坐标
    p1[1] = [cols-1,0]  # 右上角点坐标
    p1[2] = [0,rows-1]
    p2 = np.zeros((3,2),np.float32)  # 32位浮点类型空列表，倾斜图3个点
    p2[0] = [50,0]
    p2[1] = [cols-1,0]
    p2[2] = [0,rows-1]
    M = cv2.getAffineTransform(p1,p2)
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow('snow',dst)
    cv2.waitKey()


def warpPerspective():
    # 透视
    # 如果说仿射是让图像在二维平面中变形，那么透视就是让图像在三维空间中变形
    # 从不同的角度观察物体，会看到不同的变形画面
    # 例如，矩形会变成不规则的四边形，直角会变成锐角或钝角，圆形会变成椭圆，等等
    # 这种变形之后的画面就是透视图。

    # dst = cv2.warpPerspective(src, M, dsize, flags, borderMode, borderValue)
    # M：一个3行3列的矩阵，根据此矩阵的值变换原图中的像素位置。
    # dsize：输出图像的尺寸大小。
    # 后面默认

    # warpPerspective()方法也需要通过M矩阵计算透视效果
    # 但得出这个矩阵需要做很复杂的运算，于是OpenCV提供了getPerspectiveTransform()方法自动计算M矩阵
    # M = cv2.getPerspectiveTransform(src,dst)
    # src：原图4个点坐标，格式为4行2列的32位浮点数列表，例如：[[0, 0], [1, 0], [0, 1], [1, 1]]
    # dst：透视图的4个点坐标，格式与src一样。
    # 返回值说明：M：getPerspectiveTransform()方法计算出的仿射矩阵

    # m模拟从底部观察图像得到的透视效果，将图像顶部边缘收窄，底部边缘不变
    img = cv2.imread('zophie.jpg')
    hang = len(img)
    lie = len(img[0])
    p1 = np.zeros((4,2),np.float32)
    p1[0] = [0,0]
    p1[1] = [lie-1,0]
    p1[2] = [0,hang-1]
    p1[3] = [lie-1, hang - 1]
    p2 = np.zeros((4, 2), np.float32)  # 32位浮点类型空列表，倾斜图3个点
    p2[0] = [130, 0]
    p2[1] = [lie-130,0]
    p2[2] = [0,hang-1]
    p2[3] = [lie - 1, hang - 1]
    M = cv2.getPerspectiveTransform(p1,p2)
    dst = cv2.warpPerspective(img,M,(lie,hang))
    cv2.imshow('snow',dst)
    cv2.waitKey()




















# resize()
# flip()
# warpAffine()
warpPerspective()
