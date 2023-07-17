# 导入必要的模块
import machine

# 初始化PWM通道
pwm_pin = machine.Pin(12)  # 假设使用引脚12作为PWM输出
pwm = machine.PWM(pwm_pin)  # 初始化PWM对象

# 设置PWM参数
pwm.freq(1000)  # 设置频率为1kHz
pwm.duty(512)  # 设置占空比为50%（范围为0-1023）

# 启用PWM输出
pwm.enable()

# 延时一段时间
# 你可以执行其他操作或改变PWM参数

# 禁用PWM输出
pwm.disable()