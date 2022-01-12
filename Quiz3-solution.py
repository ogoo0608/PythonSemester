'''
- 키보드로 저장할 파일명을 입력받아 파일을 오픈. w 모드로 오픈 !!
- while로 계속 내용을 읽어 읽은 내용을 파일에 저장
- q를 입력하면 작성한 내용을 저장하고 종료
- 11시까지 마감
'''

print('## 노트패드 v1.0 ##')
fname = input('# 저장할 파일명을 입력하세요 : ')

with open(fname, 'w', encoding='UTF-8') as f:
    while ((msg := input()) != 'q'):
        f.writelines(msg + '\n')
f.close()