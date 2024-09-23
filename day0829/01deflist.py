# 01deflist.py

def data_hap(x,y,z,a,b,c):
    hap = x+y+z+a+b+c
    return hap

def my_hap(*args): # *을 적으면 첫번째 데이터값부터 끝까지 긁어옴
    print('*args타입', type(args)) # args타입 = 'tuple'
    hap = 0 # 생략하면 에러발생
    for num in args :
        hap = hap+num
    return hap

data = my_hap(6,11,24,16,45,7,88,3.14)
print('계산처리 합계 :', data)
print('계산처리 합계 :', data_hap(6,11,24,16,45,7))

print()

total = data_hap(6,11,24,16,45,7)
print('계산처리 합계 :', total)
print('계산처리 합계 :', data_hap(6,11,24,16,45,7))


'''
print()
def data_hap(x,y,z) :
    # 숫자 합계구해서 리턴처리
    print('x id', id(x))    # id는 주소값을 리턴해줌 데이터를 기억하는 번지
    print('y id', id(y))
    print('z id', id(z))
    print('x타입', type(x))
    print('y타입', type(y))
    print('z타입', type(z))

data_hap(6,9,56)

print('01deflist.py 문서 10 : 02')
print()
'''