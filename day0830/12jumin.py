# 12jumin.py

import re

jumin = '931224-234567'

my = int(jumin(7))
if my == 1 or my == 3 :
    print('남자')
elif my == 2 or my == 4 :
    print('여자')
else :
    print('성별표기 오류') 

gender = re.search('(-)(\d{1})', jumin)
print(gender) # <re.Match object; span=(6, 8), match='-1'>

genderNum = int(gender.group(2)) # group(2) : gender에서 찾은값에서 2번째 데이터를 출력해줘
print(genderNum)

if genderNum == 1 or genderNum == 3 :
    print('남자')
elif genderNum == 2 or genderNum == 4 :
    print('여자')
else :
    print('성별표기 오류')


print()