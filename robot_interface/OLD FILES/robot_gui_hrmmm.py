#this module allows easy taking of pictures from multiple cameras
import cv2
import time
import numpy as np
import class_button
import class_frame
import random




import cv2
s_img = cv2.imread("test.gif")
x_offset=0
y_offset = 0



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
    image = np.zeros((450,100,3), np.uint8)
    image[:] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return image

frame = np.zeros((450,800,3), np.uint8)
image = np.zeros((450,250,3), np.uint8)
image[:] = (255, 255, 255)

test_frame = class_frame.frame([0,0], action_to_get_image=get_image)
test_frame2 = class_frame.frame([250,0], action_to_get_image=get_image)
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
main_menu = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10]

main_menu_frames = [test_frame, test_frame2]

def mouse_callback_2(event,x,y,flags,params):
    if (current_button_set == 'main'):
        for button in main_menu:
            button.update((x, y), event)
    elif(current_button_set == 'calibrate'):
        for button in calibrate_menu:
            button.update((x, y), event)
    elif(current_button_set == 'profiles'):
        for button in profiles_menu:
            button.update((x, y), event)

while True:
    cv2.imshow('solver', frame)
    cv2.moveWindow('solver',1920,0)
    frame = np.zeros((450,800,3), np.uint8)

    for menu_frame in main_menu_frames:
        frame = menu_frame.render(frame)
    
    if (current_button_set == 'main'):
        for button in main_menu:
            frame = button.render(frame)
    elif(current_button_set == 'calibrate'):
        for button in calibrate_menu:
            frame = button.render(frame)
    elif(current_button_set == 'profiles'):
        for button in profiles_menu:
            frame = button.render(frame)

    cv2.setMouseCallback('solver', mouse_callback_2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break