from random import randint

goal = 0
com_num, my_num = 0, 0

print("게임 시작")

while True:
    if goal < 31:
        com_num = randint(1,3)
        goal += com_num
        print(f"컴퓨터 : {com_num}, 현재 숫자 : {goal}")

        if goal >= 31:
            print("플레이어 승리")
            continue
        else:
            my_num = int(input("말할 숫자 개수 입력"))
            while (my_num <= 0) or (my_num > 3):
                my_num = int(input("다시 입력"))

            goal += my_num
            print(f"\n\n\n현재 숫자 = {goal}\n")
            
            if goal >= 31:
                print("컴퓨터 승리")
        
    else:
        print("31이상. 게임 종료")
        break