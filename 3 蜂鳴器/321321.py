from machine import Pin,PWM
from time import sleep
from machine import I2C,UART,ADC

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
def buzzer():
        for t in range(5):
            pwm = PWM(Pin(7,Pin.OUT))
            pwm.duty_u16(32000)
            for freq in range(500,1000,20):
                #print(freq)
                pwm.freq(freq)
                sleep(0.01)
            pwm.duty_u16(65535)
        print(t)
        
my_list = mqtt_controller.run()
my_string = ' '.join(my_list)  
print(my_string)

if 'banana' in my_string:
    print('warning')
#         _thread.start_new_thread(oled_thread, ())
#         buzzer()

