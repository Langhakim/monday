# 10dict.py

mysite = {}
mydata = dict()
# 위 2줄 dict변수선언

mysite['naver'] = 'www.naver.com'
mysite['kakao'] = 'www.daum.net'
mysite['google'] = 'www.google.com'
print(mysite)
print()

print(mysite['naver'])
print(mysite['kakao'])
print(mysite['google'])
print()

for key in mysite :
    print(key, ':', mysite[key])
