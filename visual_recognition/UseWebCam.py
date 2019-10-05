import numpy as np
import cv2
import sys
from os import path

#adds robot interface to path
sys.path.append(sys.path[0])

use_synthetic_frames = False
resolution = [1920, 1080]

#set up the cameras
print('setting up cameras')
try:
    #set up the video capture
    cap0 = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)

    #sets up the resolution for the first camera
    cap0.set(3, resolution[0])
    cap0.set(4, resolution[1])

    #sets up the resolution for the second camera
    cap1.set(3, resolution[0])
    cap1.set(4, resolution[1])

    #get the frames from the cameras
    ret, frame0 = cap0.read()
    ret, frame1 = cap1.read()

    #test the frames to ensure they show
    cv2.imshow('test', frame0)
    cv2.imshow('test', frame1)
    cv2.destroyAllWindows()
except Exception as error:
    #when a camera is not pluged in swap to synthetic frames
    print('The cameras were not detected.  Switching to synthetic frames')
    frame0 = cv2.imread(sys.path[0] + '/frame0.jpg')
    frame1 = cv2.imread(sys.path[0] + '/frame1.jpg')
    use_synthetic_frames = True

print('finished setting up cameras')

def get_current_frames():
    global frame0, frame1
    if (not use_synthetic_frames):
        ret, frame0 = cap0.read()
        ret, frame1 = cap1.read()
    else:
        frame0 = cv2.imread(sys.path[0] + '/frame0.jpg')
        frame1 = cv2.imread(sys.path[0] + '/frame1.jpg')

    return [frame0, frame1]
