from machine import Pin,I2C,UART,ADC
from ssd1306 import SSD1306_I2C
import time
from wifisub0811_1 import *


i2c= I2C(0,sda= Pin(12),scl=Pin(13),freq= 400000)
oled= SSD1306_I2C(128,64,i2c)
oled.fill(0)

mqtt_controller = MQTTController()
mqtt_controller.setup_wifi_mqtt('SSID+iP14max', 'PSWD+0966331739', 'BROKER+mqttgo.io', 'TOPIC+MQTT/1112', 'TOPIC1+MQTT/2222/2222', 'ready')

while True:
    a=mqtt_controller.run()
    x1=float(a[0])
    x2=float(a[1])
    x3=float(a[2])

    
    disp = str(x1) + 'L/H'
    oled.text(disp,10,10)
    oled.show()


    disp = str(x2) + '%'
    oled.text(disp,10,31)
    oled.show()

    disp = str(x3) + 'hpa'
    oled.text(disp,10,52)
    oled.show()

    time.sleep(10)

    oled.fill(0)
    oled.show()