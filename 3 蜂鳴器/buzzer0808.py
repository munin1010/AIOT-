from machine import Pin,PWM
from time import sleep
pwm1=None

def init_buzzy_sensor(x):
    global pwm1
    pwm1 = PWM(Pin(x))
    pwm1.duty_u16(32000)

def read_water_level():
    global pwm1
    for freq in range(500,1000,20):
        print(freq)
        pwm1.freq(freq)
        sleep(0.01)