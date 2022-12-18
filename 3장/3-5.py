import random

count = 0
com_num = random.randint(1, 100)
user_num = 0

print("랜덤 숫자 맞추기 게임")

while True:
    user_num = int(input("수 입력 >> "))
    count += 1
    
    if count == 10:
        print("실패")
        break

    if com_num > user_num:
        print("업")
    elif com_num < user_num:
        print("다운")
    elif com_num == user_num:
        print("정답")
        break
    
    