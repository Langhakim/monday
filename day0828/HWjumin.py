# HWjumin.py.py

import datetime  #from  import 
import time

# dt = datetime.datetime.now()
# year = dt.strftime('%y')
# print(year)
# mytime = time.localtime()
# print(mytime.tm_year)
print()
jumin = str(input('주민번호를 입력하세요("-"포함) >> '))
# 931224-1234567

# split()사용 [시:끝+1]
# 문제1 if제어 성별체크   1/3 남자  2/4여자 
def gender():
    if jumin[7:8] == '1' or jumin[7:8] == '3' :
        return '남성입니다'
    elif jumin[7:8] == '2' or jumin[7:8] == '4' :
        return '여성입니다'
    else :
        return '주민번호를 잘 못 입력하였습니다'

# 문제2 생일 12월30일 생일 축하합니다 931224-1234567
def birth():
    bmonth = int(jumin[2:4])
    bday = int(jumin[4:6])

    if bmonth > 12 or bday > 31 :
        return '입력한 주민번호 생년월일이 잘 못 입력되었습니다.'
    else :
        return f'{bmonth}월 {bday}일'

# 문제3 나이계산 2024-1997 = 27
def age():
    mytime = time.localtime()
    year = mytime.tm_year
    yjumin = int(jumin[0:2])
    nai = year - yjumin - 1900
    return f'{nai}살'

def lencheck(): 
    if len(jumin) != 14 or jumin[6] != '-' :
        return '주민번호를 잘 못 입력했습니다.\n "-"포함해서 다시 입력해주세요.'

def info():
    check = lencheck()
    if check :
        print(f'{check}')
    else: 
        print(f'{lencheck}')
        print(f'성별 : {gender()}')
        print(f'생일 : {birth()}')
        print(f'나이 : {age()}')
    
info()

print()

jum1 = '971230'  #len() 6자릿수 체크
jum2 = '18350642' #len() 7자릿수 체크
# len1 = jum1.len() len(jum1) 수정해서 자릿수체크
# len2 = jum2.len() len(jum2) 수정해서 자릿수체크


'''
문자열을 주석처럼 사용 
dt = datetime.datetime.now() #정답
print(str(dt)[0:4])  #2024-2001 = 나이계산
mytime = time.localtime()
print(mytime.tm_year) #2024-2001 =  나이계산
'''
