from machine import ADC,Pin
import time
import math


def pre(x):
    adc = ADC(Pin(x))  
    conversion_factor=5/65535 
    reading=adc.read_u16()*conversion_factor
    pressure = round(reading*10,1)
    print("{} hpa".format(pressure))
    time.sleep(0.5)
    

