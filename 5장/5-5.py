def setup():
    global stuff
    global money
    global price
    
    money = int(input("가지고 있는 돈 입력 >>  "))
    stuff = int(input("물건 재고량 입력 >>  "))
    price = 3000

def stuff_sale(stuff, money, price):
    while True:
        if stuff >= 1:
            if money >= price:
                money -= price
                stuff -= 1
                print(f"물건 1개 판매")
                print(f"현재 물건 재고량 : {stuff}")
                print(f"거스름 돈 : {money}")
            else:
                print("잔액 부족")
                break
        else:
            print("품절")
            break

money = 0
stuff = 0
price = 0

setup()
stuff_sale(stuff, money, price)