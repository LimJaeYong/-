import random


def rn():
    i = random.randint(0, 99)
    return i


def ud(a, b):
    global count
    if a > b:
        print("up")
    elif a < b:
        print("down")
    else:
        print("정답")
        count += 6


count = 0

while True:
    count = 0
    a = rn()

    while True:
        if count < 6:
            b = int(input("숫자 입력 >> "))
            ud(a,b)
            count +=1
        elif count > 6:
            print(f"{count - 6}번 걸림")
            break
        else:
            print("땡")
            break
        
    r = int(input("1. 재시작 2. 종료"))
    if r == 1:
        continue
    else:
        break
    