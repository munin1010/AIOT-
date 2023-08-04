from machine import ADC, Pin
import utime
adc2=None
min_waterheight=19200
max_waterheight=49300


def adc():
    global adc2
    adc2 = ADC(Pin(28))  
    
def Calibraton_values():
  
    
    waterlevel = ((max_waterheight-adc2.read_u16())*100)/(max_waterheight-min_waterheight)
    waterlevel2=str(adc2.read_u16())
   
    return waterlevel,waterlevel2



def main():
    adc()
    readDelay = 0.5
    
    while 1:
        
        waterlevel,waterlevel2=Calibraton_values()
        
        print("water: " + "%.2f" % waterlevel +"% (adc: "+waterlevel2+")")
        
        utime.sleep(readDelay)

if __name__ == '__main__':
    main()     


