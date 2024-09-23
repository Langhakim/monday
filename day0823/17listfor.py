# 17listfor.py
print()

mylist = ['kim', 7] 
print(mylist)

mylist.append('LG TWINS')
print(mylist)

mylist.append('9')
print(mylist)

mylist.insert(1,'엘지트윈스')
print(mylist)
# 최종결과 ['kim', '엘지트윈스', 7, 'LG TWINS', '9']

mylist[0] = '야구'  # mylist의 0번째 값을 '야구'로 변경
print(mylist)
# 최종결과 ['야구', '엘지트윈스', 7, 'LG TWINS', '9']

print('- ' *30)

# 삭제 : 예시)엘지트윈스 삭제하기 remove(값을 정확하게 알때 삭제가능), pop(위치만 알아도 삭제가능)
# mylist.remove('엘지트윈스')
# mylist.pop(1)
del mylist[1] #del 함수 사용도 가능
print(mylist)

# mylist.sort()   # sort적용은 같은 타입만 가능하여 에러남


print()