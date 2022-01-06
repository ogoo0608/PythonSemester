'''
# 계산기 만들기
- 두 개의 숫자와 연산자를 입력받아 계산 결과를 출력
- 입력은 여러방식을 사용할 수 있음
- 지원되는 연산은 +, -, *, /
- 쉬는시간 포함해서 11:00 까지 문제를 풀어 봅시다.
- 희망자 발표
'''

num1 = int(input("첫 번째 숫자 입력 : "))
num2 = eval(input("두 번째 숫자 입력 : "))

op = input("연산자 입력 : ")

result = 0

if op == '+' :
    result = num1 + num2
elif op == '-' :
    result = num1 - num2
elif op == '*' :
    result = num1 * num2
elif op == '/' :
    result = num1 / num2 
    
print("계산 결과 : %d %s %d = %d" % (num1, op, num2, result))

'''
-> 숫자 두 개를 한꺼번에 입력 받으려면 ????

num1, num2 = map(int, input("원하는 숫자 두 개를 입력하세요 (ex:10 20)).split()) # map 함수 ==> 집합형 데이터 안에 있는 모든 원소의 공통된 기능을 수행하도록 만들어줌


op = input("연산자 입력 : ")

result = 0

if op == '+' :
    result = num1 + num2
elif op == '-' :
    result = num1 - num2
elif op == '*' :
    result = num1 * num2
elif op == '/' :
    result = num1 / num2 
    
print("계산 결과 : %d %s %d = %d" % (num1, op, num2, result))
'''