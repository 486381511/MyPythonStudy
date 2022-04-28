import cv2

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while (video.isOpened()):
    retval,img = video.read()
    faceCascade = cv2.CascadeClassifier('D:\\ceshi\\haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(img, 1.15)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
    cv2.imshow('img', img)
    key = cv2.waitKey(60)
    if key == 32:
        break
video.release()
cv2.destroyAllWindows()





