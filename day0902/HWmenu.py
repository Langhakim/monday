# HWmenu.py

import time
import sys  #프로그램종료 sys.exit()
from datetime import datetime
# import datetime

menu = dict()
flag = True
num,su,sel = 0,0,0
msg,info,message = '안내메', '안내메', '안내메'
path = 'C:/Mtest/menu.txt'

dt = datetime.now()
print('처리날짜 :', dt)
print()

# 문제1] HWmenu.py문서를 class화
# 문제2] menuInsertnew할때 일반 text파일 저장

class EmpMenu :
    menu = dict()
    flag = True
    num,su,sel = 0,0,0
    msg,info,message = '안내메', '안내메', '안내메'

    def __init__(self) :
        pass

    def munuInsertnew(self):
        name = input('이름입력key>>>')
        price = input('가격입력value >>>')
        menu[name] = price
        print(name, '등록 성공했습니다')
        file = open(path, 'r', encoding = 'UTF-8')
        file.write(name+'['+price+']'+'\n')

def menuAllprint():
    for k,v in menu.items():
        print( k ,' ', v)
    print()

def menuUpdate():
    name = input('편집대상 키값 입력>>> ')
    if menu.get(name) == None:
        print('편집대상 딕트가 key 없습니다')
    else:
        price = input('변경가격 재입력value >>>')
        menu[name] = price #mysite[200키] = '새로운값'
        print(name, '가격수정편집 성공했습니다')

def menuDelete():
    name = input('삭제대상 키값 입력>>> ')
    if menu.get(name) == None:
        print('삭제대상 딕트가 key 없습니다')
    else:
        menu.pop(name)
        print(name, '데이터삭제 성공했습니다')
        time.sleep(0.3)
        for k,v in menu.items():
            print( k ,' ', v)

def menuFind():
    key = input('조회검색 key 입력>>> ')
    if menu.get(key) == None:
        print(key, '데이터가 없습니다')
    else:
        print(key, menu[key],'데이터 조회성공했습니다')

def menuFileOpen() :
    file = open(path, 'r', encoding = 'UTF-8')
    file.close()

    with open(path, 'r', encoding = 'UTF-8') as file :
        pass

def menuExit():
    print('딕트처리를 종료합니다\n')
    flag = False

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

while flag:
    num = int(input('1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료 >> '))
    if num == 9 : menuExit()
    elif num == 1 : munuInsertnew()
    elif num == 2 : menuAllprint()
    elif num == 3 : menuUpdate()
    elif num == 4 : menuDelete()()
    elif num == 5 : menuFind()
    elif num == 6 : menuFileOpen()
    else : print('처리번호를 잘못 입력하셨네요\n')









while flag:
    print()
    num=int(input('1등록 2출력 3수정 4삭제 5조회 9종료 >> '))
    if num == 9:
        print('딕트처리를 종료합니다\n')
        #break 
        #flag = False 
        sys.exit()
    elif num == 1: #mysite[200키] = 'kakao값'
        name = input('이름입력key>>>')
        price = input('가격입력value >>>')
        menu[name] = price
        print(name, '등록 성공했습니다')
    elif num == 2:  #전체출력
        for k,v in menu.items():
            print( k ,' ', v)
        print()
    elif num == 3:  #value편집수정 
        name = input('편집대상 키값 입력>>> ')
        if menu.get(name) == None:
            print('편집대상 딕트가 key 없습니다')
        else:
            price = input('변경가격 재입력value >>>')
            menu[name] = price #mysite[200키] = '새로운값'
            print(name, '가격수정편집 성공했습니다')
    elif num == 4: #삭제
        name = input('삭제대상 키값 입력>>> ')
        if menu.get(name) == None:
            print('삭제대상 딕트가 key 없습니다')
        else:
            menu.pop(name)
            print(name, '데이터삭제 성공했습니다')
            time.sleep(0.3)
            for k,v in menu.items():
                print( k ,' ', v)
    elif num == 5: #한건만=본인꺼
        key = input('조회검색 key 입력>>> ')
        if menu.get(key) == None:
            print(key, '데이터가 없습니다')
        else:
            print(key, menu[key],'데이터 조회성공했습니다')
    else:
        pass
        print('처리번호를 잘못 입력하셨네요\n')





print()
# 사용자정의 함수 
# 클래스 
# 파일처리 - 파일저장, 파일열기
# 예외처리
# crud 
#  ㄴ c 추가신규들록create(insert=add)
#  ㄴ read읽기  update수정  delete삭제

# mysite  = dict() 
# mysite[100] = 'naver'
# mysite[200] = 'kakao'
# mysite[300] = 'apple'

# for i,k in enumerate(mysite):
#     print(i,k,' ', mysite[k])

# 등록   # 100k : 네이버v  200k : 카카오v 
# 출력 items(), enumerate(mysite)
# 수정  100:네이버  100: 에이콘
# key조회 
# mysite[100] ='에이콘'
# print()

# for k,v in mysite.items():
#     print(k,' ', v)

# print()
# # print(mysite[210]) 에러발생
# print(mysite.get(210) ) #에러대신 None출력
# print( 210 in mysite)   #에러대신 False출력


print()