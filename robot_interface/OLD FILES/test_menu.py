#this module allows easy taking of pictures from multiple cameras\
print('started')
import cv2
import numpy as np
import class_menu

def turn_side(side):
    print(side)

#cap = cv2.VideoCapture(0)

def get_current_and_resize_frame(camera):
    ret, current_frame = camera.read()
    scale_percent = 28 # percent of original size
    width = int(current_frame.shape[1] * scale_percent / 100)
    height = int(current_frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    current_frame = cv2.resize(current_frame, dim, interpolation = cv2.INTER_AREA)
    return current_frame


frame = np.zeros((450,800,3), np.uint8)

cube = np.zeros((400,266,3), np.uint8)
cube[:] = (255, 255, 255)

frame0 = {'name':'cube', 'location':[0,0], 'image':cube, 'action_to_get_image':None , 'parameters':None}

color = (100,5,255)
current_button_set = 'main'
button1 = {'size':[50, 50], 'location':[0, 400],'color':'white', 'text_color':'black', 'text':'u', 'action':turn_side, 'parameters':'u'}
button2 = {'size':[50, 50], 'location':[50, 400], 'color':'blue', 'text_color':'black', 'text':'r', 'action':turn_side, 'parameters':'r'}
button3 = {'size':[50, 50], 'location':[100, 400], 'color':'red', 'text_color':'black', 'text':'r', 'action':turn_side, 'parameters':'r'}



main_menu = class_menu.menu([frame0], [button1, button2, button3])



def mouse_callback_2(event,x,y,flags,params):
    global main_menu
    main_menu.update(x, y, event)

while True:
    frame = np.zeros((450,800,3), np.uint8)
    frame = main_menu.render(frame, {})
    cv2.imshow('frame', frame)

    cv2.setMouseCallback('frame', mouse_callback_2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break