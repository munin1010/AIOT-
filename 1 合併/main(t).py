
from water_flow import *
from pressure import *

def setup():
    
    
    init_pressure_sensor()
    init_flow_sensor()
    
    
def loop(): 
    
    
    sensor={'pressure':0,'flow_rate':0}
    
    while True:
        
        sensor['pressure']=read_pressure()               
        new_flow_rate=read_flow_rate()
        if new_flow_rate:
            sensor['flow_rate']=new_flow_rate
        
        
        print("pressure = {} hpa, Flow Rate={} Litres/Hour".
              format(sensor['pressure'],sensor['flow_rate']))   #print(flow_rate)
        
        time.sleep(0.5)
        

if __name__ == '__main__':
    setup()
    loop()