# 04display.py

import time

# from 문서이름 import 전역변수, 함수이름만
from game import user_id, user_pwd
from game import terran, LG, camp

print(user_id)
print(user_pwd)

time.sleep(0.3)
terran()

time.sleep(0.3)
LG('야구')

time.sleep(0.3)
fire = camp()
print(f'불멍횟수는 {fire}')
print('불멍횟수는', camp())

print()