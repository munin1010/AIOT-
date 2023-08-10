import _thread
from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
from font import Font  # 如果有需要的話
import time
from time import sleep

i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
f=Font(oled)  

pwm = PWM(Pin(7,Pin.OUT))
pwm.duty_u16(32000)

# OLED 顯示的二核心同時警告
def oled_thread():
    for a in range(5):
    
        f.text("warning!", 15, 20, 24)
        
        oled.invert(True)
        oled.show()

        time.sleep(0.5)
        oled.fill(0)
        
        oled.show()

        oled.invert(False)
        time.sleep(0.5)
_thread.start_new_thread(oled_thread,())

#buzzer 迴圈

for a in range(15):
    print(a)
    for freq in range(500,1000,20):
        #print(freq)
        pwm.freq(freq)
        sleep(0.01)
    
pwm.duty_u16(65535)
    



