# 07testcopy.py

import math
import random
import re
import os.path
import pickle
import time
import datetime
import copy

apple = 'LG TWINS'
my = apple
print(my)

print()

data = [11,22,33]
mydb = copy.deepcopy(data) # 복사본은 값이 수정안된상태로 출력
data[0] = 789
print('원본', data)
print('복사본', mydb)

print()