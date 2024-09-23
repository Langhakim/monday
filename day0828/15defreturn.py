# 15defreturn.py

'''
함수에서 처리 후 외부에 값을 줄때 return 값
사용자정의 함수 매개인자 + 리턴값
'''

def book() :
    title = '몽블랑'
    return title 

def pay():
    m = 7800
    return m

def main():
    print("main 함수")
    data = book()
    value = pay()
    print("책 제목 :", data)
    print("책 가격 :", value)
    print("책 제목 :", book())
    print("책 가격 :", pay())
main()

# if __name__ == '__main__': # 생략가능
#     main()