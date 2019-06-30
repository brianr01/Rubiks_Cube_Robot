import sys
from os import path
import cv2
import numpy as np

self.reference_image_sticker_points = {'u':[[0, 0], [0, 10],  [0, 20],  [0, 30],  [0, 40],  [0, 50],  [0, 60],  [0, 70],  [0, 80]],
                                       'f':[[10, 0], [10, 10],  [10, 20],  [10, 30],  [10, 40],  [10, 50],  [10, 60],  [10, 70],  [10, 80]],
                                       'r':[[20, 0], [20, 10],  [20, 20],  [20, 30],  [20, 40],  [20, 50],  [20, 60],  [20, 70],  [20, 80]], 
                                       'd':[[30, 0], [30, 10],  [30, 20],  [30, 30],  [30, 40],  [30, 50],  [30, 60],  [30, 70],  [30, 80]],
                                       'l':[[40, 0], [40, 10],  [40, 20],  [40, 30],  [40, 40],  [40, 50],  [40, 60],  [40, 70],  [40, 80]],
                                       'b':[[50, 0], [50, 10],  [50, 20],  [50, 30],  [50, 40],  [50, 50],  [50, 60],  [50, 70],  [50, 80]]}


#adds images to working directory
sys.path.append(sys.path[0] + '/images')

#this class generates and scales the images with polygons and also generates the reference image
class polygon_calibration_image_manager():
    def __init__(self, reference_image_size):
        self.reference_image = cv2.imread('cube_reference_image.jpeg')
        cv2.imshow('frame', self.reference_image)
        cv2.waitKey(0)
        self.reference_image_size = reference_image_size
        self.current_side = 'u'
        self.current_address = 1

    def get_reference_image(self):
        self.render_sticker_selectors()

    def set_current_polygon(self, new_current_polygon):
        pass

    def render_sticker_selectors(self):
        for sticker in 

    def render_sticker_selector(self, image, point, selected):
        cv2.circle(image,(point[0], point[1]), 10, (255,255,255), -1)
        if (selected == True):
            cv2.circle(image,(point[0], point[1]), 8, (100,200,0), -1)
        else:
            cv2.circle(image,(point[0], point[1]), 8, (0,0,0), -1)

        return image


test_instance = polygon_calibration_image_manager([100,100])