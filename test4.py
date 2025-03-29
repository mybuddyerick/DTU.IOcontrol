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

# These pins are for RGB LED
red_pin = Pin(15, Pin.OUT)
green_pin = Pin(32, Pin.OUT)
blue_pin = Pin(14, Pin.OUT)

i2c = I2C(0, scl=Pin(22), sda=Pin(23))
sensor = MCP9808(i2c)

def set_green():
    red_pin.value(1)    # OFF
    green_pin.value(0)  # ON
    blue_pin.value(1)   # OFF

def set_yellow():
    red_pin.value(0)    # ON
    green_pin.value(0)  # ON
    blue_pin.value(1)   # OFF

def set_red():
    red_pin.value(0)    # ON
    green_pin.value(1)  # OFF
    blue_pin.value(1)   # OFF

def turn_off_all():
    red_pin.value(1)
    green_pin.value(1)
    blue_pin.value(1)

turn_off_all()

while True:
    temp = sensor.temperature
    # print("Temperature: {:.2f} °C".format(temp))
    if temp < 26:
        set_green()
    elif temp < 28:
        set_yellow()
    else:
        set_red()
    time.sleep(0.1)
