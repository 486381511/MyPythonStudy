import time
import datetime

now_time = datetime.datetime.now()
date_up = datetime.timedelta(seconds=10)
my_time = now_time+date_up

while datetime.datetime.now() < my_time:
        #一秒一次的变量             常量
    time.sleep(1)


print('10秒之后')


