# 09tuple.py

t = (99, 96, 10, 20, 30, 20, 20, 5, 6, 88, 93, 10, 50, 67)
print(t)

print('10의 갯수 : ', t.count(10))
print('10의 색인 : ', t.index(10))  # 중복된 값일 경우 가장 첫번째 인덱스 값 출력
print()

print('30의 갯수 : ', t.count(30))
print('30의 색인 : ', t.index(30))
print()

mylist = list(t)    # 튜플에서 리스트로 형변환 / 튜플은 ()괄호 출력, 리스트는 []괄호 출력
print(mylist)
mylist.append(7)
mylist.insert(2, 60)
mylist.remove(20)
print(mylist)
print()
print(tuple(mylist))    # 리스트에서 수정 후 다시 수정불가한 튜플로 변환

# 튜플에서는 아래 함수들 지원X 에러남
# t.append(7)
# t.insert(2, 60)
# t.remove(20)