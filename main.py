import sys
from os import path
import os

#todo remove import of cv2 when camera module works
import paramiko
import cv2
import timeit
import time
import numpy
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.constraints import maxnorm

COMP = "pi"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('192.168.2.249', username="pi", password="robotpassword", timeout=10)
except Exception as e:
    print('Unable to connect to raspberry pi over the network!')
    print(e)

model = tf.keras.models.load_model("cube_ai_model_9995")
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
                               'save_visual_recognition_polygons':self.visual_recognition.save_polygons,
                               'load_visual_recognition_polygons':self.visual_recognition.load_polygons,
                               }

        self.visual_recognition.load_polygons()

        self.interface = class_robot_interface.robot_interface(interface_functions)
        self.quit = False
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
        self.virtual_rubiks_cube.cube_position = self.visual_recognition.get_colors(frame0, frame1)

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

    def mirror():
         new_cube_state_to_set = self.visual_recognition.get_colors(frame0, frame1)


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


robot = rubiks_cube_solving_robot()

# for i in range(1,5):
#     winsound.Beep(2000, 100)

while True:
    cv2.imshow('frame', robot.render())
    cv2.setMouseCallback('frame', robot.update)
    cv2.moveWindow('frame', 1920,-35)
    if cv2.waitKey(1) & 0xFF == ord('q') or robot.quit:
        break

# file_number = str(len(os.listdir('training_images/')))
# os.mkdir('training_images/' + file_number)
# os.mkdir('training_images/' + file_number + '/u')
# os.mkdir('training_images/' + file_number + '/d')
# os.mkdir('training_images/' + file_number + '/l')
# os.mkdir('training_images/' + file_number + '/r')
# os.mkdir('training_images/' + file_number + '/f')
# os.mkdir('training_images/' + file_number + '/b')
# while True:
#     robot.solve()
#     robot.scramble()
#     #robot.turn_side('r')

# cv2.destroyAllWindows()
