#3x3x3 rubics cube simulator

import Cube
from tkinter import *
import random
import time
import get_cube_pieces
import UseWebCam
notation = 'rRlLfFbBuUdD'
randomArray = []
Cube.Motor.Toggle_List_Motor_Power('udfblr', True)
#Cube.Motor.Toggle_List_Motor_Power('r', False)
motorPowerState = False
#this stores the cubes current position
cubePosition = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: '21', 22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: '28', 29: '29', 30: '30', 31: '31', 32: '32', 33: '33', 34: '34', 35: '35', 36: '36', 37: '37', 38: '38', 39: '39', 40: '40', 41: '41', 42: '42', 43: '43', 44: '44', 45: '45', 46: '46', 47: '47', 48: '48', 49:'49', 50:'50', 51:'51', 52:'52', 53:'53', 54:'54'}
#cubePosition,scores = GetCubePieces.GetCubePieces()

#cubePosition = get_cube_pieces.main()
originalCubePosition = cubePosition

converter = {1:5,2:6,3:7,4:8,5:1,6:2,7:3,8:4,9:25,10:26,11:27,12:28,13:29,14:30,15:31,16:32,17:33,18:34,19:35,20:36,21:37,22:38,23:39,24:40,25:9,26:10,27:11,28:12,29:13,30:14,31:15,32:16,33:17,34:18,35:19,36:20,37:21,38:22,39:23,40:24,41:45,42:46,43:47,44:48,45:41,46:42,47:43,48:44,49:49,50:50,51:51,52:52,53:53,54:54}

def convertIncorrectCubePosition(cubePosition,converter):
    newCubePosition = {}
    for sticker in cubePosition:
        newCubePosition[converter[sticker]] = cubePosition[sticker]
    return newCubePosition

cubePosition = convertIncorrectCubePosition(cubePosition,converter)

#this stores the cubes position with the keys and the data reversed
cubePositionInverse = {}

#defines the solved position of the cube
cubePositionSolved = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: '21', 22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: '28', 29: '29', 30: '30', 31: '31', 32: '32', 33: '33', 34: '34', 35: '35', 36: '36', 37: '37', 38: '38', 39: '39', 40: '40', 41: '41', 42: '42', 43: '43', 44: '44', 45: '45', 46: '46', 47: '47', 48: '48'}

#when the cube is solved this is true
solved = True

#defines the color of each sticker
stickerColors = 'wwwwwwwwbbbbbbbbrrrrrrrrggggggggooooooooyyyyyyyywgobry'

#temperary list for manipulating data
tempList = {}

colorDict = {'w':'white' , 'b':'blue' , 'r':'red' , 'g':'green' , 'o':'orange' , 'y':'yellow' , 'k':'black'}
colorDict = colorDict
color_mapping = colorDict
#possible different moves
possibleSides = 'uUdDrRlLfFbB'

stickerDict = {}


