import cv2
import numpy as np
image=cv2.imread('123.jpg') #读取图片
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #检测人脸
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #颜色空间转换
faces=face.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(5,5))
print(faces)
print('发现{0}个人脸！'.format((len(faces))))
for(x,y,z,w) in faces:
    # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    cv2.circle(image,int((x+x+w)/2),int((y+y+h)/2),int(w/2),(0,255,0),2)
cv2.imshow('dect',image)
cv2.imwrite('renlian.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
