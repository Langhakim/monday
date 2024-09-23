# homeworkmilk.py 

apart = [
    [101,102,103,104],
    [201,202,203,204],
    [301,302,303,304],
    [401,402,403,404]
]

inpaid = [101, 204, 302, 403]   # 비용지불 안한 세대 리스트

find = int(input('배달가능현황 >>> '))

for floor in apart :
    if find in inpaid :
        print(f'{find}호 요금미납으로 배달불가')
    else :
        print(f'{find}호 배달가능')
    break
        

print()