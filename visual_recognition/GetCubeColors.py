import cv2
import pickle
import time
import UseWebCam
import numpy as np



def LoadPolySaves():
    saveFile = open("polysSaves.pickle","rb")
    polys = pickle.load(saveFile)
    return polys

def LoadThresholdSaves():
    saveFile = open('thresholdsSaves.pickle','rb')
    Thresholds = pickle.load(saveFile)
    return Thresholds
    
polygons = LoadPolySaves()


cameraTiles = ((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,49,50,51),(25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54))
colorNumbers = ['white','blue','red','green','orange','yellow']


def GetPixels(frame,polygon):
    #defines area to scan in
    boundryBox = GetBoundryBox(polygon)
    #converts the frame into hsv which allows for more precise image color manipulation
    frame = ConvertToHsv(frame)
    #takes hsv and masks out the area that is not within the polygon
    mask = CreateMask(frame,polygon)
    #creates a threshold based of the inside of the polygon
    cubeColors = ScanPolygon(mask,polygon,boundryBox,frame)
    return cubeColors
    
    
#type 2    
def GetBoundryBox(points):
    BoundryBox = [[1000,1000],[0,0]]
    for point in points:
        if point[0] < BoundryBox[0][0]:
            BoundryBox[0][0] = point[0]
        if point[0] >BoundryBox[1][0]:
            BoundryBox[1][0] = point[0]
        if point[1] < BoundryBox[0][1]:
            BoundryBox[0][1] = point[1]
        if point[1] >BoundryBox[1][1]:
            BoundryBox[1][1] = point[1]
    return BoundryBox
    
#type 2
def ConvertToHsv(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return frame

#type 2
def CreateMask(frame,polygon):
    mask = cv2.inRange(frame, (255,255,255), (0,0,0))
    mask = RenderFilledPoly(mask,polygon)
    result = cv2.bitwise_and(frame,frame, mask=mask)
    return result

#type 3
def RenderFilledPoly(frame,polygon):
    polygon = np.array(polygon,np.int32)
    polygon = polygon.reshape((-1,1,2))
    cv2.fillConvexPoly(frame,polygon,255)
    return frame


#type 2
def ScanPolygon(mask,polygon,boundryBox,frame):
    allColors = []
    multiplier = 2
    counter = 0
    for x in range(boundryBox[0][0],boundryBox[1][0]):
        for y in range(boundryBox[0][1],boundryBox[1][1]):
            if multiplier-1 == counter:
                counter = 0
                if (mask[y,x][0] == 0 and mask[y,x][1] == 0 and mask[y,x][2] == 0) or (mask[y,x][0] == 255 and mask[y,x][1] == 255 and mask[y,x][2] == 255) or (mask[y,x][0] == 0 and mask[y,x][1] == 1 and mask[y,x][2] == 0):
                    pass
                else:
                    allColors.append([mask[y][x][0],mask[y][x][1],mask[y][x][2]])
                    counter +=1
    return allColors

def GetCubeColors(pictures):
    cubePixelColors = []
    for sticker in range(1,55): 
            print(sticker)
            
            polygon = polygons[sticker]
            if sticker in cameraTiles[0]:
                pixels = GetPixels(pictures[1],polygon)
            else:
                pixels = GetPixels(pictures[0],polygon)
            cubePixelColors.append(pixels)
    return cubePixelColors

def GetSum(array):
    sum = 0
    for number in array:
        sum += number
    return sum

def GetDifference(array1,array2):
    array3 = []
    for position in range(0,len(array1)):
        array3.append(abs(array1[position]-array2[position]))
    return array3

def IsPixelInLimit(pixel,upperLimit,lowerLimit,offset):
        if (pixel[0] >= (lowerLimit[0]-offset) and pixel[1] >= (lowerLimit[1]-offset) and pixel[2] >= (lowerLimit[2]-offset)) and (pixel[0] <= (upperLimit[0]+offset) and pixel[1] <= (upperLimit[1]+offset) and pixel[2] <= (upperLimit[2]+offset)):
            return True
        else:
            return False
    
def scores_lower_than_100(scores):
    
    for score in scores:
        if score >= 100:
            print("returned true")
            print("scores",scores)
            return False
    return True

    
def CalculateCubeColors():
    pictures = UseWebCam.TakePictures()
    '''
    while True:
        cv2.imshow('picture 0 ',pictures[0])
        cv2.imshow('picture 1 ',pictures[1])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    '''
    i = 0
    cubePosition = []
    allScores = []
    cubePixelColors = GetCubeColors(pictures)
    thresholds = LoadThresholdSaves()
    print('length',len(cubePixelColors))
    for sticker in cubePixelColors:
        scores = [0,0,0,0,0,0]
        offset = 0
        while scores_lower_than_100(scores):
            offset +=5
            for pixel in sticker:
                averageScores = []
                for color in range(0,6):
                    lowerLimit = thresholds[i + 1][color][1]
                    upperLimit = thresholds[i + 1][color][0]
                    average = thresholds[i + 1][color][2]
                    if IsPixelInLimit(pixel,upperLimit,lowerLimit,offset):
                        scores[color] += 1
            #print(averageScores)    
        i+=1
        print('scores',scores)
        allScores.append(scores)
        
        
        highest = max(scores)
        #print('highest',highest)
        for color in range(0,6):
            if scores[color] == highest:
                stickerColor = colorNumbers[color]
        cubePosition.append(stickerColor)
        
    print(stickerColor,i)
    print(cubePosition)
    return cubePosition,allScores


def main():
    cubePosition,scores = CalculateCubeColors()
    newCubePosition = []
    for sticker in cubePosition:
        newCubePosition.append(sticker[:1])
    print(newCubePosition)
    return newCubePosition


if __name__ == '__main__':
    print('start')
    print(main())
    print('end')