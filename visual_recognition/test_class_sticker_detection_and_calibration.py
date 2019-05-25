#test for class_sticker_detection_and_calibration

import class_sticker_detection_and_calibration
import cv2
import numpy as np
image = cv2.imread('cube.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

mask = cv2.inRange(image, (0,0,0), (255, 255, 100))
#print(np.count_nonzero(mask))
blue_polygon = [[0, 0],
[3, 0],
[3, 3],
[0, 3]]
sticker = class_sticker_detection_and_calibration.Sticker_Detection_And_Calibration()
sticker.calibration_polygon_points = [[55, 44],[79, 42],[76, 58],[46, 58]]
sticker.calibrate_color(image, 'r')
sticker.calibration_polygon_points = blue_polygon
sticker.calibrate_color(image, 'f')
sticker.calibrate_color(image, 'u')
sticker.calibrate_color(image, 'd')
sticker.calibrate_color(image, 'l')
sticker.calibrate_color(image, 'b')
print(sticker.thresholds)

print(sticker.get_color(image, [[55, 44],[79, 42],[76, 58],[46, 58]]))


print('done')