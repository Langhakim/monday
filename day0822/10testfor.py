# 10testfor.py

for k in range(1, 1001, 1) :
    print(k, end='\t')  # print 함수 자동 라인개행포함 
    # 5개씩 6줄 출력 if조건
    if k%5 == 0 :
        print()

    # 문제1 40까지만 출력
    if k == 40 :
        break

print()