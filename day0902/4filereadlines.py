# 4filereadlines.py

# 파일읽기 read(), readline(), readlines()
file = 'C:/Mtest/sample2.txt' # 아래 'C:/Mtest/sample.txt' 내용에 변수값 넣어도됨
with open(file, 'r', encoding='UTF-8') as myfile :
    for data in myfile.readlins():
        print(data, end = '')
print()