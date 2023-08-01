from ssd1306 import SSD1306_I2C

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                            # oled display height
 
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=200000)       # Init I2C using pins GP0 & GP1 
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display


while True:
    oled.fill(0)
    
    oled.text("Water height",10,15)
    oled.text(str("%.2f" % waterlevel)+" %",35,35)
    oled.show()
    
    utime.sleep(readDelay) # set a delay between readings   