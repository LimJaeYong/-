while 1:
    n = int(input())
    
    if n < 1:
        print("재입력")
        continue
    
    else: 
        a = []
        for i in range(1, n):
            if n % i == 0:
                a.append(i)
            
        if sum(a) == n:
            print(f"{n} = ")
            for i in range(len(a)):
                print(a)
            print('완전수')
        
        else:
            print(n, "완전수가 아님")
            break