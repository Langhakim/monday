# 04upper.py

msg = 'skENKdfEKDI'
print(msg.upper())
print(msg.lower())

print()

msg = 'skENKdfEKDI'
pos = msg.find('e') # 대소문자 구분함
if pos == -1 :
    print('값이 없습니다.')
else :
    print(pos)
print('k =', msg.find('k'))  # k의 위치
print('z =', msg.find('z'))  # 없는 값을 입력하면 -1으로 출력
