from machine import Pin, I2C, UART
import machine
import utime
from ssd1306 import SSD1306_I2C

class MQTTController:
    def __init__(self):
        self.uart = machine.UART(1, tx=Pin(8), rx=Pin(9), baudrate=115200)
        self.led = Pin(25, Pin.OUT)
        self.rst = Pin(5, Pin.OUT)
        self.rst.value(0)
        utime.sleep(0.1)
        self.rst.value(1)
        self.resp = b""
        self.wifi_ready = 0

    def send_cmd_wait_resp(self, cmd, timeout=1000):
        print(cmd)
        self.uart.write(cmd + '\r\n')
        self.wait_resp(timeout)

    def wait_resp(self, timeout=1000):
        prv_mills = utime.ticks_ms()
        self.resp = b""
        
        while (utime.ticks_ms() - prv_mills) < timeout:
            if self.uart.any():
                self.resp = b"".join([self.resp, self.uart.read(1)])

    def setup_wifi_mqtt(self, ssid, password, mqtt_server, topic_sub, topic_pub1, ready_cmd):
        self.send_cmd_wait_resp('RESET')
        utime.sleep(0.5)
        self.send_cmd_wait_resp(ssid)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(password)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(mqtt_server)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(topic_sub)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(topic_pub1)
        utime.sleep(0.01)
        self.send_cmd_wait_resp(ready_cmd)

        while not self.wifi_ready:
            utime.sleep(0.3)
            self.led.value(1)
            print('.')
            utime.sleep(0.3)
            self.led.value(0)
            print('.')
            self.wait_resp()
            if 'broker_connected' in str(self.resp):
                print('Ready')
                self.wifi_ready = 1

        print('start')
        utime.sleep(1)

    def process_response(self):
        if self.resp != b'':
            a = str(self.resp).replace('\\r\\n', '').replace('b', '').replace("'", "")
            c = a.split(' ')
            return c

    def run(self):
        while True:
            self.wait_resp()
            data = self.process_response()
            if data != None:
                return data
            utime.sleep(1)

if __name__ == "__main__":
    mqtt_controller = MQTTController()
    mqtt_controller.setup_wifi_mqtt('SSID+iP14max', 'PSWD+0966331739', 'BROKER+mqttgo.io', 'TOPIC+MQTT/1112', 'TOPIC1+MQTT/2222/2222', 'ready')
    while True:
        a=mqtt_controller.run()
        b=float(a[2])
        #print(b)
        if b==0.7:
            print('111111111111111')
        else:
           print('1')        #print(a)
