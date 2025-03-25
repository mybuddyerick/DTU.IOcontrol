from machine import Pin
import time

green_led = Pin(13, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)
red_led = Pin(27, Pin.OUT)

button = Pin(25, Pin.IN, Pin.PULL_UP)

leds = [green_led, yellow_led, red_led]
current_led = 0

green_led.on()

def clear_leds():
    for led in leds:
        led.value(0)

clear_leds()

leds[current_led].value(1) # turns on led

while True:
    if button.value() == 0: 
        time.sleep(0.02)
        while button.value() == 0:
            pass
        time.sleep(0.02) 
        
        # Cycle to the next LED
        clear_leds()
        current_led = (current_led + 1) % len(leds)  # Move to the next LED in sequence
        leds[current_led].value(1)  # Turn ON new LED
