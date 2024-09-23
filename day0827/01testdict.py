# 01testdict.py

mylist = []
mydict = {}

mydict[500] = '우중차박'
mydict[700] = '우중등산'
mydict[900] = '우중캠핑'
for k,v in mydict.items() :
    print(k, ':', v)

print()
print()

for i,k in enumerate(mydict) :
    print(i+1, ':', k, mydict[k])

print()
print()
