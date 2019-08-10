import sys
from os import path


#todo remove import of cv2 when camera module works
import cv2
import timeit
import time




#adds robot interface to path
sys.path.append(sys.path[0] + '/robot_interface')
sys.path.append(sys.path[0] + '/turn_scripts')
sys.path.append(sys.path[0] + '/virtual_rubiks_cube')
sys.path.append(sys.path[0] + '/visual_recognition')


import class_cube_detection_and_calibration
import virtual_rubiks_cube
import class_cube

import class_robot_interface
import UseWebCam


class rubiks_cube_solving_robot:
    def __init__(self):
        self.current_frame = UseWebCam.get_current_frames()

        self.virtual_rubiks_cube = virtual_rubiks_cube.Virtual_Cube()
        self.visual_recognition = class_cube_detection_and_calibration.cube_detection_and_calibration()
        interface_functions = {'get_cube_state':self.get_cube_state,
                               'get_current_frame':self.get_current_frame,
                               'get_current_image_in_lab':self.get_current_image_in_lab,
                               'turn_side':self.turn_side,
                               'solve':self.solve,
                               'scramble':self.scramble,
                               'initiate_quit':self.initiate_quit,
                               'get_acceleration_calibration':self.get_acceleration_calibration,
                               'next_polygon':self.visual_recognition.next_polygon,
                               'previous_polygon':self.visual_recognition.previous_polygon,
                               'clear_current_polygon':self.visual_recognition.clear_current_polygon,
                               'clear_all_polygons':self.visual_recognition.clear_all_polygons,
                               'get_polygon_points':self.visual_recognition.get_polygon_points,
                               'add_point_to_current_polygon':self.visual_recognition.add_point_to_current_polygon,
                               'get_current_camera_number':self.visual_recognition.get_current_camera_number,
                               'change_polygon_type':self.visual_recognition.change_polygon_type,
                               'copy_standard_polygons_to_calibration_polygons':self.visual_recognition.copy_standard_polygons_to_calibration_polygons,
                               'remove_point_from_current_polygon':self.visual_recognition.remove_point_from_current_polygon,
                               'get_current_polygon_address':self.visual_recognition.get_current_polygon_address,
                               'calibrate_cube_colors':self.calibrate_cube_colors,
                               'get_colors_calibration':self.visual_recognition.get_thresholds,
                               'save_visual_recognition_polygons':self.visual_recognition.save_polygons,
                               'load_visual_recognition_polygons':self.visual_recognition.load_polygons,
                               'save_visual_recognition_colors':self.visual_recognition.save_colors,
                               'load_visual_recognition_colors':self.visual_recognition.load_colors}

        self.interface = class_robot_interface.robot_interface(interface_functions)
        self.quit = False
        self.visual_recognition.get_thresholds()
        
        
        motors_pins = {'r':[5, 3, 12],
               'l':[11, 7, 36],
               'u':[15, 13, 16], 
               'd':[31, 29, 22], 
               'f':[35, 33, 18], 
               'b':[40, 37, 32]}
        
        self.turn_scripts = class_cube.Cube(motors_pins)

    def get_cube_state(self):
        return self.virtual_rubiks_cube.get_cube_state()

    def get_current_frame(self, camera_number):
        frames = UseWebCam.get_current_frames()

        return frames[int(camera_number)]

    def get_current_image_in_lab(self, camera_number):
        frames = UseWebCam.get_current_frames()
        frame = cv2.cvtColor(frames[int(camera_number)], cv2.COLOR_BGR2LAB)
        return frame

    def turn_side(self, move):
        self.virtual_rubiks_cube.execute_algorithm([move])
        self.turn_scripts.power_on()
        self.turn_scripts.execute_algorithm(move)
        self.turn_scripts.power_off()

    def solve(self):
        start = timeit.default_timer()
        frame0 = self.get_current_frame(0)
        frame1 = self.get_current_frame(1)
        #cube_position = self.visual_recognition.get_colors(frame0, frame1)
        cube_position = self.virtual_rubiks_cube.get_cube_state()
        self.virtual_rubiks_cube.cube_position = cube_position
        solution = self.virtual_rubiks_cube.get_solution()
        print(solution)
        self.virtual_rubiks_cube.execute_algorithm(solution)
        
        
        #solution = self.virtual_rubiks_cube.convert_algorithm(solution)
        
        self.turn_scripts.power_on()
        self.turn_scripts.execute_algorithm(solution)
        self.turn_scripts.power_off()
        print(timeit.default_timer() - start)

    def scramble(self):
        #todo write scramble method in virtual rubiks cube scramble = self.virtual_rubiks_cube.get_scramble()
        scramble = self.virtual_rubiks_cube.get_scramble(moves = 50)
        self.virtual_rubiks_cube.execute_algorithm(scramble)
        self.turn_scripts.power_on()
        self.turn_scripts.execute_algorithm(scramble)
        self.turn_scripts.power_off()


    def initiate_quit(self):
        print('end')
        self.quit = True

    def render(self):
        return self.interface.render()
    
    def update(self, event, cursor_y, cursor_x, flag, flag2):
        self.interface.update(cursor_x, cursor_y, event)
    
    def get_acceleration_calibration(self):
        #todo create acceleration calibration function in turn scrips
        return 1

    def calibrate_cube_colors(self):
        print('started')
        side_to_camera_dict = {'b':1, 'u':1, 'r':1, 'f':0, 'd':0, 'l':0}
        calibrate_instructions = [{'moves':'',                    'sides':{'r':'r', 'l':'l', 'u':'u', 'd':'d', 'f':'f', 'b':'b'}},

                                  {'moves':"U D' L' R F B' U D'", 'sides':{'r':'u', 'l':'d', 'u':'f', 'd':'b', 'f':'r', 'b':'l'}},
                                  {'moves':"U D' L' R F B' U D'", 'sides':{'r':'f', 'l':'b', 'u':'r', 'd':'l', 'f':'u', 'b':'d'}},

                                  {'moves':"U' D L R' F B' U' D", 'sides':{'r':'l', 'l':'r'                                    }},
                                  {'moves':"U' D L R' F B' U' D", 'sides':{'r':'d', 'l':'u', 'u':'b', 'd':'f'                  }},

                                  {'moves':"U D' L' R F B' U D'", 'sides':{'r':'b', 'l':'f',                   'f':'d', 'b':'u'}},
                                  {'moves':"U D' L' R F B' U D'", 'sides':{                  'u':'d', 'd':'u', 'f':'b', 'b':'f'}},

                                  {'moves':"U' D L R' F B' U' D", 'sides':{                                    'f':'l', 'b':'r'}},
                                  {'moves':"U' D L R' F B' U' D", 'sides':{                  'u':'l', 'd':'r'                  }},
                                  {'moves':"U' D L' R F' B U' D", 'sides':{                                                    }}                 ]

        for instruction in calibrate_instructions:
            moves = instruction['moves']
            sides = instruction['sides']
            print('set')
            if (moves != ''):
                self.turn_scripts.power_on()
                self.turn_scripts.execute_algorithm(moves)
                time.sleep(.5)
                self.turn_scripts.power_off()
                pass
            input('align the cube now')
            if (sides != {}):
                for side in sides:
                    self.visual_recognition.calibrate_side(self.get_current_frame(side_to_camera_dict[side]), side, sides[side])
        print ('done')
    
robot = rubiks_cube_solving_robot()
while True:
    cv2.imshow('frame', robot.render())
    cv2.setMouseCallback('frame', robot.update)
    cv2.moveWindow('frame', 0,0)
    if cv2.waitKey(1) & 0xFF == ord('q') or robot.quit:
        break


cv2.destroyAllWindows()