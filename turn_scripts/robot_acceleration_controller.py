import arduino_controller

class Robot_Acceleration_Controller:
    def __init__(self, arduino = None):
        if (arduino is not None):
            self.arduino = arduino
        else:
            self.arduino = arduino_controller.Arduino_Controller()

    def enqueue_change_acceleration(self, acceleration_curve):
        self.arduino.enqueue_command_tag('acceleration', [acceleration_curve)])

    def execute_change_acceleration(self, acceleration_curve):
        self.arduino.execute_priority_command('acceleration', [acceleration_curve])
    