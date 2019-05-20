#this module allows easy taking of pictures from multiple cameras\
print('started')
import cv2
import time
import numpy as np
import class_menus
import random

print('imported')
x_offset=0
y_offset = 0

cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 720)

print('setup camera0')


cap1 = cv2.VideoCapture(1)
cap1.set(3, 960)
cap1.set(4, 720)

print('setup camera1')

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

def change_menu(menu_name):
    real_menus.set_current_menu(menu_name)

def get_current_and_resize_frame(camera):
    ret, current_frame = camera.read()
    scale_percent = 28 # percent of original size
    width = int(camera_frame0.shape[1] * scale_percent / 100)
    height = int(camera_frame0.shape[0] * scale_percent / 100)
    dim = (width, height)
    current_frame = cv2.resize(current_frame, dim, interpolation = cv2.INTER_AREA)
    return current_frame

frame0 = {'name':'', 'location':[0,0], 'image':, 'action_to_get_image':None , 'parameters':None}
button1 = {'size':[50, 50], 'location':[0, 400],'color':'white', 'text_color':'black', 'text':'u', 'action':change_menu, 'parameters':'second'}
main_menu = {'frames':[frame0], 'buttons':[button1, button2, button3]}
menus = {'main':main_menu, 'second':second_menu}
real_menus = class_menus.menus(menus, 'main')


frame = np.zeros((450,800,3), np.uint8)

cube = np.zeros((400,266,3), np.uint8)
cube[:] = (255, 255, 255)
frame0 = {([0,0], image=cube)}


camera_0_segment = {'name':'upper_camera', 'location':[226, 0], 'action_to_get_image':get_current_and_resize_framene , 'parameters':cap1}

upper_camera_special = np.zeros((200,266,3), np.uint8)
upper_camera_special[:] = (0, 100, 255)
camera_0_special_segment = {'name':'upper_camera_special', 'location':[532, 0], 'image':upper_camera_special}


camera_1_segment = {'name':'', 'location':[266, 200], 'action_to_get_image':get_current_and_resize_frame , 'parameters':cap}

lower_camera_special = np.zeros((200,266,3), np.uint8)
lower_camera_special[:] = (255, 100, 0)
camera_1_special_segment = {'name':'lower_camera_special', 'location':[532, 200], 'image':lower_camera_special}

calibration_polygons_upper = np.zeros((200,266,3), np.uint8)
calibration_polygons_upper[:] = (255, 100, 0)
calibrate_upper_polygons_segment = {'name':'calibration_polygons_upper', 'location':[0, 0], 'image':calibration_polygons_upper}

calibration_polygons_lower = np.zeros((200,266,3), np.uint8)
calibration_polygons_lower[:] = (0, 255, 0)
calibrate_lower_polygons_segment = {'name':'calibration_polygons_lower', 'location':[0, 200], 'image':calibration_polygons_lower}

calibration_colors = np.zeros((200,532,3), np.uint8)
calibration_colors[:] = (0, 255, 255)
calibrate_colors_segment = {'name':'calibration_colors', 'location':[266, 0], 'image':calibration_colors}

calibration_acceleration = np.zeros((200,532,3), np.uint8)
calibration_acceleration[:] = (150, 10, 255)
frame7 = {'name':'calibration_acceleration', 'location':[266, 200], 'image':calibration_acceleration}

pofile_1 = np.zeros((100,100,3), np.uint8)
pofile_1[:] = (150, 10, 255)
frame8 = {'name':'pofile_1', 'location':[0, 0], 'image':pofile_1}

color = (100,5,255)
current_button_set = 'main'

u_button = {'size':[50, 50], 'location':[0, 400],'color':'white', 'text_color':'black', 'text':'u', 'action':turn_side, 'parameters':'u'}

r_button = {'size':[50, 50], 'location':[50, 400],'color':'red', 'text_color':'black', 'text':'r', 'action':turn_side, 'parameters':'r'}

f_button = {'size':[50, 50], 'location':[100, 400],'color':'green', 'text_color':'black', 'text':'f', 'action':turn_side, 'parameters':'f'}

d_button = {'size':[50, 50], 'location':[150, 400],'color':'yellow', 'text_color':'black', 'text':'d', 'action':turn_side, 'parameters':'d'}

l_button = {'size':[50, 50], 'location':[200, 400],'color':'blue', 'text_color':'black', 'text':'l', 'action':turn_side, 'parameters':'l'}

b_button = {'size':[50, 50], 'location':[250, 400],'color':'orange', 'text_color':'black', 'text':'b', 'action':turn_side, 'parameters':'b'}

solve_button = {'size':[100, 50], 'location':[300, 400],'color':'white', 'text_color':'black', 'text':'solve', 'action':solve}

scramble_button = {'size':[160, 50], 'location':[400, 400],'color':'yellow', 'text_color':'black', 'text':'scramble', 'action':scramble}

calibrate_button = {'size':[160, 50], 'location':[560, 400],'color':'blue', 'text_color':'black', 'text':'calibrate', 'action':change_menu, 'parameters':'calibrate'}

quit_button = {'size':[160, 50], 'location':[720, 400],'color':'red', 'text_color':'black', 'text':'quit', 'action':initiate_quit}

main_menu = {'buttons':[button1, button2, button3, button4, button5, button6, button7, button8, button9, button10], 'frames':[frame0, frame1, frame2, frame3, frame4]}

back_to_main_button = {'size':[100, 50], 'location':[620, 400],'color':'white', 'text_color':'black', 'text':'back', 'action':change_menu 'parameters':'main'}

polygons_button = {'size':[100, 50], 'location':[620, 400],'color':'red', 'text_color':'white', 'text':'polygons', 'action':change_menu 'parameters':'main'}

colors_button = {'size':[100, 50], 'location':[620, 400],'color':'green', 'text_color':'blue', 'text':'colors', 'action':change_menu 'parameters':'main'}

acceleration_button = {'size':[210, 50], 'location':[270, 400],'color':'red', 'text_color':'black', 'text':'acceleration', 'action':change_menu 'parameters':'main'}

profiles_button = {'size':[210, 50], 'location':[270, 400],'color':'yellow', 'text_color':'black', 'text':'profiles', 'action':change_menu 'parameters':'profiles'}

calibrate_menu = {'buttons':[button15, button14, button13, button12, button11, button10], 'frames':[frame5, frame6, frame7, frame8]}

back_to_calibrate_button = {'size':[100, 50], 'location':[620, 400], 'color':'white', 'text_color':'black', 'text':'back', 'action':change_menu 'parameters':'calibrate'}
profiles_menu = {'buttons':[button16, button10], 'frames':[frame9]}
menus = {'main':main_menu, 'calibrate':calibrate_menu, 'profiles':profiles_menu}

def mouse_callback_2(event,x,y,flags,params):
    for button in menus[current_button_set]['buttons']: 
            button.update((x, y), event)

while True:
    ret, camera_frame0 = cap.read()
    ret, camera_frame1 = cap1.read()
    cv2.imshow('frame0', camera_frame0)
    cv2.imshow('frame1', camera_frame1)
    cv2.imshow('solver', frame)
    cv2.moveWindow('solver',1920,0)
    frame = np.zeros((450,800,3), np.uint8)
    for button in menus[current_button_set]['buttons']:
        frame = button.render(frame)

    for menu_frame in menus[current_button_set]['frames']:
        frame = menu_frame.render(frame)
    cv2.setMouseCallback('solver', mouse_callback_2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break