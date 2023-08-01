from machine import ADC,Pin
import time
import math
from machine import Pin,I2C,UART,ADC
from ssd1306 import SSD1306_I2C

i2c= I2C(0,sda= Pin(12),scl=Pin(13),freq= 400000)
oled= SSD1306_I2C(128,64,i2c)
oled.fill(0)



adc = ADC(Pin(26))  
conversion_factor=5/65535    


while 1:
    reading=adc.read_u16()*conversion_factor
    pressure = round(reading*10,1)
    print(pressure)
    time.sleep(0.5)
    
    disp = str(pressure)
    oled.text(disp,10,12)
    oled.show()
    time.sleep(0.5)
    oled.fill(0)
oled.show()