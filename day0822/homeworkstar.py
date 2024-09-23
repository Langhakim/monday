# homeworkstar.py 문서
# 100페이지 while 반복문 사용금지

# 조건 중복 for 반복문사용하기
# 처리 지역변수, 특정변수 필요없음
# 반복문 대표변수 

# 숙제 아래와같이 출력되게하기
'''
⭐ 
⭐⭐
⭐⭐⭐
⭐⭐⭐⭐
⭐⭐⭐⭐⭐
'''

# for a in range(1,6,1):
#     for b in range(a) :
#         print("⭐",end='')
#     print()

# for a in range(5):
#     print('⭐' *(a+1))

for a in range(5,0,-1):
    print('⭐' *a)