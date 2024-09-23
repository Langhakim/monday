# 07rjust.py

print()

for x in range(1,6,1):
    print(f'{x} * {x} = {x*x}')

print()

for x in range(1,6,1):
    print(x,'*',x,'=',str(x*x).rjust(5))    # 문자열을 입력한 숫자만큼 공백 후 오른쪽으로 정렬
    print(x,'*',x,'=',str(x*x).zfill(5))