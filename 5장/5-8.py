import random

L = ["orange", "grape", "apple"]
 
answer = ""
i = 1
count = 1

def pick_name():
    pick = random.choice(L)
    print(pick)
    return pick

print("게임 시작")
print("정답 리스트 : ", L)
pick = pick_name()

while True:
    answer += input(f"{i}번쨰 글자 입력")
    i += 1
    print(answer)
    
    for a in range(len(answer)):
        if answer[a] == pick[a]:
            pass
        else:
            print("오답")
            answer = ""
            i = 1
            count = 1
    if count > len(pick) // 2:
        print("횟수 초과")
    if answer == pick:
        print("성공")
        break
    