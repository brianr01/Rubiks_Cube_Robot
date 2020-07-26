import threading
import time

class Packet:
    def __init__(self, packet, arduino_connection):
        self.packet = packet
        self.arduino_connection = arduino_connection
        self.is_packet_finished_sending = False
        self.start_time = None

        self.create_packet_thread()

    def create_packet_thread(self):
        self.packet_thread = threading.Thread(target=self.send_packet)

    def send(self):
        self.packet_thread.start()
    
    def send_packet(self):
        self.start_time = time.time()
        self.send_string(self.packet)
        self.wait_for_response()

    def send_string(self, string):
        for character in string:
            self.send_character(character)

    def send_character(self, character):
        self.arduino_connection.write(character.encode('UTF-8'))

    def wait_for_response(self):
        print(self.arduino_connection.readline())

    def get_is_packet_finished_sending(self):
        self.is_packet_finished_sending = not self.packet_thread.isAlive()
        return self.is_packet_finished_sending

        return self.is_packet_finished_sending

    def get_time_elapsed(self):
        return time.time() - self.start_time

    def kill_packet_thread(self):
        self.packet_thread




