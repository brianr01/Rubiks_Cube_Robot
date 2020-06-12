import sys
from os import path
import numpy as np
import cv2
#adds images to working directory
sys.path.append(sys.path[0] + '/robot_interface/menu_classes/images')
current_directory = sys.path[0]
parent_directory = path.dirname(current_directory)
sys.path.append(parent_directory)

#external functions needed get_cube_position, get_current_frame, get_current_image_in_lab, turn_side, solve, scramble, change_menu, initiate_quit
class polygons_menu():
    def __init__(self, external_functions):
        self.external_functions = external_functions

        self.cube_reference_points_dictionary = {'f':{
                                                 'f1':[97,189],
                                                      'f2':[60,181],
                                                      'f3':[28,161],
                                                      'f4':[95,151],
                                                      'f5':[57,137],
                                                      'f6':[24,119],
                                                      'f7':[93,106],
                                                      'f8':[57,88],
                                                      'f9':[22,75]},
                                                 'b':{'b1':[131,105],
                                                      'b2':[164,86],
                                                      'b3':[201,68],
                                                      'b4':[133,152],
                                                      'b5':[166,134],
                                                      'b6':[201,112],
                                                      'b7':[133,199],
                                                      'b8':[169,177],
                                                      'b9':[201,158]},
                                                 'u':{'u1':[180,37],
                                                      'u2':[146,55],
                                                      'u3':[112,71],
                                                      'u4':[144,25],
                                                      'u5':[111,39],
                                                      'u6':[75,55],
                                                      'u7':[108,10],
                                                      'u8':[75,24],
                                                      'u9':[38,41]},
                                                 'd':{'d1':[112,71],
                                                      'd2':[75,55],
                                                      'd3':[38,41],
                                                      'd4':[146,55],
                                                      'd5':[111,39],
                                                      'd6':[75,24],
                                                      'd7':[180,37],
                                                      'd8':[144,25],
                                                      'd9':[108,10]},
                                                 'l':{'l1':[201,158],
                                                      'l2':[169,177],
                                                      'l3':[133,199],
                                                      'l4':[201,112],
                                                      'l5':[166,134],
                                                      'l6':[133,152],
                                                      'l7':[201,68],
                                                      'l8':[164,86],
                                                      'l9':[131,105]},
                                                 'r':{'r1':[22,75],
                                                      'r2':[57,88],
                                                      'r3':[93,106],
                                                      'r4':[24,119],
                                                      'r5':[57,137],
                                                      'r6':[95,151],
                                                      'r7':[28,161],
                                                      'r8':[60,181],
                                                      'r9':[97,189]}}

        polygon_calibration_segment = {'name':'polygon_calibration_segment',
                                       'location':[0, 0],
                                       'size':[607, 1080],
                                       'action_to_get_image':self.draw_polygons,
                                       'parameters':{'current_frame_function':external_functions['get_current_frame'], 'polygons_function':external_functions['get_polygon_points'], 'current_camera_number':external_functions['get_current_camera_number'], 'get_current_polygon_address':external_functions['get_current_polygon_address']},
                                       'action_on_event':self.add_polygon}

        cube_refrence_segment = {'name':'cube_refrence_segment',
                                 'location':[305, 607],
                                 'size':[500,500],
                                 'action_to_get_image':self.get_cube_calibration_segment,
                                 'parameters':{'get_current_polygon_address':external_functions['get_current_polygon_address']}}

        add_button = {'size':[300, 300],
                      'location':[0, 607],
                      'color':'green',
                      'text_color':'black',
                      'text':'next',
                      'action':external_functions['next_polygon']}

        previous_button = {'size':[300, 300],
                           'location':[0, 907],
                           'color':'red',
                           'text_color':'black',
                           'text':'previous',
                           'action':external_functions['previous_polygon']}

        remove_button = {'size':[300, 200],
                        'location':[790, 607],
                        'color':'green',
                        'text_color':'black',
                        'text':'delete last point',
                        'action':external_functions['remove_point_from_current_polygon']}

        clear_button = {'size':[300, 200],
                        'location':[790, 807],
                        'color':'blue',
                        'text_color':'black',
                        'text':'clear current set',
                        'action':external_functions['clear_current_polygon']}

        reset_all_button = {'size':[300, 200],
                            'location':[790, 1007],
                            'color':'red',
                            'text_color':'black',
                            'text':'reset all polygons',
                            'action':external_functions['clear_all_polygons']}

        copy_button = {'size':[100, 100],
                        'location':[900, 1500],
                        'color':'yellow',
                        'text_color':'black',
                        'text':'copy',
                        'action':external_functions['copy_standard_polygons_to_calibration_polygons']}

        save_button = {'size':[250, 250],
                       'location':[0, 1670],
                       'color':'green',
                       'text_color':'black',
                       'text':'save',
                       'action':external_functions['save_visual_recognition_polygons']}

        load_button = {'size':[250, 250],
                       'location':[250, 1670],
                       'color':'orange',
                       'text_color':'black',
                       'text':'load',
                       'action':external_functions['load_visual_recognition_polygons']}

        back_to_calibrate_from_polygon_button = {'size':[500, 100],
                                                 'location':[300, 1107],
                                                 'color':'white',
                                                 'text_color':'black',
                                                 'text':'back',
                                                 'action':external_functions['change_menu'],
                                                 'parameters':'calibrate'}

        change_type_to_standard = {'size':[250, 250],
                                    'location':[520, 1670],
                                    'color':'blue',
                                    'text_color':'black',
                                    'text':'standard',
                                    'action':external_functions['change_polygon_type'],
                                    'parameters':'standard'}

        change_type_to_calibration = {'size':[300, 300],
                                    'location':[770, 1670],
                                    'color':'red',
                                    'text_color':'black',
                                    'text':'calibration',
                                    'action':external_functions['change_polygon_type'],
                                    'parameters':'calibration'}

        polygons_menu = {'buttons':[back_to_calibrate_from_polygon_button,
                                    add_button,
                                    previous_button, clear_button,
                                    save_button, load_button,
                                    reset_all_button,
                                    change_type_to_standard,
                                    change_type_to_calibration,
                                    copy_button,
                                    remove_button],
                         'frames':[cube_refrence_segment,
                                   polygon_calibration_segment]}
        self.menu = polygons_menu

    def draw_polygons(self, parameters):

        current_camera = parameters['current_camera_number']()
        current_frame = parameters['current_frame_function'](current_camera)
        polygons = parameters['polygons_function']()
        self.new_frame = current_frame
        print(polygons)
        for polygon in polygons:
                polygon = np.array(polygon,np.int32)
                polygon = polygon.reshape((-1,1,2))
                self.new_frame = cv2.fillConvexPoly(self.new_frame, polygon, (255,255,255), 10)
                self.new_frame = cv2.polylines(self.new_frame, polygon, True, (90,255,0), 5)

        return self.new_frame

    def add_polygon(self, x,y,event):
        if (event == 4):
            print('added')
            
            self.external_functions['add_point_to_current_polygon']([x - 50,y + 50])
            self.external_functions['add_point_to_current_polygon']([x + 50,y + 50])
            self.external_functions['add_point_to_current_polygon']([x + 50,y - 50])
            self.external_functions['add_point_to_current_polygon']([x - 50,y - 50])

    def next_polygon(self, x,y,event):
        if (event == 4):
            print('next')
            self.external_functions['add_point_to_current_polygon']([x,y])

    def get_cube_calibration_segment(self, parameters):
        current_polygon_address = parameters['get_current_polygon_address']()
        image = cv2.imread(sys.path[0] + '/cube_reference_image.jpeg')
        point = self.cube_reference_points_dictionary[current_polygon_address[0]][current_polygon_address]
        point = (point[0], point[1])
        cv2.circle(image, point, 10, (90,255,0), -1)

        return image
