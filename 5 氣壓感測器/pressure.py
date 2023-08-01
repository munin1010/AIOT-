from machine import ADC,Pin
import time
import math
adc = ADC(Pin(26))  
conversion_factor=5/65535    


while 1:
    reading=adc.read_u16()*conversion_factor
    #
    pressure = round(reading*10,1)
    print("pressure = {} hpa".format(pressure)) 
    y=str(pressure)
    #
    print(pressure)
    time.sleep(0.5)

 