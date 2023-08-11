from machine import Pin,I2C,UART,ADC
import machine
import utime
import time
from ssd1306 import SSD1306_I2C

i2c= I2C(0,sda=Pin(12),scl=Pin(13),freq=400000)
oled = SSD1306_I2C(128,64,i2c)
oled.fill(0)

b=[]
count=0
wifi_ready=0
uart = machine.UART(1,tx=Pin(8),rx=Pin(9),baudrate=115200)
led = Pin(25,Pin.OUT)
rst = Pin(5,Pin.OUT)
rst.value(0)
utime.sleep(0.1)
rst.value(1)
#=======MQTT========
reset='RESET'
ssid = 'SSID+iP14max'   # wifi 帳號
password = 'PSWD+0966331739'   # wifi 密碼
mqtt_server = 'BROKER+mqttgo.io'  # MQTT Broker
topic_sub = 'TOPIC+MQTT/1112'  #subscribe Topic     
topic_pub1= 'TOPIC1+MQTT/2222/2222'  #Publish Topic 
ready='ready'  # 資料傳送至ESP01完成，開始連線

def sendCMD_waitResp(cmd, uart=uart, timeout=1000):
    print(cmd)
    uart.write(cmd+'\r\n')
    waitResp()
   
def waitResp(uart=uart, timeout=1000):
    global count,wifi_ready,resp
    prvMills = utime.ticks_ms()
    
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
        
    if resp != b'' :
        resp = str(resp)  
        print(resp)   #印出接收MQTT的paylod
        if (resp.find('on'))>=0:
            led.value(1)
        if (resp.find('off'))>=0:
            led.value(0)
            count = 0
        if (resp.find('broker_connected'))>=0:
            print('Ready')
            wifi_ready=1
            
sendCMD_waitResp(reset)
utime.sleep(0.5)
sendCMD_waitResp(ssid)
utime.sleep(0.01)
sendCMD_waitResp(password)
utime.sleep(0.01)
sendCMD_waitResp(mqtt_server)
utime.sleep(0.01)
sendCMD_waitResp(topic_sub)
utime.sleep(0.01)
sendCMD_waitResp(topic_pub1)
utime.sleep(0.01)
sendCMD_waitResp(ready)

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
c=[]
while 1 :
    waitResp()
    disp =  'L/H'
    oled.text(disp,60,0)
    oled.show()


    disp =  '%'
    oled.text(disp,60,15)
    oled.show()

    disp =  'hpa'
    oled.text(disp,60,30)
    oled.show()

    #time.sleep(8)

    #oled.fill(0)
    #oled.show()
    
    global resp
    if resp!= b'':
        a=str(resp).replace('\\r\\n','').replace('b','').replace("'","")
        c.append(a.split(','))
        print(c)
        #oeld持續顯示
        oled.fill(0)
        row = 0
        for item in c[0]:
            oled.text(item,0,row)
            row += 15
        oled.show()
        #list清空
        if len(c) ==1:
            del c[0]
        #st=eval(c[0][0])
        #if st ==0.8:
            #print('aaa')
        #else:
            #print('bbbb')
    #else:
        #continue
        
        #if st == 0.7:
            #print('aaa')
            #del c[0]
       # else:
          #  continue
          
    
    utime.sleep(1)
    