from machine import ADC,Pin
import time
import math
adc = ADC(Pin(28))  
conversion_factor=5/65535    


while 1:
    reading=adc.read_u16()*conversion_factor
    print(reading)
    time.sleep(0.5)

 