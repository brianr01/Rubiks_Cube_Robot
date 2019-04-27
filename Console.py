import Cube
import random
notation = 'rRlLuUdDfFuudD'
#notation = 'lllLLLuuuUUU'
sideList = 'rludfb'
randomArray = []

 
while True:
    tempVar = input('alg ')
    if tempVar == 'off':
       Cube.Motor.Toggle_List_Motor_Power('udfblr', False)
    
    elif tempVar == 'on':
        Cube.Motor.Toggle_List_Motor_Power('udlrfb', True)
    
    elif tempVar == 'random':
        #Cube.Motor.Toggle_List_Motor_Power('rlfbud', False)
        for i in range(1,10000):
            #randomArray.append(notation[random.randint(1,12) - 1])
        #randomArray = Cube.Algorithm_Translator(randomArray)
            #Cube.Motor.Toggle_List_Motor_Power(move.lower(), True)
            Cube.Algorithm_Executer(notation[random.randint(1,12) - 1])
            #Cube.Motor.Toggle_List_Motor_Power(move.lower(), False)
        
            if i % 100 == 0:
                print (i)
            
    elif tempVar =='set':
        
        Cube.Motor.Toggle_List_Motor_Power('udfblr', False)
        
        for side in sideList:
            print(side)
            Cube.Motor.Toggle_List_Motor_Power(side, True)
            Cube.Algorithm_Executer([side , side , side , side])
            Cube.Motor.Toggle_List_Motor_Power(side, False)
        
 
        Cube.Motor.Toggle_List_Motor_Power('udfblr', True)
        
    else:
        #try:
        '''
        tempVar = Cube.Algorithm_Translator(tempVar)
        print (tempVar)
        '''
        Cube.Algorithm_Executer(tempVar)

        #except Exception as error:
        #    print(error , 'is not a valid command')onr