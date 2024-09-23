# 03testprint.py

# 변수 하나씩선언하거나 다중선언 가능함

# a = 7
# b = 4
# ret = 0 

a, b, ret = 7, 4, 0

ret = a*b
print(ret)  # 7*4=28

# print(변수, '문자', ~~)
print(a,'*',b,'=',ret)  

# print( %d정수, %s문자열, %f실수, %c문자 )
print('%d * %d = %d' %(a,b,ret))

# print( '{} * {} = {}' .format(a,b,ret) )
print('{} * {} = {}' .format(a,b,ret))

# print( f'{변수값}' )
print(f'{a} * {b} = {ret}')

print()