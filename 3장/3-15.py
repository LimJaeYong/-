import random

def lottoFunc():
    lottoNum = random.randint(1, 45)
    return lottoNum

lottoList = []
num = 0

print("로또 추첨 시작")

while True:
    num = lottoFunc()
    
    if num in lottoList:
        continue
    else:
        lottoList.append(num)
    if len(lottoList) == 6:
        break
    
print("오늘의 로또 번호 : ", end = '')
lottoList.sort()
for i in range(0, 6):
    print(lottoList[i], " ", end='')