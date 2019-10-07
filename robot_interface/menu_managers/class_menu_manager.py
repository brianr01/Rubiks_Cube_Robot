from class_button_manager import *
from class_frame_manager import *

class menu_manager:
    def __init__(self, frames, buttons):

        self.buttons = []
        for button in buttons:
            if 'parameters' in button:
                self.buttons.append(button_manager(button['size'], button['location'], button['color'], button['text_color'], button['text'], button['action'],parameters = button['parameters']))
            else:
                self.buttons.append(button_manager(button['size'], button['location'], button['color'], button['text_color'], button['text'], button['action']))

        self.frames = {}
        for frame in frames:
            if not('parameters' in frame):
                frame['parameters'] = None

            if not('action_to_get_image' in frame):
                frame['action_to_get_image'] = None
            
            if not('image' in frame):
                frame['image'] = None

            if not('action_on_event' in frame):
                frame['action_on_event'] = None

            self.frames[frame['name']] = frame_manager(frame['location'], frame['size'], image = frame['image'], action_to_get_image = frame['action_to_get_image'], parameters = frame['parameters'], action_on_event = frame['action_on_event'])

    def update(self, cursor_x, cursor_y, event):
        location = [cursor_x, cursor_y]
        for button in self.buttons:
            button.update(location, event)

        for frame in self.frames:
            self.frames[frame].update(location, event)
            

    def render(self, frame, new_frame_info):
        for segment in self.frames:
            if segment in new_frame_info:
                if 'image' in new_frame_info[segment]:
                    frame = self.frames[segment],render(frame, parameter = new_frame_info[segment]['image'])

                elif 'parameter' in new_frame_info[frame]:
                    frame = self.frames[segment],render(frame, parameter = new_frame_info[segment]['parameter'])
                
                else:
                    raise Exception('new_frame_info did not have a valid value inside of "image" or "parameter"')

            else:    
                frame = self.frames[segment].render(frame)

        for button in self.buttons:
            frame = button.render(frame)

        return frame





