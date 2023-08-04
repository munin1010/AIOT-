from machine import Pin
import time

def flow(x):
    flow_frequency = 0
    lastcallTime = 0

    pin = Pin(x, Pin.IN, Pin.PULL_UP)

    def callback(pin):
        nonlocal flow_frequency
        flow_frequency += 1

    pin.irq(trigger=Pin.IRQ_RISING, handler=callback)

    while True:
        if ((time.ticks_ms() - lastcallTime) > 1000):  # if time interval is more than 1 second
            flow_rate = (flow_frequency * 60 / 7.5)  # flowrate in L/hour= (Pulse frequency x 60 min) / 7.5
            flow_frequency = 0  # Reset Counter
            lastcallTime = time.ticks_ms()
            print("Flow Rate = {} Litres/Hour".format(flow_rate))
flow(28)