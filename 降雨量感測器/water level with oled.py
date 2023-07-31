# import required modules
from machine import ADC, Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
 
# use variables instead of numbers:
water = ADC(Pin(26)) # water PIN reference
 
#Calibraton values
min_waterheight=19200
max_waterheight=49300
 
readDelay = 0.5 # delay between readings
 
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                            # oled display height
 
i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=200000)       # Init I2C using pins GP0 & GP1 
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
 
while True:
    oled.fill(0)
    # read moisture value and convert to percentage into the calibration range
    waterlevel = (max_waterheight-water.read_u16())*100/(max_waterheight-min_waterheight) 
    # print values
    print("water: " + "%.2f" % waterlevel +"% (adc: "+str(water.read_u16())+")")
    
    oled.text("Water height",10,15)
    oled.text(str("%.2f" % waterlevel)+" %",35,35)
    oled.show()
    
    utime.sleep(readDelay) # set a delay between readings    