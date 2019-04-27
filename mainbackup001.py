import pickle
import cv2 
import numpy as np
import time  
import ScanImageForClustersOfPixel as Scan
resolution = [1080,1080]
threshold = 500


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
        time.sleep(.001)
       
    frame0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2HSV)
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    
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
frame0 = cv2.cvtColor(pictures[0], cv2.COLOR_HSV2BGR)
#mask = cv2.inRange(frame0,0,255)
#pts = np.array([(515,55),(217,208),(280,472),(506,687),(746,479),(805,203)],np.int32)
#cv2.fillPoly(mask,[pts],255)
#frame0 = cv2.bitwise_and(frame0,frame0, mask= mask)     
saves = GetSaves()
print(saves)

mask0 = cv2.inRange(pictures[0], saves[0]['orange']['lowerLimit'], saves[0]['orange']['upperLimit'])


mask1 = cv2.inRange(pictures[0], saves[0]['pink']['lowerLimit'], saves[0]['pink']['upperLimit'])

mask2 = cv2.inRange(pictures[0], saves[0]['yellow']['lowerLimit'], saves[0]['yellow']['upperLimit'])

mask3 = cv2.inRange(pictures[0], saves[0]['green']['lowerLimit'], saves[0]['green']['upperLimit'])

mask4 = cv2.inRange(pictures[0], saves[0]['blue']['lowerLimit'], saves[0]['blue']['upperLimit'])
mask5 = cv2.inRange(pictures[0], saves[0]['purple']['lowerLimit'], saves[0]['purple']['upperLimit'])
cv2.imshow('mask0',mask0)
cv2.imshow('mask1',mask1)
cv2.imshow('mask2',mask2)
cv2.imshow('mask3green',mask3)
cv2.imshow('mask4',mask4)
cv2.imshow('mask5',mask5)
mask7 = mask0 +mask1

mask8 = mask7 + mask2

mask9 = mask8 + mask3

mask10 = mask9 + mask4

mask11 = mask10 + mask5
cv2.imshow('mask0+1+2+3+4+5',mask11)
cv2.imshow('frame',frame0)
cv2.waitKey(0)
cv2.destroyAllWindows()
colors = ('pink','orange','blue','green','purple','yellow')
Scan.GetAveragePoints(mask11,threshold)
cv2.waitKey(0)



cv2.destroyAllWindows()

