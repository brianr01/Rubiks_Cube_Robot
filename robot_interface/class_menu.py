import cv2
import class_frame
import class_button

class menu:
    def __init__(self):
        self.buttons = []
        self.frames = {}

    def add_button(self, button):
        self.buttons.append(class_button.button(button['size'], button['location'], button['color'], button['text_color'], button['text'], button['action'], parameters = button['parameters']))

    def add_buttons(self, buttons):
        for button in buttons:
            self.add_button(button)

    def add_frame(self, frame):
        if frame['name'] in self.frames:
            self.frames[frame['name']] = class_frame.frame(frame['location'], frame['image'], frame['action_to_get_image'], frame['parameters'])
        else:
            raise Exception('frame:"', frame['name'] '" already exsists!')

    def add_frames(self, frames, frames_with_new_info):
        for frame in frames:
            if frame.name == 
            self.add_frame(frame)

    def render(self, frame):
        frame = self.render_buttons(frame)
        frame = self.render_frames(frame)
        return frame


    def render_buttons(frame):
        for button in self.button:
            frame = button.render(frame)
        return frame

    def render_frames(frame):

    def update(self):





    

    
