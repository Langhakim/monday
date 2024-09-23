# 05find.py

msg = 'skENKdfEKDI'
pos = msg.find('sk') # 대소문자 구분함
if pos == -1 :
    print('값이 없습니다.')
else :
    print(f'{pos}의 값이 존재합니다')
