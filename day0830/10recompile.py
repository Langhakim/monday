# 10recompile.py

import re


# 정규식 compile('\d{6}-\d{7}'), sub(1,2,3) 다른방법
# 문자열함수 for ~ if ~ data [시작위치]
# 정규식 re.sub() 함수를 사용 권장
# compile('') 적용 후 sub() 확인
# 문제] 주민번호 뒷자리를 *표시로 바꿔서 출력하라
data = '''
kim 931224-1236457
park 880508-1234567
lang 671104-1546987
'''
com = re.compile('-\d+')

form = re.sub('[0-9]{7}', '*******', data)
print(form)

# \n라인개행(엔터기능), \t 탭, \b 백스페이스
com = re.compile('-\d+')
# pattern = re.compile('(\d{6})[-](\d{7})') # \d는 정수를 가르킴 {}안의 숫자는 몇자리인지 지정
first = com.sub('-*******', data) # \g
print(first)


# phone = '010-6464-7878 박이썬'
# # 예제 - re.sub('1패턴', '2변경적용', phone)
# model = re.sub('-[0-9]{4}-', '-****-', phone)
# print(phone)
# print(model)

# # 두번째 정규식 예제
# msg = 'my best is myjava blue apple herry my python'
# x = re.findall('my',msg)
# y = re.findall('blue',msg)
# z = re.findall('red',msg)
# print(x)
# print(y)
# print(z) # 찾는값이 없으면 []출력
# print()

# msg = 'my best% @#$^& 야구 엘지트윈스 랑랑 ㅇ 하 Flu_it is blue 2400 %#357cherry'
# result1 = re.findall('[\w]+', msg)
# result2 = re.findall('[\W]+', msg)
# result3 = re.findall('[a-zA-Z0-9가-힣]+', msg)
# result4 = re.findall('[^a-zA-Z0-9가-힣]{3,10}', msg)
# print(result1); print()
# print(result2); print()
# print(result3); print()
# print(result4); print()

# 첫번째 정규식 예제
# msg = 'my best% Flu_it is blue 2400 %#357cherry'
# info1 = re.findall('[a-zA-Z]{3,7}', msg)
# info2 = re.findall('[a-zA-Z0-9]{3,7}', msg)
# print(info1)
# print(info2)
# print()







print()