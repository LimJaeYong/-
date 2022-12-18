stock = {}

print("물품 재고량 입력")
while True:
    item = input("입력 물품 >> ")
    if item == 'z':
        break
    
    count = int(input("재고량 >> "))
    
    stock[item] = count
    
print("물품 재고량 확인")

while True:
    item = input("찾을 물품 >> ")
    if item == "":
        break
    
    if item in stock:
        print(stock[item],"개 남음")
    else:
        print("재고 없음")

    
    