solution = []
cross = {16:{16:'',20:'BUbuluLuBUbuluL',30:'UluLUBUb',38:'luLUBUb',14:'uluLUBUb',22:'uuluLUBUb',44:'BUbuluL',42:'uBUbuluL',48:'uuBUbuluL',46:'UBUbuluL'},40:{40:'',12:'buBURUrUbuBURUr',16:'BUbuluLubuBURUr',20:'luLUBUbbuBURUr',30:'buBURUr',38:'ubuBURUr',14:'uubuBURUr',22:'UbuBURUr',44:'uRUrubuB',42:'uuRUrubuB',48:'URUrubuB',46:'RUrubuB'},32:{32:'',36:'ruRUFUfUruRUFUf',40:'RUrubuBuruRUFUf',12:'buBURUrruRUFUf',16:'BUbuluLuuruRUFUf',20:'luLUBUburuRUFUf',30:'uruRUFUf',38:'uuruRUFUf',14:'UruRUFUf',22:'ruRUFUf',44:'uuFUfuruR',42:'UFUfuruR',48:'FUfuruR',46:'uFUfuruR'},24:{24:'',28:'LUluuLuulUfuF',32:'rURfRFruLUlufuF',36:'ruRUFUffuFULUl',40:'RUrubuBuufuFULUl',12:'buBURUrufuFULUl',16:'BUbuluLUfuFULUl',20:'luLUBUbuufuFULUl',30:'uufuFULUl',38:'UfuFULUl',14:'fuFULUl',22:'ufuFULUl',44:'ULUlufuF',42:'LUlufuF',48:'uLUlufuF',46:'uuLUlufuF',},7:{7:'',9:'BUbuBUb',19:'luLUluL',23:'uBUb',29:'uluL',31:'uuBUb',37:'uuluL',39:'UBUb',13:'UluL',15:'BUb',21:'luL',45:'ulULuuluL',43:'uulULuuluL',41:'UlULuuluL',47:'lULuuluL'},5:{5:'',7:'luLRUr',33:'bUBRUr',11:'RurbuB',9:'BuubURUr',19:'RluLr',23:'buuB',29:'Ruur',31:'bUB',37:'UbuB',39:'RUr',13:'buB',15:'uRUr',21:'ubuB',45:'uuRuruuRUr',43:'URuruuRUr',41:'RuruuRUr',47:'uRuruuRUr'},3:{3:'',5:'buBFUf',7:'rlUULR',25:'rURFUf',35:'FufruR',33:'bUBuFUf',11:'buBruR',9:'BruuRb',19:'lFuufL',23:'rUR',29:'UruR',31:'FUf',37:'ruR',39:'uFUf',13:'uruR',15:'uuFUf',21:'uuruR',45:'uuRurUFUf',43:'rURuuruR',41:'RurUFUf',47:'UUrURuuruR',},1:{1:'',3:'ruRLUl',5:'fbuuFB',7:'luLfuuF',17:'LUluFlfL',27 :'fuFUfuF',25:'FuuffUF',35:'LrulR',33:'fRuurF',11:'bLuulB',9:'fBUbF',19:'luuLufuF',23:'LUl',29:'fuF',31:'uLUl',37:'Lul',39:'uuLUl',13:'uufuF',15:'ULUl',21:'UfuF',45:'LuuluLUl',43:'ruuRfuF',41:'RurLUl',47:'lULufuF'},2:{2:'' , 4:'D' , 6:'dd' , 8:'d' ,  26:'fld' , 34:'rf ', 10:'BLd' , 18:'LF' , 32:'RD' , 36:'f' , 40:'rrf' , 12:'rD' , 16:'Ld' , 20:'llF' , 24:'F' , 28:'ld' , 30:'URf' , 38:'Rf' , 14:'uRf' , 22:'lF' , 44:'ff' , 42:'uff' , 48:'uuff' , 46:'Uff'} , 4:{4:'' , 6:'fDF' , 8:'fddF' , 34:'RdBD' , 10:'br' , 18:'ldbD' , 32:'R' , 36:'Dfd' , 40:'dBD' , 12:'r' , 16:'bbr' , 20:'dbD' , 24:'DFd' , 28:'ddldd' , 30:'fRF' , 38:'UBr' , 14:'Br' , 22:'uBr' , 44:'Urr' , 42:'rr' , 48:'urr' , 46:'uurr'} , 6:{6:'' , 8:'ldLD' , 10:'BdLD' , 18:'lb' , 32:'DRd' , 36:'rrBrr' , 40:'B' , 12:'Drd' , 16:'dLD' , 20:'b' , 24:'llb' , 28:'dlD' , 30:'uLb' , 38:'rBR' , 14:'urBR' , 22:'Lb' , 44:'uubb' , 42:'Ubb' , 48:'bb' , 46:'ubb'} , 8:{8:'' , 18:'lDbd' , 32:'ddRdd' , 36:'dfD' , 40:'DBd' , 12:'ddrdd' , 16:'L' , 20:'Dbd' , 24:'dFD' , 28:'l' , 30:'Flf' , 38:'uFlf' , 14:'bLB' , 22:'ubLB' , 44:'ull' , 42:'uull' , 48:'Ull' , 46:'ll'}}
u = {1:7 , 2:8 , 3:1 , 4:2 , 5:3 , 6:4 , 7:5 , 8:6 , 9:33 , 10:34 , 11:35 , 12:12 , 13:13 , 14:14 , 15:15 , 16:16 , 17:9 , 18:10 , 19:11 , 20:20 , 21:21 , 22:22 , 23:23 , 24:24 , 25:17 , 26:18 , 27:19 , 28:28 , 29:29 , 30:30 , 31:31 , 32:32 , 33:25 , 34:26 , 35:27 , 36:36 , 37:37 , 38:38 , 39:39 , 40:40 , 41:41 , 42:42 , 43:43 , 44:44 , 45:45 , 46:46 , 47:47 , 48:48}
U = {1:3 , 2:4 , 3:5 , 4:6 , 5:7 , 6:8 , 7:1 , 8:2 , 9:17 , 10:18 , 11:19 , 12:12 , 13:13 , 14:14 , 15:15 , 16:16 , 17:25 , 18:26 , 19:27 , 20:20 , 21:21 , 22:22 , 23:23 , 24:24 , 25:33 , 26:34 , 27:35 , 28:28 , 29:29 , 30:30 , 31:31 , 32:32 , 33:9 , 34:10 , 35:11 , 36:36 , 37:37 , 38:38 , 39:39 , 40:40 , 41:41 , 42:42 , 43:43 , 44:44 , 45:45 , 46:46 , 47:47 , 48:48}
d = {1:1 , 2:2 , 3:3 , 4:4 , 5:5 , 6:6 , 7:7 , 8:8 , 9:9 , 10:10 , 11:11 , 12:12 , 13:21 , 14:22 , 15:23 , 16:16 , 17:17 , 18:18 , 19:19 , 20:20 , 21:29 , 22:30 , 23:31 , 24:24 , 25:25 , 26:26 , 27:27 , 28:28 , 29:37 , 30:38 , 31:39 , 32:32 , 33:33 , 34:34 , 35:35 , 36:36 , 37:13 , 38:14 , 39:15 , 40:40 , 41:47 , 42:48 , 43:41 , 44:42 , 45:43 , 46:44 , 47:45 , 48:46}
D = {1:1 , 2:2 , 3:3 , 4:4 , 5:5 , 6:6 , 7:7 , 8:8 , 9:9 , 10:10 , 11:11 , 12:12 , 13:37 , 14:38 , 15:39 , 16:16 , 17:17 , 18:18 , 19:19 , 20:20 , 21:13 , 22:14 , 23:15 , 24:24 , 25:25 , 26:26 , 27:27 , 28:28 , 29:21 , 30:22 , 31:23 , 32:32 , 33:33 , 34:34 , 35:35 , 36:36 , 37:29 , 38:30 , 39:31 , 40:40 , 41:43 , 42:44 , 43:45 , 44:46 , 45:47 , 46:48 , 47:41 , 48:42}
r = {1:1 , 2:2 , 3:11 , 4:12 , 5:13 , 6:6 , 7:7 , 8:8 , 9:9 , 10:10 , 11:41 , 12:42 , 13:43 , 14:14 , 15:15 , 16:16 , 17:17 , 18:18 , 19:19 , 20:20 , 21:21 , 22:22 , 23:23 , 24:24 , 25:5 , 26:26 , 27:27 , 28:28 , 29:29 , 30:30 , 31:3 , 32:4 , 33:39 , 34:40 , 35:33 , 36:34 , 37:35 , 38:36 , 39:37 , 40:38 , 41:31 , 42:32 , 43:25 , 44:44 , 45:45 , 46:46 , 47:47 , 48:48}
R = {1:1 , 2:2 , 3:31 , 4:32 , 5:25 , 6:6 , 7:7 , 8:8 , 9:9 , 10:10 , 11:3 , 12:4 , 13:5 , 14:14 , 15:15 , 16:16 , 17:17 , 18:18 , 19:19 , 20:20 , 21:21 , 22:22 , 23:23 , 24:24 , 25:43 , 26:26 , 27:27 , 28:28 , 29:29 , 30:30 , 31:41 , 32:42 , 33:35 , 34:36 , 35:37 , 36:38 , 37:39 , 38:40 , 39:33 , 40:34 , 41:11 , 42:12 , 43:13 , 44:44 , 45:45 , 46:46 , 47:47 , 48:48}
l = {1:29 , 2:2 , 3:3 , 4:4 , 5:5 , 6:6 , 7:27 , 8:28 , 9:1 , 10:10 , 11:11 , 12:12 , 13:13 , 14:14 , 15:7 , 16:8 , 17:23 , 18:24 , 19:17 , 20:18 , 21:19 , 22:20 , 23:21 , 24:22 , 25:25 , 26:26 , 27:45 , 28:46 , 29:47 , 30:30 , 31:31 , 32:32 , 33:33 , 34:34 , 35:35 , 36:36 , 37:37 , 38:38 , 39:39 , 40:40 , 41:41 , 42:42 , 43:43 , 44:44 , 45:15 , 46:16 , 47:9 , 48:48}
L = {1:9 , 2:2 , 3:3 , 4:4 , 5:5 , 6:6 , 7:15 , 8:16 , 9:47 , 10:10 , 11:11 , 12:12 , 13:13 , 14:14 , 15:45 , 16:46 , 17:19 , 18:20 , 19:21 , 20:22 , 21:23 , 22:24 , 23:17 , 24:18 , 25:25 , 26:26 , 27:7 , 28:8 , 29:1 , 30:30 , 31:31 , 32:32 , 33:33 , 34:34 , 35:35 , 36:36 , 37:37 , 38:38 , 39:39 , 40:40 , 41:41 , 42:42 , 43:43 , 44:44 , 45:27 , 46:28 , 47:29 , 48:48}
f = {1:1 , 2:2 , 3:3 , 4:4 , 5:19 , 6:20 , 7:21 , 8:8 , 9:15 , 10:16 , 11:9 , 12:10 , 13:11 , 14:12 , 15:13 , 16:14 , 17:17 , 18:18 , 19:47 , 20:48 , 21:41 , 22:22 , 23:23 , 24:24 , 25:25 , 26:26 , 27:27 , 28:28 , 29:29 , 30:30 , 31:31 , 32:32 , 33:7 , 34:34 , 35:35 , 36:36 , 37:37 , 38:38 , 39:5 , 40:6 , 41:33 , 42:42 , 43:43 , 44:44 , 45:45 , 46:46 , 47:39 , 48:40}
F = {1:1 , 2:2 , 3:3 , 4:4 , 5:39 , 6:40 , 7:33 , 8:8 , 9:11 , 10:12 , 11:13 , 12:14 , 13:15 , 14:16 , 15:9 , 16:10 , 17:17 , 18:18 , 19:5 , 20:6 , 21:7 , 22:22 , 23:23 , 24:24 , 25:25 , 26:26 , 27:27 , 28:28 , 29:29 , 30:30 , 31:31 , 32:32 , 33:41 , 34:34 , 35:35 , 36:36 , 37:37 , 38:38 , 39:47 , 40:48 , 41:21 , 42:42 , 43:43 , 44:44 , 45:45 , 46:46 , 47:19 , 48:20}
b = {1:35 , 2:36 , 3:37 , 4:4 , 5:5 , 6:6 , 7:7 , 8:8 , 9:9 , 10:10 , 11:11 , 12:12 , 13:13 , 14:14 , 15:15 , 16:16 , 17:3 , 18:18 , 19:19 , 20:20 , 21:21 , 22:22 , 23:1 , 24:2 , 25:31 , 26:32 , 27:25 , 28:26 , 29:27 , 30:28 , 31:29 , 32:30 , 33:33 , 34:34 , 35:43 , 36:44 , 37:45 , 38:38 , 39:39 , 40:40 , 41:41 , 42:42 , 43:23 , 44:24 , 45:17 , 46:46 , 47:47 , 48:48}
B = {1:23 , 2:24 , 3:17 , 4:4 , 5:5 , 6:6 , 7:7 , 8:8 , 9:9 , 10:10 , 11:11 , 12:12 , 13:13 , 14:14 , 15:15 , 16:16 , 17:45 , 18:18 , 19:19 , 20:20 , 21:21 , 22:22 , 23:43 , 24:44 , 25:27 , 26:28 , 27:29 , 28:30 , 29:31 , 30:32 , 31:25 , 32:26 , 33:33 , 34:34 , 35:1 , 36:2 , 37:3 , 38:38 , 39:39 , 40:40 , 41:41 , 42:42 , 43:35 , 44:36 , 45:37 , 46:46 , 47:47 , 48:48}
sideDict = {'u':u,'U':U,'d':d,'D':D,'r':r,'R':R,'l':l,'L':L,'f':f,'F':F,'b':b,'B':B}

