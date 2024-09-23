# homeworklottoset.py

import random

# 로또 1~45사이 숫자이며 정수
# set 사용으로 추출된 숫자 중복안되게 체크
# 오름차순 적용

lotto = set()

for lotto in range(6) :
    # lotto = list()
    lotto = random.randint(1,45)
    # lotto.sort()
    print(lotto, end = ' ')


# for k in range(6) :
#     com = random.randint(1,45)
#     print(com, end='\t')

print()