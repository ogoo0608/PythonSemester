_uname = 'hong'
_passwd = '1234'

login = False
cnt = 0
while (login == False) :
    uname = input ('# 아이디를 입력하세요 : ')
    passwd = input ('# 비밀번호를 입력하세요 : ')
    if ((uname == _uname) and (passwd == _passwd)) :
        
    else :
        cnt += 1
        if (cnt >= 3) :
            print ('3회 이상 틀렸습니다. 종료합니다')
            exit()
        
        else :
            print('>>> 아이디 혹은 비밀번호가 틀렸습니다')

print('>> 로그인 성공')