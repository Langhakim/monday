# 07except.py
# 문제1] dan입력 키보드 input(), 형변환
# 문제2] dan입력범위 정수이며 1이상 2~9사이 숫자만 입력
# 문제3] 예외처리 try : ~ / except :
 
import time

dan = 0

try :
    dan = int(input('단을 입력하세요 >>> '))
    if dan > 9 or 1 > dan:
        print('\n2~9사이 숫자만 입력해주세요\n')    
    else :
        for k in range(1,10,1) :
            print(f'{dan} * {k} = {dan*k}')      
except :
        print('\n정수만 입력해주세요\n')

