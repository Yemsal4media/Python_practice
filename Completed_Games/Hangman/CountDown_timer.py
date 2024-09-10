# Count Down timer
import time

def Countdown(t):
    while t:
        mins , secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print (timer, end="\r")
        time.sleep(1)
        t -= 1
    print("TIME UP")

t = 29
Countdown(int(t))