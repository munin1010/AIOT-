
from water_flow import *
from pressure import *
from waterlevel import *
def setup():
    init_pressure_sensor()
    init_flow_sensor()
    init_water_level_sensor()
    
def loop(): 
    
    
    sensor={'pressure':0,'flow_rate':0,'water_level':0}
    
    while True:
        
        sensor['pressure']=read_pressure()               
        new_flow_rate=read_flow_rate()
        if new_flow_rate:
            sensor['flow_rate']=new_flow_rate
        sensor['water_level']=round(read_water_level(),2)
        
        print("Pressure = {} hpa, Flow Rate = {} Litres/Hour, Water height = {} %".
              format(sensor['pressure'],sensor['flow_rate'],sensor['water_level']))   #print(flow_rate)
        
        time.sleep(0.5)
        

if __name__ == '__main__':
    setup()
    loop()