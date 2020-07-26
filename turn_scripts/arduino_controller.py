import serial
import time
import timeit
import threading
import packet
import sys

class Arduino_Controller:
    def __init__(self):
        self.command_queue = []
        self.setup_arduino()
        self.is_currenlty_executing = False
        self.wait_thread = None
        self.current_packet = None

    
    def setup_arduino(self):
        print("Setting up Arduino connection.")
        self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(1)
        self.arduino.close()
        time.sleep(1)
        self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(1)
        self.arduino.close()
        time.sleep(1)
        self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(1)
        self.arduino.close()
        time.sleep(1)
        self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(1)
        print("Finished setting up Arduino connection.")

    def execute_command_queue(self):
        self.execute_commands(self.command_queue)
        self.command_queue = []

    def execute_commands(self, commands):
        self.is_currenlty_executing = True
        print(self.get_converted_command_list_into_command_string(commands))
        self.current_packet = packet.Packet(
            self.get_converted_command_list_into_command_string(commands), 
            self.arduino
        )

        self.current_packet.send()

    def enqueue_command_tag(self, command_name, data=[]):
        self.command_queue.append(command_name)
        # self.command_queue.append(self.get_command_tag(command_name, data))

    def get_converted_command_list_into_command_string(self, commands):
        return ''.join(commands) + "|"

    # def get_command_tag(self, command_name, data):
    #     return '<' + command_name + self.get_formatted_tag_data(data) + '>'

    # def get_formatted_tag_data(self, data):
    #     return '[' + ','.join(data) + ']'

    def check_if_arduino_is_still_processing(self):
        if self.current_packet and self.current_packet != None:
            return not self.current_packet.get_is_packet_finished_sending()
        
        return False
    
    def dissconnect(self, force=False, timeout=10):
        print('Disconnecting from Arduino.')
        if not force:
            self.wait_for_ready(timeout=timeout)

        print('close')
        self.arduino.close()

    def wait_for_ready(self, timeout=10):
        start_time = time.time()

        while True:
                if (not self.check_if_arduino_is_still_processing()):
                    break
                # self.update_timer_in_terminal(self.get_time_remaining_in_timeout_in_seconds(timeout, start_time))
                # if ((time.time() - start_time) > timeout and timeout != -1):
                #     print("\nWaiting for the arduino timed out.")
                #     break

    def update_timer_in_terminal(self, time_remaining):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(int(time_remaining))) 
        sys.stdout.flush()

    def get_time_remaining_in_timeout_in_seconds(self, timeout, start_time):
        return round(timeout - (time.time() - start_time))
                    