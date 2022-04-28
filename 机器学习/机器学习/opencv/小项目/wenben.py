import numpy as np
import cv2

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

lower = np.array([0, 0, 221])
upper = np.array([180, 30, 255])

while (video.isOpened()):
    retval,img = video.read()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img = cv2.inRange(hsv, lower, upper)
    cv2.imshow('123', img)
    key = cv2.waitKey(60)
    if key == 32:
        break

