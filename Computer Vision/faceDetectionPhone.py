import os
import cv2
import numpy as np

url = "http://192.168.1.8:8080/video"
cp = cv2.VideoCapture(url)
cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier('face_detection.xml')
faceCascade = cv2.CascadeClassifier(cascPath)

while True:
    camera, frame = cp.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if frame is not None:
        cv2.imshow("Frame", frame)

    q = cv2.waitKey(1)
    if q and 0xFF==ord('q'):
        break

cp.release()  
cv2.destroyAllWindows()