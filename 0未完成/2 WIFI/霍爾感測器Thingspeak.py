while True:
    if ((time.ticks_ms()-lastcallTime) > 1000):  #if time interval is more a than 1 second
        flow_rate = (flow_frequency * 60 / 7.5)  #flowrate in L/hour= (Pulse frequency x 60 min) / 7.5 
        flow_frequency = 0                       # Reset Counter
        lastcallTime=time.ticks_ms()
        x=("Flow Rate={} Litres/Hour".format(flow_rate))   #print(flow_rate)
        y=str(flow_rate)
        print(y)
    sendCMD_waitResp('TP1+'+y)
    utime.sleep(0.1)
    sendCMD_waitResp('TX_EN')
    utime.sleep(0.1)
    utime.sleep(5)