#creates the inverse dictionary
def InvertDict():
    global cubePositionInverse
    cubePositionInverse = {}
    for x in range(1,49):
        tempvar = cubePosition[x]
        cubePositionInverse[tempvar] = x

InvertDict()


#when the cube's solution was made it was held from the incorrect angle thus making incorrect moves
#this fixes these algorithms
def ConvertIncorrectAlgorithm(algorithm):
    newAlgorithm =''
    for letter in algorithm:
        if letter == 'l':
            newAlgorithm += 'l'

        elif letter == 'L':
            newAlgorithm +='L'

        elif letter == 'r':
            newAlgorithm +='r'

        elif letter == 'R':
            newAlgorithm +='R'

        elif letter == 'f':
            newAlgorithm +='b'

        elif letter == 'F':
            newAlgorithm +='B'

        elif letter == 'b':
            newAlgorithm +='f'

        elif letter == 'B':
            newAlgorithm +='F'

        elif letter == 'u':
            newAlgorithm +='d'

        elif letter == 'd':
            newAlgorithm +='u'

        elif letter == 'U':
            newAlgorithm +='D'

        elif letter == 'D':
            newAlgorithm +='U'

        elif letter == ' ':
            pass

        else:
            print('character not found in function "ConvertIncorrectAlgorithm" charactor = ', letter , 'algorithm = ', algorithm)
    return newAlgorithm

