import random

def lottoFunc() :
    lottoNum = random.randint(1,69)
    return lottoNum

powerNum = random.randint(1,26)

lottoList = []
num = 0 

while True :
    num = lottoFunc()
    
    if num in lottoList :
        continue
    else:
        lottoList.append(num)
        
    if len(lottoList)==5:
        break
    
lottoList.sort()
print("파워볼 번호 생성")
print(f"일반볼 : ", end = "")
for i in range(5):
    print(f"{lottoList[i]} ", end = "")
    
print(f"파워볼: {powerNum}")