# 03while.py

print('* ' *30)

su = 0 # 변수선언하고 + 값초기화 0

while True :
    su = su + 1
    if su == 5 :
        continue
    print(su, end='  ')    
    if su == 10 :
        break


print()
print()
print('* ' *30)