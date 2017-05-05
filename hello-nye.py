''' 
This is a little ditty that says hello, 
and wishes you Happy New Year on the appropriate day.
'''

import time

today = time.strftime('%d/%m')

if today == '31/12':
    print('Hello world, Happy New Year!')
else:
    print('Hello world!')