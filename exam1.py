'''
파이썬 기본 문법 활용 퀴즈
- 아이디와 비밀번호를 입력받아 맞으면 로그인 성공 그렇지 않으면 성공할 때까지 반복 !
- while문을 사용 !
'''

# DB로부터 가지고 온 값으로 가정

# _uname = 'hong'
# _passwd = '1234'

while True :
    
    _uname = input("아이디를 입력하세요 : ")
    _passwd = input("비밀번호를 입력하세요 : ")
    
    if _uname == 'hong' and _passwd =='1234' :
        print("로그인 성공 ! 환영합니다.")
        break

    else :
        print("로그인 실패 ! 다시 시도하세요.")
        continue
    
# break 와 continue 잊지말자