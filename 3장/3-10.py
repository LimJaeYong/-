import random

a = input("문 a, b, c 중 입력 >> ")
b = random.choice(["a","b","c"])

print("문 맞추기")

if a == 'a':
    if b == 'a':
        print("정답")
    elif b == 'b':
        print("오답")
    else:
        print("오답")
        
elif a == 'b':
    if b == 'a':
        print("오답")
    elif b == 'b':
        print("정답")
    else:
        print("오답")
        
elif a == 'c':
    if b == 'a':
        print("오답")
    elif b == 'b':
        print("오답")
    else:
        print("정답")