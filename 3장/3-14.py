import random

WAITING = 0

class kiosk():
    print("와플 가게")
    t_i, t_w = 0, 0
    
    def total(i, w):
        return (i * 500) + (w * 2000)

    while True:
        n = int(input("1. 젤라또 500원 2. 와플 2000원 3. 결제 >> "))
        if n == 1:
            i = int(input("젤라또 수량 : "))
            print(f"젤라또 {i}개 추가")
            t_i += i
        elif n == 2:
            w = int(input("와플 수량  :"))
            print(f"와플 {w}개 추가")
            t_w += w
        elif n == 3:
            totalPrice = total(t_i, t_w)
            print(f'총 결제 금액은 {totalPrice}')
            
            my_money = int(input("결제 금액 : "))
            
            if totalPrice <= my_money:
                print(f"결제 완료. {my_money - totalPrice}")
                print(f"대기번호 {WAITING+1}")
                break
            else:
                print("잔액 부족")
                break

kiosk()