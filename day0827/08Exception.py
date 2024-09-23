# 08Exception.py
# try : ~~ / except : ~~

x, y = 0, 0
hap, gob, mok, nmg = 0,0,0,0

# 처리 연산처리, if제어처리, 반복처리
try :   
    x = int(input('x 정수입력(0숫자제외) >>> '))
    y = int(input('y 정수입력(0숫자제외) >>> '))

    hap = x + y; gob = x * y 
    mok = x / y; nmg = x % y
    
    print(f'{x} + {y} = {hap}')
    print(f'{x} * {y} = {gob}')
    print(f'{x} / {y} = {mok}')
    print(f'{x} % {y} = {nmg}')

    print()
    print('쇼핑목록')
    print('주차처리')
    print('정산성공')

except Exception as ex :    # 에러가 발생하면은 처리되는 영역
    print('에러발생이유', ex)
    print('주의! 연산처리가 잘 못 되었습니다')