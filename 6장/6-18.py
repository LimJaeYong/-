import random, time

menu = []

while True:
    print(menu)
    item = input("추가할 음식 입력 >> ")
    if item == 'q':
        break
    else:
        menu.append(item)
    
    
set_menu = set(menu) #왜 쓸까 대체

while True:
    print(set_menu)
    item = input("삭제할 음식 입력 >> ")
    if item == 'q':
        break
    else:
        set_menu.remove(item)
        
print(set_menu, "중에서 메뉴를 선택해드립니다.")

for i in range(5):
    print(5-i)
    time.sleep(1)

print(random.choice(list(set_menu)))