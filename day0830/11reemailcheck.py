# 11reemailcheck.py

import re

def email_check(email):
    check1 = re.findall(['@'], email)
    if  check1 != '@' :
        print('"@"미포함, 이메일 형식이 잘 못 되었습니다.')
    elif re.findall('.', email) != '.' :
        print('"."미포함, 이메일 형식이 잘 못 되었습니다.')
    elif re.findall('[^a-zA-Z0-9가-힣{0:@}]', email) not in None :
        print('"특수문자포함", 이메일 형식이 잘 못 되었습니다.')
    else :
        print('정상 이메일입니다.')

mail = 'iii@gmail.com'
print(re.findall('@', mail))

email_check("iii@gmail.com")
# email_check("iii_gmail")
# email_check("iii")
# email_check("iii@gmail.com")
# email_check("LLL@gmail.com")