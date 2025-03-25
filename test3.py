from machine import Pin
import time

green_led = Pin(13, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)
red_led = Pin(27, Pin.OUT)

button = Pin(25, Pin.IN, Pin.PULL_UP)

leds = [green_led, yellow_led, red_led]
current_led = 0

def clear_leds():
    for led in leds:
        led.value(0)

clear_leds()

leds[current_led].value(1)