'''
# 계산기 만들기
- 두 개의 숫자와 연산자를 입력받아 계산 결과를 출력
- 입력은 여러방식을 사용할 수 있음
- 지원되는 연산은 +, -, *, /
- 쉬는시간 포함해서 11:00 까지 문제를 풀어 봅시다.
- 희망자 발표
'''
while True :
    a = float(input('첫 번째 숫자 : '))
    b = float(input('두 번째 숫자 : '))
 
    if a == b == 0 :
        print('종료합니다.')
    c = input('연산자 : ')
    
    if c == '*' :
        d = a * b
        print('계산값은', d, '입니다.')
        continue
    
    if c == '+' :
        d = a + b
        print('계산값은', d, '입니다.')
        continue
    
    if c == '-' :
        d = a - b
        print('계산값은', d, '입니다.')
        continue
    
    if c == '/' :
        d = a / b
        print('계산값은', d, '입니다.')
        continue
 
    if c != '+' or c != '-' or c != '*' or c != '/' : 
        while True :
            print('지원하지 않는 연산자입니다.')
            c = input('연산자 : ')
 
            if c == '*' :
                d = a * b
                print('계산값은', d, '입니다.')
                exit()
            
            if c == '+' :
                d = a + b
                print('계산값은', d, '입니다.')
                exit()
            
            if c == '-' :
                d = a - b
                print('계산값은', d, '입니다.')
                exit()
            
            if c == '/' :
                d = a / b
                print('계산값은', d, '입니다.')
                exit()