import arduino_controller
import robot_direction_controller
import robot_power_controller
import robot_turn_controller
import time

class Robot_Cube_Controller:
    def __init__(self, arduino = None):
        if (arduino is not None):
            self.arduino = arduino
        else:
            self.arduino = arduino_controller.Arduino_Controller()
        
        self.direction = robot_direction_controller.Robot_Direction_Controller(arduino=self.arduino)
        self.power = robot_power_controller.Robot_Power_Controller(arduino=self.arduino)
        self.turn = robot_turn_controller.Robot_Turn_Controller(arduino=self.arduino)

    def execute(self):
        self.arduino.execute_command_queue()

    def enqueue_algorithm_string(self, algorithm_string):
        moves = algorithm_string.split(" ")

        for move in moves:
            if (len(move) == 1):
                self.turn.enqueue_side(move)
            elif (len(move) == 2):
                if (move[1] == "'"):
                    self.direction.enqueue_change_state(False)
                    self.turn.enqueue_side(move[0])
                    self.direction.enqueue_change_state(True)
                elif (move[1] == "2"):
                    self.turn.enqueue_side(move[0])
                    self.turn.enqueue_side(move[0])

    def execute_algorithm_string(self, algorithm_string, power_off_pause_time_in_seconds = 1):
        self.arduino.wait_for_ready()
    
        self.power.enqueue_change_state(True)
        self.enqueue_algorithm_string(algorithm_string)
        self.power.enqueue_change_state(False)
        self.execute()
