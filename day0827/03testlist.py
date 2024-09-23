# 03testlist.py

lotto = [23, 19, 5, 45, 19, 20]
myset = set(lotto) # 응모할때 하나 데이터 유지
print(myset)
lotto = list(lotto)
lotto.sort()
print(lotto)
print()

mylength = len(lotto)
if mylength < 6 :
    print('항목 추가해주세요\n')
elif mylength > 6 :
    print('항목 데이터 초과입니다\n')
elif mylength == 6 :
    print('정상입니다')

# 문제1] lotto 데이터 갯수가 6개 아니면 추가

# 조건1 숫자 6개
# 조건2 중복숫자 제거
# 조건3 정수숫자로만 구성 문자X, 실수X