import random

dice = 0
myList = []
total = 0

for i in range(100):
    dice = random.randint(1,6)
    myList.append(dice)
    total += myList[i]

avg = total/100
print("100번 던진 주사위 값의 평균 : %.2f"%avg)