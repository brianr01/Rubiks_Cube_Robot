import cv2
import pickle
import time
import numpy as np


def display_calibration(thresholds, height = 200, width = 532):
    image = np.zeros((width, height, 3), np.uint8)
    image[:] = (255, 255, 50)



    return image       
      
image = display_calibration(0)          
while True:
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  