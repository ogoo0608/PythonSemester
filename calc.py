'''
함수 예제 모음 
'''

def calc1(num1,num2,op) :
    
    result = 0

    if op == '+' :
        result = num1 + num2
    elif op == '-' :
        result = num1 - num2
    elif op == '*' :
        result = num1 * num2
    elif op == '/' :
        result = num1 / num2 
    return result

num1, num2 = map(int, input("원하는 숫자 두 개를 입력하세요").split())

op = input("연산자 입력 (+, -, *, /) : ")

print("계산 결과 : ", calc1(num1,num2,op))