import cv2
from tracker import *


cap = cv2.VideoCapture(r"C:\Users\chais\Downloads\video object tracking\highway.mp4")

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)


while True:
    ret, frame = cap.read()
    
    mask = object_detector.apply(frame)
     
    
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()