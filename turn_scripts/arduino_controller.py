import serial
import time
import timeit
import threading
import packet

class Arduino_Controller:
    def __init__(self):
        self.command_queue = []
        self.setup_arduino()
        self.is_currenlty_executing = False
        self.wait_thread = None
        self.current_packet = None

    
    def setup_arduino(self):
        self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(1)

    def execute_command_queue(self):
        self.execute_commands(self.command_queue)
        self.command_queue = []

    def execute_commands(self, commands):
        self.current_packet = packet.Packet(
            self.get_converted_command_list_into_command_string(commands), 
            self.arduino
        )

        self.current_packet.send()

    def enqueue_command_tag(self, command_name, data):
        self.command_queue.append(self.get_command_tag(command_name, data))

    def get_converted_command_list_into_command_string(self, commands):
        return ''.join(commands) + "|"

    def get_command_tag(self, command_name, data):
        return '<' + command_name + self.get_formatted_tag_data(data) + '>'

    def get_formatted_tag_data(self, data):
        return '[' + ','.join(data) + ']'

    def check_if_arduino_is_still_processing(self):
        if self.current_packet:
            return self.current_packet.get_is_packet_finished_sending()
        
        return False
    
    def dissconnect(self, force=False, timeout=10000):
        if not force:
            self.wait_for_ready(timeout=timeout)
    
        self.arduino.close()

    def wait_for_ready(self, timeout=10000):
        start_time_in_miliseconds = time.time() * 1000
        while not self.check_if_arduino_is_still_processing():
                if ((time.time() * 1000 - start_time_in_miliseconds) > timeout and timeout != -1):
                    print("Waiting for the arduino timed out.")
                    break
                    