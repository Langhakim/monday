# 04gugudanfor.py

import time  # 지연사용할때 편함

dan = int(input('원하는 단 입력 >>> '))  # input만 적으면 문자형으로 인식하여 int로 형변환을 해줘야함

for k in range(1,10,1) :
    # print(dan,' * ',k,' = ',dan*k)
    print(f'{dan}*{k}={dan*k}')
    time.sleep(0.3) # 입력한 숫자의 초단위로 출력됨

print()
print('엘지트윈스')
print('샌디에이고')