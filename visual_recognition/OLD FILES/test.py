import cv2
import numpy as np
#creates large boundry box to start off with
points = [[152,215],[204,200],[193,156]]
boundary_box = [points[0],points[0]]
image = np.zeros((600,600,3), np.uint8)
formatted_points = np.array(points,np.int32)
formatted_points = formatted_points.reshape((-1,1,2))
cv2.fillConvexPoly(image, formatted_points, (255, 0, 0))


#expands the size of the boundary box until it fits the exact size of the polygon
for point in points:
    print(boundary_box)
    print(point)
    for coordinate_type in range(0,2):  
        if (point[coordinate_type] < boundary_box[0][coordinate_type]):
            boundary_box[0][coordinate_type] = int(point[coordinate_type])

        elif (point[coordinate_type] > boundary_box[1][coordinate_type]):
            boundary_box[1][coordinate_type] = int(point[coordinate_type])
            
        if (point[coordinate_type] > boundary_box[0][coordinate_type]):
            boundary_box[0][coordinate_type] =+ int(point[coordinate_type])

        elif (point[coordinate_type] < boundary_box[1][coordinate_type]):
            boundary_box[1][coordinate_type] =+ int(point[coordinate_type])
            
if points != []:
    point1 = (int(boundary_box[0][0]), int(boundary_box[0][1]))
    point2 = (int(boundary_box[1][0]), int(boundary_box[1][1]))
    cv2.rectangle(image, point1, point2, (0,255,0),3)
    cv2.imshow('frame', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
