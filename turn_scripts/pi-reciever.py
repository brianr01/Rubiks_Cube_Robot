# a command structure template is below.
# |{10 charactor time stamp}{commands}|

# regex for finding command \|[0-9 a-z A-Z']{10}[a-z A-Z'0-9]*\|

import re
import time
import class_cube
import math

time_slot_increments = 1000

# clears all the text files
def clear_files():
        files = ["current", "history", "time_stamps"]
        for file in files:
                open(file + ".txt", "w").close()

# read the file that contains new commands
def read_current():
        wait_till_time_slot(7)
        file = open("current.txt", "r")
        current = file.read()
        file.close()
        return current

# read the file that contains executed commands
def read_history():
        wait_till_time_slot(7)
        file = open("history.txt", "r")
        history = file.read()
        file.close()
        return history

# append to the file that contains the executed commands
def write_history(new_history):
        wait_till_time_slot(7)
        file = open("history.txt", "a")
        file.write(new_history)
        file.close()

# append to the file that contains the time stamps for each command
def write_time_stamp(new_time_stamp):
        wait_till_time_slot(7)
        file = open("time_stamps.txt", "a")
        file.write('|' + str(new_time_stamp) + '|')
        file.close()

def get_commands_from_string(string):
        commands = re.findall("\|[0-9 a-z A-Z']{10}[a-z A-Z'0-9]*\|", string)
        return commands

# returns any new commands from the current.txt file
def get_new_commands():
        current = read_current()
        old = read_history()

        current = get_commands_from_string(current)
        old = get_commands_from_string(old)

        new = list(set(current) - set(old))
        return new

# returns a command's time stamp and instruction set
def break_down_command(command):
        time_stamp = command[1:10]
        instructions = command[11:-1]
        return [time_stamp, instructions]

# runs a command's instruction set.
def run_commands(commands):
        # if there are commands enter the loop
        if  commands:
                for command in commands:
                        broken_down_command = break_down_command(command)

                        turn_scripts.execute_algorithm(broken_down_command[1])

                        # update the logs for the commands
                        write_history(command)

                        write_time_stamp(broken_down_command[0])

def get_current_time_slot():
        current_time = time.time()
        time_in_time_slot_increments = (current_time * time_slot_increments)
        current_time_slot = math.floor(time_in_time_slot_increments % 10)
        return current_time_slot

def get_sleep_time_til_time_slot(time_slot):
        current_time_slot = get_current_time_slot()
        time_till_slot_reset = ((abs(10 - current_time_slot) + time_slot) % 10) * .001
        return time_till_slot_reset

def wait_till_time_slot(time_slot):
        sleep_time = get_sleep_time_til_time_slot(7)
        time.sleep(sleep_time)


clear_files()
motors_pins = {'r':[5, 3, 12],
               'l':[11, 7, 36],
               'u':[15, 13, 16],
               'd':[31, 29, 22],
               'f':[35, 33, 18],
               'b':[40, 37, 32]}

turn_scripts = class_cube.Cube(motors_pins)
print(time.time())
# main loop
while True:
        run_commands(get_new_commands())

