import time
from datetime import datetime

def printer(i):
    if (i < 10):
        print ('0' + str(i), end = '')
    else:
        print (i, end = '')

while(True):
    now = datetime.now()
    print('► ' + str(now.hour) + ':', end = '')
    printer(now.minute)
    print(':', end = '')
    printer(now.second)
    print(' ◄', end = '\r')
    time.sleep(1)