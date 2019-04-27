import cv2
import numpy as np
import pickle
cube_image = cv2.imread('cube.jpg',1)
#stores current camera in use
camera = 0
print_out = []
#sets resolution
resolution = [1080,720]
#sets the current camera
cap = cv2.VideoCapture(camera)
#changes the camera's resolution
cap.set(3,resolution[0])
cap.set(4,resolution[1])
#the current polygongon being edited
current_polygon = 1
polygons = {}
#sets the font for the buttons
font = cv2.FONT_HERSHEY_SIMPLEX

upper_limit = [0,0,0]
lower_limit = [255,255,255]

#sets the buttons location color and text
buttons = [(0,'+',(0,0,255)),(50,'-',(255,0,0)),(100,str(current_polygon),(0,255,0)),(150,'Q',(0,0,0)),(200,str(camera),(255,255,0)),(250,'S',(255,255,255)),(300,'L',(100,100,100)),(350,'R',(100,250,100)),(400,'r',(250,250,100)),(450,'L',lower_limit),(500,'U',upper_limit)]

#what polygons appear on what cammera
camera_0_tiles = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,49,50,51)
camera_1_tiles = (25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54)


circle_association = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,21,22,23,24,17,18,19,20,13,14,15,16,9,10,11,12,5,6,7,8,1,2,3,4,25,26,27,27,26,25]
#cirlce locations on cube image
circles = [[65, 57], [136, 38], [205, 19], [241, 43], [289, 78], [218, 95], [147, 110], [105, 78], [165, 161], [239, 145], [305, 131], [303, 200], [306, 278], [233, 295], [163, 310], [163, 231], [29, 99], [71, 132], [110, 156], [110, 232], [108, 305], [69, 273], [33, 240], [32, 174], [175, 65], [230, 217], [69, 199]]
save_file_name = 'polySaves.pickle'

#saves the current state of the polygons
def Save(polygons):
    save_file = open("polySaves.pickle2","wb")
    pickle.dump(polygons,save_file)
    save_file.close()

#loads the save file of the polygons
def Load_saves():
    global polygons
    save_file = open("polySaves.pickle","rb")
    polygons = pickle.load(save_file)

#button hander
def Use_button_at(x,y):
    global polygons
    if y <= 50:
        if x<50:
            Add_to_current_polygon()
        elif 50<x<100:
            Subtract_from_current_polygon()
            
        elif 100<x<150:
            Change_current_polygon()
            
        elif 150<x<200:
            Quit()
        
        elif 200<x<250:
            Change_camera()
        
        elif 250<x<300:
            Save(polygons)
        
        elif 300<x<350:
            Load_saves()
        
        elif 350<x<400:
            polygons = {}
        
        elif 400<x<450:
            polygons[current_polygon] = []
        
        if x<250:
            return True
    
        
    return False
    

def Check_camera_current_polygon():
    global current_polygon
    if current_polygon in camera_0_tiles and camera == 1:
        Change_camera()
    elif current_polygon in camera_1_tiles and camera == 0:
        Change_camera()
    
#adds one to current polygon
def Add_to_current_polygon():
    global current_polygon
    current_polygon += 1
    #when current_polygon is over 54 it wraps it back to 1
    if current_polygon == 55:
        current_polygon = 1
    Check_camera_current_polygon()
    

#subtracts one from current polygon
def Subtract_from_current_polygon():
    global current_polygon
    current_polygon -= 1
    #when current_polygon is under 1 it wraps it back to 54
    if current_polygon == 0:
        current_polygon = 54
    Check_camera_current_polygon()
    
#uses input to change current polygon
def Change_current_polygon():
    global current_polygon
    current_polygon = 'null'
    valid_input = False
    while valid_input != True:
        current_polygon = input('input current polygon ')
        try:
            current_polygon = int(current_polygon)
            if 0<=current_polygon<=54:
                valid_input = True
                print('current_polygon:',current_polygon)
            else:
                print(current_polygon,'is a invalid input please try again')
        except Exception as error:
            print(error,'is a invalid input please try again')
    Check_camera_current_polygon()

#exits the program
def Quit():
    global stop
    stop = True
    cv2.destroyAllWindows()
    cap.release()

#changes from one camera to the other camera
def Change_camera():
    global camera,cap,polygons
    if camera == 1:
        camera = 0
    else:
        camera = 1
    #releases the previous camera
    cap.release()
    #initiates the new camera
    cap = cv2.VideoCapture(camera)
    #sets resolution
    cap.set(3,resolution[0])
    cap.set(4,resolution[1])

    
#mouse handler
def mouse_callback(event,x,y,flags,params):
    global cap,points,print_out,camera,current_polygon,stop,polygons,frame
    #when left click occurs
    if event == 1:
        #check if a button was pressed
        Use_button_at(x,y)
    
    if event == 2:
        #add to the polygon
        polygons[current_polygon].append([x,y])
        print(x,y)
        
  
        
   
    #if middle mouse clicked
    if event == 6 :
        #if there is more than 0 in the polygon remove previous vertex
        if len(polygons[current_polygon]) >=1:
           del polygons[current_polygon][-1]
       
            

        

