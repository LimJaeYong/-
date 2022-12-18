import random


numList = list(range(1,101))
random.shuffle(numList)

def pnl():
    n = 0
    for i in range(len(numList)):
        n += 1
        if n == 10:
            print(numList[i])
            n = 0
        else:
            print(numList[i], end=" ")

pnl()
print("배열 정렬")
        
while True:
    print("1. 내림차순 2. 오름차순")
    a = int(input(" >> "))
    
    if a == 1:
        numList.sort(reverse=True)
    
    elif a == 2:
        numList.sort()
    else:
        print("잘못 입력")
        continue

    pnl()