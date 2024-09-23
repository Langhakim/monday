# homeworksu.py

'''
mylist = [5, 9, 4, 2]
print(mylist)
mylist.reverse()
print(mylist)
'''

# list[] 사용금지
# while 반복문 사용해서 su변수의 숫자가 거꾸로 출력하기
# print(), if

print()

su = 5942
print(su)

while True :
    print(su % 10, end='')
    su //= 10
    if su == 0 :
        break

print()