def Solve():
    global solution
    Cube.Motor.Toggle_List_Motor_Power('udfblr', True)
    solution = []
    Solvef2l(2)
    Solvef2l(4)
    Solvef2l(6)
    Solvef2l(8)
    Solvef2l(1)
    Solvef2l(3)
    Solvef2l(5)
    Solvef2l(7)
    Solvef2l(24)
    Solvef2l(32)
    Solvef2l(40)
    Solvef2l(16)
    SolveOle()
    SolvePle()
    SolvePlc()
    SolveOlc()
    Algorithm('rrududllbbududffudud')
    Cube.Motor.Toggle_List_Motor_Power('udfblr', False)
    print (solution)


def Solvef2l(piece):
    InvertDict()
    Algorithm(ConvertIncorrectAlgorithm(cross[piece][int(cubePositionInverse[str(piece)])]))
    InvertDict()
    Draw()


def SolveOle():
    edgeColors = [colorDict[stickerColors[int(cubePosition[48]) - 1]],colorDict[stickerColors[int(cubePosition[42]) - 1]],colorDict[stickerColors[int(cubePosition[44]) - 1]],colorDict[stickerColors[int(cubePosition[46]) - 1]]]
    amountOfCorrectEdges = 0
    for edge in edgeColors:
        if edge == 'yellow':
            amountOfCorrectEdges += 1

    if amountOfCorrectEdges == 0:
        Algorithm(ConvertIncorrectAlgorithm('ruuRRfrFUURfrF'))

    elif amountOfCorrectEdges == 2:
        if edgeColors[0] == 'yellow' and edgeColors[2] == 'yellow':
            Algorithm(ConvertIncorrectAlgorithm('ufruRUF'))

        elif edgeColors[1] == 'yellow' and edgeColors[3] == 'yellow':
            Algorithm(ConvertIncorrectAlgorithm('fruRUF'))

        elif edgeColors[0] == 'yellow' and edgeColors[1] == 'yellow':
            Algorithm(ConvertIncorrectAlgorithm('ufruRUFufruRUF'))

        elif edgeColors[1] == 'yellow' and edgeColors[2] == 'yellow':
            Algorithm(ConvertIncorrectAlgorithm('fruRUFufruRUF'))

        elif edgeColors[2] == 'yellow' and edgeColors[3] == 'yellow':
            Algorithm(ConvertIncorrectAlgorithm('ufruRUFfruRUF'))

        else:
            Algorithm(ConvertIncorrectAlgorithm('fruRUFfruRUF'))
    Draw()

