# 03listsearch.py


data = [7,8,9,1,2]
find = int(input('데이터찾기>>> '))

if find in data :
    print('결과 : ', find in data)
    print(find, '검색성공')
else :
    print('결과 : ', find in data)
    print(find, '검색실패')
    
print()


# 데이터가 있으면 성공메세지 데이터출력
# 데이터가 없으면 실패메세지 데이터출력
# for 대표변수 in range(5) :
# list에서 대이터 찾기 할때 in 키워드 사용

