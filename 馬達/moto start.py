# 引入必要的庫
from machine import Pin
import time

# 定義馬達引腳
motor_pin = Pin(17, Pin.OUT)  # 連接抽水馬達的引腳

# 定義馬達啟動函數
def start_motor():
    motor_pin.on()

# 定義馬達停止函數
def stop_motor():
    motor_pin.off()

# 主循環
while True:
    start_motor()  # 啟動馬達
    #time.sleep(10) # 開啟馬達運行10秒
    #stop_motor()   # 停止馬達
    #time.sleep(10) # 休息10秒