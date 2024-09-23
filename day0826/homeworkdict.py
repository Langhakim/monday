# homeworkdict.py

# 아래와 같이 출력하라
# 김랑하 160 80
# 박용택 170 85
# 김현수 120 60
# 이병규 118 59

score = {
    '김랑하':[100,60],
    '박용택':[90,80],
    '김현수':[86,34],
    '이병규':[82,36]
}

for k, v in score.items() : # 값을 직접추출하고 싶으면 items()를 사용해야함
    total = sum(v)
    avg = sum(v)//len(v)
    print(k, ':', total, avg)

