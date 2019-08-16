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
class colors_menu():
    def __init__(self, external_functions):

        upper_polygons__segment = {'name':'calibration_polygons_upper',
                                            'location':[0, 0],
                                            'size':[607,1080],
                                            'action_to_get_image':self.draw_polygons,
                                            'parameters':{'current_frame_function':external_functions['get_current_frame'], 'polygons_function':external_functions['get_polygon_points'], 'current_camera_number':0, 'side_to_get':'f'},
                                            }

        lower_polygons_segment = {'name':'calibration_polygons_lower',
                                            'location':[0, 607],
                                            'size':[607,1080],
                                            'action_to_get_image':self.draw_polygons,
                                            'parameters':{'current_frame_function':external_functions['get_current_frame'], 'polygons_function':external_functions['get_polygon_points'], 'current_camera_number':1, 'side_to_get':'b'},
                                            }

        back_to_calibrate_button = {'size':[150, 300],
                                    'location':[930, 1621],
                                    'color':'white',
                                    'text_color':'black',
                                    'text':'back',
                                    'action':external_functions['change_menu'],
                                    'parameters':'calibrate'}

        save = {'size':[200, 300],
                'location':[0, 1621],
                'color':'red',
                'text_color':'black',
                'text':'save',
                'action':external_functions['save_visual_recognition_colors']}

        load = {'size':[200, 300],
                'location':[200, 1621],
                'color':'orange',
                'text_color':'black',
                'text':'load',
                'action':external_functions['load_visual_recognition_colors']}

        calibrate = {'size':[300, 300],
                     'location':[400, 1621],
                     'color':'green',
                     'text_color':'black',
                     'text':'calibrate',
                     'action':external_functions['calibrate_cube_colors']}

        #not currently used
        quit_button = {'size':[100, 50],
                                    'location':[700, 400],
                                    'color':'red',
                                    'text_color':'black',
                                    'text':'quit',
                                    'action':external_functions['initiate_quit']}

        colors_menu = {'buttons':[back_to_calibrate_button, calibrate, save, load], 'frames':[lower_polygons_segment, upper_polygons__segment]}


        self.menu = colors_menu

    def draw_polygons(self, parameters):
        current_camera = parameters['current_camera_number']
        current_frame = parameters['current_frame_function'](current_camera)
        polygons = parameters['polygons_function'](side_to_get = parameters['side_to_get'], polygon_type = 'calibration')
        self.new_frame = current_frame
        for polygon in polygons:
                polygon = np.array(polygon,np.int32)
                polygon = polygon.reshape((-1,1,2))
                self.new_frame = cv2.fillConvexPoly(self.new_frame, polygon, (255,255,255), 10)
                self.new_frame = cv2.polylines(self.new_frame, polygon, True, (90,255,0), 5)
        return self.new_frame
