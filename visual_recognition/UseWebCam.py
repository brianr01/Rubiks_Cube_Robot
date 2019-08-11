import numpy as np
import cv2

use_synthetic_frames = False

#set up the cameras
print('setting up cameras')
try:
    #set up the video capture
    cap0 = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)
    
    #get the frames from the cameras
    ret, frame0 = cap0.read()
    ret, frame1 = cap1.read()
    
    #test the frames to ensure they show
    cv2.imshow('test', frame0)
    cv2.imshow('test', frame1)
except Exception as error:
    #when a camera is not pluged in swap to synthetic frames
    print('The cameras were not detected.  Switching to synthetic frames')
    frame0 = cv2.imread('frame1.jpg')
    frame1 = cv2.imread('frame2.jpg')
    use_synthetic_frames = True

print('finished setting up cameras')                        

def get_current_frames():
    global frame0, frame1
    if (not use_synthetic_frames):
        ret, frame0 = cap0.read()
        ret, frame1 = cap1.read()
        
    return [frame0, frame1]
