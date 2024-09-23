# 16defreturn.py

def book() :
    title = '몽블랑'
    return title 

def pay():
    m = 7800
    return m

# 일반함수 리턴값x 매개인자x 일반함수를 출력하면 에러
def blue():
    color = 'dark'
    return color

def main():
    print("main 함수")
    print("책 제목 :", book())
    print("책 가격 :", pay())
    print(f'블루 : {blue()}')
main()  # 함수 다독기술해서 호출

