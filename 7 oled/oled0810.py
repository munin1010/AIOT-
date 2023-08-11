oled顯示MQTT數據

from machine import Pin,I2C,UART,ADC
from ssd1306 import SSD1306_I2C
import time

i2c= I2C(0,sda= Pin(12),scl=Pin(13),freq= 400000)
oled= SSD1306_I2C(128,64,i2c)
oled.fill(0)
while True:
    disp = str(1) + 'L/H'
    oled.text(disp,10,10)
    oled.show()


    disp = str(2) + '%'
    oled.text(disp,10,31)
    oled.show()

    disp = str(3) + 'hpa'
    oled.text(disp,10,52)
    oled.show()

    time.sleep(1)

    oled.fill(0)
    oled.show()

'''
While True:
    
 

 If 流速> L/R and waterlevel > X 
  ((Buzzer on + OLED warning) (條件要持續超過a秒, 則執行b秒警報))
  Else break

 If 流速> L/R and pressure > y
  ((Buzzer on + OLED warning) (條件要持續超過a秒, 則執行b秒警報))
  Else break
 '''
