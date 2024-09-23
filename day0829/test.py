# test.py

# 문제1] name, age, gender 변수사용
# 문제2] 나이 입력범위 1~70사이
    #    ㄴ 청소년 1~20, 20~30청년 31~65중년 66이상 노년
# 문제3] 남자/남/man입력 - 남자 출력 / 여자/여/woman입력 - 여자 출력

print()

na = str(input('이름을 입력해주세요 >> '))
ag = int(input('나이를 입력해주세요 >> '))
gen = str(input('성별을 입력해주세요 >> '))

def name():
    return f'{na}'

def age():
    if 19 >= ag >= 1 :
        return f'{ag}살 청소년입니다.'
    if 30 >= ag >= 20 :
        return f'{ag}살 청년입니다.'
    if 65 >= ag >= 31 :
        return f'{ag}살 중년입니다.'
    if ag > 65 :
        return f'{ag}살 노년입니다.'

def gender():
    # 남자/남/man입력 - 남자 출력 / 여자/여/woman입력 - 여자 출력
    if gen == '남자' or gen == '남' or gen == 'man' :
        return '남자입니다.'
    elif gen == '여자' or gen == '여' or gen == 'woman' :
        return '여자입니다.'
    else : 
        return '성별을 정확히 입력해주세요.'
    
def check():
    if na == '' :
        return '이름을 정확히 입력해주세요'

    if 0 >= ag or '' == ag :
        return '나이를 정확히 입력해주세요'
    # else:
    #     pass

def main():
    print()
    ch = check()
    if ch :
        print(ch)
    else :
        print(f'이름 : {name()}')
        print(f'나이 : {age()}')
        print(f'성별 : {gender()}')

main()
print()