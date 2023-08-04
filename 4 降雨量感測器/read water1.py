from machine import ADC, Pin
import utime
adc2=None

def read_pressure():
    global adc0
    adc2= ADC(Pin(26))  
    
def main():
    water_level =read_pressure()
    while 1:
        print("Water Value is ---> %d" % water_level.read_u16())
        utime.sleep(1)

if __name__ == '__main__':
    main()     


