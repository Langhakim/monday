# 09datetime.py

import time
import datetime

# jumin = '931224 - 1234567'
# ju1 = '931224'  # len() 6자릿수 체크
# ju2 = '1234567' # len() 7자릿수 체크

jumin = str(input('주민번호를 입력하세요("-" 포함, 공백제외) >> '))
# 931224-1234567

gen = jumin[7:8]
print(gen)
birthm = jumin[2:4]
birthd = jumin[4:6]
age = 2024-int(jumin[0:2])-1900

# 문제1] 성별체크 1/3 남자 2/4여자
if jumin in gen :
    if gen > '4' or len(jumin) != 14 :
        print('주민번호를 제대로 입력해주세요\n')
    elif gen == '1' or gen == '3' :
        print('남성입니다')
    else :
        print('여성입니다')

# 문제2] 생일추출 
print(f'생일 : {birthm}월 {birthd}일')

# 문제3] 나이계산
print('나이 :', age)

# 문제4] 


# mytime = time.localtime()
# print(mytime)
# print(mytime.tm_year)
# print(mytime.tm_year-1993)