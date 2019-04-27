#this class is for assinging groups of pixels
class Group:
    #this dictionary is for acessing the group that a specific pixel is in
    #the keys are the pixel and the data asociated with the keys is the group that the pixel is in
    #it is organized like so
    # {x1:{y1:pixel1,y2:pixel1,2},
    # x2{{y3:pixel1,y5:pixel1,43}}........
    pixelsToGroup = {}
    #keeps a count of how many groups exsist
    count = 0



    def __init__(self):
        #stores the ammount of pixels in the group
        self.amountOfPixelsInGroup = 0
        #stores a list of all the pixels in the group
        self.pixelsInGroup = []
        #gives the group an id number to keep track of when it was created and where it is in a list of groups
        self.groupNumber = Group.count
        #adds one to the group count
        Group.count += 1


    #returns the pixels in the group given
    def GetPixels(self):
        return self.pixelsInGroup



    #returns the group that the pixel is in
    def GetGroupWithPixel(pixelCords):
        #puts "pixelCords" into two variables to be able to use them easily as keys with a dictionary
        x,y = pixelCords
        if x in Group.pixelsToGroup:
            if y in Group.pixelsToGroup[x]:
                return Group.pixelsToGroup[x][y]

        return False




    #returns the amount of pixels in the given group
    def GetCountInGroup(self):
        return self.amountOfPixelsInGroup


    #returns the amount of created groups
    def GetGroupCount():
        return Group.count



    def GetGroupNumber(self):
        return self.groupNumber



    #used for adding a pixel into a group
    def SetPixel(self,pixelCords):
        #makes the pixel cords easy to use for keys in a dictionary
        x,y = pixelCords

        #adds to amount of pixels in the given group
        self.amountOfPixelsInGroup += 1
        #adds the pixel to the list of pixels in the group
        self.pixelsInGroup.append(pixelCords)
        # if the x cord does not exsist for the new pixel create a new x cord dictionary
        if not(x in Group.pixelsToGroup):
                Group.pixelsToGroup[x] = {}
        # add the pixel in the dictionary of pixels to groups
        Group.pixelsToGroup[x][y] = self.groupNumber



    #removes the data for a specified group
    def RemoveGroup(self):
        self.pixelsInGroup = []
        self.amountOfPixelsInGroup = 0



    #takes the 2nd group and puts all of the data into the first group
    def InheritGroup(self,inherit):
        #updates the count in the first group

        #places all the pixels from the 2nd group into the first group
        i = 0
        for pixel in inherit.GetPixels():
            i +=1
            #places a pixel into the first group from the second group
            self.SetPixel(pixel)
            #assigns pixel a new group number
            Group.pixelsToGroup[pixel[0],pixel[1]] = self.groupNumber
            if i == 100000:
                for print in range(1,1000):
                    print("ERROR LOOP TIMEOUT IN FUNCTION INHERITGROUP IN MODULE GROUPCLASS##{#{#{#{#{#{#{#{#{#{#{}}}}}}}}}}}")
                    print(inherit.GetPixels(),'pixels In inheritGroup')
                    print(Pixel,'the current Pixel')
        #removes group 2
        inherit.RemoveGroup()



    #resets all of the class variables
    def ClearGroupData():
        pixelsToGroup = {}
        count = 0
