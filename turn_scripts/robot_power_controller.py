import arduino_controller

class Robot_Power_Controller:
    def __init__(self, arduino = None):
        self.command_map = {'1': 'a', '0': 'b'}
        if (arduino is not None):
            self.arduino = arduino
        else:
            self.arduino = arduino_controller.Arduino_Controller()

    def enqueue_change_state(self, state):
        self.state = state
        self.arduino.enqueue_command_tag(self.get_command())

    def get_command(self):
        return self.command_map[self.get_state_string()]


    def get_state_string(self):
        return '1' if self.state else '0'
    