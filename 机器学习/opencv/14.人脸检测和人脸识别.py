import cv2
import numpy as np

# 人脸识别：提取特征，然后分类

def facecheak():
    # 人脸检测
    # 级联分类器
    # opencv提供一些已经封装好训练好的级联分类器
    # 路径'\\python\Lib\site-package\cv2\data\'

    # openCV实现人脸检测需要做两步操作
    # 1. 加载级联分类器
    # 2. 使用级联分类器

    # 加载级联分类器
    # cascade = cv2.CascadeClassifier(filename)
    # cascade：分类器的对象
    # filename：级联分类器的xml文件名

    # objects = cascade.detectMultiScale(image, scaleFactor, minNeighbors, flags, minSize, maxSize)
    # cascade：已有的分类器对象。
    # image：待分析的图像。
    # scaleFactor：可选参数，扫描图像时的缩放比例。
    # minNeighbors：可选参数，每个候选区域至少保留多少个检测结果才可以判定为人脸。该值越大，分析的误差越小。
    # flags：可选参数，旧版本OpenCV的参数，建议使用默认值。
    # minSize：可选参数，最小的目标尺寸。
    # maxSize：可选参数，最大的目标尺寸。
    # objects：捕捉到的目标区域数组，数组中每一个元素都是一个目标区域，每一个目标区域都包含4个值
    # 分别是：左上角点横坐标、左上角点纵坐标、区域宽、区域高
    # object：格式为[[244 203 111 111] [432 81 113 113]]


    # 分类人脸位置
    img = cv2.imread('img\\me.jpg')
    x,y,c = img.shape
    img = cv2.resize(img,dsize=None,fy=0.5,fx=0.5)
    faceCascade = cv2.CascadeClassifier('cascades\\haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(img,2.55)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
    cv2.imshow('img',img)
    cv2.waitKey()
    # 调用其他级联分类器大差不差



# OpenCV提供了三种人脸识别方法Eigenfaces，Fisherfaces和LBPH
# 这三种方法都是通过对比样本的特征最终实现人脸识别
# 每种人脸识别方法都提供了创建识别器，训练识别器，识别三种方法

def LBPH():
    # 特征脸

    # 创建LBPH人脸识别器
    # recognizer = cv2.face.LBPHFaceRecognizer_create()

    # recognizer.train(src,labels)
    # src：用于训练的人脸图像样本列表，格式为list，样本必须宽、高一样
    # labels：样本对应的标签，格式为数组，元素类型为整数
    # 数组长度必须与样本列表长度相同。样本与标签按照插入顺序一一对应

    # 训练识别器后可以通过识别器的predict()
    # 方法识别人脸，该方法对比样本的特征，给出最相近的结果和评分，其语法如下：
    # label, confidence = recognizer.predict(src)
    # recognizer：已有的Eigenfaces人脸识别器对象
    # src：需要识别的人脸图像，该图像宽、高必须与样本一致
    # label：与样本匹配程度最高的标签值。
    # confidence：匹配程度最高的信用度评分。评分小于5000匹配程度较高，0分表示2幅图像完全一样。

    photos = list()     # 样本列表
    lables = list()     # 标签列表
    for i in range(1,10):
        photos.append(cv2.imread('D:\\ceshi\\train\\'+str(i)+'.jpg',0))
        lables.append(0)
    name = {'0':'lym'}
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(photos,np.array(lables))

    me = cv2.imread('img\\me.jpg',0)
    lable, confidence = recognizer.predict(me)
    print('confidence='+str(confidence))
    print(name[str(lable)])
    print(len(lables))
    print(len(photos))

    # 还有Fisherfaces人脸识别器
    # 调用方法与使用方法大差不差



LBPH()









