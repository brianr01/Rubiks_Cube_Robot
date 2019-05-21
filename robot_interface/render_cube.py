#this class generates an image of a cube based of of a position
import numpy as np
import cv2


faces_to_colors = {'u':(255,255,255), 'f':(0,255,0), 'r':(0,0,255), 'l':(0,100,255), 'd':(0,255,255), 'b':(255,0,0)}
points = {'u':[[87, 58], 
               [116, 58], 
               [145, 58],  
               [87, 87], 
               [116, 87], 
               [145, 87], 
               [87, 116], 
               [116, 116], 
               [145, 116]], 

    'f':
        [[87, 145], 
        [116, 145], 
        [145, 145], 
        [87, 174], 
        [116, 174], 
        [145, 174], 
        [87, 203], 
        [116, 203], 
        [145, 203]],
    'r':
        [[174, 145], 
        [203, 145], 
        [232, 145], 
        [174, 174], 
        [203, 174], 
        [232, 174], 
        [174, 203], 
        [203, 203], 
        [232, 203]],
    'l':
        [[0, 145], 
        [29, 145], 
        [58, 145], 
        [0, 174], 
        [29, 174], 
        [58, 174], 
        [0, 203], 
        [29, 203], 
        [58, 203]], 
    'd':
        [[87, 232], 
        [116, 232], 
        [145, 232], 
        [87, 261], 
        [116, 261], 
        [145, 261], 
        [87, 290], 
        [116, 290], 
        [145, 290]],
    'b':
        [[145, 377], 
        [116, 377], 
        [87, 377], 
        [145, 348], 
        [116, 348], 
        [87, 348], 
        [145, 319], 
        [116, 319], 
        [87, 319]]}


def render_cube(position):

    frame = np.zeros((400,266,3), np.uint8)
    frame[:] = (0, 0, 0)
    for side in position:
        for sticker in position[side]:

            point_1 = points[sticker[0]][int(sticker[1])-1]
            point_2 = [points[sticker[0]][int(sticker[1])-1][0] + 29 , points[sticker[0]][int(sticker[1])-1][1] + 29]
            cv2.rectangle(frame, (point_1[0], point_1[1] - 20) ,(point_2[0], point_2[1] - 20), (0,0,0), -1)
            cv2.rectangle(frame, (point_1[0]+2, point_1[1] - 18) ,(point_2[0]-2, point_2[1] - 22), faces_to_colors[side], -1)
    return frame
