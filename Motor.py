import Gpio
import time

#stored in the format 'step , direction , micro 1 , micro 2 , micro 3 , power'
motor_array = {}

def Initiate_Motor_Controll(motor_name = False , motor_step_pin = False , motor_direction_pin = False , motor_micro_step_pin_one = False , motor_micro_step_pin_two = False , motor_micro_step_pin_three = False , motor_power_pin = False):
    motor_array[motor_name] = [motor_step_pin , motor_direction_pin , motor_micro_step_pin_one , motor_micro_step_pin_two , motor_micro_step_pin_three , motor_power_pin]
    Gpio.Set_Up_Pins(motor_array[motor_name])
    

def Initiate_Motors_Controll(amount_of_motors = 0 , motor_names = False , motor_step_pins = False , motor_direction_pins = False , motor_micro_step_pins_one = False , motor_micro_step_pins_two = False , motor_micro_step_pins_three = False , motor_power_pins = False):
    motor_names = List_Modifyer(motor_names , amount_of_motors)
    motor_step_pins = List_Modifyer(motor_step_pins , amount_of_motors)
    motor_direction_pins = List_Modifyer(motor_direction_pins , amount_of_motors)
    motor_micro_step_pins_one = List_Modifyer(motor_micro_step_pins_one , amount_of_motors)
    motor_micro_step_pins_two = List_Modifyer(motor_micro_step_pins_two , amount_of_motors)
    motor_micro_step_pins_three = List_Modifyer(motor_micro_step_pins_three , amount_of_motors)
    motor_power_pins = List_Modifyer(motor_power_pins , amount_of_motors)
    for i in range(0,amount_of_motors):
        Initiate_Motor_Controll(motor_names[i] , motor_step_pins[i] , motor_direction_pins[i] , motor_micro_step_pins_one[i], motor_micro_step_pins_two[i] , motor_micro_step_pins_three[i] , motor_power_pins[i])
        
def List_Modifyer(list,amount_of_motors):
    temporary_variable = []
    if list == False:
        for i in range(0 , amount_of_motors + 1):
            temporary_variable.append(False)
        return temporary_variable
    
    return list
        

def Step_Motor(motor_name , direction , steps , delay_between_steps):
            
    Gpio.Toggle_Pin(motor_array[motor_name][1] ,direction)

    for i in range(steps):
        Gpio.Toggle_Pin(motor_array[motor_name][0] , True)
        time.sleep(delay_between_steps)
        Gpio.Toggle_Pin(motor_array[motor_name][0] , False)




def Step_Multiple_Motors(motor_names , directions , steps , delay_between_steps):
    #unused_motors = ['r','l','u','d','f','b']
    #Toggle_List_Motor_Power(unused_motors,False)
    #Toggle_List_Motor_Power(motor_names,True)
    #time.sleep(.1)
    for i in range(len(motor_names)):
            Gpio.Toggle_Pin(motor_array[motor_names[i].lower()][1] , directions[i])
    
    step = 0
    for i in range(0,steps):
        for i in range(len(motor_names)):
            Gpio.Toggle_Pin(motor_array[motor_names[i].lower()][0] , True)
        step+=1
        time.sleep(curve(step))        
        for i in range(len(motor_names)):
            Gpio.Toggle_Pin(motor_array[motor_names[i].lower()][0] , False)
        time.sleep(curve(step))


def curve(iteration):


    #sleep_time =.0002325
    #print(sleep_time,iteration)
    #return sleep_time
    

    max_sleep_time =.00005
    min_sleep_time =.000009
    steps =200
    sleep_time = ((max_sleep_time-min_sleep_time)/((0-(steps/2))**2))*((iteration-(steps/2))**2)+min_sleep_time
    #sleep_time = .00005
    return sleep_time
#additional code needed to add this functionality
#def Toggle_Micro_step():
            
def Toggle_List_Motor_Power(list, state):
    for i in range(len(list)):
        Toggle_Motor_Power(list[i] , state)
    
def Toggle_Motor_Power(motor_name , state):
    if state == True:
        Gpio.Toggle_Pin(motor_array[motor_name.lower()][5] , False)
        
    if state == False:
        Gpio.Toggle_Pin(motor_array[motor_name.lower()][5] , True)
        
            
