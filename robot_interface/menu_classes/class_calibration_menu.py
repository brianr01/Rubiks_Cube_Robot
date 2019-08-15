import sys
from os import path
import numpy as np
import cv2
import random
import pprint
#adds images to working directory
sys.path.append(sys.path[0] + '/images')
current_directory = sys.path[0]
parent_directory = path.dirname(current_directory)
sys.path.append(parent_directory)



#external functions needed get_cube_position, get_current_frame, get_current_image_in_lab, turn_side, solve, scramble, change_menu, initiate_quit
class calibration_menu():
    def __init__(self, external_functions):
        #frames
        calibrate_upper_polygons_segment = {'name':'calibrate_upper_polygons',
                                       'location':[0, 0],
                                       'size':[607,1080],
                                       'action_to_get_image':self.draw_polygons,
                                       'parameters':{'current_frame_function':external_functions['get_current_frame'], 'polygons_function':external_functions['get_polygon_points'], 'current_camera_number':1}}

        calibrate_lower_polygons_segment = {'name':'calibrate_lower_polygons',
                                       'location':[0, 607],
                                       'size':[607,1080],
                                       'action_to_get_image':self.draw_polygons,
                                       'parameters':{'current_frame_function':external_functions['get_current_frame'], 'polygons_function':external_functions['get_polygon_points'], 'current_camera_number':0}}

        calibrate_colors_segment = {'name':'calibration_colors',
                                    'location':[0, 1214],
                                    'size':[100,1080],
                                    'action_to_get_image':self.render_colors_calibration,
                                    'parameters':{'get_colors_function':external_functions['get_colors_calibration']}}

        calibrate_acceleration_segment = {'name':'calibration_acceleration',
                                          'location':[266, 200],
                                          'size':[532,200],
                                          'action_to_get_image':self.render_acceleration_calibration,
                                          'parameters':external_functions['get_acceleration_calibration']}

        #buttons
        back_to_main_button = {'size':[120, 50],
                               'location':[610, 400],
                               'color':'white',
                               'text_color':'black',
                               'text':'back',
                               'action':external_functions['change_menu'],
                               'parameters':'main'}

        polygons_button = {'size':[150, 50],
                           'location':[0, 400],
                           'color':'red',
                           'text_color':'white',
                           'text':'polygons',
                           'action':external_functions['change_menu'],
                           'parameters':'polygons'}

        colors_button = {'size':[120, 50],
                         'location':[150, 400],
                         'color':'green',
                         'text_color':'blue',
                         'text':'colors',
                         'action':external_functions['change_menu'],
                         'parameters':'colors'}

        acceleration_button = {'size':[210, 50],
                               'location':[270, 400],
                               'color':'red',
                               'text_color':'black',
                               'text':'acceleration',
                               'action':external_functions['change_menu'],
                               'parameters':'acceleration'}

        profiles_button = {'size':[130, 50],
                           'location':[480, 400],
                           'color':'yellow',
                           'text_color':'black',
                           'text':'profiles',
                           'action':external_functions['change_menu'],
                           'parameters':'profiles'}

        quit_button = {'size':[160, 50],
                       'location':[720, 400],
                       'color':'red', 
                       'text_color':'black', 
                       'text':'quit', 
                       'action':external_functions['initiate_quit']}

        #frames and buttons
        calibration_menu = {'buttons':[back_to_main_button,
                                     polygons_button, colors_button,
                                     acceleration_button,
                                     profiles_button,
                                     quit_button], 
                          'frames':[calibrate_upper_polygons_segment,
                                    calibrate_lower_polygons_segment,
                                    calibrate_colors_segment,
                                    calibrate_acceleration_segment]}
        self.menu = calibration_menu

    def draw_polygons(self, parameters):
            sides_dictionary = {1:'bur', 0:'fdl'}
            current_camera = parameters['current_camera_number']
            current_frame = parameters['current_frame_function'](current_camera)
            polygons = []
            for side in sides_dictionary[current_camera]:
                polygons += parameters['polygons_function'](side_to_get=side)

            self.new_frame = current_frame
            for polygon in polygons:
                    polygon = np.array(polygon,np.int32)
                    polygon = polygon.reshape((-1,1,2))
                    self.new_frame = cv2.fillConvexPoly(self.new_frame, polygon, (255,255,255), 10)
                    self.new_frame = cv2.polylines(self.new_frame, polygon, True, (90,255,0), 5)

            return self.new_frame

    def render_acceleration_calibration(self, get_acceleration_calibration):
        acceleration_calibration = get_acceleration_calibration()
        return cv2.imread(sys.path[0] + '/acceleration_placeholder.png')

    def convert_color_from_lab_to_bgr(self, color):
        input = color
        input = np.uint8([[input]])
        input = cv2.cvtColor(input, cv2.COLOR_LAB2BGR)
        input = (int(input[0][0][0]), int(input[0][0][1]), int(input[0][0][2]))
        return color


    def render_colors_calibration(self, parameters, height =  200, width = 532):
        cube_colors = parameters['get_colors_function']()
        image = np.zeros((height, width, 3),  np.uint8)
        image[:] = (100, 100, 100)
        
        x_width = int((532 - (532 % 36)) / 36)
        y_width = int(x_width * (width / height))
        y_width = int(x_width * 1.6)

        x_current = int((532 % 36)/6)
        
        for face in cube_colors:
            cube_faces = cube_colors[face]

            for side in cube_faces:
                cube_side = cube_faces[side]
                y_current = int(y_width / 3)
                z = 0
                for sticker in range(0, len(cube_side)):
                    limit = cube_side[sticker]

                    upper_limit = limit['upper_limit']
                    lower_limit = limit['lower_limit']

##                    upper_limit = cv2.cvtColor( np.uint8([[upper_limit_b]]) , cv2.COLOR_LAB2BGR)[0][0]
##
##                    lower_limit = cv2.cvtColor( np.uint8([[lower_limit_b]]) , cv2.COLOR_LAB2BGR)[0][0]
                    upper_limit = (int(upper_limit[0]), int(upper_limit[1]), int(upper_limit[2]))
                    lower_limit = (int(lower_limit[0]), int(lower_limit[1]), int(lower_limit[2]))
                    
                    cv2.rectangle(image, (x_current, y_current), (x_current + 10, y_current + 10) , upper_limit, -1)
                    cv2.rectangle(image, (x_current+6, y_current), (x_current + 12, y_current+10),  lower_limit, -1)
                    
                    y_current += y_width

                x_current += x_width
            x_current += int(x_width / 3)



        # cv2.rectangle(image, (x0, y0), (x1, y1) ,(b, r, g),-1)

    # 18x54
        return image  