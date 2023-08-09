import machine
import utime
from water_flow import *
from pressure import *
from waterlevel import *

class WiFiModule:
    def __init__(self):
        self.wifi_ready = False
        self.led = machine.Pin(25, machine.Pin.OUT)
        self.uart = machine.UART(1, tx=machine.Pin(8), rx=machine.Pin(9), baudrate=115200)
        self.reset_module()

    def reset_module(self):
        rst = machine.Pin(5, machine.Pin.OUT)
        rst.value(0)
        utime.sleep(0.1)
        rst.value(1)

    def send_cmd_wait_resp(self, cmd, timeout=1000):
        print(cmd)
        self.uart.write(cmd + '\r\n')
        self.wait_resp(timeout)

    def wait_resp(self, timeout=1000):
        prv_millis = utime.ticks_ms()
        resp = b""
        while (utime.ticks_ms() - prv_millis) < timeout:
            if self.uart.any():
                resp = b"".join([resp, self.uart.read(1)])
        if resp != b'':
            resp = str(resp)
            print(resp)  # Print the response
            if resp.find('connect') >= 0:
                self.wifi_ready = True

    def connect_wifi(self, ssid, password, channel, apikey):
        self.send_cmd_wait_resp("RESET")
        utime.sleep(0.5)
        self.send_cmd_wait_resp("SSID+" + ssid )
        utime.sleep(0.1)
        self.send_cmd_wait_resp("PSWD+" + password )
        utime.sleep(0.1)
        self.send_cmd_wait_resp("CHID+" + channel )
        utime.sleep(0.1)
        self.send_cmd_wait_resp("APIKEY+" + apikey )
        utime.sleep(0.1)
        self.send_cmd_wait_resp("ready")

        while not self.wifi_ready:
            utime.sleep(0.3)
            self.led.value(1)
            print('.')
            utime.sleep(0.3)
            self.led.value(0)
            print('.')
            self.wait_resp()
        print('start')

    def send_data(self, tp1, tp2, tp3 ):
        self.send_cmd_wait_resp('TP1+' + str(tp1))
        utime.sleep(0.1)
        self.send_cmd_wait_resp('TP2+' + str(tp2))
        utime.sleep(0.1)
        self.send_cmd_wait_resp('TP3+' + str(tp3))
        utime.sleep(0.1)
        self.send_cmd_wait_resp('TX_EN')
        utime.sleep(0.1)
        utime.sleep(20)

if __name__ == "__main__":
    wifi_module = WiFiModule()
    wifi_module.connect_wifi("AndroidHuang", "0987437180", "1000000", "3ZVJK8QWCNL6E0AJ")

    
    while True:
        
        wifi_module.send_data(x ,y , z)
