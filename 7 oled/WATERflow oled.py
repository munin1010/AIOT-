if ((time.ticks_ms()-lastcallTime) > 1000):  #if time interval is more a than 1 second
        flow_rate = (flow_frequency * 60 / 7.5)  #flowrate in L/hour= (Pulse frequency x 60 min) / 7.5 
        flow_frequency = 0                       # Reset Counter
        lastcallTime=time.ticks_ms()
        x=("Flow Rate={} Litres/Hour".format(flow_rate))
disp = str(x)
    oled.text(disp,10,12)
    oled.show()
    time.sleep(0.5)
    oled.fill(0)
oled.show()