# 12dict.py

mysite = dict()
# 위 2줄 dict변수선언

mysite['naver'] = 'www.naver.com'
mysite['kakao'] = 'www.daum.net'
mysite['google'] = 'www.google.com'

print(mysite)
print()
print(mysite.keys())    # mylist의 전체 키값목록
print()
print(mysite.values())  # mylist의 전체 벨류값 목록
print()
print(mysite['kakao'])  # mylist의 'kakao'의 value값을 확인

# for key in mysite :
#     print(key, ':', mysite[key])


