import Motor

motors_pins = {'r':[5, 3, 12],
               'l':[11, 7, 36],
               'u':[15, 13, 16], 
               'd':[31, 29, 22], 
               'f':[35, 33, 18], 
               'b':[40, 37, 32]}

opposite_side_dictionary = {'r':'l','l':'r','u':'d','d':'u','f':'b','b':'f'}                                                                  

motors = {}
for motor_pins in motors_pins:
    motors[motor_pins] = Motor.Motor(motors_pins[motor_pins][0], motors_pins[motor_pins][1], motors_pins[motor_pins][2])
    
    
class Cube:
    def __init__(self, motors_pins):
        self.sides = {}
        for motor_pins in motors_pins:
            self.sides[motor_pins] = Motor.Motor(motors_pins[motor_pins][0], motors_pins[motor_pins][1], motors_pins[motor_pins][2])
    
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
                    print(error)
                    
    def power_off(self):
        for motor in self.sides:
            self.sides[motor].set_motor_power(state = False)
    
    def power_on(self):
        for motor in self.sides:
            self.sides[motor].set_motor_power(state = True)   
