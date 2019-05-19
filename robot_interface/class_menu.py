import cv2
import numpy as np
import class_button
import class_frame


#input for a button [50, 50], [0, 400], (255, 255, 255), (0, 0, 0), 'u', turn_side, parameters = 'u'

#input for a frame [266,200], action_to_get_image=get_current_and_resize_frame, parameters = cap

#init button self, size, location, color, text_color, text, action, parameters = None

#init frame self, location, image = None, action_to_get_image = None, parameters = Non 

# image = actucal photo from a camera

# frame = the entire screen of the gui

# segment = a part of a screen on the gui
class menu:
    def __init__(self, frames, buttons):

        self.buttons = []
        for button in buttons:
            self.buttons.append((button.class_button.button['size'], button['location'], button['color'], button['text_color'], button['text'], button['action'], parameters = button['parameters']))

        self.frames = {}
        for frame in frames:
            self.frames[frame['name']] = class_frame.frame(frame['location'], image = frame['image'], action_to_get_image = frame['action_to_get_image'], parameters = frame['parameters'])

    def update(self, cursor_x, cursor_y, mouse_code):
        for button in self.buttons:
            location = [cursor_x, cursor_y]
            button.update(location, mouse_code)

    def render(self, frame, new_frame_info):
        for frame in self.frames:
            if frame in new_frame_info:
                if 'image' in new_frame_info[frame]:
                    frame = self.frames[frame],render(frame, parameter = new_frame_info[frame]['image'])

                elif 'parameter' in new_frame_info[frame]:
                    frame = self.frames[frame],render(frame, parameter = new_frame_info[frame]['parameter'])
                
                else:
                    raise Exception('new_frame_info did not have a valid value inside of "image" or "parameter"')

            else:    
                frame = self.frames[frame].render(frame)
