import class_sticker_detection_and_calibration
import numpy as np
import cv2
import pickle

class cube_detection_and_calibration:
    def __init__(self):
        self.sides_dictionary = {'b':1, 'u':1, 'r':1, 'f':0, 'd':0, 'l':0}
        self.side_order = 'burfdl'
        self.cube = {'f':{},
                'b':{},
                'u':{},
                'd':{},
                'l':{},
                'r':{}}
        for side in self.cube:
            for sticker_number in range(1, 10):
                sticker_name = side + str(sticker_number)
                self.cube[side][sticker_name] = class_sticker_detection_and_calibration.Sticker_Detection_And_Calibration(sticker_name)

        self.current_side = "f"
        self.current_polygon = self.cube['f']['f1']
        self.current_polygon_address = 'f1'
        self.change_current_polygon('f',1)
        self.current_polygon_type = 'standard'
        self.current_camera_number = 0

    def change_current_polygon(self, side, address_number):
        #saves the state of the previous polygon
        self.cube[self.current_side][self.current_polygon_address] = self.current_polygon

        #sets the current polygon
        self.current_polygon_address_number = address_number
        self.current_side = side
        self.current_polygon_address = self.current_side + str(self.current_polygon_address_number)
        self.current_camera_number = self.sides_dictionary[self.current_side]
        self.current_polygon = self.cube[self.current_side][self.current_polygon_address]

    def get_current_camera_number(self):
        return self.current_camera_number

    def next_polygon(self):
        if (self.current_polygon_address_number == 9):
            new_side = self.side_order[(self.side_order.find(self.current_side) + 1) % 6]
            self.change_current_polygon(new_side, 1)

        else:
            self.change_current_polygon(self.current_side, self.current_polygon_address_number + 1)

    def previous_polygon(self):
        if (self.current_polygon_address_number == 1):
            new_polygon_address_number = 9
            if (self.side_order.find(self.current_side) == 0):
                new_side = self.side_order[5]
                self.change_current_polygon(new_side, new_polygon_address_number)
            else:
                new_side = self.side_order[self.side_order.find(self.current_side) - 1]
                self.change_current_polygon(new_side, new_polygon_address_number)

        else:
            new_polygon_address_number = self.current_polygon_address_number - 1
            new_side = self.current_side
            self.change_current_polygon(new_side, new_polygon_address_number)


    def copy_standard_polygons_to_calibration_polygons(self):
        for side_letter in self.cube:
            for sticker_address in self.cube[side_letter]:
                self.cube[side_letter][sticker_address].copy_standard__polygons_to_calibration_polygons()

    def change_polygon_type(self, type):
        self.current_polygon_type = type

    def toggle_polygon_type(self):
        if (self.current_polygon_type == 'standard'):
            self.current_polygon_type = 'calibration'
        
        else:
            self.current_polygon_type = 'standard'
    

    def get_polygon_points(self, side_to_get = None, polygon_type = None):
        if (side_to_get == None):
            side_to_get = self.current_side

        if (polygon_type == None):
            polygon_type = self.current_polygon_type

        polygons = []
        for side_letter in self.cube:
            side = self.cube[side_letter]
            if (self.sides_dictionary[side_letter] == self.sides_dictionary[side_to_get]):
                for sticker_letter in side:
                    polygons.append(side[sticker_letter].get_polygon_points(polygon_type))

        return polygons


    def add_point_to_current_polygon(self, point):
        self.current_polygon.add_point(point, self.current_polygon_type)

        
    def remove_point_from_current_polygon(self):
        self.current_polygon.remove_point(self.current_polygon_type)


    def clear_current_polygon(self):
        self.current_polygon.clear_polygon_points(self.current_polygon_type)
        self.cube[self.current_side][self.current_polygon_address].clear_polygon_points(self.current_polygon_type)
    
    
    def clear_all_polygons(self):
        for side_letter in self.cube:
            side = self.cube[side_letter]
            for sticker_address in side:
                self.cube[side_letter][sticker_address].clear_polygon_points(self.current_polygon_type)


    def get_colors(self, image_0, image_1):
        sides_for_camera = {'f':image_0, 'd':image_0, 'l':image_0, 'b':image_1, 'u':image_1, 'r':image_1}
        cube_position = {'f':[],
                         'b':[],
                         'u':[],
                         'd':[],
                         'l':[],
                         'r':[]}
        for side in self.cube:
            for piece in self.cube[side]:
                print(piece)
                color = self.cube[side][piece].get_color(sides_for_camera[side])
                print('color:', color)
                cube_position[side].append(color)

        return cube_position


    def calibrate_side(self, image, side, color_side):
        for sticker in range(1,10):
            self.cube[side][side + str(sticker)].calibrate_color(image, color_side)


    def calibrate_sides(self, image, sides_to_color_sides):
        for side in colors_to_sides:
            self.calibrate_sides(image, side, sides_to_color_sides[side])

    def get_current_polygon_address(self):
        return self.current_polygon_address

    def convert_color_from_lab_to_bgr(self, color):
        input = color
        color = np.uint8([[color]])
        color = cv2.cvtColor(color, cv2.COLOR_LAB2BGR)
        color = (int(color[0][0][0]), int(color[0][0][1]), int(color[0][0][2]))
        return color


    def get_thresholds(self):
        side_order = ['r', 'l', 'u','d', 'f','b']
        thresholds = {}
        for side in side_order:
            thresholds[side] = {'r':[],
                                'l':[],
                                'u':[],
                                'd':[],
                                'f':[],
                                'b':[]}

            for sticker_number in range(1,10):
                for color in side_order:
                    sticker = self.cube[side][side + str(sticker_number)]
                    single_threshold = sticker.thresholds[color]
                    lower_limit = single_threshold['lower_limit']
                    upper_limit = single_threshold['upper_limit']

                    #lower_limit = self.convert_color_from_lab_to_bgr(upper_limit)
                    #upper_limit = self.convert_color_from_lab_to_bgr(lower_limit)

                    thresholds_to_add = {'lower_limit': lower_limit, 'upper_limit':upper_limit}
                    thresholds[side][color].append(thresholds_to_add)
        return thresholds
    
    def set_thresholds(self, thresholds):
        side_order = ['r', 'l', 'u','d', 'f','b']
        for side in side_order:
            for sticker_number in range(1,10):
                for color in side_order:
                    self.cube[side][color].thresholds = thresholds[side][color]

    def save_polygons(self):
        polygon_types = ['calibration','standard']
        polygons = {}

        #iterates over all the polygons and stores them in var polygons
        for side in self.cube:
            polygons[side] = {}
            cube_side = self.cube[side]

            for sticker in self.cube[side]:
                polygons[side][sticker] = {}
                cube_sticker = cube_side[sticker]

                for polygon_type in polygon_types:
                    polygons[side][sticker][polygon_type] = cube_sticker.get_polygon_points(polygon_type)

        #saves var polygons in polygon_saves.p
        pickle.dump(polygons, open( "polygons_save.p", "wb" ))


    def load_polygons(self):
        #loads save file
        polygons = pickle.load(open( "polygons_save.p", "rb" ))

        #iterates over all the polygons and sets them to the class
        for side in polygons:
            polygons_side = polygons[side]

            for sticker in polygons_side:
                polygons_sticker = polygons_side[sticker]

                for polygon_type in polygons_sticker:
                    polygon = polygons_sticker[polygon_type]

                    self.cube[side][sticker].set_polygon_points(polygon, polygon_type)
    
    def save_colors(self):
        thresholds = self.get_thresholds()

        #saves var polygons in polygon_saves.p
        pickle.dump(thresholds, open( "colors_save.p", "wb" ))


    def load_colors(self):
        #loads save file
        thesholds = pickle.load(open( "colors_save.p", "rb" ))

        self.set_thresholds(thesholds)
                    
    

        
    
        