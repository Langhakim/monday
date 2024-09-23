# homeworkcoffee.py

money, sel = 0, 9
# coffee, cocoa = 500, 300

money = int(input('\n투입금액 >>> '))

print()
while True :
    if 300 > money : 
        print('투입금액이 최소주문 금액보다 부족하여 종료합니다')
        break
    print('------------------커피머신------------------')
    sel = int(input(' 1.커피(500원) 2.코코아(300원) 3.환불 9:종료 >>> '))
    if sel == 1 and money >= 500 :
        print('\n주문성공! 현재 잔액은 ',money-500,'원 입니다.\n')
    elif sel == 1 and 500 > money :
        print('\n금액이 부족합니다.\n')
    elif sel == 2 and money >= 300 :
        print('\n주문성공! 현재 잔액은 ',money-300,'원 입니다.\n')
    elif sel == 2 and 300 > money :
        print('\n금액이 부족합니다.\n')
    elif sel == 3 :
        print('\n',money,'원 정상 환불되었습니다. 감사합니다.\n')
        break
    elif sel == 9 :
        print('\n이용해주셔서 감사합니다.\n')
        break
    else :
        print('\n주문번호를 정확히 입력해주세요.\n')
print()