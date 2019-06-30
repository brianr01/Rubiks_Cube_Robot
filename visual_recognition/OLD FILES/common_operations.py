import cv2
import numpy as np

#def get_pixels_in_polygon(points, image, mask = None):

points = [[100, 100],[128, 100],[140, 150],[100,167]]

image = cv2.imread('gitgupphoto.jpg', 1)
mask = np.zeros((image.shape[0],image.shape[1],1), np.uint8)
mask[:] = 0

def draw_polygon(image, points ):
    polygon = np.array(points,np.int32)
    polygon = polygon.reshape((-1,1,2))
    cv2.fillConvexPoly(image, polygon, 255)
    return image







def get_mask_with_color(image, mask, limits):
    mask = cv2.inRange(image, limits['lower'], limits['upper'])
    
    return mask_with_color





mask = draw_polygon(mask, points)
#image = cv2.bitwise_and(image, image, mask=mask)
while True:
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



print (cv2.mean(image, mask))




def get_line_of_pixels(image, point, length):
    pixels = []
    if point[0] + length > image.shape[0]:
        raise Exception('Error: The starting point plus the length of the line was greater than the size of the image.')
    for pixel in range(0, length):
        pixels.append(image[point[0] + length, point[1]])
    return pixels


#input
#   pixels - an array of colored pixels with lab colorspace
#   
#output
#   upper_limit - the max values for the colors with L fixed at 255
#   average  - the average of all the colors
#   lower_limit - the min values for the colors with L fixed at 0





def is_pixel_in_limit(pixel, limits):
    lower_limit = limits['lower']
    upper_limit = limits['upper']
    for i in range(0,3):
        if (pixel[i] < lower_limit[i]):
            return False

    for i in range(0,3):
        if (pixel[i] > upper_limit[i]):
            return False

    return True








#def calculate_upper_limit_average_and_lower_limit_for_lab(pixels):



#   def Create_mask(frame,polygon):



    
