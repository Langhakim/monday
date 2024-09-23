# 01string.py

x = 'blue'
y = 1234
print(x + str(y))
print(f'{x}{y}')
print(x,y)

msg = '김김김kb123asdfasdfasdfasdfsdfdfdfdfdfdfdfdf'
print('길이 :', len(msg))
print('갯수 :', msg.count('f')) # msg안에있는 'f'글자의 갯수를 확인할때 사용
print('kb단어추출 :', msg[3:5]) # kb글자단어를 추출 [시:끝+1]

print()