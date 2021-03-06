# 1. 변수 선언과 출력


num1 = 10
num2 = 20

print (num1, num2)
print('num1 =', num1, 'num2 =', num2)
print('num1=', num1,' , ' 'num2=', num2, sep='')
print('num1=%d, num2=%d' % (num1,num2))
print(f'num1={num1}, num2={num2}') # 이게 더 좋은 방식 ..

# 2. 입력과 형 변환

num3 = int(input('num3=>'))
num4 = eval(input('num4=>'))

print('num3 + num4 =', num3+num4)

# 3. 연산자와 자료형

a = 100, 200, 300, 400
print(a)
print(a[3])


print(type(123)) # int
print(type('hello')) # str
print(type(12.2)) # float
print(type([1,2,3,4])) # List (배열) => 변경 가능
print(type((1,2,3,4))) # Tuple => 변경 불가능
print(type({10,20,30})) # Set
print(type({'a':10, 'b':20, 'c':30})) # Map (dict)
print(type(10>50)) # boolean 

# 외부 라이브러리 참조

import calendar
calendar.prmonth(2022,1) # prmonth : print month 라는 뜻 ,,

# 4. if

_uname = 'hong'
_passwd = '1234'

uname = input('# 아이디를 입력하세요: ')
passwd = input('# 비밀번호를 입력하세요: ')

if((uname == _uname) and (passwd == _passwd)) :
    print('>> 로그인 성공!!')
else :
    print('>> 로그인 실패!!')
    
# 5. for 

for i in range(3):
    print('Hello World')
    
for i in range(1,4,1):
    print(i, ': Hello World')
    
for i in range(0,5,1):
    print(i)

for i in [10,20,30]:
    print(i)
    
for i in range(1,11,1):
    print(i, end=' ')