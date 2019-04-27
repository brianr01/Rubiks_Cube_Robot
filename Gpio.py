import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def Set_Up_Pin(pin):
    GPIO.setup(int(pin), GPIO.OUT)
	
def Set_Up_Pins(pins):
    for i in pins:
        if i != False:
            Set_Up_Pin(int(i))
		
def Toggle_Pin(pin,state):
    GPIO.output(pin,state)
    
#Set_Up_Pins([5])
#Toggle_Pin(5,False)