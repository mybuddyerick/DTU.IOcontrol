from machine import Pin, I2C
from mcp9808 import MCP9808
import time

'''
PIN LOCATION:

SDA         - 23
SCL         - 22
RGB Blue    - 14
RGB Green   - 32
RGB Red     - 15
RED         - 33
YELLOW      - 27
GREEN       - 12
BUTTON      - 25
'''

green_led = Pin(12, Pin.OUT)
yellow_led = Pin(27, Pin.OUT)
red_led = Pin(33, Pin.OUT)

button = Pin(25, Pin.IN, Pin.PULL_UP)

leds = [green_led, yellow_led, red_led]

def clear_leds():
    for led in leds:
        led.value(0)

clear_leds()

i2c = I2C(0, scl=Pin(22), sda=Pin(23))
sensor = MCP9808(i2c)

while True:
    temp = sensor.temperature
    print("Temperature: {:.2f} °C".format(temp))
    clear_leds()
    if temp < 26:
        green_led.value(1)
    elif temp < 28:
        yellow_led.value(1)
    else:
        red_led.value(1)
    time.sleep(0.1)
