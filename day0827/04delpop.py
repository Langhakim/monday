# 04delpop.py
import time

# remove, del, pop, clear 제거 삭제기능
# remove(데이터값)
# del data[위치]  대상 지정삭제 불가
# pop(위치) : 지정한 위치 값 삭제
# pop() : 맨 뒤의 데이터값 삭제
# clear 전부삭제

data = [7,8,9,10,3,5,2,4,1]
data.remove(9)
data.pop()
print(data)
print()

del data[2]
print(data)
print()

del data[1:4]   # 범위지정삭제 [시작:끝] 슬라이싱라고 표현함
print(data)
print()

time.sleep(0.5)
data = [7,8,9,10,3,5,2,4,1] # 문제] 모든데이터 전부삭제
# data.clear()
# del data[:] 전체삭제지만 비권장
del data[0:-1]
print(data)
