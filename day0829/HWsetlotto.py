# HWsetlotto.py


# 셋 항목 추가함수 lotto.add()
# lotto = list() 사용금지 X
# 난수 로또숫자발생, 중복발생, set추가
# 출력 오름차순적용 sort() -> list로 항 변환 후 해야함
import random

def mysetlotto():
    lotto = set()
    while len(lotto) < 6 :
        lotto.add(random.randint(1,45))
    print(sorted(lotto), end = '')

mysetlotto()


