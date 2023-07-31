# 引入必要的庫
from machine import Pin, PWM
import time

# 定義馬達引腳
motor_pin = Pin(17, Pin.OUT)  # 連接抽水馬達的引腳

# 初始化PWM控制器
pwm = PWM(motor_pin)

# 定義馬達轉速控制函數
def set_motor_speed(speed):
    # speed 是 0 到 1023 之間的值，0 表示停止，1023 表示最大轉速
    pwm.duty(speed)

# 主循環
while True:
    set_motor_speed(512)  # 設定馬達轉速為一半（範圍是 0-1023）
    time.sleep(5)         # 運行馬達 5 秒
    set_motor_speed(0)    # 停止馬達
    time.sleep(5)         # 休息 5 秒