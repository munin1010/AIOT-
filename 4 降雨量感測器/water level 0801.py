from machine import ADC, Pin
import utime

# use variables instead of numbers:
water = ADC(Pin(28)) # water PIN reference 3.3V

#Calibraton values
min_waterheight=19200
max_waterheight=49300

readDelay = 0.5

while True:
# read moisture value and convert to percentage into the calibration range
    waterlevel = (max_waterheight-water.read_u16())*100/(max_waterheight-min_waterheight)
    utime.sleep(readDelay)
    print("water: " + "%.2f" % waterlevel +"% (adc: "+str(water.read_u16())+")")