import cv2
import numpy as np
from deepface import DeepFace
import dlib 
import os

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector() 
ret, frame = cap.read()
model_path = f"{os.getcwd()}\BaseModels"

def extract_image(limit1):
    count = 0 
    while count < limit1: 
        cv2.imwrite(f"{model_path}/Model{count}.jpeg", frame)
        count+=1
extract_image(1)

reference_img = cv2.imread(f"{model_path}/Model0.jpeg")

def verfiy(vid): 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = detector(gray) 
    for face in faces:
        try:
            verfiedvalues = DeepFace.verify(vid, reference_img.copy())
            if verfiedvalues['verified']:
                x=verfiedvalues['facial_areas']['img1']["x"]
                y=verfiedvalues['facial_areas']['img1']["y"]
                cv2.putText(frame, "Verfied",(x, y - 1), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)     
            x, y = face.left(), face.top() 
            x1, y1 = face.right(), face.bottom() 
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        except ValueError:
            pass      
while True: 
    ret, frame = cap.read()
    if ret is False: 
        break
    verfiy(frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
