from machine import Pin
import time

green_led = Pin(34, Pin.OUT)
yellow_led = Pin(39, Pin.OUT)
red_led = Pin(36, Pin.OUT)

button = Pin(25, Pin.IN, Pin.PULL_UP)

leds = [green_led, yellow_led, red_led]
current_led = 0  # Start with green LED

def clear_leds():
    for led in leds:
        led.value(0)

# Ensure only the first LED (green) is ON at startup
clear_leds()
leds[current_led].value(1)

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
