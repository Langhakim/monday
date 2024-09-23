# homeworklotto.py

import random

# 로또 1~45사이 숫자이며 정수
# 반복문 for, while, if 사용
# 난수발생 6개 숫자 중복체크
# 난수발생 후 출력은 sort정렬
# set 사용금지

lotto = []
while len(lotto) != 6 :
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)) :
        if lotto.count((lotto[k]) > 1) :  # 랜덤으로 추출된 숫자횟수가 1보다 크냐
            lotto.pop()
            lotto.append(random.randint(1,45))

print(lotto)
lotto.sort()
print(lotto)

# for k in range(6) :
#     com = random.randint(1,45)
#     print(com, end='\t')

print()