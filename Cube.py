import Motor
import random
import time
#The pins order in terms of cube notation is 'rludfb'
direction_pins =[3,7,13,29,33,37]
step_pins =     [5,11,15,31,35,40]
power_pins =   [12,36,16,22,18,32]
Motor.Initiate_Motors_Controll(amount_of_motors = 6 , motor_names = ['r','l','u','d','f','b'] , motor_step_pins = step_pins , motor_direction_pins = direction_pins , motor_power_pins = power_pins)
opposite_side_dictionary = {'r':'l','l':'r','u':'d','d':'u','f':'b','b':'f'}                                                                  

#Motor.Toggle_List_Motor_Power('udfblr', True)


def Algorithm_Executer(moves):
    for i in range(len(moves)):
        
        directions = []
        for k in range(0,len(moves[i])):
            if moves[i][k].isupper():
                directions.append(True)
            else:
                directions.append(False)

        #start = time.clock()
        Motor.Step_Multiple_Motors(moves[i], directions , 200 , .0008)
        time.sleep(.01)
        #stop  = time.clock()
        #print(stop-start,'time')

        #005 .0001 .00001 .000001
        '''
        
        start = time.clock()
        Motor.Step_Motor(moves[i], 1 , 800 , .000001)
        stop  = time.clock()
        print(stop-start,'time')
        '''
        
        

'''        
takes an algorithm and compresses it to make the most efficent execution time for the solver.
Example: algorithm = r,u,d,l,r "the u and d moves can be done at the same time because they are on the same side of the cube"
'''
def Algorithm_Translator(algorithm):
    
    #this variable becomes true when the previous cycle of the for loop was compressed
    skip = False
    
    #list that stores the new compressed version of the algorithm this is the 'returned' variable
    new_algorithm = []
    #iterates through the algorithm to compress it

    for i in range(0,len(algorithm)):
        #if the previous cycle(the last iteration of the for loop) was compressed skip this 
        if skip == True:
            skip = False
        #when the previous cycle was not compressed test if the new set of two variables is compressible
        
        
        else:
            #test to see if two moves are compressible
            if i != len(algorithm) - 1 and Is_Compressible(algorithm[i],algorithm[i+1]) == True:
            
                #compresses two moves
                new_algorithm.append([algorithm[i],algorithm[i+1]])
                
                #skips the next cycle
                skip = True
                
            #if it is not compressible add it to the list
            else:
                
                #add it to the list
                new_algorithm.append((algorithm[i]))
    return new_algorithm
        
#takes a side in cube notation and returns the opposite side       
def Return_Opposite_Side(side):
    return opposite_side_dictionary[side]

def Is_Compressible(side0,side1):
    if side0.lower() == Return_Opposite_Side(side1.lower()):
        return True
        

