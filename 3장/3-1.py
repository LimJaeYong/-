import random

level, rand_num, player_num = 0, [], []


while True:
    print("숫자 야구\n\n")
    level = int(input("난이도 선택 (3~6) >> "))
    if level < 3 or level > 6:
        print("다시 입력")
        continue
    
    else:
        rand_num = random.sample(range(1,10), level) # 1~10 까지중복 없는 랜덤 리스트 생성
        print(rand_num)
    
    while True:        
        strike = 0
        ball = 0 
        a = input("숫자입력")
        if a.isdigit() != True or len(a) != level: # 입력 오류 검사
            print("잘못 입력")
            continue
            
        for i in a:
            player_num.append(int(i))
        print(player_num)
        
        for i in range(level): # 게임 조건 검사
            if rand_num[i] == player_num[i]:
                strike += 1
            elif player_num.count(rand_num[i]):
                ball += 1
        print(f"{strike} strike {ball} ball")
        
        if(strike == level):
            break   