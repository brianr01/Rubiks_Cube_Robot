import Gpio
import time
default_power_state = False

class Motor:
    def __init__(self, step_pin, direction_pin, power_pin, micro_step_level = 1):

        self.micro_step_level = micro_step_level

        self.step_pin = step_pin
        self.direction_pin = direction_pin
        self.power_pin = power_pin

        #defines the current direction
        self.direction = True

        #defines the current power state
        self.power = default_power_state
        self.acceleration_curve = 'default'

        #sets up the pins
        Gpio.set_up_pins([self.step_pin, self.direction_pin, self.power_pin])

        #sets the power state of the motor to the default power state
        self.set_motor_power(default_power_state)

    def set_motor_power(self, state = 'toggle'):
        if(state == 'toggle'):
            self.power != self.power
            Gpio.toggle_pin(self.power_pin, self.power)

        elif(state == True or state == False):
            self.power = state
            Gpio.toggle_pin(self.power_pin, not self.power)

        else:
            return "error: parameter 'state' was in an invalid state. value ={}".format(state)

    def set_motor_direction(self, direction = 'toggle'):
        if(direction == 'toggle'):
            self.direction != self.direction
            Gpio.toggle_pin(self.direction_pin, self.direction)

        elif(direction == True or direction == False):
            self.direction = direction
            Gpio.toggle_pin(self.direction_pin, self.direction)

        else:
            return "error: parameter 'direction' was in an invalid state. value ={}".format(direction)

    def step_motor(self):
        Gpio.toggle_pin(self.step_pin, True)
        Gpio.toggle_pin(self.step_pin, False)

    def turn_motor(self, steps):
        for step in range(0,steps):
            sleep_time = .0003
            #TODO
            #make sleep time an acceleration curve
            time.sleep(sleep_time)
            self.step_motor()

    def turn_motors(motors, steps):
        for step in range(0,steps):
            for motor in motors:
                time.sleep(0.0001)
                #TODO
                #sleep_time = motor.acceleration_curve[step]
                motor.step_motor()
