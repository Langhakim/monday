# 11dict.py

mysite = dict()
# 위 2줄 dict변수선언

mysite['dima'] = 'www.dima.com'
mysite['kakao'] = 'www.daum.net'
mysite['google'] = 'www.google.com'
print(mysite)
print()

for key in mysite :
    print(key, ':', mysite[key])

print()
print()

for k, v in enumerate(mysite) :
    print(k, ':', mysite[v])

print()
print()

for k, v in mysite.items() :
    print(k, ':', v)

print()
print()
