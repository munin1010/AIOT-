from machine import ADC,Pin
import time
import math
adc0=None

def init_pressure_sensor():
    global adc0
    adc0 = ADC(Pin(26))  

def read_pressure():
    
    conversion_factor=50/65535 
    reading=adc0.read_u16()*conversion_factor

    return round(reading,1)



def main():
    init_pressure_sensor()
    while 1:
        
        pressure=read_pressure()
        print("pressure = {} hpa".format(pressure)) 
        time.sleep(0.5)
        


if __name__ == '__main__':
    main()  

    

    
    

 