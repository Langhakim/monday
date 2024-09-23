# 03play.py
import time
import game # 물리적인 파일명만 명시

print()
print('03play.py')
print()
time.sleep(0.3)

print(game.user_id)
print(game.user_pwd)

time.sleep(0.3)
game.terran()

time.sleep(0.3)
game.LG('야구')

time.sleep(0.3)
fire = game.camp()
print(f'불멍횟수는 {fire}')
print(f'불멍횟수는 {game.camp()}')

# game.py 문서에
# 전역변수 user_id, user_pwd
# 함수    terran(), LG(lg), camp() 리턴값있음


print()