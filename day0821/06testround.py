# 06testround.py

# 변수 하나씩선언하거나 다중선언 가능함

# 변수 다중선언
a, b, ret = 7, 4, 0
mok = 34.5678
print(mok)
print('%d' %(mok)) # 실수이지만 정수 34출력
print('%f' %(mok)) # %f는 자릿수 지정안하면 6자릿수까지 출력
print('%.2f' %(mok))
print(round(mok,2))

# 내장함수
# print(), int(), type(), input('안내문'), str(), sum(), round(데이터, 실수자리수)

# %자릿수d정수 %자릿수f실수
# print( %d정수, %s문자열, %f실수, %c문자 )
# print('%d * %d = %d' %(a,b,ret))



# ret = a*b

# print(ret)  # 7*4=28

# # print(변수, '문자', ~~)
# print(a,'*',b,'=',ret)  

# # print( %d정수, %s문자열, %f실수, %c문자 )
# print('%d * %d = %d' %(a,b,ret))

# # print( '{} * {} = {}' .format(a,b,ret) )
# print('{} * {} = {}' .format(a,b,ret))

# # print( f'{변수값}' )
# print(f'{a} * {b} = {ret}')

# print()