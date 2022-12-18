store = {}

print("물품 재고")

while True:
    item = input("추가 물품명 >> ")
    
    if item == 'q':
        break
    
    value = int(input("갯수 입력 >> "))
    store[item] = value
    
print("물품 재고량 확인")

while True:
    item = input("찾을 물품명 >> ")
    
    if item == "q":
        break
    
    if item in store:
        print(store[item])

    else:
        print("재고 없음")