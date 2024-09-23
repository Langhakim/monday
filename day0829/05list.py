# 05list.py
import time

print()

lotto = [45,2,7,9,41,28]

for k in range(1,11,1):
    su = pow(k,2)
    print(su, end = ' ')

print()
print()
time.sleep(0.3)

for k in range(1,11,1):
    su = pow(k,2)
    print(su, end = ' ')

print()
print()

mylist = [ a**2 for a in range(1,7,1) ]
print(mylist)
print()

mytuple = ( b**2 for b in range(1,11,1) )
print(mytuple)  # 리스트 comprehension 적용은 튜플은 제외
print()

myset = { c**2 for c in range(1,7,1) }
print(myset)
print()