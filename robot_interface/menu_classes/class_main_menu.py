import sys
from os import path
import numpy as np
import cv2
#adds images to working directory
sys.path.append(sys.path[0] + '/images')
current_directory = sys.path[0]
parent_directory = path.dirname(current_directory)
sys.path.append(parent_directory)

faces_to_colors = {'u':(255,255,255), 'f':(0,255,0), 'r':(0,0,255), 'l':(0,100,255), 'd':(0,255,255), 'b':(255,0,0)}
points = {'u':[[87, 58],
               [116, 58],
               [145, 58],
               [87, 87],
               [116, 87],
               [145, 87],
               [87, 116],
               [116, 116],
               [145, 116]],

    'f':
        [[87, 145],
        [116, 145],
        [145, 145],
        [87, 174],
        [116, 174],
        [145, 174],
        [87, 203],
        [116, 203],
        [145, 203]],
    'r':
        [[174, 145],
        [203, 145],
        [232, 145],
        [174, 174],
        [203, 174],
        [232, 174],
        [174, 203],
        [203, 203],
        [232, 203]],
    'l':
        [[0, 145],
        [29, 145],
        [58, 145],
        [0, 174],
        [29, 174],
        [58, 174],
        [0, 203],
        [29, 203],
        [58, 203]],
    'd':
        [[87, 232],
        [116, 232],
        [145, 232],
        [87, 261],
        [116, 261],
        [145, 261],
        [87, 290],
        [116, 290],
        [145, 290]],
    'b':
        [[145, 377],
        [116, 377],
        [87, 377],
        [145, 348],
        [116, 348],
        [87, 348],
        [145, 319],
        [116, 319],
        [87, 319]]}


#external functions needed get_cube_position, get_current_frame, get_current_image_in_lab, turn_side, solve, scramble, change_menu, initiate_quit
class main_menu():
    def __init__(self, external_functions):
        color = (100,5,255)
        current_button_set = 'main'

        cube = np.zeros((400,266,3), np.uint8)
        cube[:] = (255, 255, 255)
        cube_segment = {'name':'cube',
                        'location':[0, 0],
                        'size':[266,400],
                        'action_to_get_image':self.render_cube,
                        'parameters':external_functions['get_cube_state']}

        camera_0_segment = {'name':'upper_camera',
                            'location':[266, 0],
                            'size':[266,200],
                            'action_to_get_image':external_functions['get_current_frame'],
                            'parameters':'0'}

        upper_camera_special = np.zeros((200,266,3), np.uint8)
        upper_camera_special[:] = (0, 100, 255)
        camera_0_special_segment = {'name':'upper_camera_special',
                                    'location':[532, 0],
                                    'size':[266,200],
                                    'action_to_get_image':external_functions['get_current_image_in_lab'],
                                    'parameters':'0'}

        camera_1_segment = {'name':'lower_camera',
                            'location':[266, 200],
                            'size':[266,200],
                            'action_to_get_image':external_functions['get_current_frame'],
                            'parameters':'1'}

        lower_camera_special = np.zeros((200,266,3), np.uint8)
        lower_camera_special[:] = (255, 100, 0)
        camera_1_special_segment = {'name':'lower_camera_special',
                                    'location':[532, 200],
                                    'size':[266,200],
                                    'action_to_get_image':external_functions['get_current_image_in_lab'],
                                    'parameters':'1'}

        u_button = {'size':[50, 50],
                    'location':[0, 400],
                    'color':'white',
                    'text_color':'black',
                    'text':'u',
                    'action':external_functions['turn_side'],
                    'parameters':'u'}

        r_button = {'size':[50, 50],
                    'location':[50, 400],
                    'color':'red',
                    'text_color':'black',
                    'text':'r',
                    'action':external_functions['turn_side'],
                    'parameters':'r'}

        f_button = {'size':[50, 50],
                    'location':[100, 400],
                    'color':'green',
                    'text_color':'black',
                    'text':'f',
                    'action':external_functions['turn_side'],
                    'parameters':'f'}

        d_button = {'size':[50, 50],
                    'location':[150, 400],
                    'color':'yellow',
                    'text_color':'black',
                    'text':'d',
                    'action':external_functions['turn_side'],
                    'parameters':'d'}

        l_button = {'size':[50, 50],
                    'location':[200, 400],
                    'color':'blue',
                    'text_color':'black',
                    'text':'l',
                    'action':external_functions['turn_side'],
                    'parameters':'l'}

        b_button = {'size':[50, 50],
                    'location':[250, 400],
                    'color':'orange',
                    'text_color':'black',
                    'text':'b',
                    'action':external_functions['turn_side'],
                    'parameters':'b'}

        solve_button = {'size':[100, 50],
                        'location':[300, 400],
                        'color':'white',
                        'text_color':'black',
                        'text':'solve',
                        'action':external_functions['solve']}

        scramble_button = {'size':[160, 50],
                           'location':[400, 400],
                           'color':'yellow',
                           'text_color':'black',
                           'text':'scramble',
                           'action':external_functions['scramble']}

        calibrate_button = {'size':[160, 50],
                            'location':[560, 400],
                            'color':'blue',
                            'text_color':'black',
                            'text':'calibrate',
                            'action':external_functions['change_menu'],
                            'parameters':'calibrate'}

        quit_button = {'size':[160, 50],
                       'location':[720, 400],
                       'color':'red',
                       'text_color':'black',
                       'text':'quit',
                       'action':external_functions['initiate_quit']}

        main_menu = {'buttons':[u_button,
                                r_button,
                                f_button,
                                d_button,
                                l_button,
                                b_button,
                                solve_button,
                                scramble_button,
                                calibrate_button,
                                quit_button],
                     'frames':[cube_segment,
                               camera_0_segment,
                               camera_0_special_segment,
                               camera_1_segment,
                               camera_1_special_segment]}

        self.menu = main_menu


    #returns a 266 * 400 frame with the rubik's cube current possition
    def render_cube(self, external_function):
        #creates a 266 * 400 all white frame
        frame = np.zeros((400,266,3), np.uint8)
        frame[:] = (255, 255, 255)

        #gets the cube's current position
        position = external_function()

        #iterates over the cube's position to add all the stickers to the image
        for side in position:
            for sticker_number, sticker in enumerate(position[side]):

                #get the x,y location for printing out the cube
                point_1 = points[side][sticker_number]
                point_2 = [points[side][sticker_number][0] + 29, points[side][sticker_number][1] + 29]

                #add the sticker to the frame
                cv2.rectangle(frame, (point_1[0], point_1[1] - 20) ,(point_2[0], point_2[1] - 20), (0,0,0), -1)
                cv2.rectangle(frame, (point_1[0]+2, point_1[1] - 18) ,(point_2[0]-2, point_2[1] - 22), faces_to_colors[sticker[0]], -1)
        return frame
