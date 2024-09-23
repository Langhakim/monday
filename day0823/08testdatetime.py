# 08testdatetime.py

import time
import datetime   # datetime.datetime.now() 구현가능
# from datetime import datetime   # datetime.now() 구현가능

my = time.localtime()
print(my)
print(my.tm_year,'년')
print(my.tm_mon,'월')
print(my.tm_mday,'일')
print(my.tm_wday) # 0~6 월요일~일요일 / 나라마다 시작하는 요일이 다를 수 있음
print()

dt = datetime.datetime.now()  # 현재 연월일 시분초 출력
print(dt)
print()

time.sleep(0.3)
print('aaaaa')
time.sleep(0.3)
print('bbbbb')
time.sleep(0.3)
print('ccccc')
