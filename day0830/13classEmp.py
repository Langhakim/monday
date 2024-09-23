# 13classEmp.py



class Emp:
    def insert(self):
        print('신규등록')
        print('딕트등록, 파일저장, insert into 처리')
        print('insert into 처리\n')

    def delete(self):
        print('삭제')
        print('딕트del, delete where 조건')

# Emp.delete() # delete()로만 호출하면은 에러남
ob = Emp()
ob.insert()
ob.delete()

print()
print('9월 2일 월요일 123')
print('9월 2일 월요일 456')
print('9월 2일 월요일 789')
print()
