# 14def.py


def book() :
    title = '몽블랑'
    return title    # 리턴하면 book함수가 title을 기억함

def price() :
    pay = 7800
    return pay

def main() :
    value1 = book()
    value2 = book()
    print('시작함수')
    print('main함수')
    print('book함수 title', book())
    print('price함수 pay', price())

    print('book함수 title', value1)
    print('price함수 pay', value2)


main()