def SolvePle():
    edges = [14,38,30,22]
    correctEdges = 0
    while correctEdges < 2:
        correctEdges = 0
        for edge in edges:
            if edge == int(cubePosition[edge]):
                correctEdges+=1

        if correctEdges<2:
            Algorithm('d')
    if correctEdges == 2:
        if (cubePosition[14] == '14' and cubePosition[30] == '30' or cubePosition[38] == '38' and cubePosition[22] == '22'):
            Algorithm(ConvertIncorrectAlgorithm('ruuRUrURuruuRUrUR'))

        elif(cubePosition[14] == '14' and cubePosition[38] == '38'):
            Algorithm(ConvertIncorrectAlgorithm('UruuRUrUR'))

        elif(cubePosition[38] == '38' and cubePosition[30] == '30'):
            Algorithm(ConvertIncorrectAlgorithm('uuruuRUrUR'))

        elif(cubePosition[30] == '30' and cubePosition[22] == '22'):
            Algorithm(ConvertIncorrectAlgorithm('uruuRUrURuu'))

        else:
            Algorithm(ConvertIncorrectAlgorithm('ruuRUrUR'))

    iteration = 0
    while correctEdges<4:
        if iteration != 0:
            correctEdges = 0
            Algorithm('d')

        iteration +=1
        if iteration == 5:
            print ("error in function solvePle the edges were not solved correctly")
            break
        for edge in edges:
            if edge == int(cubePosition[edge]):
                correctEdges+=1


    Draw()




