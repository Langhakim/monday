# 08set.py

# set{} 괄호사용, 출력하면은 마구잡이순서 중복된값은 하나만 출력함(순서X, 중복X)

set = {999, '홍대', 126.5454, 37.5446, '홍대', 297.2145, '홍대'}
print(set)

set.add('엘지')
set.add('트윈스')
set.add('엘지')
set.add('엘지')
print(set)