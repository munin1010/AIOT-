from machine import ADC, Pin
import utime
adc2=None

def init_water_level_sensor():
    global adc2
    adc2= ADC(Pin(28))  
    
def main():
    global adc2
    water_level =init_water_level_sensor()
    while 1:
        water=water_level.read()
        print("Water Value is ---> %d" % water)
        utime.sleep(1)

if __name__ == '__main__':
    main()     