def SolvePlc():
    correctCorners = []
    corners = [[43,31,37],[41,39,13],[47,15,21],[45,29,23]]
    for corner in corners:
        for i in range(4):
            if i == 3:
                correctCorners.append(False)
                break

            if corner[0] == int(cubePosition[corner[i]]):
                correctCorners.append(True)
                break
    if correctCorners == [False,False,False,False]:
        Algorithm(ConvertIncorrectAlgorithm('LurUluRU'))
    correctCorners = []
    for corner in corners:
        for i in range(4):
            if i == 3:
                correctCorners.append(False)
                break

            if corner[0] == int(cubePosition[corner[i]]):
                correctCorners.append(True)
                break

    if correctCorners == [True,False,False,False]:
        Algorithm(ConvertIncorrectAlgorithm('LurUluRU'))

    if correctCorners == [False,True,False,False]:
        Algorithm(ConvertIncorrectAlgorithm('uLurUluRUU'))

    if correctCorners == [False,False,True,False]:
        Algorithm(ConvertIncorrectAlgorithm('uuLurUluRu'))

    if correctCorners == [False,False,False,True]:
        Algorithm(ConvertIncorrectAlgorithm('ULurUluRUu'))
    correctCorners = []
    for corner in corners:
        for i in range(4):
            if i == 3:
                correctCorners.append(False)
                break

            if corner[0] == int(cubePosition[corner[i]]):
                correctCorners.append(True)
                break
    if correctCorners == [True,False,False,False]:
        Algorithm(ConvertIncorrectAlgorithm('LurUluRU'))

    if correctCorners == [False,True,False,False]:
        Algorithm(ConvertIncorrectAlgorithm('uLurUluRUU'))

    if correctCorners == [False,False,True,False]:
        Algorithm(ConvertIncorrectAlgorithm('uuLurUluRUUU') )

    if correctCorners == [False,False,False,True]:
        Algorithm(ConvertIncorrectAlgorithm('ULurUluRUu') )

    Draw()

def SolveOlc():
    Solved = False
    while Solved == False:


        if colorDict[stickerColors[int(cubePosition[43]) - 1]] != 'yellow':
            Algorithm(ConvertIncorrectAlgorithm('ruuRUrURLuuluLul'))
        else:
            Algorithm(ConvertIncorrectAlgorithm('u'))


        Solved = SolveCheck()
        if Solved == True:
            break

    Draw()




def SolveTester():
    for i in range(1000000000):
        if i%100 ==0:
            print(i)
        Scramble()
        InvertDict()
        Solve()
        solved = SolveCheck()
        if solved == False:
            print('the cube was not solved')
            break


#this fuction set the variable 'cubePosition' to the solved state
def motorPower():
    global cubePosition,solved,tempList,possibleSides,sideDict,motorPowerState
    motorPowerState =  not motorPowerState
    Cube.Motor.Toggle_List_Motor_Power('udfblr', motorPowerState)

    Draw()




#checks for a solved cube
def SolveCheck():
    InvertDict()
    if cubePosition == cubePositionSolved:
        solved = True


    else:
        solved = False

    return solved




#this copies the list based off of the 'side' input turning the side of the rubics cube
def CopyList(side):
    global cubePosition
    tempList = {}
    for x in range(1,49):
        tempHold = sideDict[side]
        tempList[x] = cubePosition[tempHold[x]]
    tempHold = {}
    SolveCheck()
    cubePosition = tempList
    #this part is for trouble shooting the list
    toPrint = ''
    for x in range (1,49):
        toPrint = toPrint + ' ' + str(stickerColors[int(tempList[x]) -1])

    toPrint = ''




#this is the input for turn a side this checks if the input is a valid side
def TurnSide(side):
    CopyList(side)




#executes an algoritm
def Algorithm(alg):
    Cube.Algorithm_Executer(alg)
    global solution
    #print (alg)
    solution.append(ConvertIncorrectAlgorithm(alg))
    for x in range(1,len(alg) + 1):
        TurnSide(alg[x - 1])



#puts the cube in a scrambled state
def Scramble():
    tempstr = ''
    for x in range(1,54):
        tempstr =  tempstr + possibleSides[random.randint(1,12) - 1]
    print (tempstr)
    Algorithm(tempstr)
    tempstr = ''
    Draw()

def Sync():
    global cubePosition
    cubePosition = convertIncorrectCubePosition(get_cube_pieces.main(),converter)
    Draw()

    
    


#function each button for each move
def fr():
    Algorithm('r')
    Draw()

def fR():
    Algorithm('R')
    Draw()

def fl():
    Algorithm('l')
    Draw()

def fL():
    Algorithm('L')
    Draw()

def fu():
    Algorithm('u')
    Draw()

def fU():
    Algorithm('U')
    Draw()

def fd():
    Algorithm('d')
    Draw()

def fD():
    Algorithm('D')
    Draw()

def ff():
    Algorithm('f')
    Draw()

def fF():
    Algorithm('F')
    Draw()

def fb():
    Algorithm('b')
    Draw()

def fB():
    Algorithm('B')
    Draw()




