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
class acceleration_menu():
    def __init__(self, external_functions):

        back_to_calibrate_button = {'size':[150, 300],
                                    'location':[930, 1621],
                                    'color':'white',
                                    'text_color':'black',
                                    'text':'back',
                                    'action':external_functions['change_menu'],
                                    'parameters':'calibrate'}

        #not currently used
        quit_button = {'size':[100, 50],
                                    'location':[700, 400],
                                    'color':'red',
                                    'text_color':'black',
                                    'text':'quit',
                                    'action':external_functions['initiate_quit']}

        calibrate_acceleration_segment = {'name':'calibration_acceleration',
                                          'location':[0, 0],
                                          'size':[1600,1080],
                                          'action_to_get_image':self.draw_base_graph}

        acceleration_menu = {'buttons':[back_to_calibrate_button], 'frames':[calibrate_acceleration_segment]}

        self.menu = acceleration_menu

    def draw_base_graph(self):
        image = np.zeros((1600, 1080, 3),  np.uint8)
        image[:] = (100, 100, 100)
        for i in range(0, 50):
            cv2.rectangle(image, (0, i * 32 + 10), (1080, i * 32 + 15) , (0,0,0), -1)
            cv2.rectangle(image, (0, i * 32 + 12), (1080, i * 32 + 13) , (100,0,255), -1)

        for i in range(0, 34):
            cv2.rectangle(image, (i * 32 + 11, 0), (i * 32 + 14, 1800) , (0,0,0), -1)
            cv2.rectangle(image, (i * 32 + 12, 0), (i * 32 + 13, 1800) , (255,0,100), -1)

        graph = [[0,0], [10,10], [50,0]]

        previous_point = None
        for point in graph:
            if previous_point != None:
                cv2.circle(image, (point[1], point[0]), 5, (255, 255, 255), 5)

            previous_point = point

        return image
