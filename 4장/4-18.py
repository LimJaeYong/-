L = [1, 54, 62, 57, 8, 2, 43, 5]
print(L)

i = 0
while i < len(L):
    if L[i] % 2 == 0:
        del L[i]
    else:
        i += 1
        
print(L)

while True:
    click = int(input("1 또는 2 입력"))

    if click == 1:
        L.sort()
    elif click == 2:
        L.sort(reverse=True)
    else:
        print("다시 입력")
        continue

    print(L)
    
