from machine import ADC, Pin
import utime

adc0=None
min_waterheight=19200
max_waterheight=49300
def init_water_level_sensor():
    global adc0
    adc0 = ADC(Pin(28))
    
def read_water_level():
    #Calibraton values
    reading = (max_waterheight-adc0.read_u16())*100/(max_waterheight-min_waterheight)
    
    return reading

def main():
    init_water_level_sensor()
    while True:
        waterlevel=read_water_level()
        utime.sleep(0.5)
        print("water: " + "%.2f" % waterlevel +"% (adc: "+str(adc0.read_u16())+")")

if __name__ == '__main__':
    main()  