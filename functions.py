'''
함수 관련 예제
'''

# 함수 선언만 해두고 내용은 나중에 구현
def printAll():
    pass

# 인자가 두 개인 함수
def calc(num1, num2):
    return num1+num2

print('계산결과 : ', calc(200,300))
print('계산결과 : ', calc(num1=200, num2=300))

# 가변 인자
def total(*num):
    tot = 0
    for n in num:
        tot += n
    return tot

print(total(1,2,3))
print(total(20,20,30))

# 리턴이 여러 개인 경우
def addNum(*nums):
    tot = 0
    cnt = 0
    for n in nums:
        tot += n
        cnt += 1
    return cnt, tot

cnt, total = addNum(10,20,30)
print(cnt,tot)

# 전역 변수, 지역 변수, global 예제
num4 = 10
def VarTest():
    global num5
    num5 = 20
    global num4
    num4 = 100
    print('VarTest() : ', num4)
    
VarTest()
print(num4)
# print(num5)==> 함수 안에 있는 변수는 호출 할 수 없음 .. but global 을 사용하면 가능해짐 !! 
print(num5)