#this part of code is all for displaying the cube in 2d form on tkinter screen
root = Tk()
canvas = Canvas(root, width = 550, height = 650)
canvas.pack()
frame = Frame(root)
frame.pack(side = BOTTOM)
def Draw():
    UseWebCam.GetVideoFeed()

    s1 =  canvas.create_rectangle(200,200,250,250,fill = colorDict[stickerColors[int(cubePosition[1]) - 1]])
    s2 =  canvas.create_rectangle(250,200,300,250,fill = colorDict[stickerColors[int(cubePosition[2]) - 1]])
    s3 =  canvas.create_rectangle(300,200,350,250,fill = colorDict[stickerColors[int(cubePosition[3]) - 1]])
    s4 =  canvas.create_rectangle(300,250,350,300,fill = colorDict[stickerColors[int(cubePosition[4]) - 1]])
    s5 =  canvas.create_rectangle(300,300,350,350,fill = colorDict[stickerColors[int(cubePosition[5]) - 1]])
    s6 =  canvas.create_rectangle(250,300,300,350,fill = colorDict[stickerColors[int(cubePosition[6]) - 1]])
    s7 =  canvas.create_rectangle(200,300,250,350,fill = colorDict[stickerColors[int(cubePosition[7]) - 1]])
    s8 =  canvas.create_rectangle(200,250,250,300,fill = colorDict[stickerColors[int(cubePosition[8]) - 1]])
    s9 =  canvas.create_rectangle(200,350,250,400,fill = colorDict[stickerColors[int(cubePosition[9]) - 1]])
    s10 =  canvas.create_rectangle(250,350,300,400,fill = colorDict[stickerColors[int(cubePosition[10]) - 1]])
    s11 =  canvas.create_rectangle(300,350,350,400,fill = colorDict[stickerColors[int(cubePosition[11]) - 1]])
    s12 =  canvas.create_rectangle(300,400,350,450,fill = colorDict[stickerColors[int(cubePosition[12]) - 1]])
    s13 =  canvas.create_rectangle(300,450,350,500,fill = colorDict[stickerColors[int(cubePosition[13]) - 1]])
    s14 =  canvas.create_rectangle(250,450,300,500,fill = colorDict[stickerColors[int(cubePosition[14]) - 1]])
    s15 =  canvas.create_rectangle(200,450,250,500,fill = colorDict[stickerColors[int(cubePosition[15]) - 1]])
    s16 =  canvas.create_rectangle(200,400,250,450,fill = colorDict[stickerColors[int(cubePosition[16]) - 1]])
    s17 =  canvas.create_rectangle(150,200,200,250,fill = colorDict[stickerColors[int(cubePosition[17]) - 1]])
    s18 =  canvas.create_rectangle(150,250,200,300,fill = colorDict[stickerColors[int(cubePosition[18]) - 1]])
    s19 =  canvas.create_rectangle(150,300,200,350,fill = colorDict[stickerColors[int(cubePosition[19]) - 1]])
    s20 =  canvas.create_rectangle(100,300,150,350,fill = colorDict[stickerColors[int(cubePosition[20]) - 1]])
    s21 =  canvas.create_rectangle(50,300,100,350,fill = colorDict[stickerColors[int(cubePosition[21]) - 1]])
    s22 =  canvas.create_rectangle(50,250,100,300,fill = colorDict[stickerColors[int(cubePosition[22]) - 1]])
    s23 =  canvas.create_rectangle(50,200,100,250,fill = colorDict[stickerColors[int(cubePosition[23]) - 1]])
    s24 =  canvas.create_rectangle(100,200,150,250,fill = colorDict[stickerColors[int(cubePosition[24]) - 1]])
    s25 =  canvas.create_rectangle(300,150,350,200,fill = colorDict[stickerColors[int(cubePosition[25]) - 1]])
    s26 =  canvas.create_rectangle(250,150,300,200,fill = colorDict[stickerColors[int(cubePosition[26]) - 1]])
    s27 =  canvas.create_rectangle(200,150,250,200,fill = colorDict[stickerColors[int(cubePosition[27]) - 1]])
    s28 =  canvas.create_rectangle(200,100,250,150,fill = colorDict[stickerColors[int(cubePosition[28]) - 1]])
    s29 =  canvas.create_rectangle(200,50,250,100,fill = colorDict[stickerColors[int(cubePosition[29]) - 1]])
    s30 =  canvas.create_rectangle(250,50,300,100,fill = colorDict[stickerColors[int(cubePosition[30]) - 1]])
    s31 =  canvas.create_rectangle(300,50,350,100,fill = colorDict[stickerColors[int(cubePosition[31]) - 1]])
    s32 =  canvas.create_rectangle(300,100,350,150,fill = colorDict[stickerColors[int(cubePosition[32]) - 1]])
    s33 =  canvas.create_rectangle(350,300,400,350,fill = colorDict[stickerColors[int(cubePosition[33]) - 1]])
    s34 =  canvas.create_rectangle(350,250,400,300,fill = colorDict[stickerColors[int(cubePosition[34]) - 1]])
    s35 =  canvas.create_rectangle(350,200,400,250,fill = colorDict[stickerColors[int(cubePosition[35]) - 1]])
    s36 =  canvas.create_rectangle(400,200,450,250,fill = colorDict[stickerColors[int(cubePosition[36]) - 1]])
    s37 =  canvas.create_rectangle(450,200,500,250,fill = colorDict[stickerColors[int(cubePosition[37]) - 1]])
    s38 =  canvas.create_rectangle(450,250,500,300,fill = colorDict[stickerColors[int(cubePosition[38]) - 1]])
    s39 =  canvas.create_rectangle(450,300,500,350,fill = colorDict[stickerColors[int(cubePosition[39]) - 1]])
    s40 =  canvas.create_rectangle(400,300,450,350,fill = colorDict[stickerColors[int(cubePosition[40]) - 1]])
    s41 =  canvas.create_rectangle(300,500,350,550,fill = colorDict[stickerColors[int(cubePosition[41]) - 1]])
    s42 =  canvas.create_rectangle(300,550,350,600,fill = colorDict[stickerColors[int(cubePosition[42]) - 1]])
    s43 =  canvas.create_rectangle(300,600,350,650,fill = colorDict[stickerColors[int(cubePosition[43]) - 1]])
    s44 =  canvas.create_rectangle(250,600,300,650,fill = colorDict[stickerColors[int(cubePosition[44]) - 1]])
    s45 =  canvas.create_rectangle(200,600,250,650,fill = colorDict[stickerColors[int(cubePosition[45]) - 1]])
    s46 =  canvas.create_rectangle(200,550,250,600,fill = colorDict[stickerColors[int(cubePosition[46]) - 1]])
    s47 =  canvas.create_rectangle(200,500,250,550,fill = colorDict[stickerColors[int(cubePosition[47]) - 1]])
    s48 =  canvas.create_rectangle(250,500,300,550,fill = colorDict[stickerColors[int(cubePosition[48]) - 1]])
    sw =  canvas.create_rectangle(250,250,300,300,fill = colorDict[stickerColors[int(originalCubePosition[49]) - 1]])
    sb =  canvas.create_rectangle(250,400,300,450,fill = colorDict[stickerColors[int(originalCubePosition[50]) - 1]])
    sr =  canvas.create_rectangle(100,250,150,300,fill = colorDict[stickerColors[int(originalCubePosition[51]) - 1]])
    sg =  canvas.create_rectangle(250,100,300,150,fill = colorDict[stickerColors[int(originalCubePosition[52]) - 1]])
    so =  canvas.create_rectangle(400,250,450,300,fill = colorDict[stickerColors[int(originalCubePosition[53]) - 1]])
    sy =  canvas.create_rectangle(250,550,300,600,fill = colorDict[stickerColors[int(originalCubePosition[54]) - 1]])



