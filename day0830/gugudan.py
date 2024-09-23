# gugudan.py


# 함수 4개작성 - 시작, 진입, 호출, main
# main함수에서 title(), daninput(), danoutput() endtitle() 호출
# 출력 time.sleep(1)
# 입력 daninput() 이용, 형변환

from time import sleep

def title():
    print()
    print(' ======= 구구단 출력 ======= ')
    print('*' *30)


def endtitle():
    print('*' *30)


def daninput():
    # 리턴값
    su = int(input('구구단 입력 >> '))
    print()
    return su


def danoutput(su):
    # 매개인자
    for k in range(1,10,1):
        print(f'{su} * {k} = {su*k}')

def main():
    # 진입=시작
    title()
    su = daninput() # 리턴값필수
    danoutput(su) # 매개인자
    endtitle()

# 진입함수호출
main()

print()

''' 강사님 코딩
def title():
    print()
    print(' ======= 구구단 출력 ======= ')
    print('*' *30)


def endtitle():
    print('*' *30)


def daninput():
    # dan = 1
    try:
        dan = int(input('단입력 >> '))
    except Exception as ex :
        print('에러이유', ex)
    return dan


def danoutput(dan):
    # 매개인자
    for k in range(1,10,1):
        print(f'{dan} x {k} = {dan*k}')

def main():
    # 진입=시작
    title()
    data = daninput() # 리턴값필수
    danoutput(data) # 매개인자
    endtitle()

# 진입함수호출
main()
'''