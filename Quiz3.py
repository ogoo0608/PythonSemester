'''
- 키보드로 저장할 파일명을 입력받아 파일을 오픈. w 모드로 오픈 !!
- while로 계속 내용을 읽어 읽은 내용을 파일에 저장
- q를 입력하면 작성한 내용을 저장하고 종료
- 11시까지 마감
'''

Fname = "" + input("파일명을 입력하세요 (확장자) : ")

outFp = None
outStr = ""

outFp = open(Fname, "w", encoding="UTF-8")

while True:
    outStr = input("내용을 입력하세요 (q - 저장 및 종료) : ")
    if outStr == "q":break
    
    else:
        outFp.writelines(outStr + "\n")
          
outFp.close()

print("저장했습니다.")