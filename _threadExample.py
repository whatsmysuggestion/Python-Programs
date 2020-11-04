import _thread
import time

def printing(tName, delay, counter):
    while counter:
         time.sleep(delay)
         print ("Thread name is %s: Time Is %s" %(tName, time.ctime(time.time())))
         counter =counter - 1
try:
    _thread.start_new_thread(printing("One",10,3))
    _thread.start_new_thread(printing("Two",10,3))
except Exception:
    print(Exception)

