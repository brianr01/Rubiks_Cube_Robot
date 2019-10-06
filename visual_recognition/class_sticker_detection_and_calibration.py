import cv2
import numpy as np
import statistics
import pickle

class Sticker_Detection_And_Calibration:
    def __init__(self, sticker_name):
        self.name = sticker_name
        self.polygon_points = []
        self.calibration_polygon_points = []
        self.current_color = [0, 0, 0]
        white = cv2.cvtColor( np.uint8([[(255,255,255)]] ), cv2.COLOR_BGR2LAB)[0][0]
        black = cv2.cvtColor( np.uint8([[(0,0,0)]] ), cv2.COLOR_BGR2LAB)[0][0]
        self.thresholds = {'u': {'lower_limit':black, 'upper_limit':white},
                           'd': {'lower_limit':black, 'upper_limit':white},
                           'f': {'lower_limit':black, 'upper_limit':white},
                           'b': {'lower_limit':black, 'upper_limit':white},
                           'l': {'lower_limit':black, 'upper_limit':white},
                           'r': {'lower_limit':black, 'upper_limit':white}}

        self.pixel_count_in_polygon = 0

    def calibrate_color(self, image, side):
        possible_sides = ['u', 'd', 'f', 'b', 'l', 'r']
        if (not(side in possible_sides)):
            raise Exception('error: a invalid side was inputted')
        pixels_in_polygon = self.get_pixels_in_polygon(image, self.calibration_polygon_points)

        #this is used in the method to get the color in the polygon
        self.pixel_count_in_polygon = len(pixels_in_polygon)

        self.thresholds[side] = self.get_threshold_with_pixels(pixels_in_polygon)

    def get_pixels_in_polygon(self, image, polygon_points):
        #all the pixels within the polygon
        pixels = []

        #a box that perfectly encloses the polygon
        boundary_box = self.get_polygon_boundary_box(polygon_points)

        #a mask with the polygon filled in
        mask = self.get_mask_with_filled_polygon(image, polygon_points)

        #a image with the polygon in color
        result = cv2.bitwise_and(image, image, mask=mask)

        #go through each pixel in the boundary box
        for row in range(boundary_box[0][0], boundary_box[1][0]):
            for column in range(boundary_box[0][1], boundary_box[1][1]):
                #if the pixel has color add it to the list
                for i in range(0, 3):
                   if (not(result[column, row][i]  == 0)):
                       pixels.append(result[column, row])
                       break

        return pixels

    def get_polygon_boundary_box(self, points):
            #gets all the points on the x and y axis
            x_points = []
            y_points = []
            for point in points:
                x_points.append(point[0])
                y_points.append(point[1])

            #if there are no points return a box at (0,0), (0,0)
            if (points == []):
                boundary_box = [[0, 0], [0, 0]]

                return boundary_box


            boundary_box = [[int(min(x_points)), int(min(y_points))], [int(max(x_points)), int(max(y_points))]]

            return boundary_box

    def get_mask_with_filled_polygon(self, image, polygon_points):
        #gets the width and the height of the image
        width, height, _ = image.shape

        #creates a blank binary image that is the same size as the inputted image
        mask = np.zeros((width, height, 1), np.uint8)

        #makes the mask blank
        mask[:] = (0)

        #formats the points for the polygon
        polygon_points = np.array(polygon_points,np.int32)
        formated_polygon_points = polygon_points.reshape((-1,1,2))

        #fills in the area within the polygon
        cv2.fillConvexPoly(mask, formated_polygon_points, 255)
        return mask

    def get_threshold_with_pixels(self, pixels):
        thresholds = {'lower_limit':[255,255,255], 'upper_limit':[0, 0, 0]}
        for pixel in pixels:
            #coordinate_type example = (coordinate_type_0, coordinate_type_1, coordinate_type_2) -> (L, A, B) -> (100, 230, 19)
            for color_space_type in range(0,3):
                if (pixel[color_space_type] > thresholds['upper_limit'][color_space_type]):
                    thresholds['upper_limit'][color_space_type] = pixel[color_space_type]

                elif (pixel[color_space_type] < thresholds['lower_limit'][color_space_type]):
                    thresholds['lower_limit'][color_space_type] = pixel[color_space_type]
        return thresholds

    def get_color(self, image, polygon_points = None):
        if (polygon_points == None):
            polygon_points = self.polygon_points

        pixel_counts = {'f':0,
                        'b':0,
                        'u':0,
                        'd':0,
                        'l':0,
                        'r':0}

        max_iterations = 125
        iterations = 0
        min_percent =  .05
        min_pixels = self.pixel_count_in_polygon * min_percent
        #a box that perfectly encloses the polygon
        boundary_box = self.get_polygon_boundary_box(polygon_points)

        #a mask with the polygon filled in
        polygon_mask = self.get_mask_with_filled_polygon(image, polygon_points)

        while (iterations <= max_iterations):
            iterations += 1
            #does a color have enough pixels to make a good guess at what the color is? if so break
            if (self.is_value_in_dictionary_over_x(pixel_counts, 20)):
                break

            #test to see how many pixels of the different colors is in the threshold +/- the iteration
            for side in self.thresholds:
                lower_limit = (0, self.thresholds[side]['lower_limit'][1] - iterations * 2, self.thresholds[side]['lower_limit'][2] - iterations * 2)
                upper_limit = (255, self.thresholds[side]['upper_limit'][1] + iterations * 2, self.thresholds[side]['upper_limit'][2] + iterations * 2)
                pixel_counts[side] = self.get_pixel_count_in_threshold(image, polygon_mask, lower_limit, upper_limit)

        #finds the color with the most valid pixels
        color = self.get_largest_key_value_pair_in_dictionary(pixel_counts)
        self.current_color = color
        print(color, pixel_counts)

        return color

    def is_value_in_dictionary_over_x(self, dictionary, x):
        for key in dictionary:
            if (dictionary[key] >= x):
                return True
        return False

    def get_pixel_count_in_threshold(self, image, polygon_mask, lower_limit, upper_limit):
        threshold_mask = cv2.inRange(image, (lower_limit[0], lower_limit[1], lower_limit[2]), (upper_limit[0], upper_limit[1], upper_limit[2]))

        #mask with only valid colors within the polygon
        mask = cv2.bitwise_and(threshold_mask, polygon_mask)

        #the amount of non zeros in the matrix/mask
        valid_pixels = np.count_nonzero(mask)

        return valid_pixels

    def get_largest_key_value_pair_in_dictionary(self, dictionary):
        largest_key_value_pair = {'key':'', 'value':0}
        for key in dictionary:
            if (dictionary[key] > largest_key_value_pair['value']):
                largest_key_value_pair['key'] = key
                largest_key_value_pair['value'] = dictionary[key]

        return largest_key_value_pair['key']

    def save_thresholds(self):
        thresholds = self.thresholds
        pickle.dump(thresholds, open( "colors_saves/colors_save_" + str(self.name) + ".p", "wb" ))


    def load_thresholds(self):
        thresholds = pickle.load(open( "colors_saves/colors_save_" + str(self.name) + ".p", "rb" ))
        self.thresholds = thresholds

    def get_polygon_points(self, polygon_type):
        if (polygon_type == 'calibration'):
                return self.calibration_polygon_points

        elif (polygon_type == 'standard'):
            return self.polygon_points

        else:
            raise Exception('error: the polygon type inputted was not valid')

    def set_polygon_points(self, polygon_points, polygon_type):
        if (polygon_type == 'calibration'):
            self.calibration_polygon_points = polygon_points

        elif (polygon_type == 'standard'):
            self.polygon_points = polygon_points

        else:
            raise Exception('error: the polygon type inputted was not valid')

    def add_point(self, point, polygon_type):
        if (polygon_type == 'calibration'):
            self.calibration_polygon_points.append(point)

        elif (polygon_type == 'standard'):
            self.polygon_points.append(point)

        else:
            raise Exception('error: the polygon type inputted was not valid')

    def remove_point(self, polygon_type):
        if (polygon_type == 'calibration'):
            if (self.calibration_polygon_points != []):
                del self.calibration_polygon_points[-1]

        elif (polygon_type == 'standard'):
            if (self.polygon_points != []):
                del self.polygon_points[-1]

        else:
            raise Exception('error: the polygon type inputted was not valid')

    def clear_polygon_points(self, polygon_type):
        if (polygon_type == 'calibration'):
            self.calibration_polygon_points = []

        elif (polygon_type == 'standard'):
            self.polygon_points = []

        elif (polygon_type == 'both'):
            self.polygon_points = []
            self.calibration_polygon_points = []

        else:
            raise Exception('error: the polygon type inputted was not valid')

    def copy_standard__polygons_to_calibration_polygons(self):
        self.calibration_polygon_points = self.polygon_points
