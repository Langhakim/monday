# 6testpickle.py

import pickle
import time

fileName = 'C:/Mtest/movie.txt'
mybest = {'엘지twins':2023, '홍창기':0.311}
pickle.dump(mybest, open(fileName, 'wb'))
# file = open(fileName, 'wb') # wb : 이진화하여 읽기(단독실행불가)
# file.write('') # 일반파일처리
# pickle.dump(mybest, file)
print(fileName, '피클저장 성공했습니다\n')

data = pickle.load(open(fileName, 'rb'))
print(data)