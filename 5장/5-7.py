print("구구단")

def g(n):
    for i in range(1, 10):
        print(f"{n} * {i} = {n*i}")

def g2():
    for j in range(2, 10):
        for i in range(1, 10):
            print(f"{j} * {i} = {j*i}")
        print()
    
while True:
    a = int(input("1. 입력 수 구구단 2. 전체 구구단 3. 종료 >> "))
    
    if a == 3:
        quit()
        
    n = int(input("수 입력 >> "))
    
    if a == 1:
        g(n)
    elif a == 2:
        g2(n)    
    else:
        continue
