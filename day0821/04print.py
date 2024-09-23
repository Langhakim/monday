# 04testprint.py



a, b, ret = 7, 4, 0
msg = 1234

ret = a*b
print('|{}| * |{}| = |{}|' .format(a,b,ret))
print('|{}|' .format(msg))
print('|{:0>10,}|' .format(msg))    # > 오른쪽맞춤 관계연산자 아님
print('|{:*>10,}|' .format(msg))
print('|{:,}|' .format(msg))

'''
print(ret)  # 7*4=28

# print(변수, '문자', ~~)
print(a,'*',b,'=',ret)  

# print( %d정수, %s문자열, %f실수, %c문자 )
print('%d * %d = %d' %(a,b,ret))

# print( f'{변수값}' )
print(f'{a} * {b} = {ret}')
'''

print()