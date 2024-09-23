# 01testif.py

'''
if 조건 :
    만족 문장기술
else
    불만족 문장기술
'''

# 선언 = declare
kor, eng, hap = 0,0,0 # 변수초기화
avg = 0.0
message = '안내문'

kor = 10
eng = 85
hap = kor + eng
avg = hap/2

# 처리 연산, if, 반복

# 문제해결1] 평균이 70점부터 축합격, 0~69 재시험
if avg >= 70 :
    message = '축합격'
else :
    message = '재시험'

# 출력
print('국어 : ', kor)
print('영어 : ', eng)
print('합계 : ', hap)
print('평균 : ', avg)
print('결과 : ', message)
print('😊 ' *10)
print()