from machine import Pin
import time

'''
PIN LOCATION:

RED - 13
BUTTON - 25
'''

red_led = Pin(13, Pin.OUT)      
button = Pin(25, Pin.IN, Pin.PULL_UP) 

while True:
    if button.value() == 0: 
        red_led.value(1)  
        time.sleep(0.5)
        red_led.value(0)
        time.sleep(0.5)
    else:
        red_led.value(0)
