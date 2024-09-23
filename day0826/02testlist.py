# 01testlist.py

data = [ # 3행*4열
    [1, 2, 3, 4, 5, 7],
    [5,6,7,8],
    [9, 10, 11, 12],
    [11,22,33,44]
    ]    # 리스트안에 리스트 넣기 가능
print()

for k in range(len(data)) : # 행 갯수
    for b in range(len(data[k])) : # 열 갯수
        print(data[k][b], end = '\t')
    print()


#  문제 1] 아래와 같이 출력되게 코드입력
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12

# for a in range(0,3,1) : # 3행 
#     for b in range(0,4,1) : # 4열
#         print(data[a][b], end = '\t')
#     print()

print()
print()