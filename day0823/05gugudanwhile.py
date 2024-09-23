# 05gugudanwhile.py

import time  

dan = int(input('원하는 단 입력 >>> '))  
k = 0

while True :
    k = k + 1
    gob = dan*k
    print(dan,' * ',k,' = ',gob)
    if k == 9 : break 
    time.sleep(0.3)

print()
print('엘지트윈스')
print('샌디에이고')