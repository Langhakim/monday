# 09testfor.py

# 문자열,list,tuple,set,dict
# 반복데이터 사용할때 많이 사용함

'''
for 변수대표 k 포함되어있으면 range(5) : 
    5회 처리한다 0~4까지 0부터 시작해서 5번처리함

for 변수대표 k 포함되어있으면 range(1,5) : 
    4회 처리한다 1~4까지 1부터 시작해서 4번처리함

for 변수대표 k 포함되어있으면 range(1,5,1) : 
    4회 처리한다 1~4까지
    1씩 증가일때 3번째 1생략

while 조건 :
    조건만족시 루프loop 처리
    무한루프처리일때 if제어문으로 break탈출
'''

a,b=0,0
hap,tot=0,0

# 첫번째 a, hap 1~5 출력 누적
'''
1 1
2 3
3 6
4 10
5 15
'''
a = a+1; hap=hap+a; print(a, hap)
a = a+1; hap=hap+a; print(a, hap)
print(' -' *30)

#변수 재사용할때 초기화
#for반복문, 대입연산
a, hap = 0,0  # 재선언보다는 초기화
for k in range(5) :
    a = a + 1
    hap = hap + a
    print(a, hap)


print()

