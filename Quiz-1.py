# def printReport(students, scores) :
#     total = 0
#     avg = 0
    
#     for i in range(0, len(students), 1) :
#         print(students[i], '\t', sep='', end='')
#         for k in range(0, len(scores), 1) :
#             print(scores[i][k], '\t', end='')
#             total += scores[i][k]
#         avg = total // len(scores)
#         print(total, '\t', avg, sep='',)
#         total, avg = 0, 0
        
# students = ['홍길동', '김사랑', '나대장']
# scores = [[90,85,91],[92,95,88],[87,94,96]]

# printReport(students, scores)

def printReport(stu_list, score_list) :
    for i, score in enumerate(score_list) :
        print(stu_list[i], score[0], score[1], score[2], sep='\t', end='\t')
        hap = sum(score)
        avg = hap / len(score)
        print('총점 : ', hap, '평균 :', int(avg), sep='\t')
        print('')
        
students = ['홍길동', '김사랑', '나대장']
scores = [[90,85,91],[92,95,88],[87,94,96]]

printReport(students, scores)