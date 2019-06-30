import cv2
import pickle
import time
import UseWebCam
import numpy as np



def Load_poly_saves():
    global polys
    save_file = open("polysSaves.pickle","rb")
    polys = pickle.load(save_file)
    return polys





text = ['rotate(r)','rotate(r)','rotate(r),rotate(x)','rotate(r)','rotate(r)','press ENTER to finish']
polygons = Load_poly_saves()
camera_tiles = ((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,49,50,51),(25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54))
side_tiles = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,49:0,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1,50:1,17:2,18:2,19:2,20:2,21:2,22:2,23:2,24:2,51:2,25:3,26:3,27:3,28:3,29:3,30:3,31:3,32:3,52:3,33:4,34:4,35:4,36:4,37:4,38:4,39:4,40:4,53:4,41:5,42:5,43:5,44:5,45:5,46:5,47:5,48:5,54:5}

side_color_order = ['012345','340251','253014','521430','435102','104523']



threshold_saves = {}
for i in range(1,55):
    threshold_saves[i] = {}
    for k in range(0,6):
        threshold_saves[i][k] = []
        
print (threshold_saves)
        
#type 1
def Get_threshold(frame,polygon):
    #defines area to scan in
    boundry_box = Get_boundry_box(polygon)
    #converts the frame into hsv which allows for more precise image color manipulation
    frame = Convert_to_hsv(frame)
    #takes hsv and masks out the area that is not within the polygon
    mask = Create_mask(frame,polygon)
    #creates a threshold based of the inside of the polygon
    threshold = Scan_polygon(mask,polygon,boundry_box,frame)
    return threshold
    
    
#type 2    
def Get_boundry_box(points):
    boundry_box = [[1000,1000],[0,0]]
    for point in points:
        if point[0] < boundry_box[0][0]:
            boundry_box[0][0] = point[0]
        if point[0] >boundry_box[1][0]:
            boundry_box[1][0] = point[0]
        if point[1] < boundry_box[0][1]:
            boundry_box[0][1] = point[1]
        if point[1] >boundry_box[1][1]:
            boundry_box[1][1] = point[1]
    return boundry_box
    
#type 2
def Convert_to_hsv(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return frame

#type 2
def Create_mask(frame,polygon):
    mask = cv2.inRange(frame, (255,255,255), (0,0,0))
    mask = Render_filled_poly(mask,polygon)
    result = cv2.bitwise_and(frame,frame, mask=mask)
    return result

#type 3
def Render_filled_poly(frame,polygon):
    polygon = np.array(polygon,np.int32)
    polygon = polygon.reshape((-1,1,2))
    cv2.fillConvexPoly(frame,polygon,255)
    return frame

def Render_poly(frame,points):
    
    points = np.array(points,np.int32)
    points = points.reshape((-1,1,2))
    cv2.polylines(frame,[points],True,(255,255,255))
    return frame

def mouse_callback(event,x,y,flags,params):
    if event ==1:
        print(x,',',y)
#type 2
def Scan_polygon(mask,polygon,boundry_box,frame):
    upperLimit = [0,0,0]
    lowerLimit = [255,255,255]
    average = [0,0,0]
    count = 0
    partialAverage = [0,0,0]
    multiplier = 1
    for x in range(round(boundry_box[0][0]),round(boundry_box[1][0])):
        for y in range(round(boundry_box[0][1]),round(boundry_box[1][1])):
            count +=1
            if x % multiplier == 0:
                if y % multiplier == 0:
                    if (mask[y,x][0] <= 30 and mask[y,x][1] <= 30 and mask[y,x][2] <= 30) or (mask[y,x][0] == 255 and mask[y,x][1] == 255 and mask[y,x][2] == 255):
                        pass
                    else:
                        for i in range(0,3):
                            partialAverage[i] += mask[y,x][i]
                            
                            if mask[y,x][i] >  upperLimit[i]:
                                upperLimit[i] = mask[y,x][i]
                            
                            if mask[y,x][i] < lowerLimit[i]:
                                lowerLimit[i] = mask[y,x][i]
                        if (mask[y,x][0] <= 10) or (mask[y,x][1] <= 10) or (mask[y,x][2] <= 10):
                            #print(mask[y,x])
                            pass
    #print(average)
    for i in range(0,3):
        average[i] = int(round(partialAverage[i]/count))
    '''
    print(partialAverage)
    
    averageImage = np.zeros((300,512,3), np.uint8)
    averageImage[:] = average
    lowerImage = np.zeros((300,512,3), np.uint8)
    lowerImage[:] = lowerLimit
    upperImage = np.zeros((300,512,3), np.uint8)
    upperImage[:] = upperLimit
    print(polygon)
    while True:
        cv2.imshow('averageImage',averageImage)
        cv2.imshow('lowerLimit',lowerImage)
        cv2.imshow('upperLimit',upperImage)
        cv2.imshow('mask',mask)
        polyFrame = Render_poly(frame,polygon)
        cv2.setMouseCallback('frame', mouse_callback)
        cv2.imshow('frame',polyFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    '''
    return [upperLimit,lowerLimit,average]

def SaveThreshold(threshold,sticker,rotation):
    global threshold_saves,side_tiles,side_color_order
    threshold_saves[sticker][int(side_color_order[rotation][side_tiles[sticker]])] = threshold

def Save(thresholds):
    save_file = open("thresholdsSaves.pickle","wb")
    pickle.dump(thresholds,save_file)
    save_file.close()

for rotation in range(0,6):
    pictures = UseWebCam.TakePictures()
    for sticker in range(1,55): 
        print(sticker)
        polygon = polygons[sticker]
        if sticker in camera_tiles[0]:
            threshold = Get_threshold(pictures[1],polygon)
        else:
            threshold = Get_threshold(pictures[0],polygon)
        SaveThreshold(threshold,sticker,rotation)
    print('threshold_saves',threshold_saves)
    input(text[rotation])


thresholds = {'u':[[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)]],
              'd':[[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)]]
              'l':[[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)]]
              'r':[[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)]]
              'f':[[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)]]
              'b':[[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)],[(255,0,0),(255,127),(255,255,255)]]
              }

Save(threshold_saves)
pictures = UseWebCam.TakePictures()
frame = pictures[0]
tileCount = 1
for tile in range(1,55):
    colorsCount = 0
    for colors in range(0,6):
        typeCount = 0
        for type in range(0,3):
            #print(tileCount,'tilecount',colorsCount,'colorscount',typeCount,'typecount')
            mainRow = 0
            y = tileCount*25
            if tileCount > 27:
                mainRow = 450
                y = y-675
            colorRow = 0
            colorRow = int(colorsCount) * 75
            typeRow = typeCount*25
            x = mainRow+colorRow+typeRow
        
            
            color = (int(threshold_saves[tileCount][colorsCount][typeCount][0]),int(threshold_saves[tileCount][colorsCount][typeCount][1]),int(threshold_saves[tileCount][colorsCount][typeCount][2]))
            #print(color)
            cv2.rectangle(frame,(x,y),(x+25,y+25),color ,-1)
            typeCount +=1
        colorsCount+=1
    tileCount+=1
            
            
        
while True:
    cv2.imshow('averageImage',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
print('done')
    
    
