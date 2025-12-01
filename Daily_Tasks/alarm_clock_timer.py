# Timer
# Description: Let the user set a time; the program waits until that time and then shows a message or sound alert.
import time

def countdown(seconds):
    while seconds:
        mins,secs=divmod(seconds,60)
        print(f"\rTime left:{mins}:{secs}",end="")#\r is used for overwriting previous print
        time.sleep(1)
        seconds-=1
    print("\nTime is up")

countdown(4)