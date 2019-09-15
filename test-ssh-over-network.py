import paramiko
import time
import timeit
import math
COMP = "pi"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('169.254.136.168', username="pi", password="popcornamerica23", allow_agent = False)
file_location = '/home/pi/Documents/cube_controller/'
file_name = 'execute.txt'
stdin, stdout, stderr = ssh.exec_command('echo "' + command + '" >> ' + file_location + '/' + file_name)
executed = True

print('start')



#stdin, stdout, stderr = ssh.exec_command('echo "po r u d pf" >> /home/pi/Documents/cube_controller/execute.txt')



execution_millisecond = 7
time_scale = 1000
time_stamp = ''

def send_commands(command):
    print('started')
    current_time = time.time()
    current_millisecond = math.floor((current_time % .01) * time_scale)
    time_stamp = math.floor(time.time() * 300 % 1000000000)
    if (current_millisecond > execution_millisecond):
        sleep_time = execution_millisecond - current_millisecond + 10
    else:
        sleep_time = execution_millisecond - current_millisecond

    time.sleep(sleep_time / time_scale)
    print(time.time())
    
    print(time.time())
    print('sent')
    time.sleep(.01)


send_commands("po r' r f r r pf")

