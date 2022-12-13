import random

def dice():
    diceN = random.randint(1, 7)
    return diceN

diceL = []
n = 0

print("주사위 3번 굴리기")

while True:
    n = dice()
    
    if n in diceL:
        continue
    else:
        diceL.append(n)
    
    if len(diceL) == 3:
        break
diceL.sort()
print(f">>  {diceL}", end='')


    