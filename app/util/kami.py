# from datetime import datetime,timedelta
import time
# import datetime,time


def kami_tool(ActivationTime,codeInvalidTime):
    current_time = int(time.time())
    iatime = int(codeInvalidTime) - int(ActivationTime)
    catime = current_time - int(ActivationTime)
    if iatime >= catime:
        return codeInvalidTime
    else:
        return False
   

def kami_tool_time(state):
    codeActivationTime = int(time.time())
    codeInvalidTime = int(time.time()) + int(state)
    return codeActivationTime,codeInvalidTime