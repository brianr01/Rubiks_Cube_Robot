import class_motor

opposite_side_dictionary = {'r':'l','l':'r','u':'d','d':'u','f':'b','b':'f'}                                                                      

class Cube:
    def __init__(self,motors_pins):
        self.sides = {}
        for pins in motors_pins:
            self.sides[pins] = class_motor.Motor(motors_pins[pins][0], motors_pins[pins][1], motors_pins[pins][2])

    def execute_algorithm(self, algorithm):
        print(algorithm)
        move_list = len(algorithm)
        iteration = 0

        while True:
            if (iteration >= move_list):
                break
            if ( algorithm[iteration] == ' '):
                iteration += 1
            else:
                if (iteration + 1 < move_list):
                    if (algorithm[iteration + 1] == "'"):
                        self.sides[algorithm[iteration].lower()].set_motor_direction(direction = True)
                        self.sides[algorithm[iteration].lower()].turn_motor(200)
                        iteration += 3
                    elif (algorithm[iteration + 1] == "2"):
                        self.sides[algorithm[iteration].lower()].set_motor_direction(direction = True)
                        self.sides[algorithm[iteration].lower()].turn_motor(200)
                        self.sides[algorithm[iteration].lower()].turn_motor(200)
                        iteration += 3
                    else:
                        self.sides[algorithm[iteration].lower()].set_motor_direction(direction = False)
                        self.sides[algorithm[iteration].lower()].turn_motor(200)
                        iteration += 2
                else:
                    self.sides[algorithm[iteration].lower()].set_motor_direction(direction = False)
                    self.sides[algorithm[iteration].lower()].turn_motor(200)
                    break

    def power_off(self):
        for motor in self.sides:
            self.sides[motor].set_motor_power(state = False)

    def power_on(self):
        for motor in self.sides:
            self.sides[motor].set_motor_power(state = True)
