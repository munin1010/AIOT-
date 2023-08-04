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
    reading2=str(adc0.read_u16())
    return reading,reading2

def main():
    init_water_level_sensor()
    while True:
        reading,reading2=read_water_level()
        utime.sleep(0.5)
        print("water: " + "%.2f" % reading +"% (adc: "+reading2+")")

if __name__ == '__main__':
    main()  