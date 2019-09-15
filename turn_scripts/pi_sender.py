# a command structure template is below.
# |{10 charactor time stamp}{commands}|

# regex for finding command \|[0-9 a-z A-Z']{10}[a-z A-Z'0-9]*\|
import paramiko
import time
import re
import math
import kociemba
import timeit


file_location = '/home/pi/Documents/robot/turn_scripts/'
file_name = 'current.txt'


time_slot_increments = 1000

def send_command(command, ssh):
        print(command)
        stdin, stdout, stderr = ssh.exec_command('echo "' + command + '" >> ' + file_location + '/' + file_name)

def get_sleep_time_til_time_slot(time_slot):
        current_time_slot = get_current_time_slot()
        time_till_slot_reset = ((abs(10 - current_time_slot) + time_slot) % 10) * .001
        return time_till_slot_reset

def wait_till_time_slot(time_slot):
        sleep_time = get_sleep_time_til_time_slot(7)
        time.sleep(sleep_time)

def generate_time_stamp():
        current_time =time.time()
        time_stamp = int(math.floor((current_time * 1000) % 10000000000))
        return time_stamp

def run_command(instructions, ssh):
        time_stamp = generate_time_stamp()
        command = '|' + str(time_stamp) + str(instructions) + '|'
        print(command)
        send_command(command, ssh)

