# 07comprehesion.py [ 연산 if/else, for~~ ]

print()

message = ['spam', 'ham', 'spam', 'spam', 'spam', 'ham']
# 문제1] for 반복 ~ if 사용
# spam만 출력 후 spam의 갯수출력
message_cnt = 0
for k in message :
    if k == 'spam':
        print(k, end = '')
        # message_cnt = message_cnt + 1 #정석
        message_cnt += 1 # 대입연산 약간 야매

print('갯수 :', message.count('spam'))
print('갯수 :', message_cnt)


print()
# 문제2] [ 만앞 if조건 else 붙뒤 for~~~ ]comprehension 처리
# 문제2] [ 만족하면 앞쪽값이 나옴 for~~~ if 조건만족 ] comprehension처리
# 방법1 tmep_list = [ k for k in message if k == 'spam' ]
tmep_list = [ k for k in message if 'spam' in k ]
print(tmep_list)

print()
dummy = []
# 문제3] spam=0, ham=1(스팸이면 0 출력, 햄이면 1출력) dummy = []   ret = []
# message = ['spam', 'ham', 'spam', 'spam', 'spam', 'ham', 'spam', 'ham']
# for ~~ if ~ else
# dummy_list = [ k for k in message if 'spam' in k ]
for k in message :
    if k=='spam':
        dummy.append(0) # append 사용시 () 주의 !
    else : 
        dummy.append(1)
print('반복 ~ 제어정석', dummy)
print()

mydummy = [ 0 if k == 'spam' else 1 for k in message ] # 위 26~30번과 같은 내용
print('comprehension', mydummy)
print()