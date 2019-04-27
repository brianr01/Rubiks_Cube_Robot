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