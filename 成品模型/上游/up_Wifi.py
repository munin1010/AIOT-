from machine import Pin
import machine
import utime


class ESP01_MQTT:
    def __init__(self, tx_pin, rx_pin):
        self.uart = machine.UART(1, tx=Pin(tx_pin), rx=Pin(rx_pin), baudrate=115200)
        self.led = Pin(25, Pin.OUT)
        self.count = 0
        self.wifi_ready = 0

    def send_cmd_wait_resp(self, cmd, timeout=1000):
        print(cmd)
        self.uart.write(cmd + '\r\n')
        self.wait_resp()

    def wait_resp(self, timeout=1000):
        prv_mills = utime.ticks_ms()
        resp = b""
        while (utime.ticks_ms() - prv_mills) < timeout:
            if self.uart.any():
                resp = b"".join([resp, self.uart.read(1)])
        if resp != b'':
            resp = str(resp)
            print(resp)
            if resp.find('on') >= 0:
                self.led.value(1)
            if resp.find('off') >= 0:
                self.led.value(0)
                self.count = 0
            if resp.find('broker_connected') >= 0:
                print('Ready')
                self.wifi_ready = 1

    def setup(self, ssid, password, mqtt_server, channel, apikey, topic_sub, topic_pub1,topic_pub2,topic_pub3,topic_pub4, topic_pub5,ready):
        reset = 'RESET'
        self.send_cmd_wait_resp(reset)
        utime.sleep(0.5)
        self.send_cmd_wait_resp(ssid)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(password)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(mqtt_server)
        utime.sleep(0.01)
        self.send_cmd_wait_resp("CHID+" + channel )
        utime.sleep(0.1)
        self.send_cmd_wait_resp("APIKEY+" + apikey )
        utime.sleep(0.1)
        self.send_cmd_wait_resp(topic_sub)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(topic_pub1)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(topic_pub2)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(topic_pub3)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(topic_pub4)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(topic_pub5)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(ready)

        while not self.wifi_ready:
            utime.sleep(0.3)
            self.led.value(1)
            print('.')
            utime.sleep(0.3)
            self.led.value(0)
            print('.')
            self.wait_resp()

        print('Start')
        utime.sleep(1)
    def warm_data(self, value,value2):
        self.wait_resp()
        x=str(value)
        self.send_cmd_wait_resp(f'PB4+ {x} ')
        x1=str(value2)
        self.send_cmd_wait_resp(f'PB5+ {x1} ')
        
    def publish_data(self, value1, value2, value3):
        self.wait_resp()
        y1 = str(value1)
        y2 = str(value2)
        y3 = str(value3)
        
        
        self.send_cmd_wait_resp(f'PB1+ {y1} ')
        self.send_cmd_wait_resp(f'PB2+ {y2} ')
        self.send_cmd_wait_resp(f'PB3+ {y3} ')
        self.count = value1  # You can choose which value to use for count or omit this line
        #global count
       
            
        self.send_cmd_wait_resp(f'TP1+ {y1}' )
        utime.sleep(0.5)
        self.send_cmd_wait_resp(f'TP2+ {y2}' )
        utime.sleep(0.5)
        self.send_cmd_wait_resp(f'TP3+ {y3}' )
        utime.sleep(0.5)
        self.send_cmd_wait_resp('TX_EN')
        utime.sleep(5)
 
def main():
    esp01_mqtt = ESP01_MQTT(tx_pin=8, rx_pin=9)
    esp01_mqtt.setup(
        ssid='SSID+iP14max',
        password='PSWD+0966331739',
        mqtt_server='BROKER+mqttgo.io',
        channel="1000000",
        apikey="3ZVJK8QWCNL6E0AJ",
        topic_sub='TOPIC+MQTT/1112',
        topic_pub1='TOPIC1+MQTT/2222/2222',
        topic_pub2='TOPIC2+MQTT/3333/3333',
        topic_pub3='TOPIC3+MQTT/4444/4444',
        topic_pub4='TOPIC4+MQTT/886', #警報用
        topic_pub5='TOPIC5+MQTT/887',#平常用
        ready='ready'
    )
    value1_to_send=0
    value2_to_send=0
    value3_to_send=0

    while True:
        value1_to_send += 1
        value2_to_send += value1_to_send
        value3_to_send += value2_to_send
        esp01_mqtt.publish_data(value1_to_send, value2_to_send, value3_to_send)
        utime.sleep(1)
        if value1_to_send >0 and value3_to_send>0:
            x=20
            X1=22
            esp01_mqtt.warm_data(x,X1)
        elif value1_to_send>0 and value3_to_send>0:
            x=20
            X1=22
            esp01_mqtt.warm_data(x,X1)
 
 
# Usage example:
if __name__ == '__main__':
    main()