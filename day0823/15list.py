# 15list.py

import time

# list() 함수에 중복된 데이터를 넣어도 상관없음
mylist = ['kim', 78, 3.1415, True, 'F', "lang", 78] 
print(mylist)
print()
time.sleep(1)

# tuple함수는 수정불가
mytuple = ('blue', 21, 'A')
print(mytuple)
print()
time.sleep(1)

# set함수는 반복x, 순서x
myset = {23, 'kim', 78, 23, 'kim', 78, 'kim'}  
print(myset)
print()
time.sleep(1)

# dict함수 : key:value
mydict = { 100:'naver', 200:'kakao'}
print(mydict[200])
print()
time.sleep(1)