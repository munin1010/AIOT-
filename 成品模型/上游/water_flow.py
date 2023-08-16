from machine import Pin
import time

flow_frequency=0
lastcallTime=0
global adc2


def callback(pin):
    global flow_frequency
    flow_frequency=flow_frequency+1

   
def init_flow_sensor(y):
    global adc2
    adc2 = Pin(y,Pin.IN,Pin.PULL_UP)
    adc2.irq(trigger=Pin.IRQ_RISING, handler=callback)

def read_flow_rate():
    global lastcallTime
    global flow_frequency
    if ((time.ticks_ms()-lastcallTime) > 1000):  #if time interval is more a than 1 second
            flow_rate = (flow_frequency * 60 / 7.5)  #flowrate in L/hour= (Pulse frequency x 60 min) / 7.5 
            flow_frequency = 0                       # Reset Counter
            lastcallTime=time.ticks_ms()
            return flow_rate
                     
    
    return None
            
def main():
    init_flow_sensor(y)
    flow_rate=0
  
    while True:
        
        new_flow_rate=read_flow_rate()
        if new_flow_rate:
            flow_rate=new_flow_rate
            
        print("Flow Rate={} Litres/Hour".format(flow_rate))   #print(flow_rate)
            
        time.sleep(0.5)

 
    
            
        
        


if __name__ == '__main__':
    main() 