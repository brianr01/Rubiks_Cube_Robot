#this module allows easy taking of pictures from multiple cameras\
print('started')
import sys
sys.path.append(sys.path[0] + '/robot_interface')
print(sys.path)


import cv2
import time
import numpy as np
import class_menus

import random
import render_cube




cube_state = {'u':['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9'],
                         'r':['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9'], 
                         'f':['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'],
                         'd':['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9'],
                         'l':['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9'],
                         'b':['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']}
'''
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
'''
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
    global end_loop
    end_loop = True


def set_menu(menu):
    print(menu)
    global current_button_set
    current_button_set = menu

def load_profile(profile_number):
    print('load_profile', profile_number)

def change_menu(menu_name):
    real_menus.set_current_menu(menu_name)

def get_current_and_resize_frame(camera):
    #ret, current_frame = camera.read()
    #scale_percent = 28 # percent of original size
    #width = int(current_frame.shape[1] * scale_percent / 100)
    #height = int(current_frame.shape[0] * scale_percent / 100)
    #dim = (width, height)
    #current_frame = cv2.resize(current_frame, dim, interpolation = cv2.INTER_AREA)
    #return current_frame
    cube = np.zeros((200,266,3), np.uint8)
    cube[:] = (255, 0, 255)
    return cube


def get_lab_color(camera):
    current_frame = get_current_and_resize_frame(camera)
    current_frame =  cv2.cvtColor(current_frame, cv2.COLOR_BGR2Lab)
    return current_frame

frame = np.zeros((450,800,3), np.uint8)

cube = np.zeros((400,266,3), np.uint8)
cube[:] = (255, 255, 255)
cube_segment = {'name':'cube', 'location':[0, 0], 'action_to_get_image':render_cube.render_cube, 'parameters':cube_state}


camera_0_segment = {'name':'upper_camera', 'location':[266, 0], 'action_to_get_image':get_current_and_resize_frame, 'parameters':'cap1'}

upper_camera_special = np.zeros((200,266,3), np.uint8)
upper_camera_special[:] = (0, 100, 255)
camera_0_special_segment = {'name':'upper_camera_special', 'location':[532, 0], 'action_to_get_image':get_lab_color, 'parameters':'cap1'}


camera_1_segment = {'name':'lower_camera', 'location':[266, 200], 'action_to_get_image':get_current_and_resize_frame, 'parameters':'cap'}

lower_camera_special = np.zeros((200,266,3), np.uint8)
lower_camera_special[:] = (255, 100, 0)
camera_1_special_segment = {'name':'lower_camera_special', 'location':[532, 200], 'action_to_get_image':get_lab_color, 'parameters':'cap'}

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
calibrate_acceleration_segment = {'name':'calibration_acceleration', 'location':[266, 200], 'image':calibration_acceleration}

pofile_1 = np.zeros((100,100,3), np.uint8)
pofile_1[:] = (150, 10, 255)
profile_1_segment = {'name':'pofile_1', 'location':[0, 0], 'image':pofile_1}

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

main_menu = {'buttons':[u_button, r_button, f_button, d_button, l_button, b_button, solve_button, scramble_button, calibrate_button, quit_button], 'frames':[cube_segment, camera_0_segment, camera_0_special_segment, camera_1_segment, camera_1_special_segment]}

back_to_main_button = {'size':[120, 50], 'location':[610, 400],'color':'white', 'text_color':'black', 'text':'back', 'action':change_menu, 'parameters':'main'}

polygons_button = {'size':[150, 50], 'location':[0, 400],'color':'red', 'text_color':'white', 'text':'polygons', 'action':change_menu, 'parameters':'polygons'}

colors_button = {'size':[120, 50], 'location':[150, 400],'color':'green', 'text_color':'blue', 'text':'colors', 'action':change_menu, 'parameters':'colors'}

acceleration_button = {'size':[210, 50], 'location':[270, 400],'color':'red', 'text_color':'black', 'text':'acceleration', 'action':change_menu, 'parameters':'acceleration'}

profiles_button = {'size':[130, 50], 'location':[480, 400],'color':'yellow', 'text_color':'black', 'text':'profiles', 'action':change_menu, 'parameters':'profiles'}

calibrate_menu = {'buttons':[back_to_main_button, polygons_button, colors_button, acceleration_button, profiles_button, quit_button], 'frames':[calibrate_upper_polygons_segment, calibrate_lower_polygons_segment, calibrate_colors_segment, calibrate_acceleration_segment]}

back_to_calibrate_button = {'size':[100, 50], 'location':[620, 400], 'color':'white', 'text_color':'black', 'text':'back', 'action':change_menu, 'parameters':'calibrate'}


profiles_1_button = {'size':[150, 50], 'location':[0, 400],'color':'red', 'text_color':'black', 'text':'profile 1', 'action':change_menu, 'parameters':'main'}
profiles_2_button = {'size':[150, 50], 'location':[150, 400],'color':'orange', 'text_color':'black', 'text':'profile 2', 'action':change_menu, 'parameters':'main'}
profiles_3_button = {'size':[150, 50], 'location':[300, 400],'color':'yellow', 'text_color':'black', 'text':'profile 3', 'action':change_menu, 'parameters':'main'}
profiles_4_button = {'size':[150, 50], 'location':[450, 400],'color':'green', 'text_color':'black', 'text':'profile 4', 'action':change_menu, 'parameters':'main'}

profiles_menu = {'buttons':[back_to_calibrate_button, quit_button, profiles_1_button, profiles_2_button, profiles_3_button, profiles_4_button], 'frames':[profile_1_segment]}


acceleration_menu = {'buttons':[back_to_calibrate_button, quit_button], 'frames':[]}

colors_menu = {'buttons':[back_to_calibrate_button, quit_button], 'frames':[]}

polygons_menu = {'buttons':[back_to_calibrate_button, quit_button], 'frames':[]}

menus_data = {'main':main_menu, 'calibrate':calibrate_menu, 'profiles':profiles_menu, 'acceleration':acceleration_menu, 'colors':colors_menu, 'polygons':polygons_menu}

real_menus = class_menus.menus(menus_data, 'main') 

def mouse_callback_2(event,x,y,flags,params):
    global real_menus
    real_menus.update(x,y,event)

print('test')
end_loop = False
while end_loop == False:
    #ret, camera_frame0 = cap.read()
    #ret, camera_frame1 = cap1.read()
    #cv2.imshow('frame0', camera_frame0)
    #cv2.imshow('frame1', camera_frame1)
    cv2.imshow('solver', frame)
    cv2.moveWindow('solver',1920,0)
    frame = np.zeros((450,800,3), np.uint8)
    real_menus.render(frame, {})
    cv2.setMouseCallback('solver', mouse_callback_2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()