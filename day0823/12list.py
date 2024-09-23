# 12list.py

import time

lista = [2, 1, 9, 5, 3, 7, 6]
print(lista)

time.sleep(1)
# 문제1] lista에서 9 5 3 데이터추출하기
print(lista[2:4])   # , 말고 : 콜론 사용해야함

time.sleep(1)
print(lista[-1]) # 리스트 맨 뒤에서부터 1번째값 추출해줘
print(lista[6]) # 리스트 맨 앞에서부터 7번째값 추출해줘

time.sleep(1)
print(lista[3:])

print()