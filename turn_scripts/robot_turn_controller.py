import arduino_controller

class Robot_Turn_Controller:
    def __init__(self, arduino = None):
        if (arduino is not None):
            self.arduino = arduino
        else:
            self.arduino = arduino_controller.Arduino_Controller()
        
        self.side_letter_to_number_dictionary = {
            'r':'e',
            'l':'f',
            'u':'g',
            'd':'h',
            'f':'i',
            'b':'j'
        }

    def enqueue_side(self, side):
        self.arduino.enqueue_command_tag(self.convert_side_input(side))

    def convert_side_input(self, side):
        if (self.get_side_type(side) == 'letter'):
            side = self.convert_side_to_command(side)
        
        return side.lower()

    def get_side_type(self, side):
        return 'number' if type(side) == 'int' else 'letter'
    
    def convert_side_to_command(self, side):
        return self.side_letter_to_number_dictionary[side.lower()]