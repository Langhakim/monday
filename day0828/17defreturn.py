# 17defreturn.py

def book(): # 매개인자X, 리턴값O
    title = '몽블랑'
    return title 

def pay():  # 매개인자X, 리턴값O
    m = 7800
    return m

def myCal(x,y,z): # 매개인자O, 리턴값O
    total = x+y+z
    avg = total//3
    return total, avg
    # 3개 데이터를 받아서 연산처리 후 최종값을 myCal 보내줌
myCal(100,60,55)

def gugudan(name, dan): # 매개인자O, 리턴값X
    pass
    # name출력 반복문 dan출력

def blue():
    color = 'dark'

def main():
    print("main 함수")
    


