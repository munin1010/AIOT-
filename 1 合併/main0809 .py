from WIFI0809 import *
from water_flow import *
from pressure import *
from waterlevel0804 import *


esp01_mqtt = ESP01_MQTT(tx_pin=8, rx_pin=9)

def setup():
    init_pressure_sensor()
    init_flow_sensor()
    init_water_level_sensor()
    
   
     
    esp01_mqtt.setup(
        ssid='SSID+iP14max',
        password='PSWD+0966331739',
        mqtt_server='BROKER+mqttgo.io',
        channel="1000000",
        apikey="ZRBVREF0P7C6N7XR",
        topic_sub='TOPIC+MQTT/111/11',
        topic_pub1='TOPIC1+MQTT/2222/2222',
        topic_pub2='TOPIC2+MQTT/3333/3333',
        topic_pub3='TOPIC3+MQTT/4444/4444',
        ready='ready'
    )
    


    
def loop(): 
    sensor={'pressure':0,'flow_rate':0,'water_level':0}
    while True:
        
        sensor['pressure']=read_pressure()               
        new_flow_rate=read_flow_rate()
        if new_flow_rate:
            sensor['flow_rate']=new_flow_rate
        sensor['water_level']=round(read_water_level(),2)
        
        x=sensor['pressure']   #print(flow_rate)
        y=sensor['flow_rate']
        z=sensor['water_level']

        
        time.sleep(0.5)
        value1_to_send = x
        value2_to_send = y
        value3_to_send = z
        global esp01_mqtt
        esp01_mqtt.publish_data(value1_to_send, value2_to_send, value3_to_send)
        time.sleep(1)
        
        
        

if __name__ == '__main__':
    setup()
    loop()
   

   