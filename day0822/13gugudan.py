# 13gugudan.py

data = input('구구단 숫자 입력 >>> ')
dan = int(data)
for k in range(1,10,1) :
    print(dan, '*', k, '=', (dan*k))

print()
print('구구단 연습')

'''
파이썬 화면모니터 출력 print('안내문', 값)
파이썬 키보드자판 입력 input('안내문', 값)
파이썬 키보드입력데이터 문자로 인식
int("78")
'''

# a = "1200"
# b = "15"
# print(a+b) # 숫자를 문자열로 인식시키면은 연결된 결과값 출력

# c = int(a) + int(b)
# print(int(a)+int(b))
# print(c)

#파이썬 내장함수
#int(), print(), round(), input(), str(), sum()

print()