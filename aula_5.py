import cv2
import numpy as np

cascade = cv2.CascadeClassifier("frontalface_alt.xml")

video = cv2.VideoCapture(0)

while True:
    retval, frame = video.read()

    face_retas = cascade.detectMultiScale(frame,scaleFactor=1.3,minNeighbors=3)

    for (x,y,w,h) in face_retas:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),5)

        cv2.imshow("rosto",frame)
        chave = cv2.waitKey(1)
        if chave ==27:
            break
video.release()
cv2.destroyAllWindows()