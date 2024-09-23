# 02deftuple.py

def my_hap(*args): # 같은 타입만 사용가능 함 int면 int
    print('*args타입', type(args)) 
    hap = 0 
    for num in args :
        hap = hap+num
    return hap

# data = my_hap(6,11,24,16,45,7,88,3.14)
# print('계산처리 합계 :', data)
# print('계산처리 합계 :', data_hap(6,11,24,16,45,7))

mylist = [6,11,24,16]   # 수정O, 쉽게 데이터추가 가능
mytuple = (5,10,23,15)  # 수정X, 쉽게 데이터추가 가능

mylist[1] = 54
print(mylist)

# mytuple[1] = 94   에러발생
print(mytuple)
