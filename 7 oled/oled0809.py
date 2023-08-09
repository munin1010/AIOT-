from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
from font import Font
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
f=Font(oled)

for a in range(5):
    print(a)
    
    f.text("warning!", 15, 20, 24)
    # Set white background and black text color
    oled.invert(True)
    oled.show()

    time.sleep(0.5)

    oled.fill(0)
    
    oled.show()

    oled.invert(False)
    time.sleep(0.5)