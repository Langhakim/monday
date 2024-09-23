# 02testif.py

'''
if 조건 :
    조건1 만족 문장기술
elif 조건2 : 
    조건2 만족 문장기술
elif 조건3 :
    조건3 만족 문장기술
else
    불만족 문장기술

    100~90 A
    89~80 B
    79~70 C
    69~60 E
    59~50 F
'''

# 선언 = declare
kor, eng, hap = 0,0,0 # 변수초기화
avg = 0.0
message = '안내문'
grade = 'F'

kor = 10
eng = 85
hap = kor + eng
avg = hap/2

# 처리 연산, if, 반복

# 문제해결1] 평균이 70점부터 축합격, 0~69 재시험
if avg >= 90 :
    grade = 'A'
elif avg >= 80 :
    grade = 'B'
elif avg >= 70 :
    grade = 'C'
elif avg >= 60 :
    grade = 'E'
elif avg >= 50 :
    grade = 'F'
else :
    message = '재시험'

# 출력
print('02testif.py 문서')
print('국어 : ', kor)
print('영어 : ', eng)
print('합계 : ', hap)
print('평균 : ', avg)
print('학점 : ', grade)
print('결과 : ', message)
print('😊 ' *20)
print()