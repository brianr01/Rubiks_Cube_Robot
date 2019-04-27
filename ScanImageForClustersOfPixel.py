from GroupClass import Group
import cv2
import numpy as np



'''

'''





#scans through a single line of pixels and makes 1 dimensonal and groups those who are are touching eachother
def ScanThroughLine(picture,debug = False):
    #when debug is equal to true print statements throughout this function will print usefull data to debug
    #creates new groups for the picture
    groups = []
    for x in range(0,len(picture)-1):
        print(x)
        if debug == True:
            print('--------',y,'-------')
            print(y)
        for y in range(0,len(picture[0])-1):

            if debug == True:
                print('--',x,'--')
                print("pixel:",picture[x][y])

            if picture[x][y] == 255:

                if debug == True:
                    print('colored: True')

                if Group.GetGroupWithPixel([x,y]) == False:

                    if debug == True:
                        print('added to group: True')

                    groups.append(Group())
                    groups[-1].SetPixel([x,y])

                else:

                    if debug == True:
                        print('added to group:False')

                if picture[x+1][y] == 255:

                    if debug == True:
                        print('pixel to right:Colored')

                    groups[Group.GetGroupWithPixel([x,y])].SetPixel([x+1,y])

                else:

                    if debug == True:
                        print('pixel to right:Blank')

            else:

                if debug == True:
                    print('colored: False')

    if debug == True:
        print('################ FIRST SECTION DONE #########################')

    for x in range(0,len(picture)-1):
        print(x)
        if debug == True:
            print('===================',y,'=======================')
            
        for y in range(0,len(picture[0])-1):
            if debug == True:
                print('===========',x,'=========')
                print('pixel:',picture[x][y])
                print('pixel y+1:',picture[x][y+1])
            if picture[x][y] == 255 and picture[x][y+1] == 255:
                if Group.GetGroupWithPixel([x,y]) != Group.GetGroupWithPixel([x,y+1]):
                    if debug == True:
                        print("Inherited: True")
                    groups[Group.GetGroupWithPixel([x,y])].InheritGroup(groups[Group.GetGroupWithPixel([x,y+1])])
                else:
                    if debug == True:
                        print("Inherited: False")
    if debug == True:
        print('done!')

    return groups


def GetAveragePoints(frame,threshold):
    '''
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, limits['lowerLimit'], limits['upperLimit'])
    res = cv2.bitwise_and(frame,frame, mask= mask)
    '''
    groups =  ScanThroughLine(frame)
    for group in groups:
        pixels = group.GetPixels()
        if group.GetCountInGroup() >= threshold:
            x = 0
            y = 0
            for pixel in pixels:
                x += pixel[0]
                y += pixel[1]
            if x + y != 0:
                xAverage = x/group.GetCountInGroup()
                yAverage = y/group.GetCountInGroup()
                print('----')
                print(group.GetCountInGroup(),'amount of pixels in group')
                print(round(xAverage),round(yAverage),'AVERAGE POINTS')
                print('----')
                cv2.circle(frame,(round(yAverage),round(xAverage)),5,(255,255,255) , -1)
                cv2.circle(frame,(round(yAverage),round(xAverage)),5,(0,0,0) , 2)
                print('#####################')
    #clears Group Data
    Group.count = 0
    Group.pixelsToGroup = {}
    groups = {}


    '''
    cv2.imshow("res",res)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    '''
    cv2.imshow("frame",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
