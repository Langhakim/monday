# 14def.py

'''
파이썬에서 함수 정의 시작 키워드 def() 함수이름() :
'''

# 함수정의=구현=기술 함수=function=기능
def gugudan(name,dan) :
    print('작성자 :', name)
    for k in range(1,10,1) :
        print(f'{dan} * {k} = {dan*k}')

# 문제] myTotal 함수기술 총점,평균,출력
def myTotal(kor, eng) :
    print(f'총점 : {kor+eng}')
    print(f'평균 : {(kor+eng)//2}')

myTotal(60,70)

# if __name__ == '__main__': # 생략가능
#     gugudan('랑하', 6)
#     print()
#     kor = 90
#     eng = 85
#     myTotal = 0
#     myTotal(kor, eng)