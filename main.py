import sys
from os import path
import winsound

#todo remove import of cv2 when camera module works
import paramiko
import cv2
import timeit
import time

COMP = "pi"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('169.254.136.168', username="pi", password="robotpassword", timeout=10)
except Exception as e:
    print('Unable to connect to raspberry pi over the network!')
    print(e)

#adds robot interface to path
sys.path.append(sys.path[0] + '/robot_interface')
sys.path.append(sys.path[0] + '/turn_scripts')
sys.path.append(sys.path[0] + '/virtual_rubiks_cube')
sys.path.append(sys.path[0] + '/visual_recognition')

import class_cube_detection_and_calibration
import virtual_rubiks_cube
import pi_sender
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

        self.visual_recognition.load_polygons()
        self.visual_recognition.load_colors()

        self.interface = class_robot_interface.robot_interface(interface_functions)
        self.quit = False
        self.visual_recognition.get_thresholds()
        self.current_calibration_step = 0

        #can be none, pause, or continue
        self.current_calibration_action = 'none'

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
        try:
            pi_sender.run_command('on ' + move, ssh)
            time.sleep(.5)
            pi_sender.run_command('of', ssh)
        except:
            print('unable to comunicate with rpi')

    def solve(self):
        start = timeit.default_timer()
        frame0 = self.get_current_image_in_lab(0)
        frame1 = self.get_current_image_in_lab(1)
        new_cube_state_to_set = self.visual_recognition.get_colors(frame0, frame1)

        sides = 'urfdlb'
        cube_state = {}
        for side in new_cube_state_to_set:
            cube_side = new_cube_state_to_set[side]

            cube_state[side] = []

            for  i in range(1,10):
                sticker_color = cube_side[str(i)]

                cube_state[side].append(str(sticker_color) + str(i))

        self.virtual_rubiks_cube.cube_position = cube_state
        try:
            solution = self.virtual_rubiks_cube.get_solution()
            self.virtual_rubiks_cube.execute_algorithm(solution)
            try:
                pi_sender.run_command('on ' + solution, ssh)
                time.sleep(.5)
                pi_sender.run_command('of', ssh)
            except:
                print('unable to comunicate with rpi')

            print(timeit.default_timer() - start)
        except Exception as e:
            print('couldn"t find solution')
            print(e)

    def scramble(self):
        scramble = self.virtual_rubiks_cube.get_scramble(moves = 50)
        self.virtual_rubiks_cube.execute_algorithm(scramble)
        try:
            pi_sender.run_command('on ' + scramble, ssh)
            time.sleep(.5)
            pi_sender.run_command('of', ssh)
        except:
            print('unable to comunicate with rpi')

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

                                  {'moves':"U' D L R' F B' U' D", 'sides':{                  'u':'d', 'd':'u', 'f':'b', 'b':'f'}},
                                  {'moves':"U' D L R' F B' U' D", 'sides':{'r':'d', 'l':'u', 'f':'l', 'b':'r'}},

                                  {'moves':"U D' L' R F B' U D'", 'sides':{                  'u':'l', 'd':'r', 'f':'d', 'b':'u'}},
                                  {'moves':"U D' L' R F B' U D'", 'sides':{'r':'l', 'l':'r'}},

                                  {'moves':"U' D L R' F B' U' D", 'sides':{                  'u':'b', 'd':'f'}},
                                  {'moves':"U' D L R' F B' U' D", 'sides':{'r':'b', 'l':'f'}},
                                  {'moves':"U' D L' R F' B U' D", 'sides':{}}]

        sides = calibrate_instructions[self.current_calibration_step]['sides']
        if (sides != {}):
            for side in sides:
                self.visual_recognition.calibrate_side(self.get_current_image_in_lab(side_to_camera_dict[side]), side, sides[side])

        self.current_calibration_step += 1

        if (self.current_calibration_step >= len(calibrate_instructions)):
            self.current_calibration_step = 0

        moves = calibrate_instructions[self.current_calibration_step]['moves']
        try:
            pi_sender.run_command('on ' + moves, ssh)
        except:
            print('unable to comunicate with rpi')
        self.virtual_rubiks_cube.execute_algorithm(moves)
        time.sleep(.5)
        try:
            pi_sender.run_command('of', ssh)
        except:
            print('unable to comunicate with rpi')

        if self.current_calibration_step >= len(calibrate_instructions):
            self.current_calibration_step = 0
        print ('done')
        side_dict = {'r':'right','l':'left ','u':'up   ','d':'down ','f':'front','b':'back '}
        color_dict = {'r':'red   ','l':'orange','u':'white ','d':'yellow','f':'green ','b':'blue  '}
        for side in sides:
            print([side_dict[side], color_dict[sides[side]]])


robot = rubiks_cube_solving_robot()

for i in range(1,5):
    winsound.Beep(2000, 100)

while True:
    cv2.imshow('frame', robot.render())
    cv2.setMouseCallback('frame', robot.update)
    cv2.moveWindow('frame', 1920,-35)
    if cv2.waitKey(1) & 0xFF == ord('q') or robot.quit:
        break

cv2.destroyAllWindows()
