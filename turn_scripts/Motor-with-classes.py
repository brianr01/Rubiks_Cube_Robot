import Gpio
import time
default_power_state = False

class Motor:

    def __init__(self, step_pin, direction_pin, power_pin, micro_step_level = 1):
        self.pins.step = step_pin
        self.pins.direction = direction_pin
        self.pins.power = power_pin
        self.micro_step_level = micro_step_level
        self.direction = True
        self.power = False
        Gpio.set_up_pins(self.pins)
        self.set_motor_power(default_power_state)
        self.acceleration_curve = 'default'

    def set_motor_power(self, state = 'toggle'):

        if(state == 'toggle'):
            self.power = ! self.power
            Gpio.toggle_pin(self.pins.power, self.power)
            return True

        elif(state == True or state == False):
            self.power = state
            Gpio.toggle_pin(self.pins.power, self.power)
            return True

        else:
            return False

    def set_motor_direction(self, direction = 'toggle'):
        if(state == 'toggle'):
            self.direction = ! self.direction
            Gpio.toggle_pin(self.pins.direction, self.direction)
            return True
        
        elif(state == True or state == False):
            self.direction = direction
            Gpio.toggle_pin(self.pins.direction, self.direction)
        
        else:
            return False
    
    def step_motor(self,sleep_time):
        Gpio.toggle_pin(self.pins.step, True)
        time.sleep(sleep_time)
        Gpio.toggle_pin(self.pins.step, True)

    '''
    def turn_motor(self, steps):
        set_motor_direction(self, direction = direction)
        for(step in range(0,steps)):
            sleep_time = self.acceleration_curve[step]
            step_motor(self, sleep_time)

    def turn_motors(motors, steps):
        for motor in motors:
            sleep_time = self.acceleration_curve[step]
            motor.step_motor(c)
            
    #ex nodes [[0, 0.1],[100, 0.0001],[290, 0.1]]
    def set_acceleration_curve(self, steps, nodes = 'default', type = 'linear'):
        if(nodes = 'default'):
            return False
        acceleration_curve = []
        current_node = 0
        if(type = 'linear'):
            node_number = 0
            for(step in steps):
                if(nodes[current_node + 1] == step)
                    current_node += 1
                
                
                next_node = nodes[current_node + 1]

                if(current_node = 0):
                    slope = (current_node[1] - next_node[1] / current_node[0] - next_node[0])
                    sleep_time = - slope * (current_node[0] - step) + current_node[1]
                    acceleration_curve.append(sleep_time)
    '''
        


