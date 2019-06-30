import class_motor


opposite_side_dictionary = {'r':'l','l':'r','u':'d','d':'u','f':'b','b':'f'}                                                                      

class Cube:
    def __init__(self,motors_pins):
        self.sides = {}
        for pins in motors_pins:
            self.sides[pins] = class_motor.Motor(motors_pins[pins][0], motors_pins[pins][1], motors_pins[pins][2])

    def execute_algorithm(self, algorithm):
        for move in algorithm:
            if move.islower():
                self.sides[move].set_motor_direction(direction = True)
                self.sides[move].turn_motor(200)
            else:
                try:
                    self.sides[move.lower()].set_motor_direction(direction = False)
                    self.sides[move.lower()].turn_motor(200)
                except Exception as error:
                    print(error, ': error invalid move detected:', move)
                    
    def power_off(self):
        for motor in self.sides:
            self.sides[motor].set_motor_power(state = False)
    
    def power_on(self):
        for motor in self.sides:
            self.sides[motor].set_motor_power(state = True)   
