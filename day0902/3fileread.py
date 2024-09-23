# 3fileread.py

# 리턴값 = open('파일명', '모드[읽기(w),쓰기(r), 추가(a)]', 인코딩) import 없음
# 리턴변수 .close()

import time

# 파일 읽기 처리
pathName = 'C:/Mtest/sample.txt' # 아래 'C:/Mtest/sample.txt' 내용에 변수값 넣어도됨
rfile = open(pathName, 'r', encoding='UTF-8')
data = rfile.readline() # 한라인씩읽기
# data = rfile.read() # 전체읽기
print(data)
print('- ' *50)
rfile.close()

time.sleep(1)
pathName2 = 'C:/Mtest/sample2.txt' # 아래 'C:/Mtest/sample.txt' 내용에 변수값 넣어도됨
with open(pathName2, 'r', encoding='UTF-8') as myfile :
    my = myfile.readline()
    while my != '' :
        print(my, end = '')
        my = myfile.readline()
print()