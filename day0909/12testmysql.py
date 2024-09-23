# 12testmysql.py

# 오라클대신 mysql연결
import pymysql
       
# configOracle = {
#     'user' : 'system',
#     'password' : '1234',
#     'dsn' : '127.0.0.1:1521/xe' 
# }

config={
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '1234',
    'database' : 'naver',
    'port' : 3306
}

CN = pymysql.connect(**config)
cursor = CN.cursor()

def testSelectAllInsert():
    msg = 'select * from test'
    cursor.execute(msg)
    rows = cursor.fetchall()
    print('cursor.fetchall() 함수타입 :', type(rows),'\n')
    for r in rows :
        print(r[0],r[1],r[2],r[3])

def testInsert():
    # code, name 2개 필드만 입력받아서 저장처리
    print('\n-- test테이블 신규등록 --')
    dcode = int(input('새로등록할 code를 입력하세요 >> '))
    dname = input('등록할 name을 입력하세요 >> ')
    msg = f"insert into test(code, name) values({dcode},'{dname}')"
    cursor.execute(msg)
    rows = cursor.fetchall()
    CN.commit()

print()

testSelectAllInsert()
while True :
    print()
    sel = int(input('1.신규등록 2.전체출력 3.수정 4.삭제 5.이름조회 ---- 9.종료 >> '))

    if sel == 9:
        break
    elif sel == 1 :
        testInsert()
    elif sel == 2 :
        testSelectAllInsert()
    elif sel == 3 :
        pass
    elif sel == 4 :
        pass
    elif sel == 5 :
        pass
    else :
        pass
