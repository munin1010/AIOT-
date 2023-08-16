from machine import Pin,I2C,UART,ADC,PWM
from ssd1306 import SSD1306_I2C
from time import sleep
import _thread
from font import Font
from down_wifi import *
x1,x2,x3=[],[],[]

#oled
i2c= I2C(0,sda= Pin(12),scl=Pin(13),freq= 400000)
oled= SSD1306_I2C(128,64,i2c)
oled.fill(0)
f=Font(oled) 


#OLED
def oled_run(x1,x2,x3):
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
        
def oled_warn():
        for a in range(5):
        
            f.text("warning!", 15, 20, 24)
            
            oled.invert(True)
            oled.show()

            sleep(0.5)
            oled.fill(0)
            
            oled.show()

            oled.invert(False)
            sleep(0.5)

#雙核心-->蜂鳴器          
def buzzer_thread():
        for t in range(5):
            pwm = PWM(Pin(28,Pin.OUT))
            pwm.duty_u16(32000)
            for freq in range(500,1000,20):
                #print(freq)
                pwm.freq(freq)
                sleep(0.01)
            pwm.duty_u16(65535)
        print(t)

def main():
    mqtt_controller = MQTTController()
    mqtt_controller.setup_wifi_mqtt('SSID+iP14max',
                                'PSWD+0966331739',
                                'BROKER+mqttgo.io', 
                                'TOPIC+MQTT/1112',
                                'TOPIC1+MQTT/2222/2222',
                                'ready')
    while True:
        a=mqtt_controller.run()
        if len(a)>2 :
            x1=float(a[0])
            x2=float(a[1])
            x3=float(a[2])
            oled_run(x1,x2,x3)

            if x1>11.0 and x2>750.0:
                _thread.start_new_thread(buzzer_thread,())
                oled_warn()
               
            elif x2>750.0 and x3>70.0 :
                _thread.start_new_thread(buzzer_thread,())
                oled_warn()
        else:
            continue
if __name__ == "__main__":
    main()

        

        