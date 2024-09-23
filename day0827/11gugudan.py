# 11gugudan.py

# 파이썬 함수에 들어갈 요소 def() : 함수매개인자, 함수리턴값
# 함수는 호출을해서 사용해야함

# 내장함수
# list(), len(), tuple(), set(), str(), int(), round(), print(), input()

import time

def book() : 
    pass

def main() :
    pass

def gugudan(dan) :
    for k in range(1,10,1) :
        print(f'{dan} * {k} = {dan*k}')

gugudan(3)  # 원하는 구구단의 숫자를 넣으면 함수에서 계산되어 출력됨
print('구구단 연습', time.time,'\n')

def mysum(a,b) :
    print(a,b, '합계 =', a+b)

mysum(7,5)