# 13dict.py

mysite = dict()
# 위 2줄 dict변수선언

mysite['naver'] = 'www.naver.com'
mysite['kakao'] = 'www.daum.net'
mysite['google'] = 'www.google.com'
mysite['facebook'] = 'www.facebook.com'

print(mysite['kakao'])  # mylist의 'kakao'의 value값을 확인 = print(mysite.get('kakao'))
print()
print(mysite.get('kakao')) # get은 함수라 ()사용해야함 / mylist의 'kakao'의 value값을 확인
print()
# print(mysite['googl'])  # 키 값을 잘 못 입력하면은 에러
# print(mysite.get('googl'))  # 키 값을 잘 못 입력 None 출력

# mysite안에 naver 키 값이 있는지 확인(True(있음) or False(없음)로 출력)
mya = 'naver' in mysite
myb = 'nave' in mysite
print(mya)
print(myb)

# for key in mysite :
#     print(key, ':', mysite[key])


