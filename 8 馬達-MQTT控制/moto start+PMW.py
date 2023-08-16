# 引入必要的庫
from machine import Pin, PWM
import time

# 定義馬達引腳
motor_pin = Pin(17, Pin.OUT)  # 連接抽水馬達的引腳

# 初始化PWM控制器
pwm = PWM(motor_pin)

# 定義馬達轉速控制函數
def set_motor_speed(speed):
    # speed 是 0 到 65535 之間的值，0 表示停止，65535表示最大轉速
    pwm.duty_u16(speed)

# 主循環
while True:
    set_motor_speed(60000)  # 設定馬達轉速為一半（範圍是 0-65535）
    time.sleep(1)         # 運行馬達 a 秒
#     set_motor_speed(0)    # 停止馬達
    time.sleep(1)         # 休息 a 秒