#This file is intened to help use the raspberry pi's gpio pins with more ease.

#Tries to import RPi.GPIO. If this fails it allows the program to continue without them.
use_gpio = True
try:
    import RPi.GPIO as GPIO
except Exception as error:
    print('failed to setup GPIO pins.')
    use_gpio = False

#if the gpio module imported successfuly set the mode on the board and then dissable warnings
if (use_gpio):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def set_up_pin(pin):
    try:
        if (use_gpio):
            GPIO.setup(pin, GPIO.OUT)
    except Exception as error:
        return error

def set_up_pins(pins):
    if (use_gpio):
        for pin in pins:
            set_up_pin(pin)
    
def toggle_pin(pin, state):
    try:
        if (use_gpio):
            GPIO.output(pin, state)
    except Exception as error:
        return error
    
def tear_down_pins():
    if (use_gpio):
        GPIO.cleanup()
