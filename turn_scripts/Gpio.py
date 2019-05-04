import RPi.GPIO as GPIO
#This file is intened to help use the raspberry pi's gpio pins with more ease.

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

def set_up_pin(pin):
    GPIO.setup(int(pin), GPIO.OUT)

def set_up_pins(pins):
    for (i in pins):
        if i != False:
            Set_Up_Pin(int(i))
		
def toggle_pin(pin,state):
    GPIO.output(pin,state)
    