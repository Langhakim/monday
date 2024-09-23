# 08findall.py

import re

# # 두번째 정규식 예제
# msg = 'my best is myjava blue apple herry my python'
# x = re.findall('my',msg)
# y = re.findall('blue',msg)
# z = re.findall('red',msg)
# print(x)
# print(y)
# print(z) # 찾는값이 없으면 []출력
# print()

msg = 'my best% @#$^& 야구 엘지트윈스 랑랑 ㅇ 하 Flu_it is blue 2400 %#357cherry'

result1 = re.findall('[\w]+', msg)
result2 = re.findall('[\W]+', msg)
result3 = re.findall('[a-zA-Z0-9가-힣]+', msg)
result4 = re.findall('[^a-zA-Z0-9가-힣]{3,10}', msg)
print(result1); print()
print(result2); print()
print(result3); print()
print(result4); print()

# 첫번째 정규식 예제
# msg = 'my best% Flu_it is blue 2400 %#357cherry'
# info1 = re.findall('[a-zA-Z]{3,7}', msg)
# info2 = re.findall('[a-zA-Z0-9]{3,7}', msg)
# print(info1)
# print(info2)
# print()







print()