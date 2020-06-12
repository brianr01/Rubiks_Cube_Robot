import cv2
import numpy as np
import math

class frame_manager:
    def __init__(self, location, size, image = None, action_to_get_image = None, parameters = None, action_on_event = None):
        self.parameters = parameters
        self.action_to_get_image = action_to_get_image
        self.location = location
        if image is None:
            image = np.zeros((1,1,3), np.uint8)
        else:
            self.image = image

        self.action_on_event = action_on_event
        self.scale_factor = 1
        self.size = size
        self.resized_image=np.zeros((1,1,3), np.uint8)

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


        if (frame.shape[0] < self.size[0] + self.location[0]):
            raise Exception("The image went outside the right side of the frame. The shape of the frame was '", frame.shape[0] , "' and the x location of the image was '", x_offset , "' and the width of the image was '" , self.image.shape[0] , "'")
            return frame

        elif (0 > x_offset):
            raise Exception("The image went outside the left side of the frame.")
            return frame

        elif (frame.shape[0] < self.size[0] + y_offset):
            raise Exception("The image went outside the bottom of the frame.")
            return frame

        elif (0 > y_offset):
            raise Exception("The image went outside the top of the frame.")
            return frame
        resized_image = self.image_resize(self.image, self.size)
        self.resized_image = resized_image
        frame[y_offset:y_offset+resized_image.shape[0], x_offset:x_offset+resized_image.shape[1]] = resized_image

        return frame

    def update(self, location, event):
        if (not(self.action_on_event is None)):

            x = location[0] - self.location[0]
            y = location[1] - self.location[1]
            print(location)
            print(self.scale_factor)
            if (x >= 0 and y >= 0) and (x <= self.resized_image.shape[1] and y <= self.resized_image.shape[0]):
                self.action_on_event(math.floor(x*self.scale_factor),math.floor(y*self.scale_factor),event)

    def image_resize(self, image, size):
        # return image
        width = size[0]
        height = size[1]
        (h, w) = image.shape[:2]
        if (w >= h):
            ratio = float(float(w)/float(h))
            dim = (height, int(height / ratio))
            self.scale_factor = ratio
        else:
            ratio = float(float(h)/float(w))
            dim = (int(width / ratio), width)
            self.scale_factor = ratio
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

        # return the resized image
        return resized