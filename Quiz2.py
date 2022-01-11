# 202135317 김정준

students = {2021001:'홍길동', 2020100:'김사랑', 2021002:'나대장'}

scores = {2021001:[90,85,91],2020100:[92,95,88],2021002:[87,94,96]}

sub = ["자바", "C언어", "파이썬"]

total = 0

def searchData() :
    
         key = input(" ## 조회할 학번을 입력하세요 : ")
        
         if (key in students.keys()) :
             
             print()
             
             total = 0
             
         else : 
             print(" 죄송합니다. 해당 학번이 존재하지 않습니다. ")
            
 searchData
            
 def printAll() :
     global total 
     print(" ## 학생 성적 리스트 ##")
     print("학번\t이름\t자바\tC언어\t파이썬\t총점\t평균")
     for key in students.keys() :
         total sum(socres[key])
         print(key,students[key], *scores[key], total, int(total/len(scores[key]), sep='\t'))


searchData()
printAll()

