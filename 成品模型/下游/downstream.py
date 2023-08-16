from machine import Pin,I2C,UART,ADC,PWM
from ssd1306 import SSD1306_I2C
from time import sleep
import _thread
from font import Font
from down_wifi import *

#oled
i2c= I2C(0,sda= Pin(12),scl=Pin(13),freq= 400000)
oled= SSD1306_I2C(128,64,i2c)
oled.fill(0)
f=Font(oled) 

#蜂鳴器            
def buzzer():
        for t in range(5):
            pwm = PWM(Pin(28,Pin.OUT))
            pwm.duty_u16(32000)
            for freq in range(500,1000,20):
                #print(freq)
                pwm.freq(freq)
                sleep(0.01)
            pwm.duty_u16(65535)
        print(t)


#MQTT
mqtt_controller = MQTTController()
mqtt_controller.setup_wifi_mqtt('SSID+iP14max',
                                'PSWD+0966331739',
                                'BROKER+mqttgo.io', 
                                'TOPIC+MQTT/1112',
                                'TOPIC1+MQTT/2222/2222',
                                'ready')

#雙核心-->OLED
def oled_thread():
        for a in range(5):
        
            f.text("warning!", 15, 20, 24)
            
            oled.invert(True)
            oled.show()

            sleep(0.5)
            oled.fill(0)
            
            oled.show()

            oled.invert(False)
            sleep(0.5)


def main():
    while True:
        a=mqtt_controller.run()
        x1=float(a[0])
        x2=float(a[1])
        x3=float(a[2])

        disp = str(x1) + 'hpa'
        oled.text(disp,10,10)
        oled.show()

        disp = str(x2) + 'L/H'
        oled.text(disp,10,31)
        oled.show()

        disp = str(x3) + '%'
        oled.text(disp,10,52)
        oled.show()

        sleep(10)

        oled.fill(0)
        oled.show()
        
        if x1>11 and x2==750:
            _thread.start_new_thread(oled_thread,())
            buzzer()
            
        elif x2>750 and x3>70:
            _thread.start_new_thread(oled_thread,())
            buzzer()
    

if __name__ == "__main__":
    main()

        

        