# 파일 관련 예제
fin = open('test.txt','r',encoding='utf-8') # 상대 경로
while True:
    msg = fin.readline()
    if msg == '':break
    else: print(msg.strip()) # strip() == \n 라인 제거 가능.
    
print('========================')

fin = open('test.txt','r',encoding='utf-8') # 상대 경로
while (msg := fin.readline()) != '': # := 파이썬 3.8 부터 사용 가능 (왈러스 연산자)
    print(msg.strip())
fin.close()

print('========================')

fin = open('test.txt','r',encoding='utf-8') 
for msg in fin.readlines():
    print(msg.strip())
fin.close()

print('========================')