import RPi.GPIO as GPIO
#This file is intened to help use the raspberry pi's gpio pins with more ease.

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

def set_up_pin(pin):
    try:
        GPIO.setup(pin, GPIO.OUT)
    except Exception as error:
        return error

def set_up_pins(pins):
    for pin in pins:
        set_up_pin(pin)
    

def toggle_pin(pin, state):
    try:
        GPIO.output(pin, state)
    except Exception as error:
        return error
    
def tear_down_pins():
    GPIO.cleanup()
