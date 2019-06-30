import sys
from os import path


#todo remove import of cv2 when camera module works
import cv2



#adds robot interface to path
sys.path.append(sys.path[0] + '/robot_interface')
sys.path.append(sys.path[0] + '/turn_scripts')
sys.path.append(sys.path[0] + '/virtual_rubiks_cube')
sys.path.append(sys.path[0] + '/visual_recognition')


import class_cube_detection_and_calibration
import virtual_rubiks_cube
#import class_cube TODO UNCOMMENT AND TEST FUNCTIONALITY WHEN HOOKED UP TO RASPBERRY PI

import class_robot_interface
#import UseWebCam NEED TO REMAKE THIS MODULE OR FIND WORKING VERSION

class rubiks_cube_solving_robot:
    def __init__(self):
        

        self.current_frame = [cv2.imread('frame.jpg'),cv2.imread('frame2.jpg')]


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
                               'save_visual_recognition':self.visual_recognition.save_polygons,
                               'load_visual_recognition':self.visual_recognition.load_polygons}

        self.interface = class_robot_interface.robot_interface(interface_functions)
        self.quit = False
        self.visual_recognition.get_thresholds()
        #self.turn_scripts = class_cube

    def get_cube_state(self):
        return self.virtual_rubiks_cube.get_cube_state()

    def get_current_frame(self, camera_number):
        frames = [cv2.imread('frame1.jpg'),cv2.imread('frame2.jpg')]
        return frames[int(camera_number)]

    def get_current_image_in_lab(self, camera_number):
        frames = [cv2.imread('frame1.jpg'),cv2.imread('frame2.jpg')]
        frame = cv2.cvtColor(frames[int(camera_number)], cv2.COLOR_BGR2LAB)
        return frame

    def turn_side(self, move):
        self.virtual_rubiks_cube.execute_algorithm([move])
        #self.turn_scripts.execute_algorithm([move])

    def solve(self):
        frame0 = self.get_current_frame(0)
        frame1 = self.get_current_frame(1)
        cube_position = self.visual_recognition.get_colors(frame0, frame1)
        print(cube_position)
        #cube_position = self.virtual_rubiks_cube.get_cube_state()
        self.virtual_rubiks_cube.cube_position = cube_position
        solution = self.virtual_rubiks_cube.get_solution()
        self.virtual_rubiks_cube.execute_algorithm(solution)
        #self.turn_scripts.execute_algorithm(solution)

    def scramble(self):
        #todo write scramble method in virtual rubiks cube scramble = self.virtual_rubiks_cube.get_scramble()
        scramble = self.virtual_rubiks_cube.get_scramble()
        self.virtual_rubiks_cube.execute_algorithm(scramble)
        #todo test this in robot self.turn_scripts.execute_algorithm(scramble)

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
        side_to_camera_dict = {'b':1, 'u':1, 'r':1, 'f':0, 'd':0, 'l':0}
        calibrate_instructions = [{'moves':'',       'sides':{'r':'r', 'l':'r', 'u':'r', 'd':'r', 'f':'r', 'b':'r'}},
                                  {'moves':'',       'sides':{'r':'l', 'l':'l', 'u':'l', 'd':'l', 'f':'l', 'b':'l'}},
                                  {'moves':'',       'sides':{'r':'u', 'l':'u', 'u':'u', 'd':'u', 'f':'u', 'b':'f'}},
                                  {'moves':'',       'sides':{'r':'d', 'l':'d', 'u':'d', 'd':'d', 'f':'d', 'b':'b'}},
                                  {'moves':'',       'sides':{'r':'f', 'l':'f', 'u':'f', 'd':'f', 'f':'f', 'b':'u'}},
                                  {'moves':'',       'sides':{'r':'b', 'l':'b', 'u':'b', 'd':'b', 'f':'b', 'b':'d'}},
                                ]
        for instruction in calibrate_instructions:
            moves = instruction['moves']
            sides = instruction['sides']
            if (moves != ''):
                #self.turn_scripts.execute_algorithm(moves)
                pass
            
            if (sides != {}):
                for side in sides:
                    self.visual_recognition.calibrate_side(self.get_current_frame(side_to_camera_dict[side]), side, sides[side])
        print ('done')
    
robot = rubiks_cube_solving_robot()
while True:
    cv2.imshow('frame', robot.render())
    #cv2.moveWindow('frame',1920,0)
    cv2.setMouseCallback('frame', robot.update)
    if cv2.waitKey(1) & 0xFF == ord('q') or robot.quit:
        break


cv2.destroyAllWindows()