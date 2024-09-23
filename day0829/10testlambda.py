# 10testlambda.py


# 람다 = 익명의 함수 = 함수이름이 없음
# 람다식은 import 없음
# 람다식은 lambda 키워드기술

def mysu(num):
    ret = 3*num+5
    return ret

data = int(input('숫자입력 >> '))

print('일반식', mysu(data))
print('람다식', (lambda num:3*num+5)(data))
print()