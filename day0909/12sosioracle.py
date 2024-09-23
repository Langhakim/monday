# 12sosioracle.py

# 오라클 sosi테이블 + 파이썬
import os
import pandas as pd
import cx_Oracle  

# pip install oracledb 
import oracledb     
import time
       

config = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe' 
}


# conn = oracledb.connect(**config) #오류
# conn = oracledb.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
conn = cx_Oracle.connect(**config) # 인자를 딕트값으로 받음
# print('config 매개인자 ', type(config))
cursor = conn.cursor()

print("database version: ", conn.version)
print("oracle connect ok success")
print()


def sosiInsert():
    print('\n< sosi테이블 신규등록 처리 >\n')
    
    while True :
        dcode = int(input('코드 입력>> '))
        check = f'select count(*) from sosi where code = {dcode}'
        cursor.execute(check)
        row = cursor.fetchone() # fetchone 값을 하나만 가져와 / 가져온값을 tuple로 저장
        # print('row타입', type(row))

        if row[0] > 0 :
            print('중복된 코드 입니다 다른 코드를 다시 입력해주세요.') 
        else : 
            break
    # 코드데이터 입력 후 중복체크 후 재입력
    # 1.신규등록 2.전체출력 3.수정 4.삭제 5.제목조회 9.종료
    dname = input('이름 입력>> ')
    dtitle = input('제목 입력>> ')
    dsal = int(input('급여 입력>> '))
    msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'D')"    
    cursor.execute(msg)
    conn.commit()
    print(dcode , ' 저장 성공했습니다')
    time.sleep(1)


def sosiSelectAll():
    msg = 'select * from sosi order by code'
    cursor.execute(msg)
    rows = cursor.fetchall() # 모아서처리 batch / 실시간으로 처리 fetch
    # print('rows타입 ', type(rows)) # type : list
    print()

    print('%s\t %s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:
        # print(r[0],r[1],r[2],r[3],r[4],r[5])
        print('%4d\t %4s\t %10s\t  %3d\t %10s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))
    print('- ' * 50)
    print()

def sosiUpdate():
    # 수정대상 : title, sal, grade 3개필드 수정가능하게 코딩
    while True :
        up_code = int(input('\n수정할 코드를 입력하세요 >> '))
        up_check = f'select count(*) from sosi where code = {up_code}'
        cursor.execute(up_check)
        up_low = cursor.fetchone()

        if up_low[0] > 0:
            uptitle = input('수정제목 입력 >> ')
            upsal = int(input('수정급여 입력 >> '))
            upgrade = input('수정등급 입력 >> ')
            up_msg = f"update sosi set title = '{uptitle}', sal = {upsal}, grade = '{upgrade}' where code = {up_code}"
            print(up_msg)
            cursor.execute(up_msg)
            conn.commit()
            print(f'{up_code}가 정상 수정되었습니다\n')
            sosiSelectAll()
            break
        else :
            print('없는 코드번호입니다. 다시 입력하세요.')

def sosiDelete():
    while True :
        del_code = int(input('테이블조회를 참고하여 삭제할 코드를 입력하세요 >> '))
        del_check = f'select count(*) from sosi where code = {del_code}'
        cursor.execute(del_check)
        del_row = cursor.fetchone()
        
        if del_row[0] > 0:
            del_msg = f'delete from sosi where code = {del_code}'
            cursor.execute(del_msg)
            conn.commit()
            print(f'{del_code}가 정상삭제 되었습니다.')
            sosiSelectAll()
            break

        else :
            print(f'{del_code}는 없는 코드번호 입니다 다시 입력해주세요.') 
     

def sosiSelectTitle():
    print('\n< 제목조회 필드입니다.\n')
    dtitle = input('제목조회 >> ')
    msg = f"select * from sosi where title like '%{dtitle}%' "

def sosiStart():
    while True :
        start = int(input('1.신규등록 2.전체출력 3.수정 4.삭제 5.제목조회 9.종료 >> '))
        if start == 9:
            print('\n종료합니다. 감사합니다.')
            break
        elif start == 1:
            sosiInsert()
        elif start == 2:
            sosiSelectAll()
        elif start == 3:
            sosiUpdate()
        elif start == 4:
            sosiDelete()
        elif start == 5:
            sosiSelectTitle()
        else :
            print('메뉴에 없는 번호 입니다. 번호를 다시 입력해주세요.')

sosiSelectAll()
sosiStart()