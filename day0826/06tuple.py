# 06tuple.py

pos = ('홍대', 126.5454, 37.5446, '홍대', 297.2145)
print(pos)
print()

# 튜플 for반복문으로 출력
for k in range(len(pos)) :
    print(pos[k], end = '  ')

print()
print()
print('* ' *30)
print()

for i, v in enumerate(pos) :    # enumerate
    print(i+1, ':', v)    # 인덱스값 : 벨류값 출력 / 인덱스값에 +1을 붙여주면 1부터 출력됨