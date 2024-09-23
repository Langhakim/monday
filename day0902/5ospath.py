# 5ospath.py

# 파일읽기 read(), readline(), readlines()
import sys
import os.path

save_path = os.path.abspath('C:/Mtest/ospath.txt') 
try :
    if not os.path.exists(save_path): # 파일이 없다면
        print(save_path, '대상 파일이 존재하지 않습니다')
        sys.exit()
    else:
        pass
except Exception as EX :
    print('에러이유 확인', EX)

print()