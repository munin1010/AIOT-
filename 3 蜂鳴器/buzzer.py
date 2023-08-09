from machine import Pin,PWM
from time import sleep

pwm = PWM(Pin(28))
pwm.duty_u16(32000)

cam = Pin(12)

cam.value(0)
sleep(0.5)
cam.value(1)  

while True:
    for freq in range(500,1000,20):
        print(freq)
        pwm.freq(freq)
        sleep(0.01)