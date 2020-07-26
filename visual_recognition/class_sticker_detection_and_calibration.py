import cv2
import numpy as np
import statistics
import pickle
import sys
import time

print("Loading Tensorflow and ML model.")
print("\u001b[30m")
import tensorflow as tf
model = tf.keras.models.load_model("cube_ai_model_9995")
CATEGORIES = ['u','d','l','r','f','b']
print("\u001b[37m")
print("Finished loading Tensorflow and ML model.")


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

            boundary_box = [[int(min(x_points)), int(min(y_points))],
                            [int(max(x_points)), int(max(y_points))]]

            return boundary_box


    def get_color(self, image, polygon_points = None):
        return self.get_color_prediction_for_image(
            self.format_image(
                self.get_resized_sticker_image(image, polygon_points)
            )
        )


    def get_resized_sticker_image(self, image, polygon_points = None):
        if (polygon_points == None):
            polygon_points = self.polygon_points

        self.current_color = 0
        
        boundary_box = self.get_polygon_boundary_box(polygon_points)
        image = cv2.resize(
            cv2.cvtColor(
                image[boundary_box[0][1]:boundary_box[1][1],
                boundary_box[0][0]:boundary_box[1][0]],
                cv2.COLOR_LAB2BGR
            ).astype('float32'),
            (50, 50)
        )

        return image
    
    def format_image(self, image):
        return np.array((image / 255.0)).reshape(-1, 50, 50, 3)


    def get_color_prediction_for_image(self, image):
        predictions = model.predict([image])[0].tolist()

        self.current_color = CATEGORIES[predictions.index(max(predictions))]

        return self.current_color


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
