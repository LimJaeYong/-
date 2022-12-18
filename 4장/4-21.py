print("탕수육 게임")

L = ['탕', '수', '육']
count = 0

print("="*60)
print("시작")
print("="*60)

while True:
    for i in L:
        if count % 2 == 0:
            print(i)
        
        else:
            user = input("입력 >> ")
            
            if user != L[(count%3)]:
                print("당신은 기계에 패배했습니다.")
                break
        
        count += 1
    
