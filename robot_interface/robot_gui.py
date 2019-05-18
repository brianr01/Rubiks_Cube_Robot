#this module allows easy taking of pictures from multiple cameras\
print('started')
import cv2
import time
import numpy as np
import class_button
import class_frame
import random
#import UseWebCam

print('imported')
x_offset=0
y_offset = 0

cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

def turn_side(side):
    print('turned side', side)

def solve():
    print('solve')

def scramble():
    print('scramble')

def calibrate():
    global current_button_set
    current_button_set = 2

def initiate_quit():
    print('initate_quit')

def set_menu(menu):
    print(menu)
    global current_button_set
    current_button_set = menu

def load_profile(profile_number):
    print('load_profile', profile_number)


def get_image():
    image = np.zeros((10,800,3), np.uint8)
    image[:] = (55, 34, 255)
    return image

frame = np.zeros((450,800,3), np.uint8)

cube = np.zeros((400,266,3), np.uint8)
cube[:] = (255, 255, 255)
frame0 = class_frame.frame([0,0], image=cube)

upper_camera = np.zeros((200,266,3), np.uint8)
upper_camera[:] = (255, 0, 255)
frame1 = class_frame.frame([266,0], image=upper_camera)

upper_camera_special = np.zeros((200,266,3), np.uint8)
upper_camera_special[:] = (0, 100, 255)
frame2 = class_frame.frame([532,0], image=upper_camera_special)

lower_camera = np.zeros((200,266,3), np.uint8)
lower_camera[:] = (255, 0, 10)
frame3 = class_frame.frame([266,200], image=lower_camera)

lower_camera_special = np.zeros((200,266,3), np.uint8)
lower_camera_special[:] = (255, 100, 0)
frame4 = class_frame.frame([532,200], image=lower_camera_special)

calibration_polygons_upper = np.zeros((200,266,3), np.uint8)
calibration_polygons_upper[:] = (255, 100, 0)
frame5 = class_frame.frame([0,0], image=calibration_polygons_upper)

calibration_polygons_lower = np.zeros((200,266,3), np.uint8)
calibration_polygons_lower[:] = (0, 255, 0)
frame6 = class_frame.frame([0,200], image=calibration_polygons_lower)

calibration_colors = np.zeros((200,532,3), np.uint8)
calibration_colors[:] = (0, 255, 255)
frame7 = class_frame.frame([266, 0], image=calibration_colors)

calibration_acceleration = np.zeros((200,532,3), np.uint8)
calibration_acceleration[:] = (150, 10, 255)
frame8 = class_frame.frame([266, 200], image=calibration_acceleration)

pofile_1 = np.zeros((100,100,3), np.uint8)
pofile_1[:] = (150, 10, 255)
frame9 = class_frame.frame([0, 0], image=pofile_1)

color = (100,5,255)
current_button_set = 'main'

button1 =class_button.button([50, 50], [0, 400], (255, 255, 255), (0, 0, 0), 'u', turn_side, parameters = 'u')
button2 = class_button.button([50, 50], [50, 400], (0, 19, 235), (0, 0, 0),  'r', turn_side, parameters = 'r')
button3 = class_button.button([50, 50], [100, 400], (0, 255, 10), (0, 0, 0),  'f', turn_side, parameters = 'f')
button4 = class_button.button([50, 50], [150, 400], (66, 244, 235), (0, 0, 0),  'd', turn_side, parameters = 'd')
button5 = class_button.button([50, 50], [200, 400], (255, 10, 0), (0, 0, 0),  'l', turn_side, parameters = 'l')
button6 = class_button.button([50, 50], [250, 400], (0, 150, 255), (0, 0, 0),  'b', turn_side, parameters = 'b')
button7 = class_button.button([100, 50], [300, 400], (255, 255, 255), (0, 0, 0),  'solve', solve)
button8 = class_button.button([160, 50], [400, 400], (35, 60, 255), (0, 0, 0),  'scramble', scramble)
button9 = class_button.button([160, 50], [560, 400], (255, 60, 0), (0, 0, 0),  'calibrate', set_menu, parameters = 'calibrate')
button10 = class_button.button([160, 50], [720, 400], (0, 10, 255), (0, 0, 0),  'quit', initiate_quit)
main_menu = {'buttons':[button1, button2, button3, button4, button5, button6, button7, button8, button9, button10], 'frames':[frame0, frame1, frame2, frame3, frame4]}

button11 = class_button.button([100, 50], [620, 400], (255, 255, 255), (0, 0, 0),  'back', set_menu, parameters = 'main')
button12 = class_button.button([150, 50], [0, 400], (10, 20, 150), (0, 0, 0),  'polygons', set_menu, parameters = 'main')
button13 = class_button.button([120, 50], [150, 400], (0, 255, 0), (255, 0, 0),  'colors', set_menu, parameters = 'main')
button14 = class_button.button([210, 50], [270, 400], (255, 0, 0), (0, 0, 0),  'acceleration', set_menu, parameters = 'main')
button15 = class_button.button([140, 50], [480, 400], (255, 150, 0), (0, 0, 0),  'profiles', set_menu, parameters = 'profiles')
calibrate_menu = {'buttons':[button15, button14, button13, button12, button11, button10], 'frames':[frame5, frame6, frame7, frame8]}


button16 = class_button.button([100, 50], [620, 400], (255, 255, 255), (0, 0, 0),  'back', set_menu, parameters = 'calibrate')
profiles_menu = {'buttons':[button16, button10], 'frames':[frame9]}
menus = {'main':main_menu, 'calibrate':calibrate_menu, 'profiles':profiles_menu}

def mouse_callback_2(event,x,y,flags,params):
    for button in menus[current_button_set]['buttons']: 
            button.update((x, y), event)

while True:
    ret, camera_frame0 = cap.read()
    ret, camera_frame1 = cap1.read()
    #scale_percent = 13 # percent of original size
    #width = int(camera_frame0.shape[1] * scale_percent / 100)
    #height = int(camera_frame0.shape[0] * scale_percent / 100)
    #dim = (width, height)
    # resize image
    #camera_frame0 = cv2.resize(camera_frame0, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow('frame0', camera_frame0)
    cv2.imshow('frame1', camera_frame1)
    cv2.imshow('solver', frame1)
    #cv2.moveWindow('solver',1920,0)
    frame = np.zeros((450,800,3), np.uint8)
    for button in menus[current_button_set]['buttons']:
        frame = button.render(frame)

    for menu_frame in menus[current_button_set]['frames']:
        frame = menu_frame.render(frame)
    cv2.setMouseCallback('solver', mouse_callback_2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break