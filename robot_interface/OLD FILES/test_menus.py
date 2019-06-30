
import numpy as np
import cv2
import sys
sys.path.append(sys.path[0] + '/menu_classes')
import class_menus

def turn_side(side):
    print(side)


def change_menu(menu_name):
    real_menus.set_current_menu(menu_name)

def event_handler(x,y,event):
    if (event == 1):
        print(x,y)


cube = np.zeros((400,266,3), np.uint8)
cube[:] = (255, 255, 255)

frame0 = {'name':'cube', 'location':[0,0], 'size':[400, 266], 'image':cube, 'action_to_get_image':None , 'parameters':None}

button1 = {'size':[50, 50], 'location':[0, 400],'color':'white', 'text_color':'black', 'text':'u', 'action':change_menu, 'parameters':'second'}
button2 = {'size':[50, 50], 'location':[50, 400], 'color':'blue', 'text_color':'black', 'text':'r', 'action':turn_side, 'parameters':'r'}
button3 = {'size':[50, 50], 'location':[100, 400], 'color':'red', 'text_color':'black', 'text':'r', 'action':turn_side, 'parameters':'r'}

main_menu = {'frames':[frame0], 'buttons':[button1, button2, button3]}

cube2 = np.zeros((400,266,3), np.uint8)
cube2[:] = (0, 255, 255)
frame0 = {'name':'cube', 'location':[100,200], 'size':[100, 100], 'image':cube2, 'action_on_event':event_handler, 'action_to_get_image':None , 'parameters':None}

button1 = {'size':[50, 50], 'location':[0, 400],'color':'green', 'text_color':'black', 'text':'u', 'action':change_menu, 'parameters':'main'}
button2 = {'size':[50, 50], 'location':[50, 400], 'color':'yellow', 'text_color':'black', 'text':'r', 'action':turn_side, 'parameters':'r'}
button3 = {'size':[50, 50], 'location':[100, 400], 'color':'red', 'text_color':'black', 'text':'r', 'action':turn_side, 'parameters':'r'}

second_menu = {'frames':[frame0], 'buttons':[button1, button2, button3]}


menus = {'main':main_menu, 'second':second_menu}

real_menus = class_menus.menus(menus, 'main')
5


def mouse_callback_2(event,x,y,flags,params):
    global real_menus
    real_menus.update(x, y, event)

while True:
    frame = np.zeros((450,800,3), np.uint8)

    frame = real_menus.render(frame,{})
    cv2.imshow('frame', frame)

    cv2.setMouseCallback('frame', mouse_callback_2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break