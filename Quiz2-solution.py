# 202135317 김정준

students = {2021001:'홍길동', 2020100:'김사랑', 2021002:'나대장'}

scores = {2021001:[90,85,91],2020100:[92,95,88],2021002:[87,94,96]}

major = ["JAVA", "C", "Python"]

total = 0

def searchData(sid):
    global total
    if (sid in students.keys()):
        print(f"학번 : {sid}, \t이름:{students[sid]}")
        for i in range(len(scores[sid])):
            print(f"{major[i]}:{scores[sid][i]},", end='\t')
            total += scores[sid][i]
        print(f"\n총점 : {total},\t평균 : {int(total/len(scores[sid]))}")
        total = 0
    else : 
        print("죄송합니다. 해당 정보가 없습니다.")
        
def printAll():
    global total
    print('## 학생 성적 리스트 ##')
    print('학번\t이름\tJAVA\tC\tPython\t총점\t평균')
    total = 0
    for id, st, sc in zip(students.keys(), students.values(), scores.values()):
        total = sum(sc)
        print(id, st, *sc, total, int(total/len(sc)), sep='\t')
        
Num = int(input("## 조회할 학번을 입력하세요."))

searchData(Num)
printAll()