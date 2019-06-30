import sys
from os import path

#adds images to working directory
sys.path.append(sys.path[0] + '/images')


#adds the file to test to the working directory
current_directory = sys.path[0]
parent_directory = path.dirname(current_directory)
sys.path.append(parent_directory)



import cv2
import numpy as np

class polygon_calibration_menu:
    def __init__(self, external_functions):
        self.current_polygon = 'u1'

        self.external_functions = external_functions
        self.polygon_calibration_segment = np.zeros((100,100,3), np.uint8)

        self.polygon_calibration_segment[:] = (150, 10, 255)
        #self.cube_image, self.cube_original_size = image_resize(cube_image, height = 450)


        self.polygon_calibration_segment = {'name':'polygon_calibration_segment', 'location':[0, 0], 'image':cube_image}

        self.cube_reference_segment = {'name':'cube_reference_segment', 'location':[700, 250], 'action_to_get_image':self.render_polygon_calibration_frame}

        self.add = {'size':[50, 50], 'location':[700, 0],'color':'green', 'text_color':'black', 'text':'+', 'action':self.external_functions['change_menu'], 'parameters':'polygons'}
        self.previous_button = {'size':[50, 50], 
                                'location':[750, 0],
                                'color':'red', 
                                'text_color':'black', 
                                'text':'-',
                                'action':self.external_functions['change_menu'],
                                'parameters':'polygons'}

        self.clear_button = {'size':[100, 50], 
                             'location':[700, 50],
                             'color':'blue', 
                             'text_color':'black', 
                             'text':'clear', 
                             'action':self.external_functions['change_menu'], 
                             'parameters':'polygons'}

        self.save_button = {'size':[100, 50], 
                            'location':[700, 100],
                            'color':'yellow', 
                            'text_color':'black', 
                            'text':'save', 
                            'action':self.external_functions['change_menu'], 
                            'parameters':'polygons'}

        self.load_button = {'size':[100, 50], 
                            'location':[700, 150],
                            'color':'orange', 
                            'text_color':'black', 
                            'text':'load', 
                            'action':self.external_functions['change_menu'], 
                            'parameters':'polygons'}

        self.reset_button = {'size':[100, 50], 
                             'location':[700, 200],
                             'color':'red', 
                             'text_color':'black', 
                             'text':'reset', 
                             'action':self.external_functions['change_menu'], 
                             'parameters':'polygons'}

        self.back_button = {'size':[100, 50], 
                            'location':[700, 350], 
                            'color':'white', 
                            'text_color':'black', 
                            'text':'back', 
                            'action':self.external_functions['initiate_quit'], 
                            'parameters':'calibrate'}

        self.quit_button = {'size':[100, 50], 
                            'location':[700, 400],
                            'color':'red', 
                            'text_color':'black', 
                            'text':'quit', 
                            'action':initiate_quit}

        self.polygons_menu = {'buttons':[back_button, quit_button, add_button, previous_button, clear_button, save_button, load_button, reset_all_button], 'frames':[cube_reference_segment, polygon_calibration_segment]}

        self.sticker_locations = [[0,10], [0,20], [0,30], [0,40], [0,50]]

    def set_currrent_polygon(self, address):
        self.current_polygon = address

    def change_current_side(self, side):
        sticker_number = self.current_polygon[1]
        self.current_polygon = (side + str(sticker_number))

    def increment_current_polygon(self, increment_up = True):
        side_order = ['ufrdbf']
        if (increment_up):
            if (self.current_polygon[1] == 9):
                current_side_number = side_order.find(self.current_polygon[0])
                if (current_side_number >= 5):
                    self.set_current_polygon = (side_order[0] + '1')
                
                else:
                    new_side = self.current_side_number + 1
                    self.current_polygon = new_side + '1'
            else:
                self.currrent_polygon = self.current_polygon[0] + str(int(self.current_polygon) + 1)               
        else:
            if (self.current_polygon[1] == 1):
                current_side_number = side_order.find(self.current_polygon[5])
                if (current_side_number <= 5):
                    self.set_current_polygon = (side_order[0] + '9')
                
                else:
                    new_side = self.current_side_number - 1
                    self.current_polygon = new_side + '9'
            else:
                self.currrent_polygon = self.current_polygon[0] + str(int(self.current_polygon) - 1)

    def draw_reference_image_stickers(self, image):
        for location in self.sticker_locations:
            image = self.draw_referenece_image_sticker(image, location, selected = False)
        

    def draw_reference_image_sticker(self, image, location, selected = False):
        cv2.circle(image,(location[0], location[1]), 10, (255,255,255), -1)
        if (selected == True):
            cv2.circle(image,(location[0], location[1]), 8, (100,200,0), -1)
        else:
            cv2.circle(image,(location[0], location[1]), 8, (0,0,0), -1)

        return image

    def render_polygon_calibration_frame():
        pass










def update_polygon_calibration_frame(x,y,event):
    
    if event == 1:
        print(x,y,event)
    #pass

def polygon_calibration_reference(x,y,event):
    
    if event == 1:
        print(x,y,event)
    #pass


def change_menu(parameter):
    print('change_menu')

def initiate_quit(stop_program):
    print('stopping')

test = polygon_calibration_menu({'change_menu':change_menu, 'initiate_quit':initiate_quit})