#renders a button
def Render_button(frame,x,label,color):
    cv2.rectangle(frame,(x,0),(x+50,50),color,-1)
    cv2.putText(frame,label,(x+10,37),font,1,(255,255,255),2,cv2.LINE_AA)
    return frame
    
#renders buttons
def Render_buttons(frame,buttons):
    #renders the buttons
    buttons = [(0,'+',[0,0,255]),(50,'-',(255,0,0)),(100,str(current_polygon),(0,255,0)),(150,'Q',(0,0,0)),(200,str(camera),(255,255,0)),(250,'S',(0,20,255)),(300,'L',(100,100,100)),(350,'R',(100,250,100)),(400,'r',(250,250,100))]
    for button in buttons:
        Render_button(frame,button[0],button[1],button[2])
    return frame

#render circle on cube image
def Render_circle(frame,point,selected):
    #if circle is the current polygon color it red otherwise color it wite
    if selected == True:
        color = [0,0,255]
    else:
        color = [255,255,255]

    cv2.circle(frame,(point[0],point[1]),10,(0,0,0),-1)
    cv2.circle(frame,(point[0],point[1]),8,color,-1)
    return frame

#render circles on cube image
def Render_circles(frame,circles,current_polygon):
    #iterates through all circles
    for circle in circles:
        frame = Render_circle(frame,circle,False)
    frame = Render_circle(frame,circles[circle_association[current_polygon-1]-1],True)
    return frame

def RenderFilledpolygon(frame,points):
    points = np.array(points,np.int32)
    points = points.reshape((-1,1,2))
    cv2.fillConvexPoly(frame,points,255)
    return frame

def Renderpolygon(frame,points):
    points = np.array(points,np.int32)
    points = points.reshape((-1,1,2))
    cv2.polylines(frame,[points],True,(255,255,255))
    return frame
    
def Renderpolygons(frame,polygons):
    for i in range(1,55):
        if i in polygons:
            if camera == 0 and i in camera_0_tiles:
                frame = Renderpolygon(frame,polygons[i])
            if camera == 1 and i in camera_1_tiles:
                frame = Renderpolygon(frame,polygons[i])
        else:
            polygons[i] = []
    return frame

def mouse_callback_2(event,x,y,flags,params):
    global print_out
    if event == 1:
        print_out.append([x,y])
        
    if event == 2:
        print(print_out)
        
    if event == 6:
        print_out = []
        print('6')



def GetSampleArea():
    bigX = 0
    smallX = resolution[0]
    bigY = 0
    smallY = resolution[1]
    for point in polygons[current_polygon]:
        if point[0] > bigX:
            bigX = point[0]
        
        if point[0] < smallX:
            smallX = point[0]
        
        if point[1] > bigY:
            bigY = point[1]
        
        if point[1] < smallY:
            smallY = point[1]
    points = []
    points.append([smallX,smallY])
    points.append([bigX,bigY])
    return points

def ScanSampleArea(maskPoints,mask,frame):
    global upper_limit,lower_limit
    upper_limit = [0,0,0]
    lower_limit = [255,255,255]
    for x in range(maskPoints[0][0],maskPoints[1][0]):
        for y in range(maskPoints[0][1],maskPoints[1][1]):
            if (frame[y,x][0] == 0 and frame[y,x][1] == 0 and frame[y,x][2] == 0) or (frame[y,x][0] == 255 and frame[y,x][1] == 255 and frame[y,x][2] == 255):
                pass
            
            else:
                for i in range(0,3):
                    if frame[y,x][i] >  upper_limit[i]:
                        upper_limit[i] = frame[y,x][i]
                    
                    if frame[y,x][i] < lower_limit[i]:
                        lower_limit[i] = frame[y,x][i]
    print(upper_limit,lower_limit,'upper,lower')
    return upper_limit,lower_limit

stop = False
#main
lowerColor = (0,0,0)
upperColor = (255,255,255)
while stop == False:
    
    #takes frame from current camera
    ret, frame = cap.read()
    
    #setup using mouse clicks as input
    cv2.setMouseCallback('frame', mouse_callback)
    #renders buttons on frame
    frame = Render_buttons(frame,buttons)
    frame = Renderpolygons(frame,polygons)
    cubeFrame = cube_image
    #frame = RenderTiles(frame,tiles)
    cubeFrame = Render_circles(cube_image,circles,current_polygon)
    cv2.setMouseCallback('cube', mouse_callback_2)
    cv2.imshow('cube',cube_image)
    #shows image
    cv2.imshow('frame',frame)

    
    mask = cv2.inRange(frame,lowerColor,upperColor)
    RenderFilledpolygon(mask,polygons[current_polygon])
    #emergency quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


Quit()
    
