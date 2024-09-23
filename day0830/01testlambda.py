# 01testlambda.py
# 람다식은 import 기술 안함, 키워드 lambda기술, return 값이 있어야함


def mycal(su):
    cal = 2*su+5 # 생략하고 return 값에 직접 작성가능
    return cal
    # return 2*su+5

print()

print('일반식', mycal(10))
my1 = lambda su : 2*su+5
print('람다식 예제1', my1(10))
print('람다식 예제2', (lambda su : 2*su+5)(10))
print()

def myAdd(x,y):
    return x+y

print('일반식', myAdd(6,5))
my2 = lambda x,y : x+y
print('람다식 예제 1', my2(6,5))
print('람다식 예제 2', (lambda x,y : x+y)(6,5))
print()

# 함수에서 계산처리후 if~else제어문 리턴값
def myCheck(su):
    # if~else 짝수/홀수
    msg = '안'
    if su % 2 == 0 :
        return f'{su} {msg='짝수입니다'}'
    else :
        print(su, msg = '홀수입니다')

print('일반식', myCheck(20))
print('람다식', lambda su : '짝수' if su%2==0 else '홀수' (20))
print()