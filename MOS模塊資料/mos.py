# 导入必要的模块
import mos_module

# 初始化MOS模块
mos = mos_module.MOS()

# 连接到网络
mos.connect_wifi("your_ssid", "your_password")

# 发送数据
data = "Hello, MOS!"
mos.send_data(data)

# 接收数据
received_data = mos.receive_data()
print(received_data)

# 断开网络连接
mos.disconnect_wifi()