# 11gugudan.py

# 파이썬 함수에 들어갈 요소 def() : 함수매개인자, 함수리턴값
# 함수는 호출을해서 사용해야함

# 내장함수
# list(), len(), tuple(), set(), str(), int(), round(), print(), input()

import time

mydata = 0
# name = '이름'

def gugudan(name, dan) :
    print('저자 :', name)
    for k in range(1,10,1) :
        print(f'{dan} * {k} = {dan*k}')



try :
    mydata = int(input('단을 입력하세요 >> '))
except :
    print('정수 숫자를 입력하세요(1~9사이의 숫자를 입력하세요)')

gugudan('랑하', mydata)
