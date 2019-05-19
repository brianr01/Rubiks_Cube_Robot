import cv2
import numpy as np

class frame:
    def __init__(self, location, image = None, action_to_get_image = None, parameters = None):
        self.parameters = parameters
        self.action_to_get_image = action_to_get_image
        self.location = location
        if image is None:
            image = np.zeros((1,1,3), np.uint8)
        else:
            self.image = image


    def render(self, frame, image = None, parameters = None):
        x_offset = self.location[0]
        y_offset = self.location[1]
        
        if not(image is None):
            self.image = image
        elif not(self.action_to_get_image is None):

            if not(parameters is None):
                self.image = self.action_to_get_image(parameters)
                self.parameters = parameters

            elif not(self.parameters is None):
                self.image = self.action_to_get_image(self.parameters)

            else:
                self.image = self.action_to_get_image()
            
        frame[y_offset:y_offset+self.image.shape[0], x_offset:x_offset+self.image.shape[1]] = self.image

        return frame