from machine import Pin,PWM
from time import sleep

pwm = PWM(Pin(28))
pwm.duty_u16(32000)

while True:
    for freq in range(500,1000,20):
        print(freq)
        pwm.freq(freq)
        sleep(0.01)