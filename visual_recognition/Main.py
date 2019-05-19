import pickle
import cv2 
import numpy as np
import time  
import ScanImageForClustersOfPixel014s as Scan
resolution = [720,720]
threshold = 100


##########################
numberOfGroups = 0

# pixelToGroups[x][y]
pixelToGroups = {}
for x in range(0,480):
	pixelToGroups[x] = {}
	for y in range(0,320):
		pixelToGroups[x][y] = 0



groupsToPixels = {}
for i in range(0,100000):
	groupsToPixels[i] = []

numberOfPixelsInGroups = {}
for i in range(0,100000):
	numberOfPixelsInGroups[i] = 0

previousPixel = False


def InputImage(image):
	for x in range(0,480):
		
		for y in range(0,320):
			createGroups(x,y,image)
	print(numberOfGroups)
currentGroup = 0
#######################			




def createGroups(x,y,image):
	global numberOfGroups,pixelToGroups,groupsToPixels,NumberOfPixelsInGroups,previousPixel
	pixelColor = image[x,y]


	if pixelColor[0] != 0 or pixelColor[1] != 0 or pixelColor[2] != 0 :

		if(x - 1 >=0):

			if(previousPixel == True):
				pixelToGroups[x][y] = numberOfGroups
				groupsToPixels[numberOfGroups].append([x,y])
				numberOfPixelsInGroups[numberOfGroups] += 1

			if(previousPixel == False):
				numberOfGroups += 1
				pixelToGroups[x][y] = numberOfGroups
				groupsToPixels[numberOfGroups].append([x,y])
				numberOfPixelsInGroups[numberOfGroups] += 1
				previousPixel = True
		else:
			numberOfGroups += 1
			pixelToGroups[x][y] = numberOfGroups
			groupsToPixels[numberOfGroups].append([x,y])
			numberOfPixelsInGroups[numberOfGroups] += 1
			previousPixel = True
	
	else:
		previousPixel = False


	
	


        



#takes pictures from both web cams
def TakePictures():
    cap0 = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)
    cap0.set(3,resolution[0])
    cap0.set(4,resolution[1])
    cap0.set(28,0)
    cap1.set(3,resolution[0])
    cap1.set(4,resolution[1])
    cap1.set(28,0)
    for i in range(1,100):
        ret0,frame0 = cap0.read()
        ret1,frame1 = cap1.read()
        time.sleep(.01)
    
    return frame0,frame1


def ApplyMask(frame,limits):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #creates mask
    kernel = np.ones((5,5) ,np.uint8)
    erosion = cv2.erode(frame, kernel, iterations = 1)#passes colors through mas'''
    '''
    res = cv2.bitwise_and(frame,frame, mask= mask)
    '''
    mask = cv2.inRange(erosion, limits['lowerLimit'], limits['upperLimit'])
    #show mask
    return mask

def GetSaves():
    saveFile0 = open("SliderSaves0.pickle","rb")
    saves0 = pickle.load(saveFile0)
    saveFile1 = open("SliderSaves1.pickle","rb")
    saves1 = pickle.load(saveFile1)
    return saves0,saves1
	

pictures = TakePictures()
'''
print(sliderSaves,'SLIDERSAVES 0')
frame01 = ApplyMask(pictures[0],sliderSaves['pink'])
frame02= ApplyMask(pictures[0],sliderSaves['orange'])
frame03 = ApplyMask(pictures[0],sliderSaves['green'])
frame04= ApplyMask(pictures[0],sliderSaves['blue'])
frame05 = ApplyMask(pictures[0],sliderSaves['yellow'])
frame06= ApplyMask(pictures[0],sliderSaves['purple'])
sliderSaves = GetSaves(1)
frame07 = ApplyMask(pictures[1],sliderSaves['pink'])
frame08= ApplyMask(pictures[1],sliderSaves['orange'])
frame09 = ApplyMask(pictures[1],sliderSaves['green'])
frame10= ApplyMask(pictures[1],sliderSaves['blue'])
frame11= ApplyMask(pictures[1],sliderSaves['yellow'])

frame12= ApplyMask(pictures[1],sliderSaves['purple'])
'''
saves = GetSaves()
colors = ('pink','orange','blue','green','purple','yellow')
for color in colors:
    Scan.GetAveragePoints(pictures[0],saves[0][color],threshold)    
    Scan.GetAveragePoints(pictures[1],saves[1][color],threshold)

'''
Scan.GetAveragePoints(frame02,threshold)
Scan.GetAveragePoints(frame03,threshold)
Scan.GetAveragePoints(frame04,threshold)
Scan.GetAveragePoints(frame05,threshold)
Scan.GetAveragePoints(frame06,threshold)

Scan.GetAveragePoints(frame07,threshold)
Scan.GetAveragePoints(frame08,threshold)
Scan.GetAveragePoints(frame09,threshold)
Scan.GetAveragePoints(frame10,threshold)
Scan.GetAveragePoints(frame11,threshold)
Scan.GetAveragePoints(frame12,threshold)
'''
'''
#InputImage(frame08)
cv2.imwrite("blob.jpg",frame08)
InputImage(frame11)
while True:
	cv2.imshow('pictures0',pictures[0])
	cv2.imshow('pictures1',pictures[1])
	cv2.imshow('0pink',frame01)
	cv2.imshow('0orange',frame02)
	cv2.imshow('0green',frame03)
	cv2.imshow('0blue',frame04)
	cv2.imshow('0yellow',frame05)
	cv2.imshow('0purple',frame06)
	cv2.imshow('1pink',frame07)
	cv2.imshow('1orange',frame08)
	cv2.imshow('1green',frame09)
	cv2.imshow('1blue',frame10)
	cv2.imshow('1yellow',frame11)
	

	cv2.imshow('1purple',frame12)
	if cv2.waitKey(1) & 0xFF == ord('r'):
		print('r pressed')
		pictures = TakePictures()
		
		frame01 = ApplyMask(pictures[0],sliderSaves['pink'])
		frame02= ApplyMask(pictures[0],sliderSaves['orange'])
		frame03 = ApplyMask(pictures[0],sliderSaves['green'])
		frame04= ApplyMask(pictures[0],sliderSaves['blue'])
		frame05 = ApplyMask(pictures[0],sliderSaves['yellow'])
		frame06= ApplyMask(pictures[0],sliderSaves['purple'])

		frame07 = ApplyMask(pictures[1],sliderSaves['pink'])
		frame08= ApplyMask(pictures[1],sliderSaves['orange'])
		frame09 = ApplyMask(pictures[1],sliderSaves['green'])
		frame10= ApplyMask(pictures[1],sliderSaves['blue'])
		frame11= ApplyMask(pictures[1],sliderSaves['yellow'])

		frame12= ApplyMask(pictures[1],sliderSaves['yellow'])

	if cv2.waitKey(1) & 0xFF == ord('q'):
		print('break triggereed')
		break
'''
cv2.destroyAllWindows()

