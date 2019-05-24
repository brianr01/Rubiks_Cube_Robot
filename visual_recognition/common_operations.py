import cv2


def get_pixels_in_polygon(points, image, mask = None):


def draw_polygon(points, type = 'filled_with_color'):
    #types = filled_with_color a polygon filled with one color
    #types = filled a polygon filled with white pixels
    #should handle concave polygons



#input = points of a polygon
#output the points of a box that perfectly fit the polygon
#input = [[10,10],[20,10],[21,10],[20,20],[10,20]]
#output = [[10, 10], [21, 20]
#output example [[xmin, ymin], [xmax, ymax]]
def get_polygon_boundry_box():


#inputs
#    image - the image to get the pixels of
#    point - the point where the line starts
#    length - how long the line is
# 
#    
#return a list of all of the pixels in the path of the line
def get_line_of_pixels():

#input
#   pixels - an array of colored pixels with lab colorspace
#   
#output
#   upper_limit - the max values for the colors with L fixed at 255
#   average  - the average of all the colors
#   lower_limit - the min values for the colors with L fixed at 0
def calculate_upper_limit_average_and_lower_limit_for_lab(pixels):



def Create_mask(frame,polygon):


def is_pixel_in_limit(pixel, limits):
    
