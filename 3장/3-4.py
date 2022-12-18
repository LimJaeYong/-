import random

lotto = []
mine = []
same = 0
score = [0, 6, 5, 4, 3, 2, 1]
'''원문 코드
while True:
    num = random.randint(1,45)
    if num not in lotto:
        lotto.append(num)
    if len(lotto) == 6:
        break'''

# 줄여본 코드
lotto = random.sample(range(0, 45), 6)
lotto.sort()

Mylotto = input("로또번호 6개 입력 :").split(" ")

for n in Mylotto:
    mine.append(int(n))
#당첨 검출
for myN in mine:
    if myN in lotto:
        same += 1

if same == 0:
    print("탈락")
else:
    print(f"{same}개 맞음, {score[same]}등 당첨")