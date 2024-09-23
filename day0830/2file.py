# 1file.py

# 리턴값 = open('파일명', '모드[읽기(w),쓰기(r), 추가(a)]', 인코딩) import 없음
# 리턴변수 .close()

import time

pathName = 'C:/Mtest/sample.txt' # 아래 'C:/Mtest/sample.txt' 내용에 변수값 넣어도됨
wfile = open('C:/Mtest/sample.txt', 'a', encoding='UTF-8')
name = input('이름입력 >> ')
age = input('나이입력 >> ')
address = input('주소입력 >> ')

wfile.write(name) # 라인개행시 + '\n' 사용
wfile.write(age)
wfile.write(address)
wfile.close() # close() 함수사용하는걸 권장
print('sample.txt 파일저장 성공')
print()


time.sleep(1)
pathName2 = 'C:/Mtest/카카오.txt' # 아래 'C:/Mtest/sample.txt' 내용에 변수값 넣어도됨
wfile = open(pathName2, 'a', encoding='UTF-8')
wfile.close()
with open(pathName2, 'a', encoding='UTF-8') as myfile :
    pass
    name = input('이름입력 >> ')
    age = input('나이입력 >> ')
    address = input('주소입력 >> ')

    wfile.write(name) # 라인개행시 + '\n' 사용
    wfile.write(age)
    wfile.write(address)
    wfile.close() # close() 함수사용하는걸 권장
    print(pathName2, 'sample2.txt 파일저장 성공')
    print()