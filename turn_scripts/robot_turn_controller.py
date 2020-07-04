import arduino_controller

class Robot_Turn_Controller:
    def __init__(self, arduino = None):
        if (arduino is not None):
            self.arduino = arduino
        else:
            self.arduino = arduino_controller.Arduino_Controller()
        
        self.side_letter_to_number_dictionary = {
            'r':'0',
            'l':'1',
            'u':'2',
            'd':'3',
            'f':'4',
            'b':'5'
        }

    def enqueue_side(self, side):
        self.arduino.enqueue_command_tag('3', [self.convert_side_input(side)])

    def convert_side_input(self, side):
        if (self.get_side_type(side) == 'letter'):
            side = self.convert_side_to_number(side)
        
        return side.lower()

    def get_side_type(self, side):
        return 'number' if type(side) == 'int' else 'letter'
    
    def convert_side_to_number(self, side):
        return self.side_letter_to_number_dictionary[side.lower()]