# 09dictmenu.py

# crud : c 추가신규등록 create(insert=add), read읽기, update수정, delete삭제

import time
import sys # 프로그램종료 sys.exit()

menu = dict()
flag = True
num, su, sel = 0,0,0
name, msg, info, message = '안내문', '정보', '메세지', 'ddd'

while flag :
    print()

    num = int(input('1.등록 2.리스트 3.수정 4.삭제 5.항목조회 9.종료 >>> '))

    if num == 9 :
        print('\n종료합니다')
        break
        # flag = False  # 종료하는 명령어
        # sys.exit()  # 종료하는 명령어

    elif num == 1 : # 딕트등록 mysite[200] = 'kakao'
        name = input('\n메뉴입력(key) >> ')
        price = input('가격입력(value) >> ')
        menu[name] = price
        print(name, '등록 성공')

    elif num == 2 : # 딕트전체출력 for반복문 권장
        for k,v in enumerate(menu) :
            print('번호 :',k+1,' 메뉴명:',v,' 가격:',menu[v])
        print('\n입력된 전체리스트가 출력 되었습니다')

    elif num == 3 :
        name = input('\n수정할 데이터 입력 >> ')
        if menu.get(name) == None :
            print('\n수정할 데이터가 없습니다 다시 확인 후 이용해주세요')
        else :
            price = input('\n변경할 가격 입력 >> ')
            menu[name] = price
            print(f'\n{name}의 가격이 수정되었습니다')

    elif num == 4 :
        name = input('\n삭제할 데이터 입력해주세요 >> ')
        if menu.get(name) == None :
            print('\n삭제할 데이터가 없습니다.')
        else : 
            del menu[name]
            print(f'\n{name}의 값이 모두 삭제되었습니다.')

    elif num == 5 :
        name = input('\n조회할 데이터를 입력해주세요 >> ')
        if menu.get(name) == None :
            print('\n조회한 데이터가 없습니다')
        else :
            print(f'\n{name}의 값은 {price}원 입니다.')
    else : 
        print('번호를 잘못 입력했습니다')






'''
mysite = dict() # 100k : 네이버v / 200k : 카카오v

mysite[100] = '네이버'
mysite[200] = '카카오'
mysite[300] = '애플'

for k,v in enumerate(mysite) :
    print(k,v,' ',mysite[v])

# 출력 items(), enumerate(mysite)
# 수정 100:네이버 / 100:에이콘

mysite[100] = '에이콘'

for k,v in mysite.items() :
    print(k,' ',v)

print()

print(mysite[200])  # 없는 키값을 입력하였을때 에러발생
print(mysite.get(210))  # 없는 키값을 입력하였을때 None출력
print(210 in mysite)    # 없는 키값을 입력하였을때 False출력

print()
'''