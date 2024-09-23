# 09classEmp.py

class Emp:
    user_id = 'blue'
    user_pwd = '1234'

    def __init__(self, id, pwd):
        self.user_id = id
        self.user_pwd = pwd

    def insert(self, nick, age):
        
        print('전역변수', self.user_pwd)
        print('전달된 이름', nick)
        print('전달된 나이', age)
        print('신규등록 insert(self키워드)')
        print('insert into처리\n')


    def delete(self):
        print('삭제처리')
        print('딕트del, delete where 조건')
        

ob = Emp()
ob.insert('홍길동', 7)
ob.delete()    






print()