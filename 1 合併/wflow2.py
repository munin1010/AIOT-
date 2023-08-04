from machine import Pin
import time

def measure_flow_rate(x):
    flow_frequency = 0
    lastcallTime = 0

    def callback(pin):
        nonlocal flow_frequency
        flow_frequency += 1

    pin = Pin(x, Pin.IN, Pin.PULL_UP)
    pin.irq(trigger=Pin.IRQ_RISING, handler=callback)

    # 執行一次流量測量
    while True:
        if ((time.ticks_ms() - lastcallTime) > 1000):  # if time interval is more than 1 second
            flow_rate = (flow_frequency * 60 / 7.5)  # flowrate in L/hour= (Pulse frequency x 60 min) / 7.5
            flow_frequency = 0  # Reset Counter
            lastcallTime = time.ticks_ms()
            print("Flow Rate = {} Litres/Hour".format(flow_rate))
            

# 在主程式中呼叫 measure_flow_rate 函數，進行一次流量測量（這裡假設霍爾感測器接腳為 21）
measure_flow_rate(28)