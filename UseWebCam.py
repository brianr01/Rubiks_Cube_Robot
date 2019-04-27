#this module allows easy taking of pictures from multiple cameras
import cv2
import time
resolution = [1080,720]
camera0 = cv2.VideoCapture(1)
camera0.set(3,resolution[0])
camera0.set(4,resolution[1])
camera0.set(28,0)
camera1 = cv2.VideoCapture(0)
camera1.set(3,resolution[0])
camera1.set(4,resolution[1])
camera1.set(28,0)

def TakePictures():
    global frame,hsv
    for i in range(0,10):
        ret,frame0 = camera0.read()
        ret,frame1 = camera1.read()
        time.sleep(.001)
    return frame0,frame1

def GetVideoFeed():
    ret,frame0 = camera0.read()
    ret,frame1 = camera1.read()
    return frame0,frame1