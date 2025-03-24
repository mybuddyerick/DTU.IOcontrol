from machine import Pin
import time

led = Pin(21, Pin.OUT)      
button = Pin(32, Pin.IN, Pin.PULL_UP) 

while True:
    if button.value() == 0: 
        led.value(1)  
        time.sleep(0.5)
        led.value(0) 
        time.sleep(0.5)
    else:
        led.value(0)