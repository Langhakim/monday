# 09dictreturn.py

# 함수의 리턴값을 1개이상 처리
# 함수의 매개인자 1개이상처리 (*args)
# 함수의 매개인자딕트, 리턴값 여러개
score = {
    'kim':[100,90], 
    'lee':[90,69], 
    'goo':[85,70]
    }

def score_procedure(sd):
    kor_list = []
    eng_list = []
    for v in sd.values() :
        kor_list.append(v[0])
        eng_list.append(v[1])

    kor_hap = sum(kor_list)
    eng_hap = sum(eng_list)
    kor_avg = kor_hap // len(kor_list)
    eng_avg = eng_hap // len(eng_list)
    return kor_hap, eng_hap, kor_avg, eng_avg

a, b, c, d = score_procedure(score)
print('국어합계 :', a)
print('영어합계 :', b)
print('국어평균 :', c)
print('영어평균 :', d)
    
    # return 국합계, 영합계, 국평균, 영평균



# a,b,c,d = score_procedure(score)

def guk_sum():
    for k,v in score.itmes() :
        total = sum(v[0])
    print(total)

# for k, v in score.items() : # 값을 직접추출하고 싶으면 items()를 사용해야함
#     total = sum(v)
#     avg = sum(v)//len(v)
#     print(k, ':', total, avg)