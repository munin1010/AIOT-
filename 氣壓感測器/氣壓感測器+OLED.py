from machine import ADC,Pin,I2C,UART
from ssd1306 import SSD1306_I2C
import utime
import math

sda=machine.Pin(12) #OLED
adc = ADC(Pin(28))  #感測器
i2c=I2C(0,sda=Pin(12),scl=Pin(28),freq=400000)
oled=SSD1306_I2C(128,64,i2c)
oled.fill(0)#0 全暗 1全亮
conversion_factor=5/65535    
   

while 1:
    reading=adc.read_u16()*conversion_factor
    print(reading)
    utime.sleep(0.5)
    
    disp=str(reading)
    f.text(disp,10,12,32)#X Y座標  字會在那顯示
    f.show()
    time.sleep(0.5)
    oled.fill(0)#清掉  所則字會重疊
