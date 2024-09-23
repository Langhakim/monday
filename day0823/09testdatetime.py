# 09testdatetime.py

import time

my = time.localtime()
print(my.tm_year,'년')
print(my.tm_mon,'월')
print(my.tm_mday,'일')
wday = my.tm_wday # 0~6 월요일~일요일 / 나라마다 시작하는 요일이 다를 수 있음

week = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
print(week[wday])

if wday == 0 :
    print('월요일')
elif wday == 1 :
    print('화요일')
elif wday == 2 :
    print('수요일')
elif wday == 3 :
    print('목요일')
elif wday == 4 :
    print('금요일')
elif wday == 5 :
    print('토요일')
else :
    print('일요일')


print()