r = Button(frame, text = '  r', command = fr)
R = Button(frame, text = '  R', command = fR)
l = Button(frame, text = '  l', command = fl)
L = Button(frame, text = '  L', command = fL)
u = Button(frame, text = '  u', command = fu)
U = Button(frame, text = '  U', command = fU)
d = Button(frame, text = '  d', command = fd)
D = Button(frame, text = '  D', command = fD)
f = Button(frame, text = '  f', command = ff)
F = Button(frame, text = '  F', command = fF)
b = Button(frame, text = '  b', command = fb)
B = Button(frame, text = '  B', command = fB)
solve = Button(frame, text = 'on/off' ,command = motorPower)
scramble = Button(frame, text = 'Scramble' ,command = Scramble)
solver = Button(frame, text = 'Solver' ,command = Solve)
sync = Button(frame, text = 'sync' ,command = Sync)

solver.pack(side = LEFT)
scramble.pack(side = LEFT)
r.pack(side = LEFT)
R.pack(side = LEFT)
l.pack(side = LEFT)
L.pack(side = LEFT)
u.pack(side = LEFT)
U.pack(side = LEFT)
d.pack(side = LEFT)
D.pack(side = LEFT)
f.pack(side = LEFT)
F.pack(side = LEFT)
b.pack(side = LEFT)
B.pack(side = LEFT)
solve.pack(side = RIGHT)
sync.pack(side = LEFT)

Draw()
root.mainloop()
SolveTester()
'''
while True:
    Scramble()
    start = time.time()
    Sync()
    Solve()
    end = time.time()
    print(end - start)
    time.sleep(10)
    '''
    
print('end')
