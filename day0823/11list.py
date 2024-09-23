# 11list.py

import time

lista = [20, 10, 40, 50, 30]
print(lista)

time.sleep(1)
lista.insert(2,9)  # 2번째 위치에 9를 추가
print(lista)

time.sleep(1)
lista.append(7) # 맨 뒤에 7을 추가
print(lista)

time.sleep(1)
# lista.remove(8) # 리스트에 없는 숫자를 삭제하면 에러발생
lista.pop(3) # 리스트에 4번째있는 값 삭제(0부터 시작)
print(lista)

time.sleep(1)
lista.reverse()
print(lista)

# lista.sort()  # 오름차순
# lista.sort(reverse=True) # 내림차순
# print(lista)

print()