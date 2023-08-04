import wflow
import air
import _thread
# 使用T.py中的flow函數，傳遞參數21

def core0_thread(): #獨立進行掃描  不會影響 另一核 所以不會影響整體時間
    wflow.flow(28)


    

_thread.start_new_thread(core0_thread,()) #啟動第二核心

while 1:
    air.pre(26)