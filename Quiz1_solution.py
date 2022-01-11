students = ['홍길동', '김사랑', '나대장']
scores = [[90,85,91],[92,95,88],[87,94,96]]

# 방법 1 : 중첩 for문 사용

def printReport() :
    for i in range(0, len(students)):
        print(students[i],end='\t')
        for j in range(0,3) :
            print(scores[i][j], end='\t')
        total = sum(scores[i])
        print('%d\t%d' % (total, total/len(scores[i])))
        
printReport()

# 방법 2 : 인덱스를 이용한 단일 for문 사용

def printReport2():
    for i in range(len(students)):
        total = sum(scores[i])
        print('%s\t%d\t%d\t%d\t%d' % (students[i], scores[i][0], scores[i][1], scores[i][2], scores[i][3], total, int(total/3), sep='\t'))
        
printReport2()

# 방법 3 : enumerate 사용 ==> 중요

def printReport3() :
    for i, sc in enumerate(scores) :
        total = sum(sc)
        print(students[i], sc[0], sc[1], sc[2], total, int(total/len(sc)), sep='\t')
        
printReport3()

# 방법 4 : zip과 unpacking을 사용하는 방법 ==> unpacking : 원소를 분해해서 각각의 데이터로 만들어줌 ==> 중요

def printReport4() : 
    for st, sc in zip(students,scores) :
        total = sum(sc)
        print(st, *sc, total, int(total/len(sc)), sep='\t')
        
printReport4()

