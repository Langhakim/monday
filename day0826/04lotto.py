# 04lotto.py

import random

# 로또 1~45사이 숫자이며 정수
# 반복문 for, while 사용
# 난수발생 6개 숫자 중복체크
# 난수발생 후 출력은 sort정렬

for k in range(6) :
    com = random.randint(1,45)
    print(com, end='\t')

print()