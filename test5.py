from machine import Pin, ADC, PWM
import time

'''
PIN LOCATION:

SDA             - 23
SCL             - 22
RGB Blue        - 14
RGB Green       - 32
RGB Red         - 15
POTENTIOMETER   - 13
'''

pot = ADC(Pin(13))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)

red_pwm = PWM(Pin(15), freq=100)
green_pwm = PWM(Pin(32), freq=100)
blue_pwm = PWM(Pin(14), freq=100)

while True:
    val = pot.read()
    val = val/4095
    pwm = int(1023 * val)
    red_pwm.duty(pwm)
    green_pwm.duty(pwm)
    blue_pwm.duty(pwm)
    time.sleep(0.1)
