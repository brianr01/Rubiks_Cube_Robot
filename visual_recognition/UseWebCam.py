import numpy as np
import cv2

print('setting up cameras')
cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
print('finished setting up cameras')

def get_current_frames():
    ret, frame0 = cap.read()
    ret, frame1 = cap1.read()
    return [frame0, frame1]