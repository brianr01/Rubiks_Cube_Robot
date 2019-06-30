import sys
from os import path
import numpy as np
import cv2
#adds images to working directory
sys.path.append(sys.path[0] + '/images')
current_directory = sys.path[0]
parent_directory = path.dirname(current_directory)
sys.path.append(parent_directory)



#external functions needed get_cube_position, get_current_frame, get_current_image_in_lab, turn_side, solve, scramble, change_menu, initiate_quit
class profiles_menu():
    def __init__(self, external_functions):

        back_to_calibrate_button = {'size':[100, 50],
                                            'location':[700, 350],
                                            'color':'white',
                                            'text_color':'black',
                                            'text':'back',
                                            'action':external_functions['change_menu'],
                                            'parameters':'calibrate'}

        quit_button = {'size':[100, 50],
                                    'location':[700, 400],
                                    'color':'red',
                                    'text_color':'black',
                                    'text':'quit',
                                    'action':external_functions['initiate_quit']}

        profiles_menu = {'buttons':[back_to_calibrate_button, quit_button], 'frames':[]}


        self.menu = profiles_menu


