from machine import Pin,PWM
from time import sleep
from machine import I2C,UART,ADC
from ssd1306 import SSD1306_I2C

#buzzer
pwm = PWM(Pin(7,Pin.OUT))
pwm.duty_u16(32000)
for t in range(5):
    print(t)
    for freq in range(500,1000,20):
        #print(freq)
        pwm.freq(freq)
        sleep(0.01)
    
pwm.duty_u16(65535)


'''
cam = Pin(12)
cam.value(0)
sleep(0.5)
cam.value(1)
'''

#接收數據
'''
While True:
    
 OLED顯示

 If 流速> L/R and waterlevel > X 
  ((Buzzer on + OLED warning) (條件要持續超過a秒, 則執行b秒警報))
  Else break

 If 流速> L/R and pressure > y
  ((Buzzer on + OLED warning) (條件要持續超過a秒, 則執行b秒警報))
  Else break
 '''

