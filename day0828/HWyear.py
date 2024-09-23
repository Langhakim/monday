# HWyear.py

day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

year = int(input('year >> '))
month = int(input('month >> '))
# date = int(input('date >> '))

# if제어문 or/and 중첩 if
if year == 0 :
    print('\n연도를 제대로 입력해주세요')
if month == 0 or month > 12 :
    print('\n월을 제대로 입력해주세요')
if year%4 == 0 :
    print('\n윤달이 있는 해 입니다.')
else :
    print('\n윤달이 없는 해 입니다.')

print()
'''
    윤년기준
    1. 4의배수
    2. 100의 배수가 아닌 4의 배수
    3. 400의 배수

    문제] 2024년 2월을 입력하면 윤년입니다 출력

    참고 2024년 2월 29일 / 2020년 2월 29일
        2021년 2022년 2023년 : 28일
'''