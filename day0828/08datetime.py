# 08jumin.py

import datetime
import time

x = datetime.datetime.now()
y = str(x)
# z =

print(x)
print(str(x))
print(str(x)[0:4])
print(y[0:4])

dt = datetime.datetime.now()
print(dt.strftime('현재날짜 %y년-%m월-%d일'))
print(dt.strftime('현재시간 %H시-%M분-%S초'))

mytime = time.localtime()
print(mytime)
print(mytime.tm_year)

