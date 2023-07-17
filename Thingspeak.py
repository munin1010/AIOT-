from machine import Pin
import machine
import utime
a=0
wifi_ready=0
led = Pin(25,Pin.OUT)
uart = machine.UART(1,tx=Pin(8),rx=Pin(9),baudrate=115200)
rst = Pin(5,Pin.OUT)
rst.value(0)
utime.sleep(0.1)
rst.value(1)

def sendCMD_waitResp(cmd, uart=uart, timeout=1000):
    print(cmd)
    uart.write(cmd+'\r\n')
    waitResp()
   
def waitResp(uart=uart, timeout=1000):
    global data,wifi_ready
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    if resp != b'' :      
        resp = str(resp)
        print(resp)   #印出
        if (resp.find('connect'))>=0:
            wifi_ready=1
sendCMD_waitResp("RESET")
utime.sleep(0.5)
sendCMD_waitResp("SSID+iP14max")  #SSID帳號
utime.sleep(0.1)
sendCMD_waitResp("PSWD+0966331739") #PSWD密碼
utime.sleep(0.1)
sendCMD_waitResp("CHID+1000000")
utime.sleep(0.1)
sendCMD_waitResp("APIKEY+LSG7G23E3TLUK6C0") #
utime.sleep(0.1)
sendCMD_waitResp("ready")
utime.sleep(0.1)

while (not wifi_ready) :
    utime.sleep(0.3)
    led.value(1)
    print('.')
    utime.sleep(0.3)
    led.value(0)
    print('.')
    waitResp()    
print('start')
utime.sleep(1)
while True :
    a+=1
    x=str(a)
    y=str(a+5)
    sendCMD_waitResp('TP1+'+x)
    utime.sleep(0.1)
    sendCMD_waitResp('TP2+'+y)
    utime.sleep(0.1)
    sendCMD_waitResp('TX_EN')
    utime.sleep(0.1)
    utime.sleep(20)