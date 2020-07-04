import arduino_controller

class Robot_Power_Controller:
    def __init__(self, arduino = None):
        if (arduino is not None):
            self.arduino = arduino
        else:
            self.arduino = arduino_controller.Arduino_Controller()

    def enqueue_change_state(self, state):
        self.state = state
        self.arduino.enqueue_command_tag('1', [self.get_state_string()])

    def get_state_string(self):
        return '1' if self.state else '0'
    