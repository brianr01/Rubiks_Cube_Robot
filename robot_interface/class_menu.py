import class_button
import class_frame

class menu:
    def __init__(self, frames, buttons):

        self.buttons = []
        for button in buttons:
            if 'parameters' in button:
                self.buttons.append(class_button.button(button['size'], button['location'], button['color'], button['text_color'], button['text'], button['action'],parameters = button['parameters']))
            else:
                self.buttons.append(class_button.button(button['size'], button['location'], button['color'], button['text_color'], button['text'], button['action']))

        self.frames = {}
        for frame in frames:
            if not('parameters' in frame):
                frame['parameters'] = None

            if not('action_to_get_image' in frame):
                frame['action_to_get_image'] = None
            
            if not('image' in frame):
                frame['image'] = None

            self.frames[frame['name']] = class_frame.frame(frame['location'], image = frame['image'], action_to_get_image = frame['action_to_get_image'], parameters = frame['parameters'])

    def update(self, cursor_x, cursor_y, mouse_code):
        for button in self.buttons:
            location = [cursor_x, cursor_y]
            button.update(location, mouse_code)


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





