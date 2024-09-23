# 06except.py
# try : ~~ / except : ~~

x, y = 7, 0
hap, gob, mok, nmg = 0,0,0,0

# 처리 연산처리, if제어처리, 반복처리
try :   
    pass
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

except :    # 에러가 발생하면은 처리되는 영역
    print('주의! 연산처리가 잘 못 되